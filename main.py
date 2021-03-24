import discord
import os
import datetime
import asyncio
import pytz

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

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
  while (True):
    await client.wait_until_ready()
    tz_KL = pytz.timezone('Asia/Kuala_Lumpur')
    c_time = datetime.datetime.now(tz_KL).strftime("%Y-%m-%d %H:%M:%S")
    temp = datetime.datetime(year=2021, month=3, day=24, hour=11, minute=0, second=0)
    temp = temp - datetime.timedelta(minutes = 10)
    r_time = temp.strftime("%Y-%m-%d %H:%M:%S")
    print(c_time)
    print(temp)
    print(r_time)
    channel = discord.utils.get(client.guilds[0].channels,name="time-schedule-channel")
    user = "everyone"
    if (r_time < c_time):
      message = f"Left 10 min until {c_time}! Ready for CPC251!! @{user}."
      await channel.send(message)
      break;
    await asyncio.sleep(5)

client.loop.create_task(reminder())

client.run(os.getenv('TOKEN'))