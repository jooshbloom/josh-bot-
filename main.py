import os
import discord
import requests
import json
import asyncio
import random
from discord.ext import commands

intents = discord.Intents.all()

helpCommand=commands.DefaultHelpCommand(no_category='Command')

bot = commands.Bot(command_prefix='!joosh',intents=intents, helpCommand=helpCommand)


@bot.command()
async def Help(ctx):
  embed = discord.Embed(title="Commands list", color = 0xFF5733)
  embed.set_thumbnail(description="This is a list of bot commands")

  embed.add_field(name="!jooshHelp", value="Brings up help menu", inline=False)

  embed.add_field(name="!jooshName", value="Input name to get a response", inline=False)

  embed.add_field(name="!jooshAdd", value="Input two numbers to add them", inline=False)

  embed.add_field(name="!jooshTime", value="Enter a time and recieve a message based on the time", inline=False)

  embed.add_field(name="!jooshPic", value="Enter command to get a surprise!", inline=False)

  embed.add_field(name="!jooshRandPic", value="Enter command to get a random picture", inline=False)

  embed.add_field(name="!jooshEightBall", value="Enter a yes/no question and let the bot tell your future", inline=False)

  embed.add_field(name="!jooshRPS", value="enter rock, paper, or scissors, and see if you can beat the bot", inline=False)

  embed.add_field(name="!jooshJoke", value="Enter command to get a random joke", inline=False)

  embed.add_field(name="!jooshWeather", value="Enter your zipcode to get information about the weather in your area", inline=False)

  embed.add_field(name="!jooshNationality", value="Enter your name and recieve the probability of your nationality", inline=False)

  embed.add_field(name="!jooshVideoGame", value="Enter the name of a game and get an image of the game (use quotes if game title has multiple words", inline=False)



@bot.event
async def on_connect():
  print("your bot is online")

@bot.command(brief="Enter your name after the space to recieve a message.")
async def Name(ctx,name):
  await ctx.reply("Josh hates " + name + ".")

@bot.command(brief="Enter two numbers with a space in between each to add them.")
async def Add(ctx,n1,n2):
  nTotal = int(n1) + int(n2)
  nTotal = str(nTotal)
  await ctx.reply(n1 + " + " + n2 + " = " + nTotal)

@bot.command(brief="Enter a time and recieve a message based on the time.")
async def Time(ctx, time, AmPm):
  time = int(time)
  if (AmPm.lower() == 'am' and time>= 5):
    await ctx.reply("Good Morning!")
  elif (AmPm.lower() == "pm" and time>= 0 and time<=6):
    await ctx.reply("Good Afternoon!")
  else:
    await ctx.reply("Goodnight")


@bot.command(brief="Enter command to get a surprise!")
async def Pic(ctx):
  await ctx.reply("https://dcist.com/wp-content/uploads/sites/3/2020/02/wilford_newsletter.jpg")

picList = ["https://i.kym-cdn.com/entries/icons/mobile/000/029/043/Shaq_Tries_to_Not_Make_a_Face_While_Eating_Spicy_Wings___Hot_Ones_11-21_screenshot.jpg", "https://static.wikia.nocookie.net/lolesports_gamepedia_en/images/e/e7/T1_Faker_2022_Split_2.png/revision/latest/scale-to-width-down/220?cb=20220619004304", "https://www.ladbible.com/cdn-cgi/image/width=720,quality=70,format=webp,fit=pad,dpr=1/https%3A%2F%2Fs3-images.ladbible.com%2Fs3%2Fcontent%2F772e1e415f9f55dcbb5497b699a3997f.png"]

@bot.command(brief='Enter command to get a random picture')
async def RandPic(ctx):
  rand = random.choice(picList)
  await ctx.reply(rand)

@bot.command(aliases=["8ball"], brief='Ask the eight ball a yes/no question and get a reply.')
async def EightBall(ctx, *, phrase:str):
  myList=["it is certain", "without a doubt", "outlook not so good", "don't count on it", "very doubtful"]
  await ctx.reply(phrase + ": " + random.choice(myList))



@bot.command(aliases=["wow"], brief="Enter rock, paper, or scissors and see if you can beat the bot.")
async def RPS(ctx, choice):
  rpsList = ["rock", "paper", "scissors"]
  botChoice=random.choice(rpsList)

  choice=choice.lower()

  if botChoice==choice:
    await ctx.reply(" It's a tie!💀💀 You chose " + choice + " and bot chose " + botChoice)

  elif botChoice=="rock" and choice=="paper":
    await ctx.reply("You won!💀💀 You chose " + choice + " and bot chose " + botChoice)

  elif botChoice=="scissors" and choice=="paper":
    await ctx.reply("You lost!💀💀 You chose " + choice + " and bot chose " + botChoice)

  elif botChoice=="paper" and choice=="rock":
    await ctx.reply("You lost!💀💀 You chose " + choice + " and bot chose " + botChoice)

  elif botChoice=="scissors" and choice=="rock":
    await ctx.reply("You won!💀💀 You chose " + choice + " and bot chose " + botChoice)

  elif botChoice=="rock" and choice=="scissors":
    await ctx.reply("You lost!💀💀 You chose " + choice + " and bot chose " + botChoice)

  elif botChoice=="paper" and choice=="scissors":
    await ctx.reply("You won!💀💀 You chose " + choice + " and bot chose " + botChoice)





#use a joke API to get a joke setup, wait a few seconds
#and deliver the punchline
@bot.command()
async def Joke(ctx):
  #variable to hold url
  url= "https://official-joke-api.appspot.com/random_joke"

  req = requests.get(url)

  #data variable that holds the json data that the api holds
  data = req.json()

  #pull the joke setup from json data
  setup=data["setup"]
  punchline=data["punchline"]
  await ctx.reply(setup)


  #pause your bot, but allow it to execute other functions during that time

  
  await asyncio.sleep(3)
  await ctx.reply(punchline)



@bot.command()
async def Nationality(ctx, name):
  url = "https://api.nationalize.io/?name=" + name

  req = requests.get(url)

  data = req.json()

  country1=data["country"][0]["country_id"]
  prob1=data["country"][0]["probability"]

  country2=data["country"][1]["country_id"]
  prob2=data["country"][1]["probability"]

  country3=data["country"][2]["country_id"]
  prob3=data["country"][2]["probability"]

  country4=data["country"][3]["country_id"]
  prob4=data["country"][3]["probability"]
  
  

  prob1=prob1*100
  prob2=prob2*100
  prob3=prob3*100
  prob4=prob4*100

  await ctx.send("Country 1: " + country1 + "  Probability 1: " + str(prob1) + "%")
  await ctx.send("Country 2: " + country2 + "  Probability 2: " + str(prob2) + "%")
  await ctx.send("Country 3: " + country3 + "  Probability 3: " + str(prob3) + "%")
  await ctx.send("Country 4: " + country4 + "  Probability 4: " + str(prob4) + "%")



@bot.command()
async def Weather(ctx,zip):
  my_secret_weather = os.environ['Weather API Key']
  #variable to hold url
  url= "https://api.openweathermap.org/data/2.5/weather?zip=" + zip + ",us&appid=" +my_secret_weather
  
  req = requests.get(url)

  data = req.json()

  desc=data["weather"][0]["description"] 

  temp=data["main"]["temp"]

  # temp=(temp − 273.15) * 9/5 + 32
  
  await ctx.reply(desc + " " + str(temp) + " degrees F")
  

@bot.command()
async def VideoGame(ctx, name):
  
   # my_secret_video = os.environ['Video']

  url = "https://rawg-video-games-database.p.rapidapi.com/games?key=7d6e3a45b2c240a999ceb2f66c10b48e&page_size=1&search=" + name
  headers = {
  'x-rapidapi-key': "e6ef05302emsh9c46dd59d7ac5d1p13a2d8jsneb37aae7d452",
  'x-rapidapi-host': "rawg-video-games-database.p.rapidapi.com"
  }
  response = requests.request("GET", url, headers=headers)
  
  data = response.json()

  print("total games: ", data['count'])

  for game in data['results']:
    await ctx.send(game['background_image'])


  









my_secret = os.environ['TOKEN']
bot.run(my_secret)





