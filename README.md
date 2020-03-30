# HacKSU_Discord_Bot
*Written by Joshua Behler*
## Intro
Discord, for those who are unfamilar, is a free text and voice chatting platform. You will need a Discord account in order to make and interact with a bot. You can create an account free at their [website](https://discord.com). You can either use Discord through the Desktop Application or through the browser. Additionally, you will need Python 3.8 installed. You can download Python from [here](https://python.org).
## Creating a server
You will need to be in a server where you have admin privilegdes. If you already have a server, great! If not, here is how to create one:

1: Select the plus button on the side bar of your Discord server

2: Select the "Create a server" button

3: Name your server whatever you want, and then click "Create".

You should now have a server to work with!
## Setting up Python
In order to create your bot, you will need to install the Discord.py module. To do so, follow these steps:

1: Open up your computer's terminal. For Windows, this is Command Prompt/Powershell. For Mac and Linux, this is Linux.

2: Execute the following command:
```
pip install discord
```
If all works, the Discord.py module should install and become available for use.
## Now to create the bot
Last step before coding; we have to tell Discord to make the bot account for us. Go to the [Discord Developer Portal](https://discordapp.com/developers/applications) and follow these steps:

1: Select "New Application". This tutorial is going to make a bot that tells the time, so when prompted, name your application "Time Bot".

2: When the application is created, go to the "Bot" tab and select "Add Bot" and then "Yes, do it!"

3: Click on the "Copy" button that appears. This will copy the bot's Token to your clipboard, which is essentially the bot's username and password. Do not share this token with anyone else. 

Your bot is now created, and we can move on to the part everyone has been waiting for...
## Coding the bot
Now to write the bot. Launch your favorite IDE (Python IDLE is preferred) or Text Editor, and create a new file called "bot.py".
This is where we were be placing our bot's code.

First part is to add the include statements. By default, Python can't access the Discord.py module until we import it. Add ```import discord``` to the file. Additionally, we will also need the asyncio and datetime libraries, so add ```import asyncio``` and ```import datetime``` to the file.

Your file should now look like this:
```
import discord
import asyncio
import datetime
```
Next, what we are going to do is create a class. This class will inherit from the ```discord.Client``` class we imported earlier, which will let us have our bot do custom things. Add ```class MyClient(discord.Client):``` to the file. 

This class is where we will put all of our functions. The first function we are going to add is the ```on_message``` function. This function will be called every single time our bot "sees" a message from any user, including itself! The function to add is:
```
async def on_message(self,message):
    if(message.content.startswith("/")):
        await self.process_commands(message)
```
Notice the if statement. That if statement will only ever execute if the message that the bot sees begins with a slash. That way the bot will ignore normal conversation. Next up, we will write the ```process_commands``` function that ```on_message``` uses.

The ```process_commands``` function is going to be where we determine which command the user tried to execute. It's basically going to be a long multiway if statement that checks for various keywords. However, since our bot is only going to have one command, it will just be an if/else. Write this into your file:
```
async def process_commands(self,message):
    command = message.content.split()[0].lower()
    #Command List Here
```
Below the ```#Command List Here``` line is where we are going to put this if statement. Now, add:
```
if(command == "/time"):
    await self.give_time(message)
else:
    await message.channel.send("Invalid command: my only command is `/time`")
```
So now, whenever a user sends a message that begins with "/time", the bot will call the `give_time` command. Lets go write that function.

Your file should now look like:
```
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
```

To add the ```give_time``` function, add ```async def give_time(self,message):``` to your file. The body of the function will be the following:
```
crnt_time = datetime.datetime.now()
await message.channel.send("The current time is: " + str(crnt_time.hour)+":"+str(crnt_time.minute)+":"+str(crnt_time.second)+"!")
```
This function will find the channel that the message was sent from, and then send its own message back as a response. We use the datetime module to get the current hour, minute, and second of the day.

Your code should now look like this:
```
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
```

We are almost done! Next up, add the following code to your file. These functions tell the bot to print information to the log whever it a connection event happens, and also sets the bot's status to tell people how to use it:
```
    async def on_ready(self):
        await self.change_presence(activity=discord.Game(name = "/time"))
        print("Successfully set Bot's game status")
        
    async def on_connect(self):
        print("Bot has connected to server at time:",datetime.datetime.now())
    
    async def on_disconnect(self):
        print("Bot has disconnected from server at time:",datetime.datetime.now())
```

Lastly, we need to make sure the bot can log into Discord. Add the following bit of code to your file, and make sure to replace ```TOKEN``` with the token you copied from Discord Developer:
```
print("Starting Bot")
bot = MyClient()
bot.run("TOKEN")
```
If you have done all well, your bot should work! The last step is to invite it into your server. The completed bot code can be found in this repo, so if your bot doesn't seem to work, check there to make sure you have coded everything correctly.
## Adding to bot to a server
Navigate back to your bot's Application page and follow these steps:

1: Go to the OAuth2 tab

2: From the checklist, select "bot"

3: Copy the URL it gives you, and paste it into your browser

4: From the list of servers, select the server you want to add the bot to, and then click "Authorize". If prompted, solve a CAPTCHA.

You should now see the bot in the member list, but it will say it is offline. To fix that, save and then run the bot.py file you made. If the bot now appears online, you can try out your command! Type /time and see if it responds!
