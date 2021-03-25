import discord
from discord.ext import commands
import datetime
from datetime import timedelta
import asyncio
import pytz
import sqlite3
from keep_alive import keep_alive

"""
# Set Command Prefix Here
client = commands.Bot(command_prefix="$")
"""

client = discord.Client()
botToken = 'ODIzOTE1MTQzMDQ1MzE2NjI4.YFnwxQ.840BVstv5OyabfXNjiz-ybxDw5o'

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
    day = str(datetime.datetime.now().weekday())
    cur.execute("SELECT * FROM reminder WHERE weekday=" + day)

    rows = cur.fetchall()
    return rows

def insert_reminder(db_connection):
    pass

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
    db_connection = create_connection('reminder.db')
    timetable = select_all_tasks(db_connection)
    for row in timetable:
        y=0
        for x in row:
            if y==1:
                temp_course_name = x
            elif y==3:
                tz_KL = pytz.timezone('Asia/Kuala_Lumpur')
                temp = datetime.datetime.now(tz_KL) + timedelta(hours=0, minutes=10)
                temp = temp.strftime("%H:%M:%S")
                if x > temp:
                    temp_time = x
                else:
                    temp_time = 0
            elif y==4:
                temp_target = x
            y=y+1
        while True:
          if temp_time != 0:
              tz_KL = pytz.timezone('Asia/Kuala_Lumpur')
              c_time = datetime.datetime.now(tz_KL).strftime("%H:%M:%S")
              date_time_obj = datetime.datetime.strptime(temp_time, '%H:%M:%S')
              date_time_obj = date_time_obj - datetime.timedelta(minutes=10)
              r_time = date_time_obj.strftime("%H:%M:%S")
              print(c_time)
              print(r_time)
              channel = discord.utils.get(client.guilds[0].channels, name="time-schedule-channel")
              if r_time < c_time:
                message = temp_target + "\nReminder! " + temp_course_name + " is going to start in 10mins!"
                print(message)
                await channel.send(message)
                break
              else:
                await asyncio.sleep(5)
          else:
              break
    tempDay = str(datetime.datetime.now().weekday())
    if (tempDay >= 0 and tempDay <5):
      print ("Monday to Friday")
      await asyncio.sleep(3600) 
    else:
      print("Saturday and Sunday")
      await asyncio.sleep(21600)

client.loop.create_task(reminder())

keep_alive()
client.run(botToken)