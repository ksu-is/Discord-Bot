import discord
import random
import requests
import json

TOKEN = 'YOUR_TOKEN_GOES_HERE'

client = discord.Client()

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data [0] ['q'] + " -" + json_data [0] ['a']
    return(quote)

@client.event
async def on_ready():
    print("{0.user} is now online!".format(client))

# Splits ending numbers out of username and logs chat info

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

# Keeps bot from responding to own messages
    if message.author == client.user:
        return

    if message.channel.name == 'scrappy-bot-test':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'See you later {username}!')
            return
        elif user_message.lower() == '$python-start':
            await message.channel.send(f'Get started with the newest Python version and tutorials from W3sSchools! https://www.python.org/  https://www.w3schools.com/python/')
            return
        elif user_message.lower() == '$sports':
            await message.channel.send(f'Check out upcoming KSU sporting events here! https://ksuowls.com/calendar')
            return
        elif user_message.lower() == '$random':
            response = f'This is your random number: {random.randrange(1000000)}'
            await message.channel.send(response)
            return
        elif user_message.lower() == '$joke':
            await message.channel.send(f'Owls are clearly smarter than chickens... you’ve never heard of Kentucky-fried owl!')
            return
        elif user_message.lower() == '$joke2':
            await message.channel.send(f'What is most common form of violence amongst owls? Fly-by hooting!')
            return
        elif user_message.lower() == '$inspire':
            quote = get_quote()
            await message.channel.send(quote)

client.run(TOKEN)





