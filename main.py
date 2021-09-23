import discord
import os
from discord.ext import commands
from discord.utils import get
import random
import json
import requests
import pyjokes

from keep_alive import keep_alive


client = commands.Bot(command_prefix="=", intents=discord.Intents.all())

token = os.environ['TOKEN']

prefix = '='

insults = ["uncle ", "aunty "]

man_commands = [
"help", 
"hello", 
"roll", 
"wonk", 
"lee", 
"inspire",
"pgjoke (pg = programmer)", 
"joke", 
"votd", 
"bible", 
"poll [description",
"movie", 
"dota", 
"water", 
"ping",
"reactroles [role]"
]

# get quote from API
def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q']
    author = json_data[0]['a']

    quote += ' -' + author
    return quote


# get dad joke from API
def get_dad_joke():
    url = 'https://icanhazdadjoke.com/'
    headers = {'Accept': 'application/json'}
    response = requests.request('GET', url, headers=headers)
    json_data = json.loads(response.text)
    joke = json_data['joke']
    return joke


# get verse of the day from API
def get_votd():
    url = 'http://quotes.rest/bible/vod.json'
    response = requests.get(url)
    json_data = json.loads(response.text)

    verse = json_data['contents']['verse']
    book = json_data['contents']['book']
    chapter = json_data['contents']['chapter']
    verse_num = json_data['contents']['number']

    verse_source = book + ' ' + chapter + ':' + verse_num
    verse += '\n' + verse_source
    return verse


# get random verse from API
def get_rand_verse():
    url = 'http://quotes.rest/bible/verse.json'
    response = requests.get(url)
    json_data = json.loads(response.text)

    verse = json_data['contents']['verse']
    book = json_data['contents']['book']
    chapter = json_data['contents']['chapter']
    verse_num = json_data['contents']['number']

    verse_source = book + ' ' + chapter + ':' + verse_num
    verse += '\n' + verse_source
    return verse


# get custom server emojis given its name
async def get_emoji_by_name(emoji_name):
    emojis = await client.guilds[0].fetch_emojis()
    for emoji in emojis:
        if emoji.name == emoji_name:
            return emoji
    return None


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    username = str(message.author.name)
    user_message = str(message.content)
    channel = str(message.channel.name)
    # print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    # Greet user with insult
    if user_message == f'{prefix}hello':
        insult = random.choice(insults)
        msg = await message.channel.send(f'Hello {insult} {message.author.mention}!')
        await msg.add_reaction('👋')

    # Generate random roll
    elif user_message == f'{prefix}roll':
        rand_num = str(random.randrange(0, 100))
        emb = discord.Embed(description=f'{message.author.mention} rolled: ' + rand_num)
        await message.channel.send(embed=emb)

    # HELP Page
    elif user_message == f'{prefix}help':
        help_message = ''

        for word in man_commands:
            help_message += prefix + word + '\n'

        # getting author
        ivan = message.guild.get_member(510487613019521044)

        # styling embed
        emb = discord.Embed(title='OLDCHUNKY BOT COMMANDS',
                            description=f'⛔DO NOT CLICK ON ABOVE LINK⬆',
                            color=0x32cd32,
                            url='https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        emb.set_author(name=ivan.nick,
                       icon_url=ivan.avatar_url)
        emb.add_field(name='Prefix:', value='\"=\"', inline=False)
        emb.add_field(name='Commands:', value=f'{help_message}', inline=False)

        await message.channel.send(embed=emb)

    # Viggy Wonka
    elif user_message == f'{prefix}wonk':
        msg = await message.channel.send(f"<@!702590979181510848> no wonking! Viggy no wonking!!")
        viggy_wonka_emoji = await get_emoji_by_name('ViggyWonka')
        await msg.add_reaction(f'{viggy_wonka_emoji}')

    # Ryan Lee
    elif user_message == f'{prefix}lee':
        await message.channel.send(f"Due to a complaint from Mr Lee, this command is no longer valid. Leave the poor guy alone :(")

    # Inspirational quote
    elif user_message == f'{prefix}inspire':
        quote = get_quote()
        msg = await message.channel.send(quote)
        await msg.add_reaction('💯')

    # Programmer's joke
    elif user_message == f'{prefix}pgjoke':
        joke = pyjokes.get_joke()
        await message.channel.send(joke)

    # # Special joke for Ryan Lee
    elif user_message == f'{prefix}joke' and username == "ryanleekurisinkal":
        joke = "Ryan Lee Kurisinkal"
        robcap_emoji = await get_emoji_by_name('rob')
    
        msg = await message.channel.send(joke)
        await msg.add_reaction(f'{robcap_emoji}')

    # Dad joke
    elif user_message == f'{prefix}joke':
        joke = get_dad_joke()
        bloop_emoji = await get_emoji_by_name('bloop')
        raj_emoji = await get_emoji_by_name('RAJe')

        msg = await message.channel.send(joke)
        await msg.add_reaction(f'{bloop_emoji}')
        await msg.add_reaction(f'{raj_emoji}')

    # VOTD
    elif user_message == f'{prefix}votd':
        verse = get_votd()
        await message.channel.send(verse)

    # Random verse
    elif user_message == f'{prefix}bible':
        verse = get_rand_verse()
        await message.channel.send(verse)

    # Poll
    elif user_message.startswith(f'{prefix}poll'):
        split_message = user_message.split(' ')
        desc = split_message[1:]
        desc = ' '.join(desc)

        if desc == "":
            desc = 'No description 🤡'

        emb = discord.Embed(title="VOTE", description=f"{desc}")
        msg = await message.channel.send(embed=emb)
        await msg.add_reaction('🟢')
        await msg.add_reaction('🔴')

    # Movie ping
    elif user_message == f"{prefix}movie":
        movie_role = get(message.guild.roles, name="Movie Squad")
        msg = await message.channel.send(f'{movie_role.mention} Watch movie tonight?')
        await msg.add_reaction('✅')
        await msg.add_reaction('❌')

    # Dota ping
    elif user_message == f"{prefix}dota":
        dota_role = get(message.guild.roles, name="The Internationals")
        msg = await message.channel.send(f'{dota_role.mention} Come dota bois. Grind never stops (unless sem started)')
        await msg.add_reaction('🆗')
        await msg.add_reaction('⛔')

    # drink water
    elif user_message == f"{prefix}water":
        water_emoji = await get_emoji_by_name("woter")
        await message.channel.send(f"@here remember to drink water! {water_emoji}")

    # user ping
    elif user_message == f"{prefix}ping":
        emb = discord.Embed(title='Ping', description=f'{round(client.latency*1000)} ms')
        await message.channel.send(embed=emb)

    # react roles
    elif user_message.startswith(f"{prefix}reactroles"):
        words = user_message.split(' ')
        if len(words) != 2:
            warning = f"E.g. command: {prefix}reactrole @RoleToBeGiven"
            emb = discord.Embed(title='Invalid arguments/format', description=f'{warning}')
            await message.channel.send(embed=emb)

        role_id = words[1]
        role_id = role_id.replace('<', '')
        role_id = role_id.replace('>', '')
        role_id = role_id.replace('@', '')
        role_id = role_id.replace('&', '')
        role_id = int(role_id)

        role = get(message.guild.roles, id=role_id)

        emb = discord.Embed(title=f'{role.name}', description=f'React to get the {role.name} role!')
        msg = await message.channel.send(embed=emb)
        await msg.add_reaction('🔰')

        with open('reactrole.json') as json_file:
            data = json.load(json_file)

            new_react_role = {
            'role name':role.name,
            'role id': role.id,
            'message_id':msg.id
            }

            data.append(new_react_role)

        with open('reactrole.json', 'w') as j:
            json.dump(data, j, indent=4)


@client.event
async def on_raw_reaction_add(payload):

    if payload.member.bot:
        pass

    else:
        with open('reactrole.json') as react_file:
            data = json.load(react_file)
            for x in data:
                if x['message_id'] == payload.message_id:
                    guild = client.get_guild(payload.guild_id)
                    role = get(guild.roles, id=x['role id'])

                    await payload.member.add_roles(role)


@client.event
async def on_raw_reaction_remove(payload):

    with open('reactrole.json') as react_file:
        data = json.load(react_file)
        for x in data:
            if x['message_id'] == payload.message_id:
                guild = client.get_guild(payload.guild_id)
                role = get(guild.roles, id=x['role id'])

                guild = client.get_guild(payload.guild_id)
                user = guild.get_member(payload.user_id)
                await user.remove_roles(role)


@client.event
async def on_message_delete(message):
  deleted_message_id = message.id
  
  with open('reactrole.json') as react_file:
    data = json.load(react_file)
  
  for i in range(len(data)):
    if deleted_message_id == int(data[i]["message_id"]):
      del data[i]
      break
  
  with open('reactrole.json', 'w') as react_file:
    data = json.dump(data, react_file, sort_keys=True, indent=4)


keep_alive()
client.run(token)
