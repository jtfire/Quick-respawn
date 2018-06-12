import discord
import asyncio
import logging


logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    await  client.change_presence(game=discord.Game(name='Come get your roles'))
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith("do you work"):
        """ simple test command"""
        await client.send_message(message.channel, "yes!!")

    elif message.content.startswith("!add roles"):
        roles_asked_for = message.content[11:]
        role_list = roles_asked_for.split(", ")
        user = message.author
        channel = message.channel
        try:
            for role in role_list:
                capital_role = role.title()
                current_role = discord.utils.get(message.server.roles, name=capital_role)
                await client.add_roles(user, current_role)
#                await client.send_message(channel, "you were just given " + str(current_role))
            await client.send_message(channel, "you should have all the roles you asked for")
        except AttributeError:
            await client.send_message(channel, "you just tried to request a role that doesn't exists")
        except discord.errors.Forbidden:
            await client.send_message(channel, "you just tried to ask for a role that i can't give you")

client.run("bot token")