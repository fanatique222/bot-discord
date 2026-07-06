import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user} est en ligne !")


@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name="Membre")
    if role:
        await member.add_roles(role)

    channel = bot.get_channel(1521999167252074627)
    if channel:
        await channel.send(
            f"{member.mention} nous a rejoint, nous sommes maintenant "
            f"**{member.guild.member_count}** sur le serveur !"
        )

TOKEN = os.getenv("TOKEN")

if not TOKEN:
    print("Erreur : la variable d'environnement TOKEN n'est pas définie.")
else:
    bot.run(TOKEN)
