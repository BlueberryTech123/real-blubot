import discord
import asyncio

client = discord.Client()
TOKEN = "NTI0NzI5NzE1NjA5ODI5Mzg3.Dv80hA.6_m8BsTZXi8V0bvhXbEF3ALUZ3s"

@client.event
async def on_message(message):
    bot_count = 0
    if message.author == client.user:
        return
    if message.content.startswith("!ping"):
        await client.send_message(message.channel, "Pong! :ping_pong:")
    if message.content.startswith("!help"):
        embed = discord.Embed(
            description = "Help for commands. If you\'re looking for the items, ``!shop`` would do its job :briefcase:",
            colour = discord.Colour.blue()
        )
        embed.set_author(name=client.user.name,  icon_url=client.user.avatar_url)
        embed.add_field(name="Information", value="``!help`` ``!ping`` ``!serverinfo``", inline=False)
        embed.add_field(name="Currency", value="``!buyitem`` ``!credits`` ``!shop``",   inline=False)
        await client.send_message(message.channel, embed = embed)
    if message.content.startswith("!shop"):
        shopEmbed = discord.Embed(
            description = "``!buyitem`` or ``!buy`` to buy an  item.\n:inbox_tray: **Buy amount**  :outbox_tray: **Sell amount**",
            colour = discord.Colour.blue()
        )
        shopEmbed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
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
        serverInfEmbed = discord.Embed(
            title = message.server.name + "\'s Server Information",
            colour = discord.Colour.blue()
        )
        serverInfEmbed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
        serverInfEmbed.add_field(name="Members", value=str(message.server.member_count) + " members overall\n")
        serverInfEmbed.add_field(name="Emojis (Server only)", value=message.server.emojis)
        serverInfEmbed.add_field(name="Misc", value="Server ID: " + message.server.id + "\nServer owner: **" + str(message.server.owner) + "**", inline="False")
        serverInfEmbed.set_thumbnail(url=message.server.icon_url) #-----------------------------------------------------------------------------------------------------------
        await client.send_message(message.channel, embed = serverInfEmbed)
    if message.content.startswith("!stats"):
        await client.send_message(message.channel, "```Status: Online\nDiscord.py version: " + discord.__version__ + "\nGuilds: " + str(len(client.servers)) + "```")
    # TEMPORARY WIP COMMANDS
    if message.content.startswith("!credits"): await client.send_message(message.channel, "``!credits`` is currently down. This may be because this functionality is work-in-progress :smile:")
    if message.content.startswith("!buyitem") or message.content.startswith("!buy"): await client.send_message(message.channel, "``!buyitem`` is currently down. This may be because this functionality is work-in-progress :smile:")

client.run(TOKEN)
