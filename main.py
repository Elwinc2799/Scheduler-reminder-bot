import discord
from discord.ext import commands
import os
import datetime
import asyncio
import pytz
import sqlite3


def main():
    # Connect into Database
    db_connection = connect_database()
    show_table(db_connection)


def connect_database():
    db_connection = sqlite3.connect('reminder.db')
    print("Database Connected Successfully")
    return db_connection


def insert_reminder(db_connection):
    pass


if __name__ == '__main__':
    main()

"""
# Set Command Prefix Here
client = commands.Bot(command_prefix="$")
botToken = ""

@client.event
async def on_ready():
    print('Bot is Online')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


@client.event
async def set_course_reminder(message):
    if message.content.startswith('$set'):
        await message.channel.send('Set')


@client.event
async def reminder():
    while True:
        await client.wait_until_ready()
        tz_KL = pytz.timezone('Asia/Kuala_Lumpur')
        c_time = datetime.datetime.now(tz_KL).strftime("%Y-%m-%d %H:%M:%S")
        temp = datetime.datetime(year=2021, month=3, day=24, hour=11, minute=0, second=0)
        temp = temp - datetime.timedelta(minutes=10)
        r_time = temp.strftime("%Y-%m-%d %H:%M:%S")
        print(c_time)
        print(temp)
        print(r_time)
        channel = discord.utils.get(client.guilds[0].channels, name="time-schedule-channel")
        user = "everyone"
        if r_time < c_time:
            message = f"Left 10 min until {c_time}! Ready for CPC251!! @{user}."
            await channel.send(message)
            break
        await asyncio.sleep(5)


client.loop.create_task(reminder())

client.run(os.getenv('TOKEN'))
"""
