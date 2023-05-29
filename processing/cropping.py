import cv2
from models.image_utils import PlayerCrops
import json

class Cropping:

    def __init__(self, config_path):
        self.config_path = config_path
        f = open(config_path)
        self.config = json.load(f)
        f.close()


    # given crop of 1 single player's hud: returns the agent icon image
    def getAgentImageFromPlayerHud(self, player_hud):
        start_y, end_y = self.config["single_player"]["agent_image"]["y"]["start"], self.config["single_player"]["agent_image"]["y"]["end"]
        start_x, end_x = self.config["single_player"]["agent_image"]["x"]["start"], self.config["single_player"]["agent_image"]["x"]["end"]
        hud_icon = player_hud[start_y: end_y, start_x: end_x].copy()
        return hud_icon

    # given crop of 1 single player's hud: returns the player's name crop
    def getPlayerNameFromPlayerHud(self, player_hud):
        start_y, end_y = self.config["single_player"]["player_name"]["y"]["start"], self.config["single_player"]["player_name"]["y"]["end"]
        start_x, end_x = self.config["single_player"]["player_name"]["x"]["start"], self.config["single_player"]["player_name"]["x"]["end"]
        player_name = player_hud[start_y: end_y, start_x: end_x].copy()
        return player_name

    # given crop of 1 single player's hud: returns the player's credits crop
    def getPlayerCreditsFromPlayerHud(self, player_hud):
        start_y, end_y = self.config["single_player"]["credits"]["y"]["start"], self.config["single_player"]["credits"]["y"]["end"]
        start_x, end_x = self.config["single_player"]["credits"]["x"]["start"], self.config["single_player"]["credits"]["x"]["end"]
        credits = player_hud[start_y: end_y, start_x: end_x].copy()
        return credits

    # non-astra usecases only
    # given crop of 1 single player's hud: returns array of 3 images containing ability crops
    def getAbilityCrops(self, player_hud):
        start_points = []
        for item in self.config["single_player"]["abilities"]["start_points"]:
            start_points.append((item["x"], item["y"]))
        x_offset, y_offset = self.config["single_player"]["abilities"]["offsets"]["x"], self.config["single_player"]["abilities"]["offsets"]["y"]
        img = player_hud.copy()

        ability_crops = []
        for x, y in start_points:
            crop = img[y: y + y_offset, x: x + x_offset]
            ability_crops.append(crop)

        return ability_crops

    # given crop of 1 single player's hud: returns crop of ult (could be dots, could be ult icon)
    def getUltCrop(self, player_hud):
        start_y, end_y = self.config["single_player"]["ult"]["y"]["start"], self.config["single_player"]["ult"]["y"]["end"]
        start_x, end_x = self.config["single_player"]["ult"]["x"]["start"], self.config["single_player"]["ult"]["x"]["end"]
        img = player_hud.copy()
        ult_crop = img[start_y: end_y, start_x: end_x]
        return ult_crop

    # done parametrizing 
    # given crop of 1 single player's hud: returns crop of armor number
    def getArmorNumberCrop(self, player_hud):
        start_y, end_y = self.config["single_player"]["armor"]["y"]["start"], self.config["single_player"]["armor"]["y"]["end"]
        start_x, end_x = self.config["single_player"]["armor"]["x"]["start"], self.config["single_player"]["armor"]["x"]["end"]
        armor_number = player_hud[start_y: end_y, start_x: end_x].copy()
        return armor_number

    # done parametrizing 
    def getHealthNumberCrop(self, player_hud):
        start_y, end_y = self.config["single_player"]["health"]["y"]["start"], self.config["single_player"]["health"]["y"]["end"]
        start_x, end_x = self.config["single_player"]["health"]["x"]["start"], self.config["single_player"]["health"]["x"]["end"]
        health_number = player_hud[start_y: end_y, start_x: end_x].copy()
        return health_number

    # given crop of 1 single player's hud, returns object with 9 images:
    # image 1: agent image
    # image 2: player name
    # image 3: player credits
    # image 4: first ability dots
    # image 5: second ability dots
    # image 6: third ability dots
    # image 7: ult ability dots / icon
    # image 8: armor number image
    # image 9: health number image
    def cropIndividualPlayer(self, player_hud):
        crops = PlayerCrops()
        crops.agentImage = self.getAgentImageFromPlayerHud(player_hud)
        crops.playerName = self.getPlayerNameFromPlayerHud(player_hud)
        crops.playerCredits = self.getPlayerCreditsFromPlayerHud(player_hud)
        abilities = self.getAbilityCrops(player_hud)
        crops.ability1 = abilities[0]
        crops.ability2 = abilities[1]
        crops.ability3 = abilities[2]
        crops.ult = self.getUltCrop(player_hud)
        crops.playerArmor = self.getArmorNumberCrop(player_hud)
        crops.playerHealth = self.getHealthNumberCrop(player_hud)
        return crops
        
    # done parametrizing    
    # returns 2 arrays of 5 images each - the left players crops and the right player crops
    def cropPlayerHuds(self, frame):
        h, w, alpha = frame.shape
        player_hud_x = self.config["player_hud_full"]["x"]
        player_hud_y = self.config["player_hud_full"]["y"]

        left_player_hud = frame[player_hud_y["start"]:player_hud_y["end"], player_hud_x["start"]:player_hud_x["end"]].copy()
        right_player_hud = frame[player_hud_y["start"]:player_hud_y["end"], w-player_hud_x["end"]:w-player_hud_x["start"]].copy()

        # start_points = [(6, 10), (6, 116), (6, 222), (6, 328), (6, 434)] # constants
        start_points = []

        single_player_start_points = self.config["single_player"]["start_points"]
        for item in single_player_start_points:
            start_points.append((item["x"], item["y"]))

        x_offset, y_offset = self.config["single_player"]["offsets"]["x"], self.config["single_player"]["offsets"]["y"] # constants

        left_players = []
        right_players = []

        for x, y in start_points:
            player_left = left_player_hud[y:y+y_offset, x:x+x_offset].copy()
            player_right = cv2.flip(right_player_hud[y:y+y_offset, x:x+x_offset].copy(), 1)
            left_players.append(player_left)
            right_players.append(player_right)

        return left_players, right_players

    # Unaffected by preround view vs round view
    def cropKillfeed(self, frame):
        kill_events = []
        for i in range(self.config["killfeed"]["max_events"]):
            height = self.config["killfeed"]["y"]["height"]
            y_offset = self.config["killfeed"]["y"]["offset"]
            start_x = self.config["killfeed"]["x"]["start"]
            end_x = self.config["killfeed"]["x"]["end"]
            crop = frame[(i * height) + y_offset: ((i + 1) * height) + y_offset, start_x:end_x]
            kill_events.append(crop)
        return kill_events

    # Unaffected by preround view vs round view
    def cropRoundNumber(self, frame):
        start_y, end_y = self.config["round_number"]["y"]["start"], self.config["round_number"]["y"]["end"]
        start_x, end_x = self.config["round_number"]["x"]["start"], self.config["round_number"]["x"]["end"]
        crop = frame[start_y: end_y, start_x: end_x]
        return crop

    # Unaffected by preround view vs round view
    def cropLeftScore(self, frame):
        start_y, end_y = self.config["left_score"]["y"]["start"], self.config["left_score"]["y"]["end"]
        start_x, end_x = self.config["left_score"]["x"]["start"], self.config["left_score"]["x"]["end"]
        crop = frame[start_y: end_y, start_x: end_x]
        return crop

    # Unaffected by preround view vs round view
    def cropRightScore(self, frame):
        start_y, end_y = self.config["right_score"]["y"]["start"], self.config["right_score"]["y"]["end"]
        start_x, end_x = self.config["right_score"]["x"]["start"], self.config["right_score"]["x"]["end"]
        crop = frame[start_y: end_y, start_x: end_x]
        return crop

    # Unaffected by preround view vs round view
    def cropRoundTimer(self, frame):
        start_y, end_y = self.config["round_timer"]["y"]["start"], self.config["round_timer"]["y"]["end"]
        start_x, end_x = self.config["round_timer"]["x"]["start"], self.config["round_timer"]["x"]["end"]
        crop = frame[start_y: end_y, start_x: end_x]
        return crop

    # returns images of all points of interest on the full frame
    def cropFrame(self, frame):
        # datatypes: [img], [img], img, img, img, img, [img]
        left_players, right_players = self.cropPlayerHuds(frame)
        round_timer = self.cropRoundTimer(frame)
        left_score = self.cropLeftScore(frame)
        right_score = self.cropRightScore(frame)
        round_number = self.cropRoundNumber(frame)
        killfeed = self.cropKillfeed(frame)
        return left_players, right_players, round_timer, left_score, right_score, round_number, killfeed

    def reverseRightPlayer(self, playerCrop):
        playerCrop.playerName = cv2.flip(playerCrop.playerName, 1)
        playerCrop.playerCredits = cv2.flip(playerCrop.playerCredits, 1)
        playerCrop.ability1 = cv2.flip(playerCrop.ability1, 1)
        playerCrop.ability2 = cv2.flip(playerCrop.ability2, 1)
        playerCrop.ability3 = cv2.flip(playerCrop.ability3, 1)
        playerCrop.ult = cv2.flip(playerCrop.ult, 1)
        playerCrop.playerArmor = cv2.flip(playerCrop.playerArmor, 1)
        playerCrop.playerHealth = cv2.flip(playerCrop.playerHealth, 1)
        return playerCrop

    def showPlayerCrops(self, playerCrops):
        cv2.imshow("agent image", playerCrops.agentImage)
        cv2.imshow("player name", playerCrops.playerName)
        cv2.imshow("player credits", playerCrops.playerCredits)
        cv2.imshow("ability 1", playerCrops.ability1)
        cv2.imshow("ability 2", playerCrops.ability2)
        cv2.imshow("ability 3", playerCrops.ability3)
        cv2.imshow("ult", playerCrops.ult)
        cv2.imshow("armor", playerCrops.playerArmor)
        cv2.imshow("health", playerCrops.playerHealth)
        cv2.waitKey(0)

    def getLoadoutValueLabel(self, frame):
        start_x, end_x = self.config["loadout_value_label"]["x"]["start"], self.config["loadout_value_label"]["x"]["end"]
        start_y, end_y = self.config["loadout_value_label"]["y"]["start"], self.config["loadout_value_label"]["y"]["end"]
        crop = frame[start_y:end_y, start_x:end_x]
        return crop

    def getTeamNames(self, frame):
        start_x, end_x = self.config["left_team_name"]["x"]["start"], self.config["left_team_name"]["x"]["end"]
        start_y, end_y = self.config["left_team_name"]["y"]["start"], self.config["left_team_name"]["y"]["end"]
        leftName = frame[start_y:end_y, start_x:end_x]

        start_x, end_x = self.config["right_team_name"]["x"]["start"], self.config["right_team_name"]["x"]["end"]
        start_y, end_y = self.config["right_team_name"]["y"]["start"], self.config["right_team_name"]["y"]["end"]
        rightName = frame[start_y:end_y, start_x:end_x]
        return leftName, rightName

    