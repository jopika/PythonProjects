import discord
import asyncio

DEBUG = False
token = ""

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    print(message.author.name)
    if (message.author.id != "315355771200208908") and (message.content.startswith('!')):
        commandString = message.content.split()
        command = commandString[0][1:]
        await func_dict.get(command, invalidCommand)(message)
        if DEBUG:
            await client.send_message(message.channel, message.content)


async def help(message):
    await client.send_message(message.author, "-------")
    await client.send_message(message.author, "!help - gives you this message")
    await client.send_message(message.author, "-------")

async def invalidCommand(message):
    await client.send_message(message.channel, "Invalid command, use !help for list of commands")

async def listRoles(message):
    server = message.server
    for role in server.roles:
        await client.send_message(message.channel, role)

async def addRole(message):
    roleList = message.content.split()[1:]
    for role in message.server.roles[1:]:
        if str(role) in roleList:
            await client.add_roles(message.author, role)
    await client.send_message(message.channel, "done!")

async def removeRole(message):
    roleList = message.content.split()[1:]
    for role in message.server.roles[1:]:
        if str(role) in roleList:
            await client.remove_roles(message.author, role)
    await client.send_message(message.channel, "done!")


async def quit(message):
    stringOfRoles = [str(x) for x in message.author.roles]
    if 'admin' in stringOfRoles:
        if DEBUG:
            await client.send_message(message.channel, "Shutting down")
        await client.close()
    else:
        if DEBUG:
            await client.send_message(message.channel, "Not authorized to use this command!")

func_dict = {'help':help, 'addRole':addRole, 'listRoles': listRoles, 'quit':quit, 'removeRole': removeRole}

client.run(token)
client.close()