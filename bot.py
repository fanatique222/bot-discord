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
        embed = discord.Embed(
            title="🎉 Bienvenue !",
            description=(
                f"Bienvenue {member.mention} sur **{member.guild.name}** !\n\n"
                f"👥 Nous sommes maintenant **{member.guild.member_count} membres**.\n"
                f"🎭 Le rôle **{role.name if role else 'Membre'}** t'a été attribué !"
            ),
            color=discord.Color.green()
        )

        if member.avatar:
            embed.set_thumbnail(url=member.avatar.url)

        embed.set_footer(text=f"ID du membre : {member.id}")

        await channel.send(embed=embed)

bot.run("TON_TOKEN_ICI")
