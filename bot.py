# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 17:46:37 2020

@author: chris
"""

# bot.py
import os
import urllib3
import json
import certifi

import discord
from dotenv import load_dotenv
from discord.ext import commands

def get_champions_name(_id):
    """
    this functions takes an _id and returns the associate champions name
    :param _id: any integer from 1 to 555. if there is a champion, it will return the name.
    :return: champions name
    """
    all_champion_id = {

        1: "Annie",

        2: "Olaf",

        3: "Galio",

        4: "TwistedFate",

        5: "XinZhao",

        6: "Urgot",

        7: "LeBlanc",

        8: "Vladimir",

        9: "Fiddlesticks",

        10: "Kayle",

        11: "Master Yi",

        12: "Alistar",

        13: "Ryze",

        14: "Sion",

        15: "Sivir",

        16: "Soraka",

        17: "Teemo",

        18: "Tristana",

        19: "Warwick",

        20: "Nunu",

        21: "MissFortune",

        22: "Ashe",

        23: "Tryndamere",

        24: "Jax",

        25: "Morgana",

        26: "Zilean",

        27: "Singed",

        28: "Evelynn",

        29: "Twitch",

        30: "Karthus",

        31: "Cho'Gath",

        32: "Amumu",

        33: "Rammus",

        34: "Anivia",

        35: "Shaco",

        36: "Dr.Mundo",

        37: "Sona",

        38: "Kassadin",

        39: "Irelia",

        40: "Janna",

        41: "Gangplank",

        42: "Corki",

        43: "Karma",

        44: "Taric",

        45: "Veigar",

        48: "Trundle",

        50: "Swain",

        51: "Caitlyn",

        53: "Blitzcrank",

        54: "Malphite",

        55: "Katarina",

        56: "Nocturne",

        57: "Maokai",

        58: "Renekton",

        59: "JarvanIV",

        60: "Elise",

        61: "Orianna",

        62: "Wukong",

        63: "Brand",

        64: "LeeSin",

        67: "Vayne",

        68: "Rumble",

        69: "Cassiopeia",

        72: "Skarner",

        74: "Heimerdinger",

        75: "Nasus",

        76: "Nidalee",
        77: "Udyr",
        78: "Poppy",
        79: "Gragas",
        80: "Pantheon",
        81: "Ezreal",
        82: "Mordekaiser",

        83: "Yorick",

        84: "Akali",

        85: "Kennen",

        86: "Garen",

        89: "Leona",

        90: "Malzahar",

        91: "Talon",

        92: "Riven",

        96: "Kog'Maw",

        98: "Shen",

        99: "Lux",

        101: "Xerath",

        102: "Shyvana",

        103: "Ahri",

        104: "Graves",

        105: "Fizz",

        106: "Volibear",

        107: "Rengar",

        110: "Varus",

        111: "Nautilus",

        112: "Viktor",

        113: "Sejuani",

        114: "Fiora",

        115: "Ziggs",

        117: "Lulu",

        119: "Draven",

        120: "Hecarim",

        121: "Kha'Zix",

        122: "Darius",

        126: "Jayce",

        127: "Lissandra",

        131: "Diana",

        133: "Quinn",

        134: "Syndra",

        136: "AurelionSol",

        141: "Kayn",

        142: "Zoe",

        143: "Zyra",

        145: "Kai'sa",

        150: "Gnar",

        154: "Zac",

        157: "Yasuo",

        161: "Vel'Koz",

        163: "Taliyah",

        164: "Camille",

        201: "Braum",

        202: "Jhin",

        203: "Kindred",

        222: "Jinx",

        223: "TahmKench",

        235: "Senna",

        236: "Lucian",

        238: "Zed",

        240: "Kled",

        245: "Ekko",

        246: "Qiyana",

        254: "Vi",

        266: "Aatrox",

        267: "Nami",

        268: "Azir",

        350: "Yuumi",

        412: "Thresh",

        420: "Illaoi",

        421: "Rek'Sai",

        427: "Ivern",

        429: "Kalista",

        432: "Bard",

        497: "Rakan",

        498: "Xayah",

        516: "Ornn",

        517: "Sylas",

        523: "Aphelios",

        518: "Neeko",

        555: "Pyke",

        875: "Sett",
    }
    return all_champion_id.get(_id)


http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())
api_key = 'RGAPI-8a27fbd9-12df-4cad-9402-86b7729598db'
region = 'na1'

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')



#client = discord.Client()

#@client.event
#async def on_ready():
#    print(f'{client.user} has connected to Discord!')
#@client.event
#async def on_message(message):
#    if message.author == client.user:
#        return
    
#    if message.content == 'topisdone!':
#        await message.channel.send('TRULY')
#client.run(TOKEN)


bot = commands.Bot(command_prefix='$')
@bot.command(name = 'games', help = 'For checking how many games you have on a champion (use underscores for spaces)')
async def games(ctx, summoner_name: str, champion_id: str):
    while (summoner_name.find('_')!=-1):
        summoner_name = summoner_name[:summoner_name.find('_')]+"%20"+summoner_name[summoner_name.find('_')+1:]
    #print(name)
    URL1 = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+summoner_name+"?api_key="+api_key
    r1 = http.request('GET', URL1)
    rJson = json.loads(r1.data.decode("utf-8"))
    #print(rJson)
    SumID = rJson['accountId']
    #print(SumID)
    URL = "https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/"+SumID+"?champion="+champion_id+"&api_key="+api_key
    r = http.request('GET', URL)
    rJson = json.loads(r.data.decode("utf-8"))
    #print(rJson['totalGames'])
    strJson = str(rJson['totalGames'])
    await ctx.send( strJson+" games on {}".format(get_champions_name(int(champion_id))))
    
bot.run(TOKEN)