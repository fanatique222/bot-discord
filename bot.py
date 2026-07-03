import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True  # Obligatoire pour détecter les nouveaux membres

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1521769165055070270) 
    if channel:
        embed = discord.Embed(
            title="🎉 Nouveau membre !",
            description=(
                f"Bienvenue {member.mention} sur **{member.guild.name}** !\n\n"
                f"👥 Tu es le **{member.guild.member_count}ᵉ membre** du serveur.\n
            ),
            color=discord.Color.blue()
        )

        if member.avatar:
            embed.set_thumbnail(url=member.avatar.url)

        embed.set_footer(text=f"ID du membre : {member.id}")

        await channel.send(embed=embed)

bot.run("TON_TOKEN")
