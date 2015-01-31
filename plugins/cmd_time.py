from . import bot
from datetime import datetime

@bot.command('time')
def command_currnet_time(args):
    now = datetime.now()
    bot.speak('Current Time: {0}'.format(now))
