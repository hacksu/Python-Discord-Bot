import discord
import asyncio
import datetime

class MyClient(discord.Client):

    
    async def on_message(self,message):
        if(message.content.startswith("/")):
            await self.process_commands(message)


    async def process_commands(self,message):
        command = message.content.split()[0].lower()
        #Command List Here
        if(command == "/time"):
            await self.give_time(message)
        else:
            await message.channel.send("Invalid command: my only command is `/time`")
    
    async def give_time(self,message):
        crnt_time = datetime.datetime.now()
        await message.channel.send("The current time is: " + str(crnt_time.hour)+":"+str(crnt_time.minute)+":"+str(crnt_time.second)+"!")


    async def on_ready(self):
        await self.change_presence(activity=discord.Game(name = "/time"))
        print("Successfully set Bot's game status")
        
    async def on_connect(self):
        print("Bot has connected to server at time:",datetime.datetime.now())
    
    async def on_disconnect(self):
        print("Bot has disconnected from server at time:",datetime.datetime.now())

print("Starting Bot")
bot = MyClient()
bot.run("TOKEN")
