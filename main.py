import discord
import os
import random
from replit import db

client = discord.Client()

@client.event
async def on_ready():
  print("Logged in.")

@client.event
async def on_message(message):
  if message.author == client.user:
    return


client.run(os.environ['TOKEN'])


##db["search_deck"] = ["Curse Doll", "Fire Flask", "Health Potion 1", "Health Potion 2", "Health Potion 3", "Secret Passage", "Power Potion", "Stamina Potion 1", "Stamina Potion 2", "Stamina Potion 3", "Treasure Chest", "Warding Talisman"]
##db["travel_deck"] = ["BG Travel Event 1 Of 10","BG Travel Event 2 Of 10","BG Travel Event 3 Of 10","BG Travel Event 4 Of 10","BG Travel Event 5 Of 10","BG Travel Event 6 Of 10","BG Travel Event 7 Of 10","BG Travel Event 8 Of 10","BG Travel Event 9 Of 10","BG Travel Event 10 Of 10","LW Travel Event 1 Of 3","LW Travel Event 2 Of 3","LW Travel Event 3 Of 3","LR Travel Event 1 Of 8","LR Travel Event 2 Of 8","LR Travel Event 3 Of 8","LR Travel Event 4 Of 8","LR Travel Event 5 Of 8","LR Travel Event 6 Of 8","LR Travel Event 7 Of 8","LR Travel Event 8 Of 8","TF Travel Event 1 Of 3","TF Travel Event 2 Of 3","TF Travel Event 3 Of 3","MB Travel Event 1 Of 5","MB Travel Event 2 Of 5","MB Travel Event 3 Of 5","MB Travel Event 4 Of 5","MB Travel Event 5 Of 5","CR Travel Event 1 Of 2","CR Travel Event 2 Of 2"]
##db["OL_xp"] = 0
##db["hero1_xp"] = 0
##db["hero2_xp"] = 0
##db["hero3_xp"] = 0
##db["hero4_xp"] = 0
##db["gold"] = 0
## need a database for OL deck


"""
## private messages user
  if message.content.startswith("!PBF PM"):
    await message.author.send("yo")

  
  
  if message.content.startswith("!PBF username"):
    print(message.author.id)
    
  if message.content.startswith("!PBF hero"):
    await message.channel.send("hero1")

 ## random.shuffle() 
##  if message.content.startswith("!PBF search"):
##    search_card = random.choice(search_deck)
##    await message.channel.send(search_card)    

##  if message.content.startswith("!PBF travel"):
##    travel_card = random.choice(travel_deck)
##    await message.channel.send(travel_card)    

"""

