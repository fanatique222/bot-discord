import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True  # Obligatoire pour détecter les nouveaux membres

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_member_join(member):
    # Donne un rôle automatiquement
    role = discord.utils.get(member.guild.roles, name="Membre")
    if role:
        await member.add_roles(role)

    # Salon de bienvenue
    channel = bot.get_channel(1521999167252074627) 
    if channel:
        embed = discord.Embed(
            title="🎉 Bienvenue !",
            description=(
                f"Bienvenue {member.mention} sur **{member.guild.name}** !\n\n"
                f"👥 Nous sommes maintenant **{member.guild.member_count} membres**.\n"
                f"🎭 Le rôle **{membre}** t'a été attribué !"
            ),
            color=discord.Color.green()
        )

        if member.avatar:
            embed.set_thumbnail(url=member.avatar.url)

        await channel.send(embed=embed)

        embed.set_footer(text=f"ID du membre : {member.id}")

        await channel.send(embed=embed)

bot.run("TON_TOKEN")
