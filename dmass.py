#import discord
#from discord.ext.commands import bot
#from discord import game
#from discord.ext import commands
#import asyncio
#import platform
#import colorsys
#import random
#import time

client = commands.Bot(command_prefix = '-', case_insensitive=True)
Client = discord.client
Clientdiscord = discord.Client()

@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('--------')
    print('CREATED AND HOSTED BY INVADER OP')

@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)     
async def userinfo(ctx, user: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await client.say(embed=embed)
    
@commands.has_permissions(administrator=True)
@client.command(pass_context = True)
#async def send(ctx, *, content: str):

msg.edit("", { 
     						embed: new RichEmbed().setColor('#0099ff').setTitle("10 INVITES = 5$")
     						.setColor("#0099ff").setDescription("Invite for Free Nitro | Spotify Account | Giveway Everyday")
     						.setThumbnail('https://pbs.twimg.com/profile_images/895122980115800064/vSLIjXzk.jpg')
     						.addField("Free Discord Bot Server", "[Click Here For Invite The Bot](https://discordapp.com/oauth2/authorize?client_id=688465861802983473&permissions=8&scope=bot)")
     						.addField("Free Discord Giveway Server", "[Click Here For Server Link](https://discord.gg/setv9YD)")
     						.setFooter('Invite For Free Giveway EveryDay')
     						.setImage('https://support.discordapp.com/hc/article_attachments/360013519091/gif.gif')
     					});

#        for member in ctx.message.server.members:
#            try:
#                await client.send_message(member, content)
#                await client.say("DM Sent To : {} :white_check_mark:  ".format(member))
#            except:
#                print("can't")
#                await client.say("DM can't Sent To : {} :x: ".format(member))


client.run("Njg4NDY1ODYxODAyOTgzNDcz.Xm0waw.hY2tNjxL1mimd6A7cDLA1s3CznM")                
