from . import bot
from datetime import datetime
from faker import Faker

@bot.command('fake')
def command_fake_info(args):
    fake = Faker()
    name = fake.name()
    first = name.split(' ')[0]
    last = name.split(' ')[1]
    email = '{0}.{1}@gmail.com'.format(first, last)
    bot.speak('Name: {0}\nEmail: {1}'.format(name, email))
