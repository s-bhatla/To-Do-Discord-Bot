import discord
import os
from replit import db

client = discord.Client()
string = ['The todo List is : \n']
db["todos"] = string


@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('$todo'):
    words = message.content.split(' ')
    if (words[1] == 'display'):
      fstring = 'The todo List is : \n'
      for i in range(1, len(string)):
        fstring = fstring + '('+ str(i) + ') ' + string[i]
      await message.channel.send(fstring)

    if (words[1] == 'add'):
      todo = message.content[9:] + '\n'
      string.append(todo)
      db["todo"] = string
      fstring = 'The todo List is : \n'
      for i in range(1, len(string)):
        fstring = fstring + '('+ str(i) + ') ' + string[i]
      await message.channel.send(fstring)
    
    if (words[1] == 'remove'):
      if (words[2].isdigit() and int(words[2]) <= len(string)-1 and int(words[2]) != 0):
        rem = int(words[2])
        string.pop(rem)
        db["todo"] = string
        await message.channel.send('Done!')
      else : 
        await message.channel.send('Wrong Input!')
      

client.run(os.getenv('TOKEN'))

#Made a .env to store the keyfrom replit import db