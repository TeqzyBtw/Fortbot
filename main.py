import nextcord
import requests

bot = nextcord.Client()

@bot.event
async def on_ready():
    print("bot is ready")

@bot.slash_command()
async def new(interaction: nextcord.Interaction,mode:int = nextcord.SlashOption(name="modes",choices={"Battle Royal": 1,"Save The World": 2,"Creative": 3})):
    if mode == 1:
        r = requests.get("https://fortnite-api.com/v2/news/br")
        data = r.json()
        embed = nextcord.Embed(title="Fortnite Battle Royal News")
        embed.add_field(
            name="Data",
            value=data["data"]["data"])
        embed.set_image(url=data["data"]["image"])
        await interaction.response.send(embed=embed)
    if mode == 2:
        r = requests.get("https://fortnite-api.com/v2/news/stw")
        data = r.json()
        embed = nextcord.Embed(title="Fortnite Save The World News")
        embed.add_field(
            name="Data",
            value=data["data"]["data"])
        embed.set_image(url=data["data"]["image"])
        await interaction.response.send(embed=embed)
    else:
        r = requests.get("https://fortnite-api.com/v2/news/creative")
        data = r.json()
        embed = nextcord.Embed(title="Fortnite Creative News")
        embed.add_field(
            name="Data",
            value=data["data"]["data"])
        embed.set_image(url=data["data"]["image"])
        await interaction.response.send(embed=embed)

bot.run("OTk2NDI3NDI4NTAxMTMxMjg0.GgqBxU.mriC2HIgUA1qPp5kUVBCecXn85ummcO9RH6Zcc")
