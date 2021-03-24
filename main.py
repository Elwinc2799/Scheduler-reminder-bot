import discord
from discord.ext import commands
import os
import datetime
import asyncio
import pytz
import sqlite3

"""
# Set Command Prefix Here
client = commands.Bot(command_prefix="$")
"""

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Database Connected Successfully")
    except sqlite3.Error as e:
        print(e)
    return conn

def select_all_tasks(conn):
    cur = conn.cursor()
    day = str(datetime.datetime.now().weekday().__add__(1))
    cur.execute("SELECT * FROM reminder WHERE weekday=" + day)

    rows = cur.fetchall()
    return rows

def insert_reminder(db_connection):
    pass

def main():
    # Connect into Database
    db_connection = create_connection('reminder.db')
    #timetable = select_all_tasks(db_connection)

if __name__ == '__main__':
    main()

client = discord.Client()
botToken = 'ODIzOTE1MTQzMDQ1MzE2NjI4.YFnwxQ.840BVstv5OyabfXNjiz-ybxDw5o'

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
    db_connection = create_connection('reminder.db')
    timetable = select_all_tasks(db_connection)
    for row in timetable:
        y=0
        for x in row:
            if y==1:
                v_time = x
            elif y==2:
                v_message = x
            elif y==4:
                v_channel = x
            y=y+1

        while True:
            await client.wait_until_ready()
            tz_KL = pytz.timezone('Asia/Kuala_Lumpur')
            c_time = datetime.datetime.now(tz_KL).strftime("%H:%M:%S")
            date_time_obj = datetime.datetime.strptime(v_time, '%H:%M:%S')
            date_time_obj = date_time_obj - datetime.timedelta(minutes=10)
            r_time = date_time_obj.strftime("%H:%M:%S")
            print(c_time)
            print(r_time)
            channel = discord.utils.get(client.guilds[0].channels, name=v_channel)
            user = "everyone"
            if r_time < c_time:
                message = v_message + f" @{user}."
                print(message)
                # await channel.send(message)
                break
            await asyncio.sleep(5)

client.loop.create_task(reminder())

client.run(botToken)