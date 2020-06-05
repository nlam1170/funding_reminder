import funding
import discord
import asyncio
import time
from datetime import datetime

token = r"NzE4MjI3NDQyODc5MTY4NTQz.XtmpNA.RxlUDJfdy7CW5duQBN9y9LA1lic"
target_channel = 718235792547250276
client = discord.Client()

round_one_times = [3, 11, 19]
round_one_notif_times = ['230', '1030', '1830']
round_two_times = [4, 15, 23]
round_two_notif_times = ['330', '1430', '2230']


async def round_one_action():
    channel = client.get_channel(target_channel)
    info = funding.round_one()
    await channel.send("@everyone" + "Funding paid for Okex/Binance/Bybit")
    msg = r"```"
    for index in info:
        msg += index + ": " + str(info[index]) + "\n"
    msg += r"```"
    await channel.send(msg)

async def round_one_notif():
    channel = client.get_channel(target_channel)
    info = funding.round_one()
    await channel.send("@everyone" + "30 mins till Okex/Binance/Bybit")
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
        notif_check = str(now.hour) + str(now.minute)
        
        if now.hour in round_one_times:
            time.sleep(60)
            await round_one_action()
        if now.hour in round_two_times:
            time.sleep(60)
            await round_two_action()
        if notif_check in round_one_notif_times:
            await round_one_notif()
        if notif_check in round_two_notif_times:
            await round_two_notif()

client.run(token)


