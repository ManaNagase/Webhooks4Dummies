#Setup
import discord
from discord_webhook import DiscordWebhook, DiscordEmbed
import sys
from requests.models import Response
import requests
from discord import Webhook, RequestsWebhookAdapter, AsyncWebhookAdapter, channel, embeds, webhook
import time
#Setup
iconurl = input("Icon url (Put a link to your pfp, igmur or do /avatar and copy link) ")
name = input( "Name: ")
tit = input("Title: ")
descrip = input("Description: ")
weeb = input("Webhook Url: ")
#Internal stuff
embed=discord.Embed(title=tit, description=descrip())
embed.set_author(name=name, icon_url=iconurl)
webhook = Webhook.from_url(weeb, adapter=RequestsWebhookAdapter())
webhook.send(embed=embed)
print("Message sent")
print("""

this app will be closed in 5 seconds""")
time.sleep(5)
sys.exit()