import praw
import requests
from discord_webhook import DiscordWebhook, DiscordEmbed
import config

r = None
try:
    reddit = praw.Reddit(client_id=config.id, client_secret=config.secret,
                    password=config.password, user_agent=config.user_agent, username=config.username)
except Exception as e:
    log(f'Error connecting to reddit: {e}')

subreddit = reddit.subreddit(config.subreddit)

print('r/', subreddit)

sub = subreddit.subscribers
active = subreddit.active_user_count

print('Users Online:', active)
print('Total Subscribers:', sub)


webhook = DiscordWebhook(url=config.webhookURL)

# create embed object for webhook
embed = DiscordEmbed(title='Subreddit Stats', description=config.subreddit, color=242424)
embed.set_timestamp()
embed.set_footer(text='Subreddit Stats by daningy#0001')
embed.add_embed_field(name='Subscribers', value=sub)
embed.add_embed_field(name='Online Users', value=active)
# add embed object to webhook
webhook.add_embed(embed)

response = webhook.execute()

print('Webhook Posted')
