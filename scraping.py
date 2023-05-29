import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import re
import pickle

base_url = "https://www.vlr.gg"
match_url_example = "https://www.vlr.gg/184513/zeta-division-vs-team-secret-champions-tour-2023-pacific-league-playoffs-ur1/?game=119677&tab=overview"
all_pacific_games_url = 'https://www.vlr.gg/event/matches/1191/champions-tour-2023-pacific-league/?series_id=all'
all_americas_games_url = "https://www.vlr.gg/event/matches/1189/champions-tour-2023-americas-league/?series_id=all"
all_emea_games_url = "https://www.vlr.gg/event/matches/1190/champions-tour-2023-emea-league/?series_id=all"
map_url_example = "https://www.vlr.gg/184513/zeta-division-vs-team-secret-champions-tour-2023-pacific-league-playoffs-ur1/?map=1"
bo5_example = "https://www.vlr.gg/184522/paper-rex-vs-drx-champions-tour-2023-pacific-league-playoffs-gf"
player_url_example = "https://www.vlr.gg/player/17086/something"

class VLRScraper():
    def __init__(self):
        self.base_url = "https://www.vlr.gg"
        self.player_cache_path = "config\\players.pickle"
        self.match_links_cache_path = "config\\matches.pickle"
        self.map_links_cache_path = "config\\maps.pickle"
        if os.path.exists(self.player_cache_path):
            self.player_cache = pd.read_pickle(self.player_cache_path)
        else:
            self.player_cache = pd.DataFrame(columns=["player_link", "aliases"])

        if os.path.exists(self.match_links_cache_path):
            f = open(self.match_links_cache_path)
            self.matches_cache = pickle.load(open(self.match_links_cache_path, "rb"))
            f.close()
        else:
            self.matches_cache = []

        if os.path.exists(self.map_links_cache_path):
            self.maps_cache = pd.read_pickle(self.map_links_cache_path)
        else:
            self.maps_cache = pd.DataFrame(columns=["map_link", "map_name", "vod_link", "team_names", "comp_mappings"])
        

    def getMatchLinks(self, region_all_matches_link):
        response = requests.get(region_all_matches_link)
        soup = BeautifulSoup(response.text, 'html.parser')
        all_matches = soup.findAll("a", class_="match-item")
        print(all_matches)
        match_links = []
        for match in all_matches:
            print(match['href'])
            match_links.append(base_url + match['href'])
        print(len(all_matches))
        return match_links

    def getInfoFromMatchPage(self, match_page_link):
        if match_page_link in self.matches_cache:
            return


        response = requests.get(match_page_link)
        soup = BeautifulSoup(response.text, 'html.parser')
        vods_container = soup.find("div", class_="match-vods")
        vod_links = vods_container.findAll("a", href=True)
        vod_links_list = []
        for vod in vod_links:
            regex_exp = re.compile(r"Map \d")
            if len(regex_exp.findall(vod.get_text().strip())) > 0:
                print(vod['href'])
                vod_links_list.append(vod['href'])
        print(vod_links_list)
        map_links = soup.findAll("div", class_="vm-stats-gamesnav-item")
        links = []
        map_names = []
        for map_link in map_links[1:1 + len(vod_links_list)]:
            print(map_link["data-href"])
            map_name = map_link.find("div", attrs={"style": "margin-bottom: 2px; text-align: center; line-height: 1.5;"}).get_text().strip()
            map_names.append(re.sub('\s+', '', map_name)[1:])
            links.append(match_page_link + "/?game=" + map_link["data-game-id"] + "&tab=overview")

        for link in links:
            if self.maps_cache["map_link"].str.contains(link).any():
                continue
            else:
                print("processing {}".format(link))
                response = requests.get(link)
                soup = BeautifulSoup(response.text, 'html.parser')
                team_name_links = soup.findAll("div", class_="wf-title-med")
                print(len(team_name_links))
                team_names = []
                for team_name in team_name_links:
                    print(team_name.get_text().strip())
                    team_names.append(team_name.get_text().strip())
                stats_container = soup.find("div", class_="vm-stats-container")
                stats_container = stats_container.find("div", class_="vm-stats-game mod-active")
                stats_table = stats_container.findAll("table", class_="mod-overview")
                print(len(stats_table))
                table_bodies = [table.find("tbody") for table in stats_table]
                print("NEW MAP")
                team1, team2 = table_bodies[0], table_bodies[1]
                comp_mappings = []
                for row in team1.findAll("tr"):
                    player_cell = row.find("td", class_="mod-player")
                    player_cell_text = (player_cell.find("div", class_="text-of")).get_text().strip()
                    player_link = self.base_url + player_cell.find("a")['href']
                    self.updatePlayersInfo(player_link)
                    agent_cell = row.find("td", class_="mod-agents")
                    agent_name = agent_cell.find("img")["title"]
                    print("{} {}".format(player_cell_text, agent_name))
                    comp_mappings.append((player_cell_text, agent_name))
                print("-----")
                for row in team2.findAll("tr"):
                    player_cell = row.find("td", class_="mod-player")
                    player_cell_text = (player_cell.find("div", class_="text-of")).get_text().strip()
                    player_link = self.base_url + player_cell.find("a")['href']
                    self.updatePlayersInfo(player_link)
                    agent_cell = row.find("td", class_="mod-agents")
                    agent_name = agent_cell.find("img")["title"]
                    print("{} {}".format(player_cell_text, agent_name))
                    comp_mappings.append((player_cell_text, agent_name))
                print("-----")
                newRow = {"map_link": link, "map_name": map_names.pop(), "vod_link": vod_links_list.pop(), "team_names": team_names, "comp_mappings": comp_mappings}
                self.maps_cache = pd.concat([self.maps_cache, pd.DataFrame([newRow])])

        self.matches_cache.append(match_page_link)
        f = open(self.match_links_cache_path, 'wb')
        pickle.dump(self.matches_cache, f)
        self.maps_cache.to_pickle(self.map_links_cache_path)

    def updatePlayersInfo(self, player_link):
        if self.player_cache["player_link"].str.contains(player_link).any():
            return
        else:
            response = requests.get(player_link)
            soup = BeautifulSoup(response.text, 'html.parser')
            player_header = soup.find('div', class_="player-header")
            primary_alias = player_header.find('h1', class_="wf-title").get_text().strip()
            alias = player_header.find_all('span', attrs={'style': 'font-style: italic;'})
            aliases = [primary_alias]
            for elem in alias:
                aliases.append(elem.get_text().strip())
            print(aliases)
            newRow = {"player_link": player_link, "aliases": aliases}
            self.player_cache = pd.concat([self.player_cache, pd.DataFrame([newRow])])
            self.player_cache.to_pickle(self.player_cache_path)
            # print(self.player_cache)

    def execute(self, all_matches_url):
        match_links = self.getMatchLinks(all_matches_url)
        for match_link in match_links:
            self.getInfoFromMatchPage(match_link)

    def viewPlayerCache(self):
        print(self.player_cache)

    def viewMatchesCache(self):
        print(self.matches_cache)

    def viewMapsCache(self):
        # return self.maps_cache
        print(self.maps_cache)


vlr = VLRScraper()
vlr.execute(all_pacific_games_url)
vlr.execute(all_americas_games_url)
vlr.execute(all_emea_games_url)
vlr.viewMapsCache()
# vlr.viewPlayerCache()
# vlr.viewMapsCache().to_csv("maps_cache.csv")
# vlr.getInfoFromMatchPage("https://www.vlr.gg/167358/drx-vs-cloud9-champions-tour-2023-lock-in-s-o-paulo-alpha-qf")
