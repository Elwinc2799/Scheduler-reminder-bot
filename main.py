import discord
from discord.ext import commands
import datetime
from datetime import timedelta
import asyncio
import pytz
import sqlite3
from keep_alive import keep_alive
import extra

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


def select_all_tasks(conn, counter):
    cur = conn.cursor()
    tz_KL = pytz.timezone('Asia/Kuala_Lumpur')
    day = str(datetime.datetime.now(tz_KL).weekday() + counter)
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

    elif message.content.startswith('$quote'):
        await message.channel.send(extra.chooseQuote())

    elif message.content.startswith('$dice'):
        channel = message.channel
        def check(m):
            return m.author == message.author

        try:
            await message.channel.send('Player 1: ')
            player1 = await client.wait_for('message', timeout=30, check=check)
            if player1 != '':
                await channel.send('Player 2: ')
                player2 = await client.wait_for('message', timeout=30, check=check)
                if player2 != '':
                    await channel.send(extra.playDice(player1.content, player2.content))
        except asyncio.TimeoutError:
            await channel.send('Timeout to input name')

    elif message.content.startswith('$mudae'):
        await message.channel.send('Mudae is noob! Dont use Mudae!')

    elif message.content.startswith('$next'):
        db_connection = create_connection('reminder.db')
        timetable = select_all_tasks(db_connection, 0)
        num = 0
        for row in timetable:
            y = 0
            temp_n = ""
            temp_t = 0
            temp_tg = ""
            for x in row:
                if y == 1:
                    temp_n = x
                elif y == 3:
                    tz_KL = pytz.timezone('Asia/Kuala_Lumpur')
                    temp = datetime.datetime.now(tz_KL).strftime("%H:%M:%S")
                    tempX = datetime.datetime.strptime(x, '%H:%M:%S') - timedelta(hours=0, minutes=10)
                    tempX = tempX.strftime("%H:%M:%S")
                    if tempX > temp:
                        temp_t = x
                    else:
                        temp_t = 0
                elif y == 4:
                    temp_tg = x
                y = y + 1
            if temp_t != 0:
                await message.channel.send("Next course: " + temp_n + "\nStart: " + temp_t + "\nAttendees: " + temp_tg)
                break
            else:
                num = num + 1
        if num == len(timetable):
            await message.channel.send("There are no more classes for today. Yay~")

    elif message.content.startswith('$tmr'):
        db_connection = create_connection('reminder.db')
        timetable = select_all_tasks(db_connection, 1)
        num = 0
        for row in timetable:
            y = 0
            temp_n = ""
            temp_t = 0
            temp_tg = ""
            for x in row:
                if y == 1:
                    temp_n = x
                elif y == 3:
                    temp_t = x
                elif y == 4:
                    temp_tg = x
                y = y + 1
            if temp_t != 0:
                await message.channel.send("Next course: " + temp_n + "\nStart: " + temp_t + "\nAttendees: " + temp_tg)
                break
            else:
                num = num + 1
        if num == len(timetable):
            await message.channel.send("There are no more classes for tomorrow. Yay~")


@client.event
async def reminder():
    while True:
        await client.wait_until_ready()
        tz_KL = pytz.timezone('Asia/Kuala_Lumpur')
        tempDay = datetime.datetime.now(tz_KL).weekday()
        print(tempDay)
        if 0 <= tempDay < 5:
            print("Monday to Friday")
            db_connection = create_connection('reminder.db')
            timetable = select_all_tasks(db_connection, 0)
            for row in timetable:
                y = 0
                for x in row:
                    if y == 1:
                        temp_course_name = x
                    elif y == 3:
                        tz_KL = pytz.timezone('Asia/Kuala_Lumpur')
                        temp = datetime.datetime.now(tz_KL).strftime("%H:%M:%S")
                        tempX = datetime.datetime.strptime(x, '%H:%M:%S') - timedelta(hours=0, minutes=10)
                        tempX = tempX.strftime("%H:%M:%S")
                        if tempX > temp:
                            temp_time = x
                        else:
                            temp_time = 0
                    elif y == 4:
                        temp_target = x
                    y = y + 1
                while True:
                    if temp_time != 0:
                        tz_KL = pytz.timezone('Asia/Kuala_Lumpur')
                        c_time = datetime.datetime.now(tz_KL).strftime("%H:%M:%S")
                        date_time_obj = datetime.datetime.strptime(temp_time, '%H:%M:%S')
                        date_time_obj = date_time_obj - timedelta(minutes=10)
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
            await asyncio.sleep(3600)
        else:
            print("Saturday and Sunday")
            await asyncio.sleep(3600)


client.loop.create_task(reminder())

keep_alive()
client.run(botToken)