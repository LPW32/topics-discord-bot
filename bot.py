import asyncio, discord, wiki_scrape, string, datetime
from discord.ext import commands

global success 
success = True

if not discord.opus.is_loaded():
    discord.opus.load_opus('/usr/lib/libopus.so')


client = discord.Client()
myownchannel = discord.Object(id='195695061319548928')
vchannel = discord.Object(id='195698520454332416')

@client.event
async def on_ready():
    await client.send_message(discord.Object(id='195695061319548928'), 'Fisto Mk. IV is now online. Hello, world!')

def is_bot(m):
    return m.author == client.user

def not_pinned(m):
    return not m.pinned

help = 'Available commands:\n!hello - Says hi!\n!ping - Tests my speed!\n!purge - Deletes all un-pinned messages!\n!purgebot - Deletes all my messages :c\n!purgeall - Deletes everything! EVERYTHING!\n!wiki [article name] - Learns you a thing!'

thebot = client.user

@client.event
async def on_message(message):
    print (message.content)
    if message.author == client.user:
        return
    elif '!hello' in message.content:
        await client.send_message(myownchannel, 'Hello, '+str(message.author)[:-5]+'!')
    elif message.content.startswith('!purgebot'):
        await client.purge_from(myownchannel, limit=500, check=is_bot)
    elif message.content.startswith('!ping'):
        start = datetime.datetime.now()
        await client.send_message(myownchannel, 'pong')
        end = datetime.datetime.now()
        delta = end - start
        total = int(delta.total_seconds() * 1000)
        await client.send_message(myownchannel, '('+str(total)+'ms)')
    elif message.content.startswith('!purgeall'):
        await client.purge_from(myownchannel, limit=500, check=None)
    elif message.content.startswith('!purge'):
        await client.purge_from(myownchannel, limit=500, check=not_pinned)
    elif message.content.startswith('!wiki'):
        if len(message.content) <= 5:
            await client.send_message(myownchannel, 'I\'m gonna need an article, bub.')
            return
        article_name = message.content[6:]
        article_name = string.capwords(article_name)
        article_name = article_name.replace(" ","_")
        await client.send_message(myownchannel, wiki_scrape.citeStrip(wiki_scrape.getWiki(article_name)))
    elif message.content.startswith('!help'):
        await client.send_message(myownchannel, help)
    elif message.content.startswith('!join'):
        voice = await client.join_voice_channel(vchannel)
        player = voice.create_ffmpeg_player('tintin.mp3')
        song = 'tintin.mp3'
        def check (m):
            try:
                if m.content.startswith('!start'):
                    player.volume = 0.15
                    player.start()
                elif m.content.startswith('!pause'):
                    player.pause()
                elif m.content.startswith('!play'):
                    player.resume()
                elif m.content.startswith('!stop'):
                    player.stop()
                elif m.content.startswith('!leave'):
                    return m
            except:
                success = False
                print (success)
                return m

        await client.wait_for_message(channel=myownchannel, author=message.author, check = check)
        await voice.disconnect()
        global success

client.run('MTk1NzQyMjE4NzE4MjgxNzI4.Ck46pQ.UWQKj-fGoD410qhwJY4coXskdXY')
