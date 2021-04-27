import discord
client = discord.Client()

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('$todo'):
    await message.channel.send('TODO : ')

client.run()

#Must make a .env to store the key