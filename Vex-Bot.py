import nextcord

from nextcord.ext import commands, tasks

import json
asjda = 1142331204566270012

try:
    with open('user_data.json', 'r') as file:
        user_data = json.load(file)
except FileNotFoundError:
    user_data = {}

user_message_counts = {}

# Create a bot instance and specify the command prefix
intents = nextcord.Intents(messages=True, guilds=True, members=True)
bot = commands.Bot(command_prefix="!a", intents=intents)
level_up_channel = bot.get_channel(asjda)
import time

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

        # Check if the channel already exists, if not, create it

    # Initialize user_data for all members in the server
    for guild in bot.guilds:
        for member in guild.members:
            user_id = str(member.id)
            if user_id not in user_data:
                user_data[user_id] = {'username': member.name, 'xp': 0, 'level': 0}





import io
import aiohttp
http_session = aiohttp.ClientSession()



# Usage in your command
@bot.slash_command(name='level', description="check levels")
async def level(ctx, member: nextcord.Member = None):
    await ctx.send("Sorry, Level Is Currently being Rebuilt In discord.js")





allowed_users = [1019065963506839572, 895788406347558922]

@bot.slash_command(name='add_level', description="add some user levels")
async def set_level(ctx, member: nextcord.Member, level: int):
    if ctx.author.id not in allowed_users:
        await ctx.send('You do not have permission to use this command.')
        return
    
    user_id = str(member.id)

    if user_id not in user_data:
        await ctx.send(f'{member.display_name} is not ranked yet.')
        return

    current_xp = user_data[user_id]['xp']
    while current_xp < (level * 120):
        current_xp += 120
        user_data[user_id]['level'] += 1
    
    user_data[user_id]['xp'] = current_xp

    setlvlemb = nextcord.Embed(
        title=f"XP Added",
        description=f"{ctx.author.mention} Gave {current_xp} To {member.mention}",
    )
    guildname=ctx.guild.name
    # Send a message to the specified level up channel
    
    if level_up_channel:
        await level_up_channel.send(embed=setlvlemb)
    setlvlemb.set_author(name=guildname, icon_url="https://images-ext-1.discordapp.net/external/K1JD11UqtGrM1DzhSIxhZvfvBN37kD8a6tpHdps29mw/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1019065963506839572/cbc0a3e3ec689ee7182fd8974853bfc9.png")

    await ctx.send(f'{member.display_name}\'s level has been set to {level}. They now have {current_xp} XP.')

@bot.slash_command(name='remove_level', description="reset user level")
@commands.has_permissions(administrator=True)
async def remove_level(ctx, member: nextcord.Member = None):
    member = member or ctx.author
    user_id = str(member.id)

    if user_id not in user_data:
        await ctx.send(f'{member.display_name} is not ranked.')
        return

    # Remove user's level and XP
    del user_data[user_id]

    # Save user data (replace with your actual data storage)
    # For example, you can save it to a JSON file
    with open('user_data.json', 'w') as file:
        json.dump(user_data, file)
    guildname = ctx.guild.name
    rmvelog = nextcord.Embed(
        title=f"{ctx.guild.name}",
        description=f"{ctx.author.mention} Removed All Of {member.display_name}'s Levels And XP...."
    )
    rmvelog.set_author(name=guildname, icon_url="https://images-ext-1.discordapp.net/external/K1JD11UqtGrM1DzhSIxhZvfvBN37kD8a6tpHdps29mw/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1019065963506839572/cbc0a3e3ec689ee7182fd8974853bfc9.png")

    level_up_channel = bot.get_channel(asjda)
    if level_up_channel:
        await level_up_channel.send(embed=rmvelog)
@bot.slash_command(name="beta", description="activate some beta features :)")
async def betainquotes(ctx):
    jamie = 895788406347558922
    hsrole = 1153371272235995177
    susy = nextcord.Embed(
        title="Beta Features.",
        description=f"Hello {ctx.author.mention} You Have Requested To Enable Beta Features."
    )
    role21 = nextcord.utils.get(ctx.author.guild.roles, id=hsrole)
    await ctx.author.add_roles(role21)
    shit = ctx.author
    ihatepplfp = shit.avatar.url
    susy.add_field(name="1. Better Giveaways", value="Improved Giveaway System")
    susy.add_field(name="2. Improved Logs", value="Improved Logging System Seen In #Logs")
    susy.add_field(name="3. Better Level Up Message", value="Improved The Level Up Message")
    susy.set_footer(text="Coded by .wuid | For dsc.gg/infamousvex")
    susy.set_thumbnail(url=ihatepplfp)
    await ctx.send(embed=susy)
    
@bot.slash_command(name='replace', description="deletes every message in a channel")
@commands.has_permissions(administrator=True)
async def replace_channel(ctx):
    # Get the current channel's information
    channel = ctx.channel
    channel_name = channel.name
    channel_category = channel.category
    channel_permissions = channel.overwrites
    channel_position = channel.position

    # Create a new text channel with the same name, category, and permissions
    new_channel = await ctx.guild.create_text_channel(
        name=channel_name,
        category=channel_category,
        overwrites=channel_permissions
    )


    await new_channel.edit(position=channel_position)
    # Set the topic (description) of the new channel
    channel_description = channel.topic
    if channel_description:
        await new_channel.edit(topic=channel_description)

    # Delete the old channel
    await channel.delete()
    grabname = ctx.guild.name
    logreplace = nextcord.Embed(
        title="/replace",
        description=f"{ctx.author.mention} Has Used /replace On {channel_name}"
    )
    logreplace.set_author(name=grabname, icon_url="https://images-ext-1.discordapp.net/external/K1JD11UqtGrM1DzhSIxhZvfvBN37kD8a6tpHdps29mw/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1019065963506839572/cbc0a3e3ec689ee7182fd8974853bfc9.png")

    level_up_channel = bot.get_channel(asjda)
    if level_up_channel:
        await level_up_channel.send(embed=logreplace)
        await new_channel.send(f"```Nuked By {ctx.author.name}```")

 # Use process_message instead of process_commands

@bot.slash_command(name='reset')
async def reset(ctx):
    # Check if the user running the command has the specific user ID
    if ctx.author.id == 895788406347558922:
        # Reset the levels of all users
        for user_id in user_data:
            user_data[user_id]['xp'] = 0
            user_data[user_id]['level'] = 0
        
        # Save the updated user data (you can save it to a file here)
        
        await ctx.send("All user levels have been reset.")
    else:
        await ctx.send("You do not have permission to run this command.")

@bot.slash_command(name="yturl", description="/help fo more")
async def SHOTTY(ctx):
    sh = random.choice('asdfghjklqwertyuiopzxcvbnm-_')
    sh1 = random.choice('asdfghjklqwertyuiopzxcvbnm-_')
    sh2 = random.choice('asdfghjklqwertyuiopzxcvbnm-_')
    sh7 = random.choice('asdfghjklqwertyuiopzxcvbnm-_')
    sh5 = random.choice('asdfghjklqwertyuiopzxcvbnm-_')
    sh4 = random.choice('asdfghjklqwertyuiopzxcvbnm-_')
    sh3 = random.choice('asdfghjklqwertyuiopzxcvbnm-_')
    shutthefuckupdawg = random.randrange(2, 69)
    shh = random.choice('_-')
    stfud = str(shutthefuckupdawg)
    haha = sh+sh2+sh1+sh4+shh+sh3+sh5+sh7+stfud
    await ctx.send("https://www.youtube.com/watch?v=" + haha)
lvl5role = 1145894669406978138
lvl10role = 1145894755537006612
lvl20role = 1145894829646163968
lvl50role = 1145894998945058896

@bot.slash_command()
async def urban(ctx, *, search_query):
    try:
        response = requests.get(f"https://api.urbandictionary.com/v0/define?term={search_query}")
        if response.status_code == 200:
            data = response.json()
            if data["list"]:
                # Take the first definition from the response
                definition = data["list"][0]["definition"]
                example = data["list"][0]["example"]

                # Send the definition and example as a message
                embed = nextcord.Embed(title=f"Urban Dictionary Definition: {search_query}")
                embed.add_field(name="Definition", value=definition, inline=False)
                embed.add_field(name="Example", value=example, inline=False)
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"No definitions found for '{search_query}' on Urban Dictionary.", ephemeral=True)
        else:
            await ctx.send("An error occurred while fetching data from Urban Dictionary.")
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")


iloveawd = 1153529619643904140
time_minutes = 5  # Adjust the time limit in minutes here
import time
@bot.event
async def on_message(message):
    if message.author.bot:
        return  # Ignore messages from bots

    author_id = str(message.author.id)
    current_time = time.time()

    # Check if the user has sent messages recently
    if author_id in user_message_counts:
        last_message_time, message_count = user_message_counts[author_id]
        memberperson = message.author
        time.sleep(100)
        # Check if the user has sent 4 or more messages in less than the specified time limit
        if current_time - last_message_time < time_minutes * 60 and message_count >= 8:
            total = datetime.utcnow() + timedelta(minutes=5)  # Timeout for 30 minutes
            await memberperson.timeout(until=total, reason="spamming")
            msganti = bot.get_channel(iloveawd)
            await msganti.send(f"{memberperson.mention}, Has Been Spamming Since {datetime.utcnow()} UTC")
            # You can customize this part to handle spam as needed
            await message.channel.send(f"{message.author.mention}, stop spamming!", ephemeral=True)
            return

        # Update the user's message count and timestamp
        user_message_counts[author_id] = (current_time, message_count + 1)
    else:
        # Initialize the user's message count and timestamp
        user_message_counts[author_id] = (current_time, 1)

    # Add XP to the user for each message sent (adjust as needed)
    if author_id not in user_data:
        user_data[author_id] = {'xp': 0, 'level': 0}
    user_data[author_id]['xp'] += 6

    # Calculate the amount of XP needed for the next level
    next_level_xp = (user_data[author_id]['level'] + 1) * 120

    # Check if the user has leveled up
    if user_data[author_id]['xp'] >= next_level_xp:
        user_data[author_id]['level'] += 1

        # Increase XP requirement every 2 levels
        if user_data[author_id]['level'] % 2 == 0:
            next_level_xp += 120
        main = bot.get_channel(1166672384934285353)
        
        embed = nextcord.Embed(
            title=f'{message.author.display_name} has leveled up!',
            description=f'Congratulations, {message.author.mention}! You are now level {user_data[author_id]["level"]}!',
            color=nextcord.Color.green()  # You can adjust the color as needed
        )
        await main.send(embed=embed)

        # Check and assign roles based on user level
        member = message.author
        if user_data[author_id]['level'] >= 5:
            # Assign roles for level 5+
            role5 = nextcord.utils.get(member.guild.roles, id=lvl5role)
            await member.add_roles(role5)

            if user_data[author_id]['level'] >= 10:
                # Assign roles for level 10+
                role10 = nextcord.utils.get(member.guild.roles, id=lvl10role)
                await member.add_roles(role10)

            if user_data[author_id]['level'] >= 20:
                # Assign roles for level 20+
                role20 = nextcord.utils.get(member.guild.roles, id=lvl20role)
                await member.add_roles(role20)

            if user_data[author_id]['level'] >= 50:
                # Assign roles for level 50+
                role50 = nextcord.utils.get(member.guild.roles, id=lvl50role)
                await member.add_roles(role50)

    # Save user data to the file
    with open('user_data.json', 'w') as file:
        json.dump(user_data, file)

    await bot.process_commands(message)

# Set up your bot with the desired command prefix





@bot.slash_command(name='leaderboard', description="check the best")
async def leaderboard(ctx):
    sorted_users = sorted(user_data.items(), key=lambda x: x[1]['xp'], reverse=True)
    max_entries = min(10, len(sorted_users))  # Limit to 10 entries or less if there are fewer users
    
    embed = nextcord.Embed(title='Leaderboard')
    
    for index, (user_id, data) in enumerate(sorted_users[:max_entries], start=1):
        user = ctx.guild.get_member(int(user_id))
        if user and not user.bot:
            display_name = data.get('display_name', user.display_name)  # Use display_name
            embed.add_field(
                name=f'{index}. {display_name}',
                value=f'Level: {data["level"]} | XP: {data["xp"]}',
                inline=False
            )
    
    await ctx.send(embed=embed)

@bot.slash_command(name="serverinfo", description="view some info my bottom q")
async def haxinstalled(ctx):
    siemb= nextcord.Embed(
        title=f"{ctx.guild.name} Info.",
        description=f" **About** "
    )
    role_mentions = [role.mention for role in ctx.guild.roles]
    role_mentions_part1 = role_mentions[:len(role_mentions) // 2]
    role_mentions_part2 = role_mentions[len(role_mentions) // 2:]
    server= ctx.guild
    
    # Initialize variables
    invitelink = None
    vccount = 0
    tccount = 0
    tccount = len(server.text_channels)
    vccount = len(server.voice_channels)
    # Iterate through voice channels
    for voice_channel in server.voice_channels:
          # Increment the voice channel count

        # Check if the voice channel name contains "https://"
        if "https://" in voice_channel.name:
            invitelink = voice_channel.name
            break 
    servericon=ctx.guild.icon.url
    siemb.set_footer(text=f'{ctx.author.display_name} Requested This.', icon_url=f'{ctx.author.avatar.url}')
    siemb.add_field(name=f"Owner :", value=f"{ctx.guild.owner.mention}", inline=True)
    siemb.add_field(name=f"**Members :**", value=f"{ctx.guild.member_count}" )
    siemb.add_field(name=f"Created At :", value=f"{server.created_at.strftime('%Y-%m-%d')}")
    siemb.set_thumbnail(url=servericon)
    siemb.add_field(name="ID :", value=f"{server.id}")
    siemb.add_field(name="Boost Count :", value=f"{server.premium_subscription_count}")
    siemb.add_field(name="Rules :", value=f'{server.rules_channel}')
    siemb.add_field(name=" ", value=' '.join(role_mentions_part2), inline=False)
    siemb.add_field(name=" ", value=' '.join(role_mentions_part1), inline=False)
    siemb.add_field(name="System Channel :", value=f'{server.system_channel}')
    siemb.add_field(name="Invite Link :", value=f'{invitelink}')
    siemb.add_field(name="Channels :", value=f'VCs = {vccount}, Text Channels = {tccount}')
    si2emb = nextcord.Embed(
        title=f' ',
        description=' '
    )

    await ctx.send(embed=siemb)



@bot.slash_command(name="members", description='membercount')
async def mcount(ctx):
    mcemb = nextcord.Embed(
        title="Member Count",
        description=f'Members : {ctx.guild.member_count}'
    )
    await ctx.send(embed=mcemb)

import asyncio
import datetime 




@bot.slash_command(name='updateusr', description="update your username on the leaderboard.")
async def update_username(ctx):
    author_id = str(ctx.author.id)
    
    if author_id not in user_data:
        await ctx.send(f'<@{ctx.author.id}> is not ranked yet.')
        return
    
    user_data[author_id]['username'] = ctx.author.name
    
    with open('user_data.json', 'w') as file:
        json.dump(user_data, file)
    
    with open('user_data.json', 'r') as file:
        user_data = json.load(file)

    await ctx.send(f'Your username has been updated to {ctx.author.name}.')

# Define a simple command
@bot.slash_command(name='hello', description="hi!")
async def hello(ctx):
    await ctx.send(f'Hello {ctx.user.mention}, How Is Your Day?')


@bot.slash_command(name="say", description="say stuff")
async def sayshit(ctx, msg: str):
    sayemb = nextcord.Embed(
        title=f"{ctx.author.name} Said :",
        description=msg,
    )
    sayemb.set_footer(text="coded by .wuid")
    await ctx.send(embed=sayemb)
from datetime import datetime, timedelta
bot.giveaway_message = None

@bot.slash_command(description="create a giveaway :)")
@commands.has_permissions(manage_nicknames=True)
async def gmake(ctx, duration: int, *, prize: str):
    ongdigga = ctx.author.mention
    current_time = datetime.utcnow()
    end_time = current_time + timedelta(seconds=duration)  # Calculate end time

    embed = nextcord.Embed(
        title='🎉 Giveaway',
        description=f'Prize: {prize}\n Hosted By {ongdigga}\n Ends At: {end_time.strftime("%H:%M UTC")}',
        color=nextcord.Color.gold()
    )
    embed.set_footer(text=f'https://dsc.gg/infamousvex | Coded By .wuid')
    embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon.url)
    giveaway_message = await ctx.send("Giveaway!", embed=embed)
    await giveaway_message.add_reaction('🎉')

    await asyncio.sleep(duration)

    # Get updated message from server
    giveaway_message = await ctx.fetch_message(giveaway_message.id)

    participants = [user for reaction in giveaway_message.reactions if str(reaction.emoji) == '🎉' for user in await reaction.users().flatten()]
    if participants:
        winner = random.choice(participants)
        if winner == ctx.author.bot:
            winner = random.choice(participants)
        # Create a new embed with desired changes
        new_embed = nextcord.Embed(
            title="🎉 Giveaway Ended",
            description=f"Prize: {prize}\n Hosted By {ongdigga}\n Ended At: {end_time.strftime('%Y-%m-%d %H:%M:%S UTC')}\n Winner: {winner.mention}",
        )
        new_embed.set_footer(text=f'https://dsc.gg/infamousvex | Coded By .wuid')
        new_embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon.url)

        # Edit the message with the new embed
        await giveaway_message.edit(embed=new_embed)
        await ctx.send(f'Congratulations to {winner.mention}! You won: {prize}')
    else:
        await ctx.send('No one participated in the giveaway. Better luck next time!')





@bot.slash_command(name="help", description="get some help..")
async def helpembed(ctx):
    emb = nextcord.Embed(
        title="Help Command.",
        description=" ",
    )
    emb.add_field(name="/yturl", value="Random YT URL - May Have NSFW")
    emb.add_field(name="/gmake", value="make those G's MY DUDE!")
    emb.add_field(name="/leaderboard", value="Leader The Board")
    emb.add_field(name="/level", value="view ur level")
    emb.add_field(name="/say", value="say stuff")
    emb.add_field(name="/ban", value="Bans Mentioned User.")
    emb.set_footer(text="coded by .wuid")
    emb.add_field(name="/kick", value="Kicks Mentioned User.")
    emb.add_field(name="/timeout", value="Timeout Mentioned User.")
    emb.set_thumbnail(url="https://images-ext-1.discordapp.net/external/K1JD11UqtGrM1DzhSIxhZvfvBN37kD8a6tpHdps29mw/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1019065963506839572/cbc0a3e3ec689ee7182fd8974853bfc9.png")
    await ctx.send(embed=emb)
@bot.slash_command(name="ban", description="banned by (admin name here)")
@commands.has_permissions(ban_members=True)
async def banuser(ctx, toban: nextcord.Member):
    banemb = nextcord.Embed(
        title="Banned",
        description=toban,
    )
    banemb.set_footer(text="coded by .wuid")
    try:
        await toban.ban()
        await ctx.send(embed=banemb)
    except nextcord.Forbidden:
        await ctx.send("Invaild Perms.")
from datetime import datetime, timedelta
@bot.slash_command(name="kick", description="cant kick meeeeee")
@commands.has_permissions(kick_members=True)
async def kickuser(ctx, tokick: nextcord.Member):
    kickemb = nextcord.Embed(
        title=f" Kicked {tokick}",
        description=" "
    )
    kickemb.set_footer(text="coded by .wuid")
    await tokick.kick()
    await ctx.send(embed=kickemb)
@bot.slash_command(name="timeout", description="timeout in minutes.")
@commands.has_permissions(kick_members=True)
async def timemeoutpls(ctx, user1: nextcord.Member, *, time: int):
    timeoutemb = nextcord.Embed(
        title=f" Muted {user1}",
        description=f"For {time} minutes.",
    )
    total = datetime.utcnow() + timedelta(minutes=time)
    await user1.timeout(until=total, reason="dsc.gg/infamousvex, coded by .wuid")
    await ctx.send(embed=timeoutemb)
import requests
WEBHOOK_URL = "https://discord.com/api/webhooks/1147849980716011612/EIkoFqq7xaaZDguuKFjaIdfDbrPZFju8yTAmhTEJeFLNUk89W1MwxZth4RqwYVQSY_ro"
@bot.slash_command()
async def suggest(ctx, *, suggestion):
    # Send the suggestion to the webhook URL
    payload = {"content": f"Suggestion from {ctx.author.mention}: {suggestion}"}
    response = requests.post(WEBHOOK_URL, json=payload)

    if response.status_code == 204:
        await ctx.send("Suggestion sent successfully.")
    else:
        await ctx.send("Failed to send suggestion to the webhook.")

@bot.slash_command()
async def bug_report(ctx, *, bugtoreport):
    # Send the suggestion to the webhook URL
    payload = {"content": f"Bug Report from {ctx.author.mention}: {bugtoreport}"}
    response = requests.post(WEBHOOK_URL, json=payload)

    if response.status_code == 204:
        await ctx.send("Thanks For Reporting Bugs!")
    else:
        await ctx.send("Error, DM .wuid Or Join discord.gg/9zhh9wykhH For Help.")

@bot.event
async def on_member_join(member):
    # Get the welcome channel by ID (replace with your channel ID)
    welcome_channel = bot.get_channel(1147103036079083562)
    
    welemb = nextcord.Embed(
        title=f"Welcome {member.display_name}, We Hope You Enjoy The Server!",
        description=" ",
    )
    welemb.add_field(name="1.", value="Read <#1069549812833325146>")
    welemb.add_field(name="2.", value="Read <#1069549814368448573>")
    welemb.set_footer(text="dsc.gg/infamousvex | Coded By .wuid")
    welemb.set_thumbnail(url=f'{member.avatar.url}')

    if welcome_channel:
        # Send a welcome message in the specified channel
        await welcome_channel.send(f'{member.mention}', embed=welemb)

import time

allowed_channels = {}
startenabled = False
import random
import asyncio


# Run the bot with your token
bot.run('')
