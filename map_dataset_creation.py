import cv2
import pafy
import urllib
import random
import os
import json
import threading
import numpy as np
from PIL import Image
import string

attacker_color = (109, 57, 239)
defender_color = (123, 171, 56)

"""
def generate_fake_icon_for_image(icon_path, agent):
    img = cv2.imread(icon_path,  cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (256, 256), 0, 0)
    w, h, alpha = img.shape
    attacker_img = cv2.circle(
        img.copy(), (int(2*w/3) - 5, int(h/2) + 10), int(2*w/7), attacker_color, 15)
    defender_img = cv2.circle(
        img.copy(), (int(2*w/3) - 5, int(h/2) + 10), int(2*w/7), attacker_color, 15)
    attacker_img = attacker_img[int(h/2) + 10 - int(2*w/7): int(h/2) + 10 + int(
        2*w/7), int(2*w/3) - 5 - int(2*w/7):int(2*w/3) - 5 + int(2*w/7)]
    defender_img = defender_img[int(h/2) + 10 - int(2*w/7): int(h/2) + 10 + int(
        2*w/7), int(2*w/3) - 5 - int(2*w/7):int(2*w/3) - 5 + int(2*w/7)]
    atk_cropped = cropAroundCircle(attacker_img.copy())
    atk_cropped = cv2.resize(atk_cropped, (17, 17), 0, 0)
    def_cropped = cropAroundCircle(defender_img.copy())
    def_cropped = cv2.resize(def_cropped, (17, 17), 0, 0)
    # cv2.imshow("image", attacker_img)
    # cv2.imshow("cropped", cropped)
    # cv2.waitKey(0)
    cv2.imwrite("assets\\fake_minimap_icons\\atk_" + agent, atk_cropped)
    cv2.imwrite("assets\\fake_minimap_icons\\def_" + agent, def_cropped)
    # cv2.waitKey(0)
"""

def generate_fake_icon_for_image(icon_path, agent):
    img = cv2.imread(icon_path,  cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (18, 18), 0, 0)
    atk_circle = cv2.circle(img.copy(), (9, 9), 9, attacker_color, thickness=2)
    def_circle = cv2.circle(img.copy(), (9, 9), 9, defender_color, thickness=2)
    atk_cropped = cropAroundCircle2(atk_circle)
    def_cropped = cropAroundCircle2(def_circle)
    cv2.imshow("atkcircle", atk_cropped)
    cv2.imshow("defcircle", def_cropped)
    cv2.imwrite("assets\\fake_minimap_icons\\atk_" + agent, atk_cropped)
    cv2.imwrite("assets\\fake_minimap_icons\\def_" + agent, def_cropped)
    cv2.waitKey(0)


def generate_fake_minimap_icons():
    for agent_icon in os.listdir("assets\\icons\\"):
        filepath = os.path.join("assets\\icons\\" + agent_icon)
        generate_fake_icon_for_image(filepath, agent_icon)


def cropAroundCircle(img):
    h, w, a = img.shape
    mask = np.zeros((h, w), np.uint8)
    circle_image = cv2.circle(
        mask, (int(2*w/3) - 24, int(h/2)), int(2*w/7) + 30, (255, 255, 255), -1)
    masked_data = cv2.bitwise_and(img, img, mask=circle_image)
    return masked_data

def cropAroundCircle2(img):
    h, w, a = img.shape
    mask = np.zeros((h, w), np.uint8)
    circle_image = cv2.circle(
        mask, (int(w/2), int(h/2)), 90, (255, 255, 255), -1)
    masked_data = cv2.bitwise_and(img, img, mask=circle_image)
    return masked_data

def build_dataset():
    maps = sorted(os.listdir("assets\\maps"))
    agent_icons = sorted(os.listdir("assets\\fake_minimap_icons"))
    attack_icons = agent_icons[:21]
    defense_icons = agent_icons[21:]
    number_of_attack_players = random.randint(0, 5)
    number_of_defense_players = random.randint(0, 5)
    atk_agents = random.sample(attack_icons, number_of_attack_players)
    def_agents = random.sample(defense_icons, number_of_defense_players)
    all_agents = atk_agents + def_agents
    selected_map = random.sample(maps, 1)[0]
    print(atk_agents)
    print(def_agents)
    print(selected_map)
    map_image = Image.open("assets\\maps\\" + selected_map)
    map_w, map_h = map_image.size
    filename = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    txtfile = open("map_dataset\\" + filename + ".txt", "a")
    for agent in all_agents:
        agent_image = Image.open("assets\\fake_minimap_icons\\" + agent)
        agent_w, agent_h = agent_image.size
        random_x = random.randint(0, map_w - agent_w)
        random_y = random.randint(0, map_h - agent_h)
        map_image.paste(agent_image, (random_x, random_y))
        label = agent.split(".")[0]
        center_x = (random_x + (agent_w / 2)) / map_w
        center_y = (random_y + (agent_h / 2)) / map_h
        width = agent_w / map_w
        height = agent_h / map_h
        txtfile.write("{} {:.5f} {:.5f} {:.5f} {:.5f}\n".format(label, center_x, center_y, width, height))

    txtfile.close
    map_image.save("map_dataset\\" + filename + ".png")
    # map_image.show()

        
f = open("yolov5labels.txt", "a")
for agent in sorted(os.listdir("assets\\fake_minimap_icons")):
    f.write(agent + "\n")
f.close()

for i in range(0, 3000):
    build_dataset()
# generate_fake_minimap_icons()
