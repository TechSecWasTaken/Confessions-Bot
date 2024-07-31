import discord
import os

bot = discord.Bot(intents=discord.Intents.all())
TOKEN = os.getenv("DISCORD_TOKEN")
OWNER = os.getenv("OWNER_ID")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

@bot.slash_command()
async def send_message(ctx, message:str, anonymous:bool):
    OWNER_ID = int(OWNER)
    OWNER_USER = bot.get_user(OWNER_ID)
    SENDER = bot.get_user(ctx.author.id)

    embed=discord.Embed(title="You got mail!", color=discord.Colour.blurple())

    if not anonymous:
        embed.set_author(name=SENDER.display_name, icon_url=SENDER.avatar.url)
    else:
        embed.set_author(name="Anonymous")
    
    embed.add_field(name="Message:", value=message, inline=True)

    await OWNER_USER.send(embed=embed)
    await ctx.respond("Sent!\nResponse will delete in 3 seconds.",ephemeral=True)

bot.run(TOKEN)
