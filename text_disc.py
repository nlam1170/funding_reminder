import funding
import discord
import asyncio
import time
from datetime import datetime

token = r"NzE4MjI3NDQyODc5MTY4NTQz.XtmsZQ.MjlW2tCgbKTDySJwstRdrIeKB-M"
target_channel = 718555773789011979
client = discord.Client()

round_one_times = [3, 11, 19]
round_two_times = [7, 15, 23]


async def round_one_action():
    channel = client.get_channel(target_channel)
    info = funding.round_one()
    await channel.send("@everyone " + "Funding paid for Okex/Binance/Bybit")
    msg = r"```"
    for index in info:
        msg += index + ": " + str(info[index]) + "\n"
    msg += r"```"
    await channel.send(msg)

async def round_one_notif():
    channel = client.get_channel(target_channel)
    info = funding.round_one()
    await channel.send("@everyone " + "30 mins till Okex/Binance/Bybit")
    msg = r"```"
    for index in info:
        msg += index + ": " + str(info[index]) + "\n"
    msg += r"```"
    await channel.send(msg)
     
async def round_two_action():
    channel = client.get_channel(target_channel)
    info = funding.round_two()
    await channel.send("@everyone" + "Funding paid for Bitmex/Huboi")
    msg = r"```"
    for index in info:
        msg += index + ": " + str(info[index]) + "\n"
    msg += r"```"
    await channel.send(msg)

async def round_two_notif():
    channel = client.get_channel(target_channel)
    info = funding.round_one()
    await channel.send("@everyone" + "30 mins till Bitmex/Huboi")
    msg = r"```"
    for index in info:
        msg += index + ": " + str(info[index]) + "\n"
    msg += r"```"
    await channel.send(msg)

@client.event
async def on_ready():
    while True:
        now = datetime.now()
        
        if now.hour in round_one_times and now.minute == 0:
            time.sleep(25)
            await round_one_action()
            time.sleep(65)
        if now.hour in round_two_times and now.minute == 0:
            time.sleep(25)
            await round_two_action()
            time.sleep(65)

        if now.hour+1 in round_one_times and now.minute == 30:
            await round_one_notif()
            time.sleep(65)
        if now.hour+1 in round_two_times and now.minute == 30:
            await round_two_notif()
            time.sleep(65)
       
        await asyncio.sleep(1)

client.run(token)


