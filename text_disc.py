import funding
import discord
import asyncio
import time
from datetime import datetime

token = r"DISCORD_TOKEN"
target_channel = 718555773789011979
client = discord.Client()

round_one_times = [3, 11, 19]
round_two_times = [7, 15, 23]


async def round_one_action():
    channel = client.get_channel(target_channel)
    info = funding.round_one_info()
    msg = "@everyone Funding paid for Okex/Binance/Bbybit\n```"
    for index in info:
        msg += index + ": " + str(info[index]) + "\n"
    msg += "```"
    await channel.send(msg)

async def round_one_notif():
    channel = client.get_channel(target_channel)
    info = funding.round_one_info_notif()
    msg = "@everyone 30 mins till Okex/Binance/Bybit\n```"
    for index in info:
        msg += index + ": " + str(info[index]) + "\n"
    msg += "```"
    await channel.send(msg)
     
async def round_two_action():
    channel = client.get_channel(target_channel)
    info = funding.round_two_info()
    msg = "@everyone Funding paid for Bitmex/Huboi\n```"
    for index in info:
        msg += index + ": " + str(info[index]) + "\n"
    msg += "```"
    await channel.send(msg)

async def round_two_notif():
    channel = client.get_channel(target_channel)
    info = funding.round_two_info_notif()
    msg = "@everyone 30 mins till Bitmex/Huboi\n```"
    for index in info:
        msg += index + ": " + str(info[index]) + "\n"
    msg += r"```"
    await channel.send(msg)

@client.event
async def on_ready():
    while True:
        now = datetime.now()
        
        if now.hour in round_one_times and now.minute == 0:
            await asyncio.sleep(25)
            await round_one_action()
            await asyncio.sleep(60)
            continue
        if now.hour in round_two_times and now.minute == 0:
            await asyncio.sleep(25)
            await round_two_action()
            await asyncio.sleep(60)
            continue

        if now.hour+1 in round_one_times and now.minute == 30:
            await round_one_notif()
            await asyncio.sleep(70)
            continue
        if now.hour+1 in round_two_times and now.minute == 30:
            await round_two_notif()
            await asyncio.sleep(70)
            continue
       
        await asyncio.sleep(1)

client.run(token)


