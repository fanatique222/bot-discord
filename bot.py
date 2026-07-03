import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} est en ligne !")

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="selem")

    if channel:
        await channel.send(
            f"👋 Selem {member.mention} sur **{member.guild.name}** !\n"
            f"👥 Nous sommes maintenant **{member.guild.member_count}** membres."
        )

bot.run(os.getenv("TOKEN"))
