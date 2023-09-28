import discord
from discord.ext import commands
import datetime

bot = discord.Bot()
token="getgood"
@bot.event
async def on_ready():
	print("ready")
	
	
@bot.command(name="hi", description="hey hi hello")
async def hello(ctx):
	await ctx.respond(f"{ctx.author.mention} Hello!")
	
@bot.command(name="ban", description="ban members")
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member):
    await user.ban()
    await ctx.respond(f"Banned {user.mention}")
    
@bot.command(name="timeout", description="timeout in minutes.")
@commands.has_permissions(kick_members=True)
async def timemeoutpls(ctx, user1: discord.Member, *, time: int):
    timeoutemb = discord.Embed(
        title=f" Muted {user1}",
        description=f"For {time} minutes.",
    )
    total = datetime.datetime.utcnow() + timedelta(minutes=time)
    await user1.timeout(until=total, reason="coded by .wuid")
    await ctx.respond(embed=timeoutemb)

@bot.command()
async def ping(ctx):
    await ctx.send('Pong! {0}'.format(round(bot.latency, 1)))
	
bot.run(token)
