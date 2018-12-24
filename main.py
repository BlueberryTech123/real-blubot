import discord
import asyncio

client = discord.Client()
TOKEN = "AlEgItToKeN"

#emoji_credits = discord.Emoji(
#    name="CREDITS",
#    id=526481493464317962
#)

@client.event
async def on_message(message):
    bot_count = 0
    if message.author == client.user:
        return
    if message.content.startswith("!ping"):
        await client.send_typing(message.channel)
        await client.send_message(message.channel, "Pong! :ping_pong:")
    if message.content.startswith("!help"):
        await client.send_typing(message.channel)
        embed = discord.Embed(
            description = "Help for commands. If you\'re looking for the items, ``!shop`` would do its job :briefcase:",
            colour = discord.Colour.blue()
        )
        embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
        embed.add_field(name="Information", value="``!botinfo`` ``!help`` ``!ping`` ``!serverinfo``", inline=False)
        embed.add_field(name="Currency", value="``!buyitem`` ``!credits`` ``!profile`` ``!shop``",   inline=False)
        await client.send_message(message.channel, embed = embed)
    if message.content.startswith("!shop"):
        await client.send_typing(message.channel)
        shopEmbed = discord.Embed(
            description = "``!buyitem`` or ``!buy`` to buy an  item.\n:inbox_tray: **Buy amount**  :outbox_tray: **Sell amount**",
            colour = discord.Colour.blue()
        )
        shopEmbed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
        shopEmbed.add_field(name="Items", value=":inbox_tray: $1 :outbox_tray: $1   :cheese: - **Rotten Cheese**\n:inbox_tray: $10 :outbox_tray: $8   :alembic: - **Silverfish remover**\n:inbox_tray: $50 :outbox_tray: $40   :pick: - **Pickaxe**\n:inbox_tray: $51 :outbox_tray: $41   :fishing_pole_and_fish: - **Fishing Rod**\n:inbox_tray: $55 :outbox_tray: $44   :wrench: - **Wrench**\n:inbox_tray: $100 :outbox_tray: $80   :8ball: - **8ball**\n:inbox_tray: $1050 :outbox_tray: $870   :computer: - **Laptop**\n:inbox_tray: $1050 :outbox_tray: $870   :iphone: - **Smartphone**\n:inbox_tray: $2000 :outbox_tray: $1600   :tv: - **TV**\n:inbox_tray: $3000 :outbox_tray: $2999   :blue_car: - **Car**\n:inbox_tray: $5000 :outbox_tray: $4999   :rocket: - **Spaceship**", inline=False)
        shopEmbed.add_field(name="Earnable Items", value="\n:inbox_tray: $N/A :outbox_tray: $N/A   :shrimp: - **Silverfish**\n:inbox_tray: $N/A :outbox_tray: $10   :house: - **House Upgrade**\n:inbox_tray: $N/A :outbox_tray: $12   :fish: - **Fish**\n:inbox_tray: $N/A :outbox_tray: $15   :herb: - **Twigs**\n:inbox_tray: $N/A :outbox_tray: $15   :evergreen_tree: - **Tree Logs**\n:inbox_tray: $N/A :outbox_tray: $100   :gift: - **Lootbox**\n:inbox_tray: $N/A :outbox_tray: $500   :gem: - **Diamond**\n:inbox_tray: $N/A :outbox_tray: $510   :shell: - **Fossil**\n:inbox_tray: $N/A :outbox_tray: $90000   :sparkles: - **Stardust**", inline=False)
        await client.send_message(message.channel, embed = shopEmbed)
    if message.content.startswith("!serverinfo"): # --------------------------------------
        # ---------------------------------------------------------------------------------
        # apply bot count
        #for i in message.server.members:
        #    if i == i.user.bot:
        #        bot_count = bot_count + 1
        # ---------------------------------------------------------------------------------
        await client.send_typing(message.channel)
        serverInfEmbed = discord.Embed(
            title = message.server.name + "\'s Server Information",
            colour = discord.Colour.blue()
        )
        serverInfEmbed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
        serverInfEmbed.add_field(name="Members", value=str(message.server.member_count) + " members")
        serverInfEmbed.add_field(name="Emojis (Server only)", value=message.server.emojis)
        serverInfEmbed.add_field(name="Misc", value="Server ID: " + message.server.id + "\nServer owner: **" + str(message.server.owner) + "**", inline="False")
        serverInfEmbed.set_thumbnail(url=message.server.icon_url) #-----------------------------------------------------------------------------------------------------------
        await client.send_message(message.channel, embed = serverInfEmbed)
    if message.content.startswith("!botinfo"):
        await client.send_typing(message.channel)
        await client.send_message(message.channel, "```Status: Online\nDiscord.py version: " + discord.__version__ + "\nGuilds: " + str(len(client.servers)) + "\nWebcosket Gateway: " + str(client.ws) + "```")
    if message.content.startswith("!profile"):
        await client.send_typing(message.channel)
        profileEmbed = discord.Embed(
            title = str(message.author) + "\'s profile card",
            colour = discord.Colour.blue()
        )
        profileEmbed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
        profileEmbed.set_thumbnail(url=message.author.avatar_url)
        profileEmbed.add_field(name="Currency Info", value="<:CREDITS:526481493464317962> 0")
        profileEmbed.add_field(name="Badges", value=":credit_card:")
        profileEmbed.add_field(name="Other Information", value="<:XP:526481594005979137> 0/1\n<:LVL:526481522534907904> 0\n<:HP:526481508949557250> None")
        await client.send_message(message.channel, embed = profileEmbed)
    # TEMPORARY WIP COMMANDS
    if message.content.startswith("!credits"):
        await client.send_typing(message.channel)
        await client.send_message(message.channel, "``!credits`` is currently down. This may be because this functionality is work-in-progress :smile:")
    if message.content.startswith("!buyitem") or message.content.startswith("!buy"):
        await client.send_typing(message.channel)
        await client.send_message(message.channel, "``!buyitem`` is currently down. This may be because this functionality is work-in-progress :smile:")

client.run(TOKEN)
