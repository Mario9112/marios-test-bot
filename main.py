
maintenance = None

import discord, random, time, asyncio
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from math import inf, nan, ceil, sqrt, floor
import DiscordUtils as DU
import time
import builtins as bt
import blackmarket as __bm__
import discord_components
def float(*args):
     if len(args) == 0:
        return 0.0
     elif len(args) >= 1:
        if type(args[0]) == bt.int:
            return bt.float(args[0])
        elif type(args[0]) == str:
            g = ''
            for x in args[0]:
                if x != ',':
                    g += x
            return bt.float(g)
        else:
            return bt.float(args[0])

infinity = inf
Infinity = inf
emojis = {
    'pickaxe': '<:pickaxe:942852910088327259>',
    'enchanted_pickaxe': '<:enchanted_pickaxe:942852910201602068>',
    'durability': '<a:durability:942857311578370078>'
}
Inf = inf
INF = inf
iNF = inf
NaN = nan
NAN = nan
Nan = nan
nAN = nan
def hc(x):
    'Hunt consume'
    if x == 1:
        return 35
    elif x in range(2,3):
        return 10
    elif x in range(3,5):
        return 8
    elif x in range(5,7):
        return 6
    elif x in range(7,10):
        return 4
    elif x in range(10,13):
        return 2
    elif x in range(13,15):
        return 1
    elif x >= 15:
        return 0
def atc(x):
    if x <= 15:
        return {1:70,2:49,3:30,4:25,5:23,6:20,7:23,8:19,9:16,
                10:13,11:10,12:8,13:5,14:3,15:2}[x]
    else:
        return 0
def atp(x):
    'x - strength'
    if x == 1:
        return 40
    elif 1 < x <= 3:
        return 60
    elif 3 < x <= 5:
        return 80
    elif 5 <= x <= 7:
        return 150
    elif 7 < x <= 9:
        return 210
    elif 9 < x <= 13:
        return 300
    elif 13 < x <= 16:
        return 450
    elif 16 < x <= 18:
        return 610
    elif 18 < x <= 20:
        return 720
    elif 20 < x:
        return 910
def fc(x):
    'Feed cooldown'
    if x <= 5:
        return {1:30,2:20,3:15,4:10,5:7}[x]
    elif 6 <= x <= 10:
        return {6:5,7:4,8:3,9:3,10:3}[x]
    elif 10 < x <= 14:
        return {11:2,12:2,13:1,14:1}[x]
    else:
        return 0
def agt(x):
    if x == 1:
        return 90
    elif x == 2:
        return 69
    elif x in [3,4,5,6,7]:
        return {3:30,4:23,5:10,6:3,7:2}[x]
    else:
        return 1
def yon(x):
    return {1:'Yes',0:'No',
            True: 'Yes',
            False: 'No'}[x]
def open(*args, **kwargs):
    kwargs['encoding'] = 'utf-8'
    return bt.open(*args, **kwargs)
bot = commands.Bot(command_prefix=['ft!', 'Ft!', 'FT!', 'fT!', '<@!936524828389814324> ', '<@!936524828389814324>'],
                   global_slash_commands=False,case_insensitive=True, intents = discord.Intents.all())
file = open('c:\\python\\farmbotdatas.txt', 'r', encoding='utf-8')
filep = open('c:\\python\\farmbotpets.txt', 'r', encoding='utf-8')
filew = open('c:\\python\\farmbotweapons.txt', 'r', encoding='utf-8')
fileg = open('c:\\python\\farmbotgens.txt', 'r', encoding='utf-8')
files = open('c:\\python\\farmbotstuns.txt', 'r', encoding='utf-8')
filea = open('c:\\python\\farmbotadvs.txt', 'r', encoding='utf-8')
e1file = open('c:\\python\\fbextras1.txt', 'r')
e3file = open('c:\\python\\fbextras1.txt', 'r')
reade1 = e1file.read()
reade3 = e3file.read()
e1s = eval(reade1)
e3s = eval(reade1)
bot.remove_command('help')
read_data = file.read()
saved_data = eval(read_data)
read_pet_data = filep.read()
read_weapon_data = filew.read()
read_gen_data = fileg.read()
read_stun_data = files.read()
read_adv_data = filea.read()
pets = eval(read_pet_data)
weapons = eval(read_weapon_data)
gens = eval(read_gen_data)
stuns = eval(read_stun_data)
advs = eval(read_adv_data)
bms = __bm__.getbms()
intents = discord.Intents.all()
async def is_owner(ctx):
    return ctx.message.author.id == 874625603310059530
@bot.event
async def on_ready():
    activity = discord.Game(name="Watching f!help | in {0} servers".format(len(bot.guilds)), type=1)
    await bot.change_presence(status=discord.Status.do_not_disturb, activity=activity)
    print("Bot is ready!")
def startcheck(user_id):
       global saved_data
       if user_id not in saved_data:
           saved_data[user_id] = [0, 0, 0, [
               100, 0, 0
               ,0, 99], 0, 0, 0, 0, 0,
                                 [0, 0, 0, 0, 0, 0, 0, [
                                     0, 0, 0, 0, 0
                                     ]
                                     , 0]  ]
       else:
           return
def startpetcheck(user_id):
       global pets
       if user_id not in pets:
           pets[user_id] = [0,
                            0, 0,
                            0, 0, 0,
                            'cat', 0, 0, 0,
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
       else:
           return       


@bot.command(aliases=['bal', 'balance', 'cred', 'credit'])
async def credits(ctx, *args):
    "Shows your credits."
    startcheck(ctx.message.author.id)
    id = ctx.message.author.id
    name = ctx.message.author
    if len(args)==0:
        id = ctx.message.author.id
        name = ctx.message.author
    elif len(args) >= 1:
     if len(ctx.message.mentions) == 0:
        try:
            f_user = await bot.fetch_user(int(args[0]))
            name = f_user
            id = int(args[0])
            del f_user
        except:
            name = ctx.message.author
            id = ctx.message.author.id
     else:
         try:
             g_user = ctx.message.mentions[0]
         except:
             g_user = await bot.fetch_user(ctx.message.author.id)
         name = g_user
         id = g_user.id
    startcheck(id)
    await ctx.send(embed=discord.Embed(
        description=f'%s has :star2: {saved_data[id][0]:,}'%name))   

@bot.command()
async def farm(ctx, *args):
  global saved_data
  "Shows your potato crops, potatoes and fertilizer."
  startcheck(ctx.message.author.id)
  if len(args) == 0:
    if saved_data[ctx.message.author.id][5] > time.time():
                 ready_for_harvest = ' '
    else:
                ready_for_harvest = ' [READY]'
    startcheck(ctx.message.author.id)
    await ctx.send(embed=discord.Embed(title='%s\'s Farm'%ctx.message.author,
    description=':seedling: Potato Crops (%s)%s \n:potato: Potatoes (%s)'
                '\n:bowl_with_spoon: Fertilizer (%s)'%\
    (f'{int(saved_data[ctx.message.author.id][2]):,}', ready_for_harvest, f'{int(saved_data[ctx.message.author.id][6]):,}',
      f'{int(saved_data[ctx.message.author.id][1]):,}'),color=random.randint(0, 16777200)))
  elif len(args) != 0:
    try:
      if '<@!' in args[0]:
          id=int(args[0][3:-1:])
          startcheck(int(args[0]))
          user = await bot.fetch_user(int(args[0][3:-1:]))
      else:
          startcheck(int(args[0]))
          id=int(args[0])
          user = await bot.fetch_user(int(args[0]))
      if saved_data[ctx.message.author.id][5] > time.time():
                 ready_for_harvest = ' '
      else:
                 ready_for_harvest = ' [READY]'
      startcheck(ctx.message.author.id)
      await ctx.send(embed=discord.Embed(title='%s\'s Farm'%user,
      description=':seedling: Potato Crops (%s)%s \n:potato: Potatoes (%s)'
                '\n:bowl_with_spoon: Fertilizer (%s)'%\
    (f'{int(saved_data[id][2]):,}', ready_for_harvest, f'{int(saved_data[id][6]):,}',
      f'{int(saved_data[id][1]):,}'),color=random.randint(0, 16777200)))
    except:
        if saved_data[ctx.message.author.id][5] > time.time():
                 ready_for_harvest = ' '
        else:
                ready_for_harvest = ' [READY]'
        startcheck(ctx.message.author.id)
        await ctx.send(embed=discord.Embed(title='%s\'s Farm'%ctx.message.author,
        description=':seedling: Potato Crops (%s)%s \n:potato: Potatoes (%s)'
                '\n:bowl_with_spoon: Fertilizer (%s)'%\
    (f'{int(saved_data[ctx.message.author.id][2]):,}', ready_for_harvest, f'{int(saved_data[ctx.message.author.id][6]):,}',
      f'{int(saved_data[ctx.message.author.id][1]):,}'),color=random.randint(0, 16777200)))
@bot.command()
async def shop(ctx):
    "Opens the shop."
    embed=discord.Embed(title='Shop', description=
'''Welcome to the FarmBot shop! You can buy anything safely.
`ID /` Use `f!buy <id> <amount>` to buy an item from this shop
`[1]` :seedling: Potato Crop - yields :potato: 8, harvested every 2 hours | Price: :star2: 5,000
`[2]` :star2: 375 Credits - Sell your potatoes to someone else | Price: :potato: 1
`[3]` :bowl_with_spoon: Fertilizer - Reduce your crops' cooldowns by half | Price: :star2: 8,000
`[4]` :magnet: Horseshoe - Earn more credits from searching | Price: :star2: 50,000
`[5]` :pound: E-Credits - Event Credits, able to be dropped with `f!edrop`, can be used to purcha'''
                        '''se event items and can be sold with `f!esell 5 <amount>`. | Price: :star2: 400''')
    embed.add_field(name='Cars', value='''`[6]` Volkswagen - A slightly fast car. Price: :star2: 90,000
`[7]` Toyota - This car is a little bit slow... Price: :star2: 85,000
`[8]` Volvo - A basic car. Price: :star2: 120,000
`[9]` Ferrari - Nice and fast car. Price: :star2: 100,000
`[10]` Mercedes Benz - A heavy car which is a little bit slow. Price: :star2: 80,000''')
    await ctx.send(embed=embed)

@bot.command()
async def buy(ctx, *args):
    "Purchases an item securely."
    startcheck(ctx.message.author.id)
    startcarcheck(ctx.message.author.id)
    global saved_data, cars
    if len(args) == 0:
        await ctx.send('Specify an item ID you want to buy')
    elif len(args) == 1:
      try:
        if int(args[0]) in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            if int(args[0]) == 1:
                if saved_data[ctx.message.author.id][0] >= 5000:
                    saved_data[ctx.message.author.id][0] -= 5000
                    saved_data[ctx.message.author.id][2] += 1
                    await ctx.send(embed=discord.Embed(
                    description='%s has successfully purchased :seedling: 1!'%
                    (ctx.message.author)
                    ,color=random.randint(0, 16777200)))
                else:
                    await ctx.send('You don\'t have enough '
                                   'to buy :seedling: 1')
            elif int(args[0]) == 2:
                if saved_data[ctx.message.author.id][6] >= 1:
                    saved_data[ctx.message.author.id][6] -= 1
                    saved_data[ctx.message.author.id][0] += 375
                    await ctx.send(embed=discord.Embed(
                    description='%s has successfully sold :potato: 1!'%
                    (ctx.message.author)
                    ,color=random.randint(0, 16777200)))
                else:
                    await ctx.send('You don\'t have :potato: 1')
            elif int(args[0]) == 3:
                if saved_data[ctx.message.author.id][0] >= 80000:
                    saved_data[ctx.message.author.id][0] -= 8000
                    saved_data[ctx.message.author.id][1] += 1
                    await ctx.send(embed=discord.Embed(
                    description='%s has successfully pur'
                    'chased :bowl_with_spoon: 1!'%
                    (ctx.message.author)
                    ,color=random.randint(0, 16777200)))
                else:
                    await ctx.send('You don\'t have enough '
                                   'to buy :bowl_with_spoon: 1')
            elif int(args[0]) == 4:
                if saved_data[ctx.message.author.id][0] >= 50000:
                    saved_data[ctx.message.author.id][0] -= 50000
                    saved_data[ctx.message.author.id][7] += 1
                    await ctx.send(embed=discord.Embed(
                    description='%s has successfully pur'
                    'chased :magnet: 1!'%
                    (ctx.message.author)
                    ,color=random.randint(0, 16777200)))
                else:
                    await ctx.send('You don\'t have enough to buy :magnet: 1')
            elif int(args[0]) == 5:
                if saved_data[ctx.message.author.id][0] >= 400:
                    saved_data[ctx.message.author.id][0] -= 400
                    saved_data[ctx.message.author.id][9][0] += 1
                    await ctx.send(embed=discord.Embed(
                    description='%s has successfully pur'
                    'chased :pound: 1!'%
                    (ctx.message.author)
                    ,color=random.randint(0, 16777200)))
                else:
                    await ctx.send('You don\'t have enough to buy :pound: 1')
            elif int(args[0]) == 6:
              if cars[ctx.message.author.id][0]['volkswagen'] != True:
                if saved_data[ctx.message.author.id][0] >= 90000:
                    saved_data[ctx.message.author.id][0] -= 90000
                    cars[ctx.message.author.id][0]['volkswagen'][0] = True
                    await ctx.send(embed=discord.Embed(
                    description='%s has successfully pur'
                    'chased a <:Volkswagen:985221821399986346> Volkswagen! `f!cars`' %
                    (ctx.message.author)
                    ,color=random.randint(0, 16777200)))
                else:
                    await ctx.send('You don\'t have enough to buy a <:Volkswagen:985221821399986346> Volkswagen')
              else:
                   await ctx.send('You already have a Volkswagen! `f!cars`')
            elif int(args[0]) == 7:
              if cars[ctx.message.author.id][0]['toyota'] != True:
                if saved_data[ctx.message.author.id][0] >= 85000:
                    saved_data[ctx.message.author.id][0] -= 85000
                    cars[ctx.message.author.id][0]['toyota'][0] = True
                    await ctx.send(embed=discord.Embed(
                    description='%s has successfully pur'
                    'chased a <:Toyota:985078103388848168> Toyota! `f!cars`' %
                    (ctx.message.author)
                    ,color=random.randint(0, 16777200)))
                else:
                    await ctx.send('You don\'t have enough to buy a <:Toyota:985078103388848168> Toyota')
              else:
                   await ctx.send('You already have a Toyota! `f!cars`')
            elif int(args[0]) == 8:
              if cars[ctx.message.author.id][0]['volvo'] != True:
                if saved_data[ctx.message.author.id][0] >= 120000:
                    saved_data[ctx.message.author.id][0] -= 120000
                    cars[ctx.message.author.id][0]['volvo'][0] = True
                    await ctx.send(embed=discord.Embed(
                    description='%s has successfully pur'
                    'chased a <:Volvo:997419119475425321> Volvo! `f!cars`' %
                    (ctx.message.author)
                    ,color=random.randint(0, 16777200)))
                else:
                    await ctx.send('You don\'t have enough to buy a <:Volvo:997419119475425321> Volvo')
              else:
                   await ctx.send('You already have a Volvo! `f!cars`')
            elif int(args[0]) == 9:
              if cars[ctx.message.author.id][0]['ferrari'] != True:
                if saved_data[ctx.message.author.id][0] >= 100000:
                    saved_data[ctx.message.author.id][0] -= 100000
                    cars[ctx.message.author.id][0]['ferrari'][0] = True
                    await ctx.send(embed=discord.Embed(
                    description='%s has successfully pur'
                    'chased a <:Ferrari:985076724293304330> Ferrari! `f!cars`' %
                    (ctx.message.author)
                    ,color=random.randint(0, 16777200)))
                else:
                    await ctx.send('You don\'t have enough to buy a <:Ferrari:985076724293304330> Ferrari')
              else:
                   await ctx.send('You already have a Ferrari! `f!cars`')
            elif int(args[0]) == 10:
              if cars[ctx.message.author.id][0]['mercedes'] != True:
                if saved_data[ctx.message.author.id][0] >= 80000:
                    saved_data[ctx.message.author.id][0] -= 80000
                    cars[ctx.message.author.id][0]['mercedes'][0] = True
                    await ctx.send(embed=discord.Embed(
                    description='%s has successfully pur'
                    'chased a <:MercedesBenz:985077274716041216> Mercedes Benz! `f!cars`' %
                    (ctx.message.author)
                    ,color=random.randint(0, 16777200)))
                else:
                    await ctx.send('You don\'t have enough to buy a <:MercedesBenz:985077274716041216> Mercedes Benz')
              else:
                   await ctx.send('You already have a Mercedes Benz! `f!cars`')
            else:
                await ctx.send('Invalid item ID')
      except:
          await ctx.send('Invalid item ID')
    else:
      try:
        if int(args[0]) in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
         if int(float(args[1])) >= 0:
            if int(args[0]) == 1:
                if saved_data[ctx.message.author.id][0] >= 5000*int(float(args[1])):
                    saved_data[ctx.message.author.id][0] -= 5000*int(float(args[1]))
                    saved_data[ctx.message.author.id][2] += int(float(args[1]))
                    await ctx.send(embed=discord.Embed(
                    description='%s has successfully purchased :seedling: %s!'%
                    (ctx.message.author, int(float(args[1])))
                    ,color=random.randint(0, 16777200)))
                else:
                    await ctx.send('You don\'t have enough to buy :seedling: %s'%int(float(args[1])))
            elif int(args[0]) == 2:
             if saved_data[ctx.message.author.id][0] <= Infinity:
                if saved_data[ctx.message.author.id][6] >= 1*int(float(args[1])):
                    saved_data[ctx.message.author.id][6] -= 1*int(float(args[1]))
                    saved_data[ctx.message.author.id][0] += 375*int(float(args[1]))
                    await ctx.send(embed=discord.Embed(
                    description='%s has successfully sold :potato: %s!'%
                    (ctx.message.author,int(float(args[1])))
                    ,color=random.randint(0, 16777200)))
                else:
                    await ctx.send('You don\'t have :potato: %'%int(float(args[1])))
             else:
                 await ctx.send('You can\'t hold any more credits right now.')
            elif int(args[0]) == 3:
                if saved_data[ctx.message.author.id][0] >= 8000*int(float(args[1])):
                    saved_data[ctx.message.author.id][0] -= 8000*int(float(args[1]))
                    saved_data[ctx.message.author.id][1] +=int(float(args[1]))
                    await ctx.send(embed=discord.Embed(
                    description='%s has successfully pur'
                    'chased :bowl_with_spoon: %s!'%
                    (ctx.message.author,int(float(args[1])))
                    ,color=random.randint(0, 16777200)))
                else:
                    await ctx.send('You don\'t have enough to buy :bowl_with_spoon: %s'%int(float(args[1])))
            elif int(args[0]) == 4:
                if saved_data[ctx.message.author.id][0] >= 50000*int(float(args[1])):
                    saved_data[ctx.message.author.id][0] -= 50000*int(float(args[1]))
                    saved_data[ctx.message.author.id][7] += 1*int(float(args[1]))
                    await ctx.send(embed=discord.Embed(
                    description='%s has successfully pur'
                    'chased :magnet: %s!'%
                    (ctx.message.author,int(float(args[1])))
                    ,color=random.randint(0, 16777200)))
                else:
                    await ctx.send('You don\'t have enough to buy :magnet: %s'%int(float(args[1])))
            elif int(args[0]) == 5:
                if saved_data[ctx.message.author.id][0] >= 400*int(float(args[1])):
                    saved_data[ctx.message.author.id][0] -= 400*int(float(args[1]))
                    saved_data[ctx.message.author.id][9][0] += 1*int(float(args[1]))
                    await ctx.send(embed=discord.Embed(
                    description='%s has successfully pur'
                    'chased :pound: %s!'%
                    (ctx.message.author,f'{int(float(args[1])):,}')
                    ,color=random.randint(0, 16777200)))
                else:
                    await ctx.send('You don\'t have enough to buy :pound: %s'%int(float(args[1])))
            elif int(args[0]) == 5:
                if saved_data[ctx.message.author.id][0] >= 400:
                    saved_data[ctx.message.author.id][0] -= 400
                    saved_data[ctx.message.author.id][9][0] += 1
                    await ctx.send(embed=discord.Embed(
                    description='%s has successfully pur'
                    'chased :pound: 1!'%
                    (ctx.message.author)
                    ,color=random.randint(0, 16777200)))
                else:
                    await ctx.send('You don\'t have enough to buy :pound: 1')
            elif int(args[0]) == 6:
              if cars[ctx.message.author.id][0]['volkswagen'] != True:
                if saved_data[ctx.message.author.id][0] >= 90000:
                    saved_data[ctx.message.author.id][0] -= 90000
                    cars[ctx.message.author.id][0]['volkswagen'][0] = True
                    await ctx.send(embed=discord.Embed(
                    description='%s has successfully pur'
                    'chased a <:Volkswagen:985221821399986346> Volkswagen! `f!cars`' %
                    (ctx.message.author)
                    ,color=random.randint(0, 16777200)))
                else:
                    await ctx.send('You don\'t have enough to buy a <:Volkswagen:985221821399986346> Volkswagen')
              else:
                   await ctx.send('You already have a Volkswagen! `f!cars`')
            elif int(args[0]) == 7:
              if cars[ctx.message.author.id][0]['toyota'] != True:
                if saved_data[ctx.message.author.id][0] >= 85000:
                    saved_data[ctx.message.author.id][0] -= 85000
                    cars[ctx.message.author.id][0]['toyota'][0] = True
                    await ctx.send(embed=discord.Embed(
                    description='%s has successfully pur'
                    'chased a <:Toyota:985078103388848168> Toyota! `f!cars`' %
                    (ctx.message.author)
                    ,color=random.randint(0, 16777200)))
                else:
                    await ctx.send('You don\'t have enough to buy a <:Toyota:985078103388848168> Toyota')
              else:
                   await ctx.send('You already have a Toyota! `f!cars`')
            elif int(args[0]) == 8:
              if cars[ctx.message.author.id][0]['volvo'] != True:
                if saved_data[ctx.message.author.id][0] >= 120000:
                    saved_data[ctx.message.author.id][0] -= 120000
                    cars[ctx.message.author.id][0]['volvo'][0] = True
                    await ctx.send(embed=discord.Embed(
                    description='%s has successfully pur'
                    'chased a <:Volvo:997419119475425321> Volvo! `f!cars`' %
                    (ctx.message.author)
                    ,color=random.randint(0, 16777200)))
                else:
                    await ctx.send('You don\'t have enough to buy a <:Volvo:997419119475425321> Volvo')
              else:
                   await ctx.send('You already have a Volvo! `f!cars`')
            elif int(args[0]) == 9:
              if cars[ctx.message.author.id][0]['ferrari'] != True:
                if saved_data[ctx.message.author.id][0] >= 100000:
                    saved_data[ctx.message.author.id][0] -= 100000
                    cars[ctx.message.author.id][0]['ferrari'][0] = True
                    await ctx.send(embed=discord.Embed(
                    description='%s has successfully pur'
                    'chased a <:Ferrari:985076724293304330> Ferrari! `f!cars`' %
                    (ctx.message.author)
                    ,color=random.randint(0, 16777200)))
                else:
                    await ctx.send('You don\'t have enough to buy a <:Ferrari:985076724293304330> Ferrari')
              else:
                   await ctx.send('You already have a Ferrari! `f!cars`')
            elif int(args[0]) == 10:
              if cars[ctx.message.author.id][0]['mercedes'] != True:
                if saved_data[ctx.message.author.id][0] >= 80000:
                    saved_data[ctx.message.author.id][0] -= 80000
                    cars[ctx.message.author.id][0]['mercedes'][0] = True
                    await ctx.send(embed=discord.Embed(
                    description='%s has successfully pur'
                    'chased a <:MercedesBenz:985077274716041216> Mercedes Benz! `f!cars`' %
                    (ctx.message.author)
                    ,color=random.randint(0, 16777200)))
                else:
                    await ctx.send('You don\'t have enough to buy a <:MercedesBenz:985077274716041216> Mercedes Benz')
              else:
                   await ctx.send('You already have a Mercedes Benz! `f!cars`')
         else:
             await ctx.send('You must enter a positive number!')
        else:
            if (str(int(args[0])) not in [1,2,3,4,5,6,7,8,9,10]) and len(args) >= 2:
                await ctx.send('Invalid item ID or item amount')
      except:
        if (str(int(args[0])) not in [1,2,3,4,5,6,7,8,9,10]) and len(args) >= 2:
          await ctx.send('Invalid item ID or item amount')
@bot.command()
async def harvest(ctx):
    "Harvests your potato crops."
    startcheck(ctx.message.author.id)
    if saved_data[ctx.message.author.id][2] >= 1:
      if saved_data[ctx.message.author.id][5] < time.time():
        saved_data[ctx.message.author.id][6] += saved_data[ctx.message.author.id][2]*8
        await ctx.send(embed=discord.Embed(description=
    ('%s has harvested :potato: '%ctx.message.author)+f'{saved_data[ctx.message.author.id][2]*8:,}'+\
    ' from :seedling: %s' % saved_data[ctx.message.author.id][2]))
        saved_data[ctx.message.author.id][5] = time.time() + 7200 # :D
      else:
          await ctx.send('You must wait another %s minutes before harvesting your potato crops again'%
                         int((int(saved_data[ctx.message.author.id][5]) - int(time.time()))/60))
    else:
        await ctx.send('You have no potato crops to harvest!')
@bot.command(aliases=['fert'])
async def fertilize(ctx):
    "Shortens your potato crops' cooldowns by half."
    startcheck(ctx.message.author.id)
    if saved_data[ctx.message.author.id][2] >= 1:
        if saved_data[ctx.message.author.id][1] >= 1:
            if saved_data[ctx.message.author.id][5] > time.time():
             if saved_data[ctx.message.author.id][8] <= time.time():
                saved_data[ctx.message.author.id][5]=saved_data[ctx.message.author.id][5]-((int((int(saved_data[ctx.message.author.id][5]) - int(time.time()))/60))//2)*60
                await ctx.send(embed=discord.Embed(description=
            '%s has dumped :bowl_with_spoon: on their :seedling: and shortened their cooldowns by half'%\
                                                   ctx.message.author,color=random.randint(0, 16777200)))
                saved_data[ctx.message.author.id][8] = time.time() + (3600)
                saved_data[ctx.message.author.id][1] -= 1
             else:
                 await ctx.send('You must wait another %i minutes before using fertilizer again' %
                          ((saved_data[ctx.message.author.id][8] - time.time())//60))
                 
            else:
                await ctx.send('Your potato crops are already ready for harvest!')
        else:
            await ctx.send('You don\'t have any fertilizer')
    else:
        await ctx.send('You have no potato crops to fertilize!')
@bot.command(aliases=['cf', 'flip'])
async def coinflip(ctx, *args):
     "Flips a coin and gives/removes your credits."
     global saved_data
     startcheck(ctx.message.author.id)
     err = 1
     if len(args) <= 1:
          await ctx.send('`f!coinflip <amount> <side>` is how you use this.')
     else:
          try:
               amt = type(1)(float(args[0]))
               assert amt >= 0
               err = 0
          except (ValueError,AssertionError):
               if args[0].lower() == 'all':
                    amt = type(0)(saved_data[ctx.message.author.id][0])
                    err = 0
               else:
                    await ctx.reply('Your argument should be a positive integer')
                    err = 1
          if 1:
               if err: return
               if amt >= 1200:
                 if amt <= 360000:
                    if amt <= saved_data[ctx.message.author.id][0]:
                        argside = args[1]
                        if argside.lower().startswith('h'):
                            side='heads'
                        elif argside.lower().startswith('t'):
                            side='tails'
                        else:
                            await ctx.reply('Invalid side entered, must be `heads` or `tails`')
                            return
                        landed = random.choice(['heads', 'tails'])
                        if side == landed:
                            cfEmbed=discord.Embed(title=':coin: Coin Flip - You Won!',
                                color=0xCC32, description=f'You bet on **{side}**, and the'
                            f' coin landed on **{landed}**! You win :star2: {amt:,}!')
                            saved_data[ctx.message.author.id][0]+=amt
                        else:
                            cfEmbed=discord.Embed(title=':coin: Coin Flip - You Lost!',
                                color=0xCC1200, description=f'You bet on **{side}**, and the'
                            f' coin landed on **{landed}**! You lost :star2: {amt:,}!')
                            saved_data[ctx.message.author.id][0]-=amt
                        await ctx.reply(embed=cfEmbed, mention_author=0)
                    else:
                         await ctx.reply(f'You only have :star2: {saved_data[ctx.message.author.id][0]:,} therefore cannot bet :star2: {amt:,}!')
                 else:
                    await ctx.reply('The maximum amount you can bet for coin flip is :star2: 260,000.')
               else:
                    await ctx.reply('You have to bet at least :star2: 1,200!')
@bot.command(aliases=['se'])
async def snake_eyes(ctx, *args):
     "Rolls 2 dice. One eye pays out 2x, two pays out 10x."
     global saved_data
     startcheck(ctx.message.author.id)
     err = 1
     if len(args) == 0:
          await ctx.send('`f!snake_eyes <amount>` is how you use this.')
     else:
          try:
               amt = type(1)(float(args[0]))
               assert amt >= 0
               err = 0
          except (ValueError,AssertionError):
               if args[0].lower() == 'all':
                    amt = type(0)(saved_data[ctx.message.author.id][0])
                    err = 0
               else:
                    await ctx.reply('Your argument should be a positive integer')
                    err = 1
          if 1:
               if err: return
               if amt >= 1200:
                 if amt <= 480000:
                    if amt <= saved_data[ctx.message.author.id][0]:
                         saved_data[ctx.message.author.id][0] -= amt
                         r1 = (random.randint(0,12)%6)+1
                         r2 = (random.randint(0,12)%6)+1
                         seEmojis = {
                        1: '<:SE_1:997435266203652136>',
                        2: '<:SE_2:997435271433957428>',
                        3: '<:SE_3:997435273627582474>',
                        4: '<:SE_4:997435275993174047>',
                        5: '<:SE_5:997435278669123675>',
                        6: '<:SE_6:997435280489447456>'
                         }
                         if [1, 1] == [r1, r2]:
                             seEmbed=discord.Embed(title='Snake Eyes - Snake Eyes!!!', color=0x1DD00,
                            description=f'{seEmojis[r1]} {seEmojis[r2]}\n'
                            '**SNAKE EYES!** :star_struck: You'
                                            f' won :star2: {type(0)(amt*7):,}')
                             saved_data[ctx.message.author.id][0] += type(0)(amt*7)
                         elif (1 in [r1, r2]) and ([1, 1] != [r1, r2]):
                             seEmbed=discord.Embed(title='Snake Eyes - You Win!', color=0xCC41,
                            description=f'{seEmojis[r1]} {seEmojis[r2]}\n'
                            f'A single eye, not bad. You won :star2: {type(0)(amt*1.5):,}')
                             saved_data[ctx.message.author.id][0] += type(0)(amt*1.5)                         
                         else:
                             seEmbed=discord.Embed(title='Snake Eyes - You lost!', color=0xCC1200,
                            description=f'{seEmojis[r1]} {seEmojis[r2]}\n'
                            f'You didn\'t get any snake eyes. Sad. You lost :star2: {amt:,}.')
                             seEmbed.set_footer(text='Each snake eye in this game is a dice with a single dot')
                             saved_data[ctx.message.author.id][0] -= amt
                         await ctx.reply(embed=seEmbed, mention_author=0)                                 
                    else:
                         await ctx.reply(f'You only have :star2: {saved_data[ctx.message.author.id][0]:,} therefore cannot bet :star2: {amt:,}!')
                 else:
                    await ctx.reply('The maximum amount you can bet for snake eyes is :star2: 480,000.')
               else:
                    await ctx.reply('You have to bet at least :star2: 1,200!')
      
@bot.command(aliases=['bet','roll'])
async def gamble(ctx, *args):
     global saved_data
     startcheck(ctx.message.author.id)
     err = 1
     if len(args) == 0:
          await ctx.send('`f!gamble <amount>` is how you use this.')
     else:
          try:
               amt = type(1)(float(args[0]))
               assert amt >= 0
               err = 0
          except (ValueError,AssertionError):
               if args[0].lower() == 'all':
                    amt = type(0)(saved_data[ctx.message.author.id][0])
                    err = 0
               else:
                    await ctx.reply('Your argument should be a positive integer')
                    err = 1
          if 1:
               if err: return
               if amt >= 1200:
                 if amt <= 480000:
                    if amt <= saved_data[ctx.message.author.id][0]:
                         saved_data[ctx.message.author.id][0] -= amt
                         botroll = random.randint(1, 12)
                         yourroll = random.randint(1, 12)
                         if botroll < yourroll:
                            betEmbed = discord.Embed(title='Dice Roll - You won!', color=0x00CC21,
                            description=f'You won :star2: {amt:,}!')
                            saved_data[ctx.message.author.id][0] += amt*2
                            betEmbed.add_field(name='You', value=f'{yourroll:,}')
                            betEmbed.add_field(name='Bot', value=f'{botroll:,}')
                         elif botroll == yourroll:
                            betEmbed = discord.Embed(title='Dice Roll - You tied!', color=0xCCCC21,
                            description=f'You lost :star2: {type(0)(amt*0.3):,}!')
                            saved_data[ctx.message.author.id][0] += type(0)(amt*0.7)
                            betEmbed.add_field(name='You', value=f'{yourroll:,}')
                            betEmbed.add_field(name='Bot', value=f'{botroll:,}')
                            betEmbed.set_footer(text='You lose 30% your bet if you tie')
                         else:
                            betEmbed = discord.Embed(title='Dice Roll - You lost!', color=0xCC0000,
                            description=f'You lost :star2: {amt:,}!')
                            betEmbed.add_field(name='You', value=f'{yourroll:,}')
                            betEmbed.add_field(name='Bot', value=f'{botroll:,}')
                         await ctx.reply(embed=betEmbed)
                    else:
                         await ctx.reply(f'You only have :star2: {saved_data[ctx.message.author.id][0]:,} therefore cannot bet :star2: {amt:,}!')
                 else:
                    await ctx.reply('The maximum amount you can bet for gamble is :star2: 480,000.')
               else:
                    await ctx.reply('You have to bet at least :star2: 1,200!')

@bot.command()
async def pay(ctx, *args):
    "Pays the amount of credits to the mentioned user."
    global saved_data
    startcheck(ctx.message.author.id)
    id = None
    name = None
    if len(args)==0:
        id = None
        name = None
    elif len(args) >= 1:
     if len(ctx.message.mentions) > 0:
        try:
            f_user = await bot.fetch_user(int(ctx.message.mentions[0].id))
            name = f_user
            id = int(ctx.message.mentions[0].id)
            del f_user
        except:
            name = None
            id = None
     else:
         try:
             g_user = await bot.fetch_user(int(args[0]))
         except:
             class fake_user:
                 def __init__(self):
                     self.id = None
                     self.name = None
                 id = None
                 name = None
             g_user = fake_user()
         name = g_user
         id = g_user.id
    startcheck(id)
    if len(args) == 0:
         await ctx.send('You must mention somebody to pay!')
    elif len(args) == 1:
         if id != None:
              await ctx.send('You have to provide a positive number of credits to work.')
         else:
              await ctx.send('You must mention somebody to pay!')
    elif len(args) >= 2:
         if id != None:
              try:
                   amt = type(0)(float(args[1]))
              except OverflowError:
                   await ctx.send('You\'re paying infinity... aren\'t you???')
                   return
              except ValueError:
                   amt = -1
              if amt <= saved_data[ctx.message.author.id][0]:
               if amt >= 0:
                saved_data[id][0] += amt
                saved_data[ctx.message.author.id][0] -= amt
                await ctx.reply(embed=discord.Embed(description='You have '
                f'successfully paid :star2: {int(amt):,} to %s\'s account. You now have '
                    f':star2: {saved_data[ctx.message.author.id][0]:,}.' % name, timestamp=datetime.datetime.fromtimestamp(int(time.time()))))
               else:
                await ctx.reply(f'You must enter a positive number!')
              else:
                await ctx.reply(f'You only have :star2: {saved_data[ctx.message.author.id][0]:,}, you can\'t pay :star2: {amt:,}!')
         else:
             await ctx.send('You must mention somebody to pay!')
              
dropped = {}
@bot.command(aliases=['eventdrop', 'ed'])
async def edrop(ctx, *args):
  'Drops some event credits, able to be picked up with `f!grab`.'
  global saved_data, dropped
  startcheck(ctx.message.author.id)
  if ctx.message.channel.type is discord.ChannelType.private:
      await ctx.send('This command may only be used in server channels')
  else:
      if len(args) == 0:
          await ctx.send('You must specify the amount of :pound: you want to drop')
      elif len(args) >= 1:
          if int(float(args[0])) > 0:
            if int(float(args[0])) <= saved_data[ctx.message.author.id][9][0]:
             if (ctx.message.channel.id, ctx.message.guild.id) not in dropped:
                await ctx.message.delete()
                saved_data[ctx.message.author.id][9][0] -= int(float(args[0]))
                dropped[(ctx.message.channel.id, ctx.message.guild.id)] = [ctx.message.author.id, int(float(args[0]))]
                await ctx.send('Someone just dropped their Event Credits in this channel! Hurry and pick th'
                               'em up with `f!grab` before someone else gets them!')
             else:
                await ctx.send('Sorry, this channel already has Event Credits dropped here :(')
            else: await ctx.send('You do not have enough event credits for that') 
          else: await ctx.send('You must enter a positive number')
@bot.command()
async def grab(ctx, *args):
  'Grabs the dropped event credits.'
  global saved_data, dropped
  startcheck(ctx.message.author.id)
  if ctx.message.channel.type is discord.ChannelType.private:
      await ctx.send('This command may only be used in server channels')
  else:
      if (ctx.message.channel.id, ctx.message.guild.id) in dropped:
          if dropped[(ctx.message.channel.id, ctx.message.guild.id)][0] == ctx.message.author.id:
              await ctx.send('You cannot grab your own dropped event credits')
          else:
              saved_data[ctx.message.author.id][9][0] += dropped[(ctx.message.channel.id, ctx.message.guild.id)][1]
              
              await ctx.send(embed=discord.Embed(
            description=('%s has picked up E-Credits and found'%ctx.message.author) +
            f' :pound: {dropped[(ctx.message.channel.id, ctx.message.guild.id)][1]:,}!'
           ,color=random.randint(0, 16777207)))
              del dropped[(ctx.message.channel.id, ctx.message.guild.id)]
      else:
          await ctx.send('There are no E-Credits to grab right now')
@bot.command(aliases=['ebal'])
async def ecred(ctx, *args):
  "Shows your event credits."
  startcheck(ctx.message.author.id)
  if len(args) == 0:
    startcheck(ctx.message.author.id)
    await ctx.send(embed=discord.Embed(title='',
                description=(('%s'%ctx.message.author)+
     ' has :pound: ' + f'{saved_data[ctx.message.author.id][9][0]:,}')))
  else:
    try:
      if '<@!' in args[0]:
          startcheck(int(args[0][3:-1:]))
          user = await bot.fetch_user(int(args[0][3:-1:]))
          await ctx.send(embed=discord.Embed(title='',
                description=(('%s'%user)+
     ' has :pound: ' + f'{saved_data[user.id][9][0]:,}')))
      else:
          startcheck(int(args[0]))
          user = await bot.fetch_user(int(args[0]))
          await ctx.send(embed=discord.Embed(title='',
                description=(('%s'%user)+
     ' has :pound: ' + f'{saved_data[user.id][9][0]:,}')))
    except:
        startcheck(ctx.message.author.id)
        await ctx.send(embed=discord.Embed(title='',
                description=(('%s'%ctx.message.author)+
     ' has :pound: ' + f'{saved_data[ctx.message.author.id][9][0]:,}')))
@bot.command()
async def epay(ctx, *args):
    "Pays the amount of credits to the mentioned user."
    global saved_data
    startcheck(ctx.message.author.id)
    id = None
    name = None
    if len(args)==0:
        id = None
        name = None
    elif len(args) >= 1:
     if len(ctx.message.mentions) > 0:
        try:
            f_user = await bot.fetch_user(int(ctx.message.mentions[0].id))
            name = f_user
            id = int(ctx.message.mentions[0].id)
            del f_user
        except:
            name = None
            id = None
     else:
         try:
             g_user = await bot.fetch_user(int(args[0]))
         except:
             class fake_user:
                 def __init__(self):
                     self.id = None
                     self.name = None
                 id = None
                 name = None
             g_user = fake_user()
         name = g_user
         id = g_user.id
    startcheck(id)
    if len(args) == 0:
         await ctx.send('You must mention somebody to pay!')
    elif len(args) == 1:
         if id != None:
              await ctx.send('You have to provide a positive number of credits to work.')
         else:
              await ctx.send('You must mention somebody to pay!')
    elif len(args) >= 2:
         if id != None:
              try:
                   amt = type(0)(float(args[1]))
              except OverflowError:
                   await ctx.send('Stop trying to break event economy')
                   return
              except ValueError:
                   amt = -1
              if amt <= saved_data[ctx.message.author.id][9][0]:
               if amt >= 0:
                saved_data[id][9][0] += amt
                saved_data[ctx.message.author.id][9][0] -= amt
                await ctx.send(embed=discord.Embed(description='You have '
                f'successfully paid :pound: {int(amt):,} to %s\'s account. You now have '
                    f':pound: {saved_data[ctx.message.author.id][9][0]:,}.' % name,timestamp=datetime.datetime.fromtimestamp(int(time.time())))
               )
               else:
                await ctx.reply(f'You must enter a positive number!')
              else:
                await ctx.reply(f'You only have :pound: {saved_data[ctx.message.author.id][9][0]:,}, you can\'t pay :pound: {amt:,}!')
         else:
             await ctx.send('You must mention somebody to pay!')
              

@bot.command(aliases=['eventshop', 'es'])
async def eshop(ctx):
    embed=discord.Embed(title='Event Shop',
description = '''Want to unlock cool commands? Get them with `f!ebuy <id>`!''')
    embed.add_field(name='Items', value='''
[1] :chart_with_upwards_trend: Statistician - :pound: 120
[2] :comet: Conjuror - :pound: 250
[3] :smoking: Junkie - :pound: 350
[4] :moneybag: Investor - :pound: 640
[5] :dove: Seagull - :pound: 1,000''')
    embed.add_field(name='Packages', value='''
[6] :package: Custom Command Package 1 - Unlocks `f!petname` - :pound: 540''')
    await ctx.send(embed=embed)
@bot.command(aliases=['eventbuy', 'eb'])
async def ebuy(ctx, *args):
    "Purchases an item securely."
    startcheck(ctx.message.author.id)
    extrastartcheck1(ctx.message.author.id)
    global saved_data
    global e1s
    if len(args) == 0:
        await ctx.send('Specify an item ID you want to buy! e.g. `f!ebuy 2` to buy conjuror')
    elif len(args) != 0:
        if str(args[0]).strip() in '123456':
            if str(args[0]).strip() == '1':
                if saved_data[ctx.message.author.id][9][0] >= 120:
                    if not saved_data[ctx.message.author.id][9][1]:
                        saved_data[ctx.message.author.id][9][0] -= 120;
                        saved_data[ctx.message.author.id][9][1] = True;
                        await ctx.send(embed=discord.Embed(
            description='%s has successfully purchased :chart_wi'
            'th_upwards_trend:!' % ctx.message.author
           ,color=random.randint(0, 16777207)))
                    else: await ctx.send('You already own this item!')
                else:
                   await ctx.send('Your balance of :pound: %i is insufficient to '
                                  'complete this transaction; you may purchase t'
                                  'hrough `f!buy 5 <amount>`'%saved_data[ctx.message.author.id][9][0])
            elif str(args[0]).strip() == '2':
                if saved_data[ctx.message.author.id][9][0] >= 250:
                    if not saved_data[ctx.message.author.id][9][2]:
                        saved_data[ctx.message.author.id][9][0] -= 250;
                        saved_data[ctx.message.author.id][9][2] = True;
                        await ctx.send(embed=discord.Embed(
            description='%s has successfully purchased :co'
            'met:!' % ctx.message.author
           ,color=random.randint(0, 16777207)))
                    else: await ctx.send('You already own this item!')
                else:
                   await ctx.send('Your balance of :pound: %i is insufficient to '
                                  'complete this transaction; you may purchase t'
                                  'hrough `f!buy 5 <amount>`'%saved_data[ctx.message.author.id][9][0])
            elif str(args[0]).strip() == '3':
                if saved_data[ctx.message.author.id][9][0] >= 350:
                    if not saved_data[ctx.message.author.id][9][3]:
                        saved_data[ctx.message.author.id][9][0] -= 350;
                        saved_data[ctx.message.author.id][9][3] = True;
                        await ctx.send(embed=discord.Embed(
            description='%s has successfully purchased :smok'
            'ing:!' % ctx.message.author
           ,color=random.randint(0, 16777207)))
                    else: await ctx.send('You already own this item!')
                else:
                   await ctx.send('Your balance of :pound: %i is insufficient to '
                                  'complete this transaction; you may purchase t'
                                  'hrough `f!buy 5 <amount>`'%saved_data[ctx.message.author.id][9][0])
            elif str(args[0]).strip() == '4':
                if saved_data[ctx.message.author.id][9][0] >= 640:
                    if not saved_data[ctx.message.author.id][9][4]:
                        saved_data[ctx.message.author.id][9][0] -= 640;
                        saved_data[ctx.message.author.id][9][4] = True;
                        await ctx.send(embed=discord.Embed(
            description='%s has successfully purchased :mon'
            'e''yb''ag:!' % ctx.message.author
           ,color=random.randint(0, 16777207)))
                    else: await ctx.send('You already own this item!')
                else:
                   await ctx.send('Your balance of :pound: %i is insufficient to'
                                  ' complete this transaction; you may purchase t'
                                  'hrough `f!buy 5 <amount>`'%saved_data[ctx.message.author.id][9][0])
            elif str(args[0]).strip() == '5':
                if saved_data[ctx.message.author.id][9][0] >= 1000:
                    if not saved_data[ctx.message.author.id][9][5]:
                        saved_data[ctx.message.author.id][9][0] -= 1000;
                        saved_data[ctx.message.author.id][9][5] = True;
                        await ctx.send(embed=discord.Embed(
            description='%s has successfully purchased :dove:!'
            % ctx.message.author
           ,color=random.randint(0, 16777207)))
                    else: await ctx.send('You already own this item!')
                else:
                   await ctx.send('Your balance of :pound: %i is insufficient to '
                                  'complete this transaction; you may purchase t'
                                  'hrough `f!buy 5 <amount>`'%saved_data[ctx.message.author.id][9][0])
            elif str(args[0]).strip() == '6':
                if saved_data[ctx.message.author.id][9][0] >= 540:
                    if not e1s[ctx.message.author.id][2]:
                        saved_data[ctx.message.author.id][9][0] -= 540;
                        e1s[ctx.message.author.id][2] = True;
                        await ctx.send(embed=discord.Embed(
            description='%s has successfully purchased Custom Command Package 1!'
            % ctx.message.author
           ,color=random.randint(0, 16377207)))
                    else: await ctx.send('You already own this package!')
                else:
                   await ctx.send('Your balance of :pound: %i is insufficient to '
                                  'complete this transaction; you may purchase t'
                                  'hrough `f!buy 5 <amount>`'%saved_data[ctx.message.author.id][9][0])

        else:
            await ctx.send('Unknown event item/package ID "%s"; pick a number from 1-6' % args[0].strip())
@bot.command()
async def interest(ctx):
    "Boosts your credits by 10%."
    if saved_data[ctx.message.author.id][9][4]:
        if saved_data[ctx.message.author.id][9][6] < time.time():
            await ctx.send(embed=discord.Embed(
            description=('%s has successfully collected '%ctx.message.author)+
                        ':star2:'f' {saved_data[ctx.message.author.id][0]//10:,}'
                        ' in interest', color=0x38bf36))
            saved_data[ctx.message.author.id][9][6] = time.time()+(4800)
            saved_data[ctx.message.author.id][0] *= 1.1
            saved_data[ctx.message.author.id][0] = int(
                saved_data[ctx.message.author.id][0])
        else:
            await ctx.send('You must wait another %i minutes '
                           'before collecting :star2: in int'
                           'erest' % (int((saved_data[ctx.message.author.id][9][6] - time.time())/60)))
            
    else:await ctx.send("You're not allowed to use this command! You can"
                        " unlock it using `f!ebuy`")
        
@bot.command()
async def fish(ctx):
    global saved_data
    if saved_data[ctx.message.author.id][9][5]:
      if saved_data[ctx.message.author.id][9][7][4] < time.time():
        rolled = random.randint(1,256)
        if (64 < rolled < 212):
            saved_data[ctx.message.author.id][9][7][0] += 1
            saved_data[ctx.message.author.id][9][7][4] = time.time()+(60) //(1+saved_data[
                        ctx.message.author.id][2])

            await ctx.send(embed=discord.Embed(description=
                    "%s's seagull has caught a :fish: worth :pound: 2"%ctx.message.author,
                    color=random.randint(0, 16777215)))
        elif rolled <= 64:
            saved_data[ctx.message.author.id][9][7][1] += 1
            saved_data[ctx.message.author.id][9][7][4] = time.time()+(40) //(1+saved_data[
                        ctx.message.author.id][2])

            await ctx.send(embed=discord.Embed(description=
                    "%s's seagull has caught a :tropical_fish: worth :pound: 5"%ctx.message.author,
                    color=random.randint(0, 16777215)))
        elif 212 <= rolled <= 242:
            saved_data[ctx.message.author.id][9][7][2] += 1
            saved_data[ctx.message.author.id][9][7][4] = time.time()+(30) //(1+saved_data[
                        ctx.message.author.id][2])

            await ctx.send(embed=discord.Embed(description=
                    "%s's seagull has caught a :dolphin: worth :pound: 20"%ctx.message.author,
                    color=random.randint(0, 16777215)))
        elif rolled >= 243:
            saved_data[ctx.message.author.id][9][7][3] += 1
            saved_data[ctx.message.author.id][9][7][4] = time.time()+(20)  //(1+saved_data[
                        ctx.message.author.id][2])

            await ctx.send(embed=discord.Embed(description=
                    "%s's seagull has caught a :shark: worth :pound: 30"%ctx.message.author,
                    color=random.randint(0, 16777215)))
      else:
          await ctx.send("You must wait another %i seconds before fishing again"%
                         (saved_data[ctx.message.author.id][9][7][4] - time.time()))
    else:
        await ctx.send('You\'re not allowed to use this command! You can'
                        " unlock it using `f!ebuy`")

@bot.command(aliases=['i'])
async def items(ctx, *args):
  if len(args) == 0:
    startcheck(ctx.message.author.id)
    await ctx.send(embed=discord.Embed(title='%s\'s event items'%ctx.message.author,
                description=(
'''
`f!esell <id>` to sell a fish or credits
[1] :fish: Fish [%i] - Worth :pound: 2
[2] :tropical_fish: Tropical Fish [%i] - Worth :pound: 5
[3] :dolphin: Dolphin [%i] - Worth :pound: 20
[4] :shark: Shark [%i] - Worth :pound: 30
'''%tuple(saved_data[ctx.message.author.id][9][7][0:4]))))
  else:
    try:
      if '<@!' in args[0]:
          startcheck(int(args[0][3:-1:]))
          user = await bot.fetch_user(int(args[0][3:-1:]))
          await ctx.send(embed=discord.Embed(title='%s\'s event items'%user,
                description=(
'''
`f!sell <id>` to sell a fish or credits
[1] :fish: Fish [%i] - Worth :pound: 2
[2] :tropical_fish: Tropical Fish [%i] - Worth :pound: 5
[3] :dolphin: Dolphin [%i] - Worth :pound: 20
[4] :shark: Shark [%i] - Worth :pound: 30
'''%tuple(saved_data[int(args[0][3:-1:])][9][7][0:4]))))
      else:
          startcheck(int(args[0]))
          user = await bot.fetch_user(int(args[0]))
          await ctx.send(embed=discord.Embed(title='%s\'s event items'%user,
                description=(
'''
`f!esell <id>` to sell a fish or credits
[1] :fish: Fish [%i] - Worth :pound: 2
[2] :tropical_fish: Tropical Fish [%i] - Worth :pound: 5
[3] :dolphin: Dolphin [%i] - Worth :pound: 20
[4] :shark: Shark [%i] - Worth :pound: 30
'''%tuple(saved_data[int(args[0])][9][7][0:4]))))
    except:
        startcheck(ctx.message.author.id)
        await ctx.send(embed=discord.Embed(title='%s\'s event items'%ctx.message.author,
                description=(
'''
`f!esell <id>` to sell a fish or credits
[1] :fish: Fish [%i] - Worth :pound: 2
[2] :tropical_fish: Tropical Fish [%i] - Worth :pound: 5
[3] :dolphin: Dolphin [%i] - Worth :pound: 20
[4] :shark: Shark [%i] - Worth :pound: 30
'''%tuple(saved_data[ctx.message.author.id][9][7][0:4]))))
@bot.command(aliases=['eventsell'])
async def esell(ctx, *args):
    startcheck(ctx.message.author.id)
    global saved_data
    if len(args) == 0:
        await ctx.send('Specify an item ID you want to sell')
    elif len(args) == 1:
      try:
        if int(args[0]) in [1, 2, 3, 4, 5]:
            if int(args[0]) == 1:
                if saved_data[ctx.message.author.id][9][7][0] >= 1:
                    saved_data[ctx.message.author.id][9][7][0] -= 1
                    saved_data[ctx.message.author.id][9][0] += 2
                    await ctx.send(embed=discord.Embed(
                    description='%s has successfully sold :fish: 1!'%
                    (ctx.message.author)
                    ,color=random.randint(0, 16777200)))
                else:
                    await ctx.send('You don\'t have :fish: 1')
            elif int(args[0]) == 2:
                if saved_data[ctx.message.author.id][9][7][1] >= 1:
                    saved_data[ctx.message.author.id][9][7][1] -= 1
                    saved_data[ctx.message.author.id][9][0] += 5
                    await ctx.send(embed=discord.Embed(
                    description='%s has successfully sold :tropical_fish: 1!'%
                    (ctx.message.author)
                    ,color=random.randint(0, 16777200)))
                else:
                    await ctx.send('You don\'t have :tropical_fish: 1')
            elif int(args[0]) == 3:
                if saved_data[ctx.message.author.id][9][7][2] >= 1:
                    saved_data[ctx.message.author.id][9][7][2] -= 1
                    saved_data[ctx.message.author.id][9][0] += 20
                    await ctx.send(embed=discord.Embed(
                    description='%s has successfully sol'\
                                'd :dolphin: 1!'%
                    (ctx.message.author)
                    ,color=random.randint(0, 16777200)))
                else:
                    await ctx.send('You don\'t have :dol'\
                                   'phin: 1')
            elif int(args[0]) == 4:
                if saved_data[ctx.message.author.id][9][7][3] >= 1:
                    saved_data[ctx.message.author.id][9][7][3] -= 1
                    saved_data[ctx.message.author.id][9][0] += 30
                    await ctx.send(embed=discord.Embed(
                    description='%s has successfully s'\
                                'old :shark: 1!'%
                    (ctx.message.author)
                    ,color=random.randint(0, 16777200)))
                else:
                    await ctx.send('You don\'t have :shark: 1')
            elif int(args[0]) == 5:
                if saved_data[ctx.message.author.id][9][0] >= 1:
                    saved_data[ctx.message.author.id][9][0] -= 1
                    saved_data[ctx.message.author.id][0] += 400
                    await ctx.send(embed=discord.Embed(
                    description='%s has successfully s'\
                    'old :pound: 1!'%
                    (ctx.message.author)
                    ,color=random.randint(0, 16777200)))
                else:
                    await ctx.send('You don\'t have :pound: 1')
            else:
                await ctx.send('Invalid item ID')
         
      except:
          await ctx.send('Invalid item ID')
    else:
      try:
       if int(args[1]) >= 0:
        if int(args[0]) in [1, 2, 3, 4, 5]:
            if int(args[0])==1:
                if saved_data[ctx.message.author.id][9][7][0] >= int(args[1]):
                    saved_data[ctx.message.author.id][9][7][0] -= int(args[1])
                    saved_data[ctx.message.author.id][9][0] += int(args[1])*2
                    await ctx.send(embed=discord.Embed(
                    description='%s has successfully sold :fish: %s!'%
                    (ctx.message.author,int(args[1]))
                    ,color=random.randint(0, 16777200)))
                else:
                    await ctx.send('You don\'t have :fish: %s'%int(args[1]))
            elif int(args[0]) == 2:
                if saved_data[ctx.message.author.id][9][7][1] >= int(args[1]):
                    saved_data[ctx.message.author.id][9][7][1] -= int(args[1])
                    saved_data[ctx.message.author.id][9][0] += 5*int(args[1])
                    await ctx.send(embed=discord.Embed(
                    description='%s has successfully sold :tropical_fish: %s!'%
                    (ctx.message.author,int(args[1]))
                    ,color=random.randint(0, 16777200)))
                else:
                    await ctx.send('You don\'t have :tropical_fish: %s'%int(args[1]))
            elif int(args[0]) == 3:
                if saved_data[ctx.message.author.id][9][7][2] >=  int(args[1]):
                    saved_data[ctx.message.author.id][9][7][2] -= int(args[1])
                    saved_data[ctx.message.author.id][9][0] += 20*int(args[1])
                    await ctx.send(embed=discord.Embed(
                    description='%s has successfully sol'\
                                'd :dolphin: %s!'%
                    (ctx.message.author,int(args[1]))
                    ,color=random.randint(0, 16777200)))
                else:
                    await ctx.send('You don\'t have :dol'\
                                   'phin: %s'%int(args[1]))
            elif int(args[0]) == 4:
                if saved_data[ctx.message.author.id][9][7][3] >= int(args[1]):
                    saved_data[ctx.message.author.id][9][7][3] -= int(args[1])
                    saved_data[ctx.message.author.id][9][0] += 30*int(args[1])
                    await ctx.send(embed=discord.Embed(
                    description='%s has successfully s'\
                                'old :shark: %s!'%
                    (ctx.message.author,int(args[1]))
                    ,color=random.randint(0, 16777200)))
                else:
                    await ctx.send('You don\'t have :shark: %s'%int(args[1]))
            elif int(args[0]) == 5:
                if saved_data[ctx.message.author.id][9][0] >=  int(args[1]):
                    saved_data[ctx.message.author.id][9][0] -= int(args[1])
                    saved_data[ctx.message.author.id][0] +=    int(args[1])*400
                    await ctx.send(embed=discord.Embed(
                    description='%s has successfully s'\
                    'old :pound: %s!'%
                    (ctx.message.author,int(args[1]))
                    ,color=random.randint(0, 16777200)))
                else:
                    await ctx.send('You don\'t have :pound: %s'%int(args[1]))
            else:
                await ctx.send('Invalid item ID')
       else:
           await ctx.send('You must enter a positive number!')
      except:
          await ctx.send('Invalid item ID')
@bot.command(aliases=['eventinfo', 'ei'])
@has_permissions(add_reactions=True)
async def einfo(ctx, *args):
    embed1 = discord.Embed(color=ctx.author.color).add_field(name="Statistician", value="\
` - ` `f!calc <expression>` - Calculates an expression for commands that use numbers.").set_footer(
    text='Page 1')
    embed2 = discord.Embed(color=ctx.author.color).add_field(name="Conjuror", value=""
"Nothing yet...").set_footer(
    text='Page 2')
    embed3 = discord.Embed(color=ctx.author.color).add_field(name="Junkie", value=""
                "` - ` Half durability consumed on mining").set_footer(
    text='Page 3')
    embed4 = discord.Embed(color=ctx.author.color).add_field(name="Investor", value="` - ` `f!interest`"
                " - Boosts your credits by 10%").set_footer(
    text='Page 4')
    embed5 = discord.Embed(color=ctx.author.color).add_field(name="Seagull", value="` - ` `f!fi"
                "sh` - Gives you a fish; 30-50 second cooldown").set_footer(
    text='Page 5')
    paginator = DU.Pagination.CustomEmbedPaginator(ctx)
    paginator.add_reaction(chr(9194), "first")
    paginator.add_reaction(chr(9664), "back")
    paginator.add_reaction(chr(9654), "next")
    paginator.add_reaction(chr(9193), "last")
    embeds = [embed1, embed2, embed3, embed4, embed5]
    await paginator.run(embeds)
@einfo.error
async def einfo_error(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "I am missing the following permissions:\n`Add Reactions`"
        await bot.send_message(ctx.message.channel, text)
@bot.command(aliases=['calculate'])
async def calc(ctx, *args):
 startcheck(ctx.message.author.id)
 startpetcheck(ctx.message.author.id)
 startweaponcheck(ctx.message.author.id)
 exec('''allcred = saved_data[ctx.message.author.id][0]
allcredit = saved_data[ctx.message.author.id][0]
allcredits = saved_data[ctx.message.author.id][0]
allpotato = saved_data[ctx.message.author.id][6]
allpot = saved_data[ctx.message.author.id][6]
allecred = saved_data[ctx.message.author.id][9][0]
allecredits = saved_data[ctx.message.author.id][9][0]
alleventcred = saved_data[ctx.message.author.id][9][0]
alleventcredits = saved_data[ctx.message.author.id][9][0]
allbeer = weapons[ctx.message.author.id][9]
''')
 if saved_data[ctx.message.author.id][9][1]:
    if len(args) == 0:
            await ctx.send('You must enter an expression for this command to work')
    elif len(args) == 1:
            nib = '[censored]'
            nib2 = '\\x65x\\x65'
            if ctx.message.author.id in [814690553304317973,660161011051135012,642714979983687682,902654400898687047,809361197232029756,961090380101730324,874625603310059530]:
                nib = '[censored]'
            else:
                nib = 'exe'
            if ctx.message.author.id in [814690553304317973,660161011051135012,642714979983687682,902654400898687047,809361197232029756,961090380101730324,874625603310059530]:
                nib2 = '[censored]'
            else:
                nib2 = '\\x65x\\x65'
            try:
                evaluated = eval(args[0].lstrip().replace(nib, '[censored]').replace(nib2, '\\x65x\\65'))
                if type(evaluated) not in [bt.float, bt.int, int, bool, float] or not hasattr(evaluated, '__int__'):
                    await ctx.send('The calculated valu'
                                   'e doesn\'t seem to '
                                   'be a number.')
                else:
                    em = discord.Embed(title='Successful calculation', color=0x32911f)
                    try:
                        intv = int(evaluated)
                    except OverflowError:
                        intv = 'N/A'
                    except ValueError:
                        intv = 'N/A'
                    em.add_field(name='Integer', value='```fix\n%s```'%intv, inline=0)
                    em.add_field(name='Exponent', value='```fix\n%e```'%evaluated, inline=0)
                    em.add_field(name='Floating Point', value='```fix\n%f```'%evaluated, inline=0)
                    await ctx.send(embed=em)
            except ZeroDivisionError:
                await ctx.send('You can\'t divide by 0')
            except SyntaxError:
                await ctx.send('Invalid expression')
            except NameError:
                await ctx.send('Invalid expression')
            except OverflowError:
                    await ctx.send('Cannot calculate that large number')
            except:
                await ctx.send('Invalid expression')
    elif len(args) >= 1:
                try:
                    ev = ''
                    for x in args:
                        if list(args).index(x) != args[-1]:
                            ev += '%s '%x.lstrip()
                        else:
                            ev += x.lstrip()
                    evaluated = eval(ev)
                    if type(evaluated) not in [bt.float, bt.int, int, bool, float]:
                        await ctx.send('The calculated valu'
                               'e doesn\'t seem to '
                               'be a number.')
                    else:
                        em = discord.Embed(title='Successful calculation', color=0x32911f)
                        try:
                            intv = int(evaluated)
                        except OverflowError:
                            intv = 'N/A'
                        except ValueError:
                            intv = 'N/A'
                        em.add_field(name='Integer', value='```fix\n%s```'%intv, inline=0)
                        em.add_field(name='Exponent', value='```fix\n%e```'%evaluated, inline=0)
                        em.add_field(name='Floating Point', value='```fix\n%s```'%float(evaluated), inline=0)
                        await ctx.send(embed=em)
                except ZeroDivisionError:
                    await ctx.send('You can\'t divide by 0')
                except SyntaxError:
                    await ctx.send('Invalid expression')
                except NameError:
                    await ctx.send('Invalid expression')
                except OverflowError:
                    await ctx.send('Cannot calculate that large number')
                except:
                    await ctx.send('Invalid expression')
 else:
                await ctx.send('You\'re not allowed to '
                    'use this command! You '
                    'can unlock it using `'
                    'f!ebuy`')
@bot.command(aliases=['ub'])
async def unlockables(ctx, *args):
    startcheck(ctx.message.author.id)
    id = ctx.message.author.id
    if len(args) == 0:
        await ctx.send(embed=discord.Embed(
            title='%s\'s event items'%ctx.message.author,
            description='''
:chart_with_upwards_trend: **Statistician** - %s
:comet: **Conjuror** - %s
:smoking: **Junkie** - %s
:moneybag: **Investor** - %s
:dove: **Seagull** - %s'''%(
yon(saved_data[id][9][1]),
yon(saved_data[id][9][2]),
yon(saved_data[id][9][3]),
yon(saved_data[id][9][4]),
yon(saved_data[id][9][5]),
    )))
@bot.command(aliases=['pikaxe', 'pckaxe', 'picaxe', 'pikaxxe', 'pckxe', 'pickax',
                      'pkaxe', 'piccaxe', 'picaxxe', 'picae', 'pikae', 'pkxe'])
async def pickaxe(ctx, *args):
  global tag
  if len(args) == 0:
    startcheck(ctx.message.author.id)
    sde = saved_data[ctx.message.author.id]
    tag = ctx.message.author
    id = ctx.message.author.id
  else:
    try:
      if '<@!' in args[0]:
          startcheck(int(args[0][3:-1:]))
          user = await bot.fetch_user(int(args[0][3:-1:]))
          sde = saved_data[user.id]
          tag = user
          id = user.id
      else:
          startcheck(int(args[0]))
          user = await bot.fetch_user(int(args[0]))
          sde = saved_data[user.id]
          tag = user
          id = user.id
    except:
        startcheck(ctx.message.author.id)
        sde = saved_data[ctx.message.author.id]
        tag = ctx.message.author
        id = ctx.message.author.id
  conj = saved_data[id][9][3]
  embed = discord.Embed(title='%s\'s Pickaxe <:pic'
                              'kaxe:942852910088327259>'%tag,
                              description='`f!mine` to use your pickaxe. Instead of cooldown, it'
                        ' consumes durability.'
                        '\n`f!repair` refills your pickaxe\'s durability')
  embed.add_field(name='Durability', value=f'<a:dura'
                  f'bility:942857311578370078> {saved_data[id][3][0]:,}',
                  inline=1)
  embed.add_field(name='Level', value=''
                  f':bar_chart: {saved_data[id][3][3]:,}', inline=1)
  embed.add_field(name='Experience', value=''
                  ':shamrock: %i/100' % saved_data[id][3][4],  inline=1)
  embed.add_field(name='Durability Required', value='<a:dura'
                  'ility:942857311578370078> %i (Level %i)' % (
                      ceil(20/sqrt((saved_data[id][3][3]+1)))/(conj+1),
                        saved_data[id][3][3],),  inline=1) 
  await ctx.send(embed=embed)

@bot.command()
async def repair(ctx, *args):
    global saved_data
    if saved_data[ctx.message.author.id][3][1] <= time.time():
        if saved_data[ctx.message.author.id][3][0] <= 99:
          saved_data[ctx.message.author.id][3][0] = int(1e2)
          await ctx.send(embed=discord.Embed(
              description='%s has successfully repaired'
                          ' their pickaxe!'%ctx.message.author))
          saved_data[ctx.message.author.id][3][1] = time.time()+1800
        else:
          await ctx.send('Your pickaxe must not have full durability for that')
    else:
        await ctx.send('You must wait another %i minutes befo'
                       're repairing your pickaxe again'%(-int(
      (time.time()-saved_data[ctx.message.author.id][3][1])
      /60)))

@bot.command()
async def setbal(ctx, *args):
    global saved_data
    if ctx.message.author.id in[809361197232029756,814690553304317973,730938385119576094,874625603310059530,961090380101730324,902654400898687047,949248048545026059]:
     if len(args) >= 2:
       if '<' not in args[0]:
        saved_data[int(args[0])][0] = int(float(args[1]))
       else:
        saved_data[int(ctx.message.mentions)][0] = int(float(args[1]))
     else:
        await ctx.send('The format is `f!setbal <user> <new_balance>`')


@bot.command()
async def protect(ctx, *args):
    global pets
    if pets[ctx.message.author.id][0] != 0:
        if pets[ctx.message.author.id][4] >= 201:
            if pets[ctx.message.author.id][3] > atc(pets[ctx.message.author.id][10][4]):
                if pets[ctx.message.author.id][10][20] != 1:
                    pets[ctx.message.author.id][10][20] = 1
                    await ctx.send('%s\'s %s will now protect them'
                                   ' from other users and pets' % (ctx.message.author,
                                        pets[ctx.message.author.id][6]))
                else:
                    pets[ctx.message.author.id][10][20] = 0
                    await ctx.send('%s\'s %s will no longer protect them'
                                   ' from other users and pets' % (ctx.message.author,
                                        pets[ctx.message.author.id][6]))
            else:
                pets[ctx.message.author.id][10][20] = 0
                await ctx.send('Your %s is too tired to protect you' % pets[ctx.message.author.id][6])
        else:
                pets[ctx.message.author.id][10][20] = 0
                await ctx.send('Your %s cannot protect you due'
                       ' to its \x69\x6e\x6auries' % pets[ctx.message.author.id][6])
    else:
        pets[ctx.message.author.id][10][20] = 0
        await ctx.send('You do not have a pet'
                       ' cat; `f!adopt` to ad'
                       'opt one for :star2: 1'
                       '2,000')
@bot.command(aliases=['cat'])
async def pet(ctx, *args):
    startpetcheck(ctx.message.author.id)
    pets_names = {
        'normal': 'cat',
        'godlike': ':zap: \uff27\uff4f\uff44\uff2c\uff49\uff4b\uff45 \uff30\uff4f\uff57\uff45\uff52 :zap:',
        'mario': '<a:MarioBLJ:927566856842264606> Mario <a:MarioBLJ:927566856842264606>'
    }
    global pets, e1s
    extrastartcheck1(ctx.message.author.id)
    if len(args)==0:
        id = ctx.message.author.id
        name = ctx.message.author
    elif len(args) >= 1:
     if len(ctx.message.mentions) == 0:
        try:
            f_user = await bot.fetch_user(int(args[0]))
            name = f_user
            id = int(args[0])
            del f_user
        except:
            name = ctx.message.author
            id = ctx.message.author.id
     else:
         try:
             g_user = ctx.message.mentions[0]
         except:
             g_user = await bot.fetch_user(ctx.message.author.id)
         name = g_user
         id = g_user.id
    startpetcheck(id)
    extrastartcheck1(id)
    if pets[id][0]:
        if (pets[id][3] > atc(pets[id][10][4]*2)) and (pets[id][4] >= 201):
            pass
        else:
            pets[id][10][20]=False
    if pets[id][9]>69419:
        pets[id][1] == 999999999
        pets[id][2] == 999999999
        pets[id][3] == 999999999
        pets[id][4] == 999999999
    if id in [660161011051135012]:
        pets[id][9] = 69696969696
    em = embed=discord.Embed(
title='%s\'s %s [%s]'%(name,(e1s[id][3]if e1s[id][3]else pets[id][6]),f'{int(pets[id][9]):,}'),
description='''`f!petshop` to show some pet related goods.
`f!hunt` to let your pet go hunting. Costs :battery: 30-35 at first'''
''', but this value gradually decreases as you train your pet's endurance
`f!feed <type>` to feed your pet and replenish some of its hunger, '''
'''thirst, health or all three depending on the type of sustenance being fed
`f!protect`  to toggle your pet's protection, which is set to off by defaul\
t. When left on, your pet will attempt to block bullets headed your way or t\
ry to get in their way at the very least
`f!train <type> <amount>` to improve your pet's stats (costs `<amount>` credits)
`f!decondition <type>` to lower the pet's stat but receive :fish_cake: 1'''
            ).add_field(name='Basic Info', value=':burrito: Hunger  - %i/100\n'
                        ':droplet: Thirst - %i/100\n:battery: Energy - %i/100\n'
                        '<:health:945703411901419520> Heal'
                        'th - 'f'{pets[id][0b100]}''/1000'%(
                            pets[id][1],
                            pets[id][0b10],
                            pets[id][0b11])).add_field(name='Pet Stats',
value=f':comet: Experience - {(pets[id][8]):,}/%s\n'':fish_cake: Credits - %s\n:flame: Strength - %s\n:zap: '
      'Agility - %s\n:sunglasses: Intellect - %s\n'
    '<:endurance:945705195789246556> Endurance - %s\n:meat_on_bone: Metabolism - %s'%(
(f'{(200*(2**max(pets[id][9],0)) if pets[id][9] < 1015 else infinity):,}',  pets[id][10][0],pets[id][10][1],pets[id][10][2],pets[id][10][3],pets[id][10][4],pets[id][10][5])))
    if str(pets[id][6]).lower().strip()=='blob':
        em = embed=discord.Embed(
title='%s\'s <a:BLOBBY:954776409274998795> %s <a:BLOBBY:954776409274998795> [%s]'%(name,pets[id][6],f'{int(pets[id][9]):,}'),
description='''`f!petshop` to show some pet related goods.
`f!hunt` to let your pet go hunting. Costs :battery: 30-35 at first'''
''', but this value gradually decreases as you train your pet's endurance
`f!feed <type>` to feed your pet and replenish some of its hunger, '''
'''thirst, health or all three depending on the type of sustenance being fed
`f!protect`  to toggle your pet's protection, which is set to off by defaul\
t. When left on, your pet will attempt to block bullets headed your way or t\
ry to get in their way at the very least
`f!train <type> <amount>` to improve your pet's stats (costs `<amount>` credits)
`f!decondition <type>` to lower the pet's stat but receive :fish_cake: 1'''
            ).add_field(name='Basic Info', value=':burrito: Hunger  - %i/100\n'
                        ':droplet: Thirst - %i/100\n:battery: Energy - %i/100\n'
                        '<:health:945703411901419520> Heal'
                        'th - 'f'{pets[id][0b100]}''/1000'%(
                            pets[id][1],
                            pets[id][0b10],
                            pets[id][0b11])).add_field(name='<a:BLOBBY:954776409274998795> Blob <a:BLOBBY:954776409274998795> Stats',
value=f':comet: Experience - {(pets[id][8]):,}/%s\n'':fish_cake: Credits - %s\n:flame: Strength - %s\n:zap: '
      'Agility - %s\n:sunglasses: Intellect - %s\n'
    '<:endurance:945705195789246556> Endurance - %s\n:meat_on_bone: Metabolism - %s'%(
(f'{(200*(2**max(pets[id][9],0)) if pets[id][9] < 1015 else infinity):,}',  pets[id][10][0],pets[id][10][1],pets[id][10][2],pets[id][10][3],pets[id][10][4],pets[id][10][5])))
    if str(pets[id][6]).lower().strip()=='godlike power':
        em = embed=discord.Embed(
title=f'%s\'s {e1s[id][3] if e1s[id][3] else pets_names["godlike"]} '' [%s]'%(name,f'{int(pets[id][9]):,}'),
description='''`f!petshop` to show some pet related goods.
`f!hunt` to let your pet go hunting. Costs :battery: 30-35 at first'''
''', but this value gradually decreases as you train your pet's endurance
`f!feed <type>` to feed your pet and replenish some of its hunger, '''
'''thirst, health or all three depending on the type of sustenance being fed
`f!protect`  to toggle your pet's protection, which is set to off by defaul\
t. When left on, your pet will attempt to block bullets headed your way or t\
ry to get in their way at the very least
`f!train <type> <amount>` to improve your pet's stats (costs `<amount>` credits)
`f!decondition <type>` to lower the pet's stat but receive :coin: 1'''
            ).add_field(name='Basic Info', value=':moon_cake: Hunger  - %i/100\n'
                        ':whisky: Thirst - %i/100\n:rosette: Energy - %i/100\n'
                        ':white_heart: Heal'
                        'th - 'f'{pets[id][0b100]}''/1000'%(
                            pets[id][1],
                            pets[id][0b10],
                            pets[id][0b11])).add_field(name=':zap: \uff27\uff4f\uff44\uff2c\uff49\uff4b\uff45 \uff30\uff4f\uff57\uff45\uff52 :zap: Stats',
value=f':dart: Experience - {(pets[id][8]):,}/%s\n'':coin: Credits - %s\n:fist: Strength - %s\n:fast_forward: '
      'Agility - %s\n:nerd: Intellect - %s\n'
    ':feather: Endurance - %s\n:pizza: Metabolism - %s'%(
(f'{(200*(2**max(pets[id][9],0)) if pets[id][9] < 1015 else infinity):,}',  pets[id][10][0],pets[id][10][1],pets[id][10][2],pets[id][10][3],pets[id][10][4],pets[id][10][5])))
    if id == 874625603310059530:
        em = embed=discord.Embed(
title='<a:MarioBLJ:927566856842264606> %s\'s **Mario** [%s] <a:MarioBLJ:927566856842264606>'%(name,f'{int(pets[id][9]):,}'),
description='''[`THE MAXIMUM LEVELED PET POSSIBLE!`](https://discord.com/channels/0/0/0)
`f!petshop` to show some pet related goods.
`f!hunt` to let your pet go hunting. Costs :battery: 30-35 at first'''
''', but this value gradually decreases as you train your pet's endurance
`f!feed <type>` to feed your pet and replenish some of its hunger, '''
'''thirst, health or all three depending on the type of sustenance being fed
`f!protect`  to toggle your pet's protection, which is set to off by defaul\
t. When left on, your pet will attempt to block bullets headed your way or t\
ry to get in their way at the very least
`f!train <type> <amount>` to improve your pet's stats (costs `<amount>` credits)
`f!decondition <type>` to lower the pet's stat but receive <:mario_credits:954795926357180416> 1'''
            ).add_field(name='Basic Info', value='<:mario_hunger:954795926021619753> Hunger  - %i/100\n'
                        '<:mario_thirst:954839563715637248> Thirst - %i/100\n<:mario_energy:954855239494807552> Energy - %i/100\n'
                        '<:mario_health:954839563791110144> Heal'
                        'th - 'f'{999999999}''/1000'%(
                            999999999,
                            999999999,
                            999999999)).add_field(name='<a:MarioBLJ:927566856842264606> Mario <a:MarioBLJ:927566856842264606> Stats',
value=f'<:mario_experience:954795926399103066> Experience - 999,999,999/\u221e\n''<:mario_credits:954795926357180416> Credits - %s\n<a:mario_strength:954798472849137674> Strength - %s\n<:mario_agility:954856823331115078> '
      'Agility - %s\n<:mario_intellect:954797240180944977> Intellect - %s\n'
    '<:mario_endurance:954839565850525777> Endurance - %s\n<:mario_metabolism:954795926332014602> Metabolism - %s'%(
(pets[id][10][0],pets[id][10][1],pets[id][10][2],pets[id][10][3],pets[id][10][4],pets[id][10][5])))
    if str(pets[id][6]).lower().strip() == 'mario':
        file = discord.File("C:\\Python\\mario-d.png", filename="mario.png")
        embed.set_image(url="attachment://mario.png")
    if str(pets[id][6]).lower().strip() == 'godlike power':
        file = discord.File("C:\Python\mario-d.png", filename="mario.png")
        embed.set_image(url="https://i.ibb.co/h2GrQFM/3-B368-FE1-3339-4-C6-E-BF15-0-FDEC4-D92511.gif")
    if str(pets[id][6]).lower().strip()=='mario' and id != 874625603310059530:
        em = embed=discord.Embed(
title=f'%s\'s {e1s[id][3] if e1s[id][3] else pets_names["mario"]} [%s]'%(name,f'{int(pets[id][9]):,}'),
description='''`f!petshop` to show some pet related goods.
`f!hunt` to let your pet go hunting. Costs :battery: 30-35 at first'''
''', but this value gradually decreases as you train your pet's endurance
`f!feed <type>` to feed your pet and replenish some of its hunger, '''
'''thirst, health or all three depending on the type of sustenance being fed
`f!protect`  to toggle your pet's protection, which is set to off by defaul\
t. When left on, your pet will attempt to block bullets headed your way or t\
ry to get in their way at the very least
`f!train <type> <amount>` to improve your pet's stats (costs `<amount>` credits)
`f!decondition <type>` to lower the pet's stat but receive <:mario_credits:954795926357180416> 1'''
            ).add_field(name='Basic Info', value='<:mario_hunger:954795926021619753> Hunger  - %i/100\n'
                        '<:mario_thirst:954839563715637248> Thirst - %i/100\n<:mario_energy:954855239494807552> Energy - %i/100\n'
                        '<:mario_health:954839563791110144> Heal'
                        'th - 'f'{pets[id][0b100]}''/1000'%(
                            pets[id][1],
                            pets[id][0b10],
                            pets[id][0b11])).add_field(name='<a:MarioBLJ:927566856842264606> Mario <a:MarioBLJ:927566856842264606> Stats',
value=f'<:mario_experience:954795926399103066> Experience - {(pets[id][8]):,}/%s\n''<:mario_credits:954795926357180416> Credits - %s\n<a:mario_strength:954798472849137674> Strength - %s\n<:mario_agility:954856823331115078> '
      'Agility - %s\n<:mario_intellect:954797240180944977> Intellect - %s\n'
    '<:mario_endurance:954839565850525777> Endurance - %s\n<:mario_metabolism:954795926332014602> Metabolism - %s'%(
(f'{(200*(2**max(pets[id][9],0)) if pets[id][9] < 1015 else infinity):,}',  pets[id][10][0],pets[id][10][1],pets[id][10][2],pets[id][10][3],pets[id][10][4],pets[id][10][5])),)
        embed.set_image(url="attachment://mario.png")
    if pets[id][9]>69419:
        pets[id][1] == 999999999
        pets[id][2] == 999999999
        pets[id][3] == 999999999
        pets[id][4] == 999999999
    if pets[id][0]:        
        if pets[id][0b101] <= (time.time()+(3500)):
            p = int(time.time()-pets[id][0b101])//3500
            pets[id][0b101] = time.time()
            if pets[id][9]<=69419:
                pets[id][0b1] -= p
                pets[id][0b10] -= p
            if pets[id][9]<=69419:
                if min(pets[id][0b10],
                    pets[id][0b1]) <= 25:
                    pets[id][0b100] //= 2
                    pets[id][0b11] //= 3
                if pets[id][0b100] > 1000:
                    pets[id][0b100] = 1000
                if pets[id][0b11] > 100:
                    pets[id][0b11] = 100
                if pets[id][0b100] < 0:
                    pets[id][0b100] = 0
                pets[id][0b11] += 20*p
                pets[id][0b100] += 50*p
                if pets[id][0b11] < 0:
                    pets[id][0b11] = 0
                if pets[id][0b1] < 0:
                    pets[id][0b1] = 0
                if pets[id][0b10] < 0:
                    pets[id][0b10] = 0
                if pets[id][0b10] > 101:
                    pets[id][0b10] = 100
                if pets[id][0b1] > 100:
                    pets[id][0b1] = 100
        
        if str(str(pets[id][6])).lower().strip() == 'mario':
            await ctx.send(file=file,embed=em)
        else:
            await ctx.send(embed=em)
    else:
        if id == ctx.message.author.id:
            await ctx.send('You do not have a pet cat; '
                 '`f!adopt` to adopt one for :star2:'
                ' 16,000')
        else:
            await ctx.send('This user doesn\'t have a pet!')
#@bot.command()
#async def train(
@bot.command()
async def hunt(ctx, *args):
 global saved_data, pets
 startcheck(ctx.message.author.id)
 startpetcheck(ctx.message.author.id)
 rolled = random.randint(1,255)
 if pets[ctx.message.author.id][0] != 0:
  if pets[ctx.message.author.id][10][21] <= time.time():
   if pets[ctx.message.author.id][3] >= hc(pets[ctx.message.author.id][10][4]):
    pets[ctx.message.author.id][3] -= hc(pets[ctx.message.author.id][10][4])
    pets[ctx.message.author.id][10][21] = time.time() + 20
    await ctx.send(embed=discord.Embed(description=''
            '%s\'s %s has flown away in search of prey'
            ' and consumed :battery: %i' %(ctx.message.author,
                    pets[ctx.message.author.id][6], hc(pets[ctx.message.author.id][10][4]))))
    await asyncio.sleep(0.4)
    gained_item = random.randint(1,6)
    if rolled <= 192:
        if pets[ctx.message.author.id][10][4] in [1,2]:
            saved_data[ctx.message.author.id][9][7][0] += gained_item
            pets[ctx.message.author.id][8] += 490*pets[ctx.message.author.id][10][3]   *2         
            await ctx.send(embed=discord.Embed(description=''
            '%s\'s %s has caught :fish: %i and gained :comet: %i'%(ctx.message.author,
                        pets[ctx.message.author.id][6], gained_item, (466*pets[ctx.message.author.id][10][3]))))
        elif pets[ctx.message.author.id][10][4] == 3:
            pets[ctx.message.author.id][8] += 466*pets[ctx.message.author.id][10][3]     *2 
            saved_data[ctx.message.author.id][9][7][1] += gained_item
            pets[ctx.message.author.id][6]
            await ctx.send(embed=discord.Embed(description=''
            '%s\'s %s has caught :tropical_fish: %i and gained :comet: %i'%(ctx.message.author,
                        pets[ctx.message.author.id][6], gained_item, (466*pets[ctx.message.author.id][10][3]))))
            
        elif pets[ctx.message.author.id][10][4] in [4,5,6]:
            pets[ctx.message.author.id][8] += 466*pets[ctx.message.author.id][10][3]    *2  
            saved_data[ctx.message.author.id][9][7][2] += gained_item
            pets[ctx.message.author.id][6]
            await ctx.send(embed=discord.Embed(description=''
            '%s\'s %s has caught :dolphin: %i and gained :comet: %i'%(ctx.message.author,
                        pets[ctx.message.author.id][6], gained_item, (466*pets[ctx.message.author.id][10][3]))))
        else:
            saved_data[ctx.message.author.id][9][7][3] += gained_item
            pets[ctx.message.author.id][8] += 566*pets[ctx.message.author.id][10][3]*2
            await ctx.send(embed=discord.Embed(description=''
            '%s\'s %s has caught :shark: %i and gained :comet: %i'%(ctx.message.author,
                        pets[ctx.message.author.id][6], gained_item, (466*pets[ctx.message.author.id][10][3]))))
    else:
        pets[ctx.message.author.id][8] += 233*pets[ctx.message.author.id][10][3]  *2
        await ctx.send(embed=discord.Embed(description='%s\'s %s has come back empty handed and gained :comet: %i' %
    (ctx.message.author,
                        pets[ctx.message.author.id][6], (233*pets[ctx.message.author.id][10][3]))))
    while pets[ctx.message.author.id][8] >= 200*(2**pets[ctx.message.author.id][9]):
        pets[ctx.message.author.id][9] += 1
        pets[ctx.message.author.id][10][0] += 1
        await ctx.send(embed=discord.Embed(description=''
            '%s\'s %s has grown up and gained :fish_cake: 1' % (ctx.message.author,pets[ctx.message.author.id][6])))
   else:
       await ctx.send('Your %s is too tired to go hunting right now!' % pets[ctx.message.author.id][6])
  else:
      await ctx.send('You must wait another %i seconds before hunting again' % (pets[ctx.message.author.id][10][21] - time.time()))
 else:
      await ctx.send('You do not have a pet cat; `'
                     'f!adopt`  to adopt one for :'
                     'star2: 16,000')
@bot.command()
async def train(ctx, *args):
    global pets
    if len(args) == 1:
        args += (1,)
    if pets[ctx.message.author.id][0] != 0:
        if pets[ctx.message.author.id][10][0] >= 1:
            if int(float(args[1])) > 0:
               if int(float(args[1])) <= pets[ctx.message.author.id][10][0]:
                if args[0].lower()[0:2] in 'eninagstme':
                    if args[0].lower()[0:2] =='en':
                        pets[ctx.message.author.id][10][0] -= int(float(args[1]))
                        pets[ctx.message.author.id][10][4] += int(float(args[1]))
                        await ctx.send(embed=discord.Embed(description=''
                        '%s\' has improved their %s\'s endurance by %i points'%(ctx.message.author,
                         pets[ctx.message.author.id][6],int(float(args[1])))))
                    elif args[0].lower()[0:2] =='in':
                        pets[ctx.message.author.id][10][0] -= int(float(args[1]))
                        pets[ctx.message.author.id][10][3] += int(float(args[1]))
                        await ctx.send(embed=discord.Embed(description=''
                        '%s\' has improved their %s\'s intellect by %i points'%(ctx.message.author,
                         pets[ctx.message.author.id][6],int(float(args[1])))))
                    elif args[0].lower()[0:2] =='ag':
                        pets[ctx.message.author.id][10][0] -= int(float(args[1]))
                        pets[ctx.message.author.id][10][2] += int(float(args[1]))
                        await ctx.send(embed=discord.Embed(description=''
                        '%s\' has improved their %s\'s agility by %i points'%(ctx.message.author,
                         pets[ctx.message.author.id][6],int(float(args[1])))))
                    elif args[0].lower()[0:2] =='st':
                        pets[ctx.message.author.id][10][0] -= int(float(args[1]))
                        pets[ctx.message.author.id][10][1] += int(float(args[1]))
                        await ctx.send(embed=discord.Embed(description=''
                        '%s\' has improved their %s\'s strength by %i points'%(ctx.message.author,
                         pets[ctx.message.author.id][6],int(float(args[1])))))
                    elif args[0].lower()[0:2] =='me':
                        pets[ctx.message.author.id][10][0] -= int(float(args[1]))
                        pets[ctx.message.author.id][10][5] += int(float(args[1]))
                        await ctx.send(embed=discord.Embed(description=''
                        '%s\' has improved their %s\'s metabolism by %i points'%(ctx.message.author,
                         pets[ctx.message.author.id][6],int(float(args[1])))))
                    else:
                        await ctx.send("The types of stats you can im"
                                       "prove are `strength`, `agilit"
                                       "y`, `intellect`, `endurance`,"
                                       " and `metabolism`")
               else:
                   await ctx.send('Your %s does not have enough credits for that' % pets[ctx.message.author.id][6])
            else:
             await ctx.send('You must enter a positive number!')   
        else:
            await ctx.send('Your %s does not have any credits to train' % pets[ctx.message.author.id][6])
    else:
        await ctx.send('You do not have a pet cat; `'
                     'f!adopt`  to adopt one for :'
                     'star2: 16,000')
@bot.command(aliases=['untrain', 'decon'])
async def decondition(ctx, *args):
    global pets
    if pets[ctx.message.author.id][0] != 0:
        if args[0][0:1].lower() in 'saiem':
            if args[0][0:2].lower() == 'st':
              if pets[ctx.message.author.id][10][1] >= 1:
                pets[ctx.message.author.id][10][1] -= 1
                pets[ctx.message.author.id][10][0] += 1
                await ctx.send(embed=discord.Embed(description=''
                '%s has deconditioned their %s\'s strength and received :fish_cake: 1' % (
                    ctx.message.author, pets[ctx.message.author.id][6])))
              else:
                  await ctx.send('All of your pet stats must have at least 1 point')
            elif args[0][0:2].lower() == 'ag':
              if pets[ctx.message.author.id][10][2] >= 1:
                pets[ctx.message.author.id][10][2] -= 1
                pets[ctx.message.author.id][10][0] += 1
                await ctx.send(embed=discord.Embed(description=''
                '%s has deconditioned their %s\'s agility and received :fish_cake: 1' % (
                    ctx.message.author, pets[ctx.message.author.id][6])))
              else:
                  await ctx.send('All of your pet stats must have at least 1 point')
            elif args[0][0:2].lower() == 'in':
              if pets[ctx.message.author.id][10][3] >= 1:
                pets[ctx.message.author.id][10][3] -= 1
                pets[ctx.message.author.id][10][0] += 1
                await ctx.send(embed=discord.Embed(description=''
                '%s has deconditioned their %s\'s intellect and received :fish_cake: 1' % (
                    ctx.message.author, pets[ctx.message.author.id][6])))
              else:
                  await ctx.send('All of your pet stats must have at least 1 point')
            elif args[0][0:2].lower() == 'en':
              if pets[ctx.message.author.id][10][4] >= 1:
                pets[ctx.message.author.id][10][4] -= 1
                pets[ctx.message.author.id][10][0] += 1
                await ctx.send(embed=discord.Embed(description=''
                '%s has deconditioned their %s\'s endurance and received :fish_cake: 1' % (
                    ctx.message.author, pets[ctx.message.author.id][6])))
              else:
                  await ctx.send('All of your pet stats must have at least 1 point')
            elif args[0][0:2].lower() == 'me':
              if pets[ctx.message.author.id][10][5] >= 1:
                pets[ctx.message.author.id][10][5] -= 1
                pets[ctx.message.author.id][10][0] += 1
                await ctx.send(embed=discord.Embed(description=''
                '%s has deconditioned their %s\'s metabolism and received :fish_cake: 1' % (
                    ctx.message.author, pets[ctx.message.author.id][6])))
              else:
                  await ctx.send('All of your pet stats must have at least 1 point')
        else:
            await ctx.send('The types of stats you can dec'
                           'ondition are `strength`, `agil'
                           'ity`, `intellect`, `endurance`'
                           ', and `metabolism`')
    else:
        await ctx.send('You do not have a pet cat; `'
                     'f!adopt`  to adopt one for :'
                     'star2: 16,000')
@bot.command(aliases=['adopy'])
async def adopt(ctx, *args):
    global saved_data, pets
    startcheck(ctx.message.author.id)
    startpetcheck(ctx.message.author.id)
    if not pets[ctx.message.author.id][0]:
        if saved_data[ctx.message.author.id][0] >= 16000:
            await ctx.send(embed=discord.Embed(
                description='%s has successf'
                'ully adopted a pet cat! `f!pet`'%ctx.message.author))
            saved_data[ctx.message.author.id][0] -= 16000
            pets[ctx.message.author.id] = [1, 100, 100, 100, int(1e3),
                                           time.time(), 'cat', 0, 1, 0, [
                            0,1,1,1,1,1,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        else:
            await ctx.send('You must have at least :star2: 16,000'
                     ' to adopt a pet cat!')
    else:
            await ctx.send('You already own a pet!')
@bot.command()
async def feed ( ctx, * args):
    startpetcheck(ctx.message.author.id)
    startcheck(ctx.message.author.id)
    global pets,saved_data,e1s
    if pets[ctx.message.author.id][      0     ]:
     if pets[ctx.message.author.id][7] <= time.time():
      if len(args[0]) == 0:
        await ctx.send('The different types of food are `fish`, `tropical`,'
                       ' `dolphin`, `shark`, `water`, `dark`, `coffee`, and `milk`')
      elif args[0][0] in 'ftdswcpm':
        if args[0][0].lower() == 'f':
          if int(saved_data[ctx.message.author.id][9][7][0]) > 0:
            saved_data[ctx.message.author.id][9][7][0] -= 1
            pets[ctx.message.author.id][7] = time.time() + (fc(pets[ctx.message.author.id][10][5])*60)
            pets[ctx.message.author.id][1] += 3
            await ctx.send(embed=discord.Embed(description=''
                        '%s has fed their %s a :fish: and restored :burrito: 3'%(
                            ctx.message.author,pets[ctx.message.author.id][6])))
          else:
            await ctx.send('You don\'t have that type of food')
        if args[0][0].lower() == 't':
          if int(saved_data[ctx.message.author.id][9][7][1])>0:
            saved_data[ctx.message.author.id][9][7][1] -= 1
            pets[ctx.message.author.id][7] = time.time() + (fc(pets[ctx.message.author.id][10][5])*60)
            pets[ctx.message.author.id][1] += 6
            await ctx.send(embed=discord.Embed(description=''
                        '%s has fed their %s a :tropical_fish: and restored :burrito: 6'%(
                            ctx.message.author,pets[ctx.message.author.id][6])))
          else:
            await ctx.send('You don\'t have that type of food')
        if args[0].lower().startswith('do'):
          if int(saved_data[ctx.message.author.id][9][7][2])>0:
            saved_data[ctx.message.author.id][9][7][2] -= 1
            pets[ctx.message.author.id][7] = time.time() + (fc(pets[ctx.message.author.id][10][5])*60)
            pets[ctx.message.author.id][1] += 10
            await ctx.send(embed=discord.Embed(description=''
                        '%s has fed their %s a :dolphin: and restored :burrito: 10'%(
                            ctx.message.author,pets[ctx.message.author.id][6])))
          else:
            await ctx.send('You don\'t have that type of food')
        if args[0][0].lower() == 's':
          if int(saved_data[ctx.message.author.id][9][7][3])>0:
            pets[ctx.message.author.id][1] += 20
            saved_data[ctx.message.author.id][9][7][3] -= 1
            pets[ctx.message.author.id][7] = time.time() + (fc(pets[ctx.message.author.id][10][5])*60)
            await ctx.send(embed=discord.Embed(description=''
                        '%s has fed their %s a :shark: and restored :burrito: 20'%(
                            ctx.message.author,pets[ctx.message.author.id][6])))
          else:
            await ctx.send('You don\'t have that type of food')
        if args[0][0].lower() == 'w':
          if int(pets[ctx.message.author.id][10][15])>0:
            pets[ctx.message.author.id][2] += 12
            pets[ctx.message.author.id][7] = time.time() + (fc(pets[ctx.message.author.id][10][5])*60)
            pets[ctx.message.author.id][10][15] -= 1
            await ctx.send(embed=discord.Embed(description=''
                        '%s has fed their %s a :cup_with'
                                               '_straw: and restored :droplet: 12'%(
                            ctx.message.author,pets[ctx.message.author.id][6])))
          else:
            await ctx.send('You don\'t have that type of food')
        if args[0][0].lower() == 'c':
          if int(pets[ctx.message.author.id][10][16])>0:
            pets[ctx.message.author.id][2] += 12
            pets[ctx.message.author.id][3] += 20
            pets[ctx.message.author.id][7] = time.time() + (fc(pets[ctx.message.author.id][10][5])*60)
            pets[ctx.message.author.id][10][16] -= 1
            pets[ctx.message.author.id][10][19] = time.time() + 3603
            await ctx.send(embed=discord.Embed(description=''
                        '%s has fed their %s a :coffee'
                                               ': and restored :droplet: 12'
                        ' and :battery: 20'%(
                            ctx.message.author,pets[ctx.message.author.id][6])))
          else:
            await ctx.send('You don\'t have that type of food')
        if args[0].lower().startswith('da') or args[0].lower().startswith('po'):
          if int(e1s[ctx.message.author.id][0])>0:
            e1s[ctx.message.author.id][0] -= 1
            restoredenergy1 = random.randint(0,37)
            restoredenergy2 = random.randint(0,37)
            restoredenergy = 25 + restoredenergy1 + restoredenergy2
            pets[ctx.message.author.id][3] += restoredenergy
            pets[ctx.message.author.id][4] += 50
            pets[ctx.message.author.id][7] = time.time() + (fc(pets[ctx.message.author.id][10][5])*20)
            await ctx.send(embed=discord.Embed(description=''
                        '%s has fed their %s a <:potionofdarkne'
                                               f'ss:971863500429328445>, and restored :battery: {restoredenergy:,} and <:health:945703411901419520> 50!'%(
                            ctx.message.author,pets[ctx.message.author.id][6])))
          else:
            await ctx.send('You don\'t have that type of food!')
        if args[0].lower().startswith('mil'):
          if int(e1s[ctx.message.author.id][1])>0:
            e1s[ctx.message.author.id][1] -= 1
            healthrestored = random.randint(40, 160)
            pets[ctx.message.author.id][4] += healthrestored
            pets[ctx.message.author.id][7] = time.time() + (fc(pets[ctx.message.author.id][10][5])*40)
            await ctx.send(embed=discord.Embed(description=''
                        f'%s has fed their %s a :milk:, and restored <:health:945703411901419520> {healthrestored:,}!'%(
                            ctx.message.author,pets[ctx.message.author.id][6])))
            if random.randint(10, 1000) <= 90:
                pets[ctx.message.author.id][10][0] += 1
                await ctx.send(embed=discord.Embed(color=16777215,description='Wow! %s\'s %s has gained :fish_cake: 1!'%(ctx.message.author, pets[ctx.message.author.id][6])))
          else:
            await ctx.send('You don\'t have that type of food!')
      else:
            await ctx.send('The different types of food are `fish`, `tropical`,'
                       ' `dolphin`, `shark`, `water`, `dark`, `milk`, and `coffee`')
     else:
         await ctx.send('Your %s is ignoring you. It might be best to'
                        ' wait another %i minutes before approaching i'
                        't with food again' % (
                            pets[ctx.message.author.id][6],
                            (pets[ctx.message.author.id][7
                                ] - time.time())//60))
         # If your pet is ignoring you #
    else:
        await ctx.send( 'You do not have a pet cat; '
                 '`f!adopt` to adopt one for :star2:'
                ' 16,000')


@bot.command(aliases=['pshop'])
async def petshop(ctx, *args):
    await ctx.send(embed=discord.Embed(title='Pet Shop',
                description='''`f!pbuy <id> <amount>` to buy from here
[1] :fish: Fish - Restores :burrito: 3 - Price: :star2: 800
[2] :tropical_fish: Tropical Fish - Restores :burrito: 6 - Price: :star2: 2,000
[3] :dolphin: Dolphin - Restores :burrito: 10 - Price: :star2: 8,000
[4] :shark: Shark - Restores :burrito: 20 - Price: :star2: 12,000
[5] '''+chr(0x1f964)+''' Water - Restores :droplet: 5 - Price: :star2: 1,150
[6] :coffee: Coffee - Restores :droplet: 12 and :battery: 20 - Price: :star2: 2,900
[7] <:potionofdarkness:971863500429328445> Potion of Darkness - Restores :battery: 25-100 - Price: :star2: 25,000
[8] :milk: Milk - Restores <:health:945703411901419520> 40 - 160, gives a pet credit rarely - Price: :star2: 45,000'''))
@bot.command(aliases=['petbuy'])
async def pbuy(ctx, *args):
    global pets, saved_data, e1s
    if pets[ctx.message.author.id][0] != 0:
        if len(args) == 0:
            await ctx.send('You must specify an ID under the format of `f!pbuy <id> <amount>`')
        elif len(args) == 1:
            if int(args[0]) == 1:
                if saved_data[ctx.message.author.id][0] >= 800:
                    saved_data[ctx.message.author.id][0] -= 800
                    saved_data[ctx.message.author.id][9][7][0] += 1
                    await ctx.send(embed=discord.Embed(description = ''
                            '%s has successfully purchased :fish: 1' % ctx.message.author))
                else:
                    await ctx.send('You don\'t have enough to buy :fish: 1')
            elif int(args[0]) == 2:
                if saved_data[ctx.message.author.id][0] >= 2000:
                    saved_data[ctx.message.author.id][0] -= 2000
                    saved_data[ctx.message.author.id][9][7][1] += 1
                    await ctx.send(embed=discord.Embed(description = ''
                            '%s has successfully purchased :tropical_fish: 1' % ctx.message.author))
                else:
                    await ctx.send('You don\'t have enough to buy :tropical_fish: 1')
            elif int(args[0]) == 3:
                if saved_data[ctx.message.author.id][0] >= 8000:
                    saved_data[ctx.message.author.id][0] -= 8000
                    saved_data[ctx.message.author.id][9][7][2] += 1
                    await ctx.send(embed=discord.Embed(description = ''
                            '%s has successfully purchased :dolphin: 1' % ctx.message.author))
                else:
                    await ctx.send('You don\'t have enough to buy :dolphin: 1')
            elif int(args[0]) == 4:
                if saved_data[ctx.message.author.id][0] >= 12000:
                    saved_data[ctx.message.author.id][0] -= 12000
                    saved_data[ctx.message.author.id][9][7][3] += 1
                    await ctx.send(embed=discord.Embed(description = ''
                            '%s has successfully purchased :shark: 1' % ctx.message.author))
                else:
                    await ctx.send('You don\'t have enough to buy :shark: 1')
            elif int(args[0]) == 5:
                if saved_data[ctx.message.author.id][0] >= 1150:
                    saved_data[ctx.message.author.id][0] -= 1150
                    pets[ctx.message.author.id][10][15] += 1
                    await ctx.send(embed=discord.Embed(description = (''
                            '%s has successfully purchased '+chr(0x1f964)+' 1') % ctx.message.author))
                else:
                    await ctx.send('You don\'t have enough to buy '+chr(0x1f964)+' 1')
            elif int(args[0]) == 6:
                if saved_data[ctx.message.author.id][0] >= 2900:
                    saved_data[ctx.message.author.id][0] -= 2900
                    pets[ctx.message.author.id][10][16] += 1
                    await ctx.send(embed=discord.Embed(description = ''
                            '%s has successfully purchased :coffee: 1' % ctx.message.author))
                else:
                    await ctx.send('You don\'t have enough to buy :coffee: 1')
            elif int(args[0]) == 7:
                if saved_data[ctx.message.author.id][0] >= 25000:
                    saved_data[ctx.message.author.id][0] -= 25000
                    e1s[ctx.message.author.id][0] += 1
                    await ctx.send(embed=discord.Embed(description = ''
                            '%s has successfully purchased <:potionofdarkness:971863500429328445> 1' % ctx.message.author))
                else:
                    await ctx.send('You don\'t have enough to buy <:potionofdarkness:971863500429328445> 1')
            elif int(args[0]) == 8:
                if saved_data[ctx.message.author.id][0] >= 45000:
                    saved_data[ctx.message.author.id][0] -= 45000
                    e1s[ctx.message.author.id][1] += 1
                    await ctx.send(embed=discord.Embed(description = ''
                            '%s has successfully purchased :milk: 1' % ctx.message.author))
                else:
                    await ctx.send('You don\'t have enough to buy :milk: 1')

        else:
         if int(float(args[1])) >= 0:
            if int(args[0]) == 1:
                if saved_data[ctx.message.author.id][0] >= 800 * int(float(args[1])):
                    saved_data[ctx.message.author.id][0] -= 800 * int(float(args[1]))
                    saved_data[ctx.message.author.id][9][7][0] += int(float(args[1]))
                    await ctx.send(embed=discord.Embed(description = ''
                            '%s has successfully purchased :fish: %s' % (ctx.message.author, int(float(args[1])))))
                else:
                    await ctx.send('You don\'t have enough to buy :fish: %i'%int(float(args[1])))
            elif int(args[0]) == 2:
                if saved_data[ctx.message.author.id][0] >= 2000* int(float(args[1])):
                    saved_data[ctx.message.author.id][0] -= 2000* int(float(args[1]))
                    saved_data[ctx.message.author.id][9][7][1] += int(float(args[1]))
                    await ctx.send(embed=discord.Embed(description = ''
                            '%s has successfully purchased :tropical_fish: %i' % (ctx.message.author, int(float(args[1])))))
                else:
                    await ctx.send('You don\'t have enough to buy :tropical_fish: %i'%int(float(args[1])))
            elif int(args[0]) == 3:
                if saved_data[ctx.message.author.id][0] >= 8000  * int(float(args[1])):
                    saved_data[ctx.message.author.id][0] -= 8000 * int(float(args[1]))
                    saved_data[ctx.message.author.id][9][7][2] +=  int(float(args[1]))
                    await ctx.send(embed=discord.Embed(description = ''
                            '%s has successfully purchased :dolphin: %i' % (ctx.message.author, int(float(args[1])))))
                else:
                    await ctx.send('You don\'t have enough to buy :dolphin: %i'%int(float(args[1])))
            elif int(args[0]) == 4:
                if saved_data[ctx.message.author.id][0] >= 12000 * int(float(args[1])):
                    saved_data[ctx.message.author.id][0] -= 12000 * int(float(args[1]))
                    saved_data[ctx.message.author.id][9][7][3] += int(float(args[1]))
                    await ctx.send(embed=discord.Embed(description = ''
                            '%s has successfully purchased :shark: %i' % (ctx.message.author, int(float(args[1])))))
                else:
                    await ctx.send('You don\'t have enough to buy :shark: %i'%int(float(args[1])))
            elif int(args[0]) == 5:
                if saved_data[ctx.message.author.id][0] >= 1150 * int(float(args[1])):
                    saved_data[ctx.message.author.id][0] -= 1150 * int(float(args[1]))
                    pets[ctx.message.author.id][10][15] += int(float(args[1]))
                    await ctx.send(embed=discord.Embed(description = (
                            ('%s has successfully purchased '+chr(0x1f964)+' %i') % (ctx.message.author, int(float(args[1]))))))
                else:
                    await ctx.send(('You don\'t have enough to buy '+chr(0x1f964)+' %i')%int(float(args[1])))
            elif int(args[0]) == 6:
                if saved_data[ctx.message.author.id][0] >= 2900 * int(float(args[1])):
                    saved_data[ctx.message.author.id][0] -= 2900 * int(float(args[1]))
                    pets[ctx.message.author.id][10][16] += int(float(args[1]))
                    await ctx.send(embed=discord.Embed(description = ''
                            '%s has successfully purchased :coffee: %i' % (ctx.message.author, int(float(args[1])))))
                else:
                    await ctx.send('You don\'t have enough to buy :coffee: %i'%int(float(args[1])))
            elif int(args[0]) == 7:
                 if saved_data[ctx.message.author.id][0] >= 25000 * int(float(args[1])):
                    saved_data[ctx.message.author.id][0] -= 25000 * int(float(args[1]))
                    e1s[ctx.message.author.id][0] += int(float(args[1]))
                    await ctx.send(embed=discord.Embed(description = ''
                            '%s has successfully purchased <:potionofdarkness:971863500429328445> %i' % (ctx.message.author, int(float(args[1])))))
                 else:
                    await ctx.send('You don\'t have enough to buy <:potionofdarkness:971863500429328445> %i'%int(float(args[1])))
            elif int(args[0]) == 8:
                 if saved_data[ctx.message.author.id][0] >= 45000 * int(float(args[1])):
                    saved_data[ctx.message.author.id][0] -= 45000 * int(float(args[1]))
                    e1s[ctx.message.author.id][1] += int(float(args[1]))
                    await ctx.send(embed=discord.Embed(description = ''
                            '%s has successfully purchased :milk: %i' % (ctx.message.author, int(float(args[1])))))
                 else:
                    await ctx.send('You don\'t have enough to buy :milk: %i'%int(float(args[1])))
         else:
             await ctx.send('You must enter a positive number!')
    else:
        await ctx.send( 'You do not have a pet cat; '
                 '`f!adopt` to adopt one for :star2:'
                ' 16,000')
###############################################################
def startweaponcheck(user):
    if user not in weapons:
        weapons[user] = [0]*17
def shotconsume(x):
    if x in [0,1,2,3,4,5]:
        return {0:69,1:8,2:6,3:4,4:2,5:1,6:0}[x]
    else:
        return 0
@bot.command()
async def pub(ctx, *args):
    startweaponcheck(ctx.message.author.id)
    await ctx.send('',embed=discord.Embed(title='Pub',description=''
                '`f!purchase <id> [amount]` to buy from here\n[1] :beer: Beer - '
                'Order a golden cup of beer - Price: :star2: 100\n'
                '[2] :star2: Nine credits - Don\'t like your beer? You can '
                'sell it back to us for a 90\x25 refund - Price: :beer: 1').add_field(name='Weapons',value=''
                '[3]{}:archery: Crossbow - Steals the square root of your balance away'
                ' from the target\'s balance - Price: :beer: 400\n[4]{}:gun: Pisto'
                'l - Steals 1-5\x25 - Price: :beer: 900'.format({0:' ',1:' :white_check_mark: **BOUGHT** - '}[weapons[ctx.message.author.id][0]],
                                                       {0:' ',1:' :white_check_mark: **BOUGHT** - '}[weapons[ctx.message.author.id][1]])).add_field(name='Ammunition',value=''
                '[5] <:arrow:951731936886415400> Arrow - Ammunition for crossbows - Pr'
                'ice: :beer: 80\n[6] :smoking: Pistol Bullet - Ammunition for pisto'
                'ls - Price: :beer: 180'))
@bot.command()
async def purchase(ctx, *args):
    i = ctx.message.author.id
    startcheck(i)
    startweaponcheck(i)
    if len(args) == 0:
        await ctx.send('You must specify an ID under the format of `f!purchase <id> <amount>`')
    elif len(args) >= 1:
        cnf = args + (1,)
        if int(float(cnf[0])) in [1,2,3,4,5,6]:
         if int(float(cnf[1])) >= 1:
            if int(float(cnf[0])) == 1:
                 if (saved_data[i][0]*100) >= (int(float(cnf[1]))*100):
                     saved_data[i][0] -= (int(float(cnf[1]))*100)
                     weapons[i][9] += int(float(cnf[1]))
                     await ctx.send(embed=discord.Embed(description=(''
                        f'%s has successfully ordered :beer: {int(float(cnf[1])):,}! Enjoy :3' % ctx.message.author)))
                 else:
                     await ctx.send('You don\'t have enough to'
                                    ' buy :beer: 'f'{int(float(cnf[0o1])):,}')
            elif int(float(cnf[0])) == 2:
                if (weapons[i][9]) >= (int(float(cnf[1]))):
                     saved_data[i][0] += (int(float(cnf[1]))*90)
                     weapons[i][9] -= int(float(cnf[1]))
                     await ctx.send(embed=discord.Embed(description=(''
                        f'%s has successfully sold :beer: {int(float(cnf[1])):,}!' % ctx.message.author)))
                else:
                     await ctx.send('You don\'t have '
                                    ':beer: 'f'{int(float(cnf[0o1])):,}!')
            elif int(float(cnf[0])) == 3:
                if not(weapons[i][0]):
                     if weapons[i][9] >= 400:
                         weapons[i][9] -= 400
                         weapons[i][0] = True
                         await ctx.send(embed=discord.Embed(description=(''
                        f'%s has successfully purchased a :archery:!' % ctx.message.author)))
                     else:
                         await ctx.send('You don\'t have enough'
                                        ' beer to purchase a :archery:!')
                else:
                     await ctx.send('You already have a :archery:!')
            elif int(float(cnf[0])) == 4:
                if not(weapons[i][1]):
                     if weapons[i][9] >= 900:
                         weapons[i][9] -= 900
                         weapons[i][1] = True
                         await ctx.send(embed=discord.Embed(description=(''
                        f'%s has successfully purchased a :gun:!' % ctx.message.author)))
                     else:
                         await ctx.send('You don\'t have enough'
                                        ' beer to purchase a :gun:!')
                else:
                     await ctx.send('You already have a :gun:!')
            elif int(float(cnf[0])) == 5:
                if (weapons[i][9]) >= (int(float(cnf[1]))*80):
                     weapons[i][5] += (int(float(cnf[1])))
                     weapons[i][9] -= int(float(cnf[1]))*80
                     await ctx.send(embed=discord.Embed(description=(''
                        f'%s has successfully purchased <:arrow:951731936886415400> {int(float(cnf[1])):,}' % ctx.message.author)))
                else:
                     await ctx.send(f'You can\'t afford <:arrow:951731936886415400> {int(float(cnf[1])):,}')
            elif int(float(cnf[0])) == 6:
                if (weapons[i][9]) >= (int(float(cnf[1]))*180):
                     weapons[i][6] += (int(float(cnf[1])))
                     weapons[i][9] -= int(float(cnf[1]))*180
                     await ctx.send(embed=discord.Embed(description=(''
                        f'%s has successfully purchased :smoking: {int(float(cnf[1])):,}' % ctx.message.author)))
                else:
                     await ctx.send(f'You can\'t afford :smoking: {int(float(cnf[1])):,}')
            else:
                await ctx.send('Unknown Item ID "%s"; pick a number from 1-6' % cnf[0])
         else:
             await ctx.send('You must provide a positive number')
@bot.command()
async def select(ctx, *args):
    global weapons
    if len(args) == 0:
        await ctx.send('The supported types of weapons are `crossbow`, and `pistol`.')
    elif len(args) >= 1:
        if len(args[0]) == 0:
            await ctx.send('The supported types of weapons are `crossbow`, and `pistol`.')
        elif args[0].startswith('cr') or args[0].startswith('b') or args[0].startswith('arc'):
            if weapons[ctx.message.author.id][0]:
                weapons[ctx.message.author.id][16] = b'crossbow'
                await ctx.send(embed=discord.Embed(description='%s has switched to their :archery:'%ctx.message.author))
            else:
                await ctx.send('You don\'t have a crossbow!')
        elif args[0].startswith('pi') or args[0].startswith('g'):
            if weapons[ctx.message.author.id][1]:
                weapons[ctx.message.author.id][16] = b'pistol'
                await ctx.send(embed=discord.Embed(description='%s has switched to their :gun:'%ctx.message.author))
            else:
                await ctx.send('You don\'t have a pistol!')
        else:
            await ctx.send('The supported types of weapons are `crossbow`, and `pistol`.')
@bot.command()
async def shoot(ctx, *args):
    global weapons, pets, saved_data
    startweaponcheck(ctx.message.author.id)
    startcheck(ctx.message.author.id)
    id = None
    name = None
    if len(args)==0:
        id = None
        name = None
    elif len(args) >= 1:
     if len(ctx.message.mentions) > 0:
        try:
            f_user = await bot.fetch_user(int(ctx.message.mentions[0].id))
            name = f_user
            id = int(ctx.message.mentions[0].id)
            del f_user
        except:
            name = None
            id = None
     else:
         try:
             g_user = await bot.fetch_user(int(args[0]))
         except:
             class fake_user:
                 def __init__(self):
                     self.id = None
                     self.name = None
                 id = None
                 name = None
             g_user = fake_user()
         name = g_user
         id = g_user.id
    startcheck(id)
    startpetcheck(id)
    print(id)
    if weapons[ctx.message.author.id][16] in [b'crossbow', b'pistol']:
       if id == None:
           await ctx.send(embed=discord.Embed(color=13995405,title='Your Projectile Missed!',
                                        description='You need to mention your target for'
                                              ' `f!shoot`!'))
       else:
           if weapons[ctx.message.author.id][16] == b'crossbow':
               if weapons[ctx.message.author.id][5] >= 1:
                   delta_bal = saved_data[ctx.message.author.id][0]
                   shoot = 0
                   if weapons[ctx.message.author.id][10] <= time.time():
                       pass
                   else:
                       em=discord.Embed(color=0xe8c14d,
                        title='Cooldown!',description='You already shot a user with your :archery: in the last'
                        ' 3 hours! Try again <t:%i:R>'%weapons[ctx.message.author.id][10])
                       em.set_thumbnail(url='https://i.ibb.co/6Fznr3b/cooldown.png')
                       await ctx.send(embed=em)
                       
                       return
                   if pets[id][10][20] and(pets[id][4]>=200) and(pets[id][3] > atc(pets[id][10][4])):
                       r=random.randint(1,100)
                       if agt(pets[id][10][2]) < r:
                           shoot=0
                           if r > 0 and r <= 30:
                               pets[id][3] -= shotconsume(pets[id][10][4])
                               await ctx.send(embed=discord.Embed(color=13995405,title='Arrow Blocked!',
                                        description='Your target\'s pet has caught the arrow spending :battery: %i!'%shotconsume(pets[id][10][4])))
                           if r > 30 and r <= 60:
                               weapons[ctx.message.author.id][5]-=1
                               pets[id][3] -= shotconsume(pets[id][10][4])
                               await ctx.send(embed=discord.Embed(color=13995405,title='Arrow Destroyed!',
                                        description='Your target\'s pet has destroyed the arrow spending :battery: %i!'%shotconsume(pets[id][10][4])))
                           if r > 60 and r <= 100:
                               pets[id][4] -= 800//(pets[id][10][4]+0b100)
                               await ctx.send(embed=discord.Embed(color=13995405,title='Arrow Blocked!',
                                    description='Your target\'s pet has been hit by the arrow and lost <:health:945703411901419520> %i!'%(800//(pets[id][10][4]+0b100))))
                       else:
                           shoot = 1
                           await ctx.send(embed=discord.Embed(color=13995405,title='Pet isn\'t Agile Enough!',
                                        description='Your target\'s pet wasn\'t agile enough to block the arrow!'))
                           
                   else:
                       shoot = 1
                   if shoot != 0:
                       stolen = floor(min(delta_bal, sqrt(saved_data[id][0])))
                       saved_data[id][0] -= stolen
                       saved_data[ctx.message.author.id][0] += stolen
                       weapons[ctx.message.author.id][10]=time.time()+10000
                       weapons[ctx.message.author.id][5] -= 1
                       await ctx.send(embed=discord.Embed(color=0x117d2f,title='User Shot!',
                            description='You\'ve shot %s with your :archery: and stolen :star2: %s!'%
                                (name, f'{stolen:,}')))
                       await name.send(embed=discord.Embed(color=0xe84d4d,title='You\'ve been shot!',
                            description='You\'ve been shot by %s with their :archery: and lost :star2: %s!'%
                                (ctx.message.author, f'{stolen:,}')))
                                                          
                   else:
                       pass
               else:
                   await ctx.send(embed=discord.Embed(color=13995405,title='Missing Ammunition!',
                                        description='You forgot to buy an <:arrow:951731936886415400> Arrow'
                                                    ' to shoot with a :archery:!'))
           elif weapons[ctx.message.author.id][16] == b'pistol':
               if weapons[ctx.message.author.id][6] >= 1:
                   delta_bal = saved_data[ctx.message.author.id][0]
                   shoot = 0
                   if weapons[ctx.message.author.id][11] <= time.time():
                       pass
                   else:
                       em=embed=discord.Embed(color=0xe8c14d,
                        title='Cooldown!',description='You already shot a user with your :gun: in the last'
                        ' 4 hours! Try again <t:%i:R>'%weapons[ctx.message.author.id][11])
                       em.set_thumbnail(url='https://i.ibb.co/6Fznr3b/cooldown.png')
                       await ctx.send(embed=em)
                       return
                   if pets[id][10][20] and(pets[id][4]>=200) and(pets[id][3] > atc(pets[id][10][4])):
                       r=random.randint(1,100)
                       if agt(pets[id][10][2]) < r:
                           shoot=0
                           if r > 0 and r <= 30:
                               pets[id][3] -= shotconsume(pets[id][10][4])
                               await ctx.send(embed=discord.Embed(color=13995405,title='Bullet Blocked!',
                                        description='Your target\'s pet has caught the bullet spending :battery: %i!'%shotconsume(pets[id][10][4])))
                           if r > 30 and r <= 60:
                               weapons[ctx.message.author.id][6]-=1
                               pets[id][3] -= shotconsume(pets[id][10][4])
                               await ctx.send(embed=discord.Embed(color=13995405,title='Bullet Destroyed!',
                                        description='Your target\'s pet has destroyed the bullet spending :battery: %i!'%shotconsume(pets[id][10][4])))
                           if r > 60 and r <= 100:
                               pets[id][4] -= 900//(pets[id][10][4]+0b100)
                               await ctx.send(embed=discord.Embed(color=13995405,title='Bullet Blocked!',
                                    description='Your target\'s pet has been harmed by the bullet and lost <:health:945703411901419520> %i!'%(900//(pets[id][10][4]+0b100))))
                       else:
                           shoot = 1
                           await ctx.send(embed=discord.Embed(color=13995405,title='Pet isn\'t Agile Enough!',
                                        description='Your target\'s pet wasn\'t agile enough to block the bullet!'))
                           
                   else:
                       shoot = 1
                   if shoot != 0:
                       a = saved_data[id][0]//100
                       b = random.randint(1,5)
                       stolen = a * b
                       saved_data[ctx.message.author.id][0]+=stolen
                       saved_data[id][0]-=stolen
                       weapons[ctx.message.author.id][11] = time.time()+14000
                       weapons[ctx.message.author.id][6] -= 1
                       await ctx.send(embed=discord.Embed(color=0x117d2f,title='User Shot!',
                            description='You\'ve shot %s with your :gun: and stolen :star2: %s!'%
                                (name, f'{stolen:,}')))
                       await name.send(embed=discord.Embed(color=0xe84d4d,title='You\'ve been shot!',
                            description='You\'ve been shot by %s with their :gun: and lost :star2: %s!'%
                                (ctx.message.author, f'{stolen:,}')))
                                                          
                   else:
                       pass
               else:
                   await ctx.send(embed=discord.Embed(color=13995405,title='Missing Ammunition!',
                                        description='You forgot to buy :smoking: Bullet'
                                                    ' to shoot with a :archery:!')) 
           
               
    else:
        await ctx.send(':x: Select a weapon using `f!select`.')
@bot.command()
async def ammo(ctx,  *args):
    startweaponcheck(ctx.message.author.id)
    id = ctx.message.author.id
    name = ctx.message.author
    if len(args)==0:
        id = ctx.message.author.id
        name = ctx.message.author
    elif len(args) >= 1:
     if len(ctx.message.mentions) > 0:
        try:
            f_user = await bot.fetch_user(int(args[0]))
            name = f_user
            id = int(args[0])
            del f_user
        except:
            name = ctx.message.author
            id = ctx.message.author.id
     else:
         try:
             g_user = await bot.fetch_user(int(args[0]))
         except:
             g_user = await bot.fetch_user(ctx.message.author.id)
         name = g_user
         id = g_user.id
    startweaponcheck(id)
    await ctx.send(embed=discord.Embed(title='%s\'s Ammunition' % (name),
        description='`f!shoot <@user>` to use up your ammo\n<:arrow:951731936886415400> Arrow | %s'
                    '\n:smoking: Pistol Bullet | %s' %(weapons[id][5],weapons[id][6])))
@bot.command()
async def beer(ctx,  *args):
    startweaponcheck(ctx.message.author.id)
    id = ctx.message.author.id
    name = ctx.message.author
    if len(args)==0:
        id = ctx.message.author.id
        name = ctx.message.author
    elif len(args) >= 1:
     if len(ctx.message.mentions) == 0:
        try:
            f_user = await bot.fetch_user(int(args[0]))
            name = f_user
            id = int(args[0])
            del f_user
        except:
            name = ctx.message.author
            id = ctx.message.author.id
     else:
         try:
             g_user = await bot.fetch_user(ctx.message.mentions[0].id)
         except:
             g_user = await bot.fetch_user(ctx.message.author.id)
         name = g_user
         id = g_user.id
    startweaponcheck(id)
    await ctx.send(embed=discord.Embed(
        description=f'%s has :beer: {weapons[id][9]:,}'%name))    
@bot.command(aliases=['ui'])
async def userinfo(ctx,  *args):
    startweaponcheck(ctx.message.author.id)
    id = ctx.message.author.id
    name = ctx.message.author
    if len(args)==0:
        id = ctx.message.author.id
        name = ctx.message.author
    elif len(args) >= 1:
     if len(ctx.message.mentions) > 0:
        try:
            f_user = await bot.fetch_user(ctx.message.mentions[0].id)
            name = f_user
            id = int(ctx.message.mentions[0].id)
            del f_user
        except:
            name = ctx.message.author
            id = ctx.message.author.id
     else:
         try:
             g_user = await bot.fetch_user(int(args[0]))
         except:
             g_user = await bot.fetch_user(ctx.message.author.id)
         name = g_user
         id = g_user.id
    em=discord.Embed(title='%s - %s' % (name, id))
    em.set_thumbnail(url=name.avatar_url)
    em.add_field(name='Created At', value='<t:%i:d> (<t:%i:R>)'%((name.created_at.timestamp(),)*2))
    em.add_field(name='Avatar URL', value='[Click here](%s)'%name.avatar_url, inline=0)
    await ctx.send(embed=em)
    print(name.avatar_url)
@bot.command(aliases=['dr'])
async def drink(ctx, *args):
    global weapons,gens,saved_data,advs,pets,bms
    startweaponcheck(ctx.message.author.id)
    startcheck(ctx.message.author.id)
    startpetcheck(ctx.message.author.id)
    startgencheck(ctx.message.author.id)
    startadvcheck(ctx.message.author.id)
    startbmcheck(ctx.message.author.id)
    if weapons[ctx.message.author.id][15] <= time.time():
        if weapons[ctx.message.author.id][9] >= 1:
            saved_data[ctx.message.author.id][1]=0
            saved_data[ctx.message.author.id][3][1]=0
            saved_data[ctx.message.author.id][8]=0
            saved_data[ctx.message.author.id][9][6]=0
            weapons[ctx.message.author.id][10]=0
            weapons[ctx.message.author.id][11]=0
            weapons[ctx.message.author.id][15] = time.time()+1800
            gens[ctx.message.author.id][6]=0
            bms[ctx.message.author.id][3]=0
            await ctx.send(embed=discord.Embed(color=0x32e60e,description=''
                 'You drank a :beer: beer and lost some cooldowns!'))
        else:
            await ctx.send(embed=discord.Embed(color=0xe60e0e,description=''
                 'You don\'t have any beers to drink! `f!pub`'))
    else:
        await ctx.send(embed=discord.Embed(title='Cooldown!',color=0xe6960e,description=''
        'Your head is still pounding from your last drink\'s hangover! You can drink '
                'beer again <t:%i:R>'%weapons[ctx.message.author.id][15]))
##### NEW COMMANDS: PUB, DRINK, BEER, AMMO, SHOOT, SELECT #####
###############################################################
@bot.command()
async def help_ctx(ctx):
    await ctx.message.delete()
    print(dir(ctx))
    print(dir(ctx.message))
    print(dir(ctx.message.author))
def startgencheck(user_id):
       global gens
       if user_id not in gens:
            gens[user_id] = [0, 0, 0, 0, 0, 0, 1]
       else:
           return
@bot.command()
async def buy_shares(ctx, *args):
    global saved_data
    if len(args) == 0:
        if saved_data[ctx.message.author.id][0] >= 5612:
            saved_data[ctx.message.author.id][0] -= 5612
            saved_data[ctx.message.author.id][9][8] += 1
            await ctx.send(embed=discord.Embed(description='%s has bought 1 shares for :star2: 5,612.'%ctx.message.author))
        else:
            await ctx.send('You don\'t have enough credits to buy 1 shares!')
    elif len(args) >= 1:
      if int(float(args[0])) >= 0:
        if saved_data[ctx.message.author.id][0] >= 5612*int(float(args[0])):
            saved_data[ctx.message.author.id][0] -= (5612*int(float(args[0])))
            saved_data[ctx.message.author.id][9][8] += int(float(args[0]))
            await ctx.send(embed=discord.Embed(description=f'%s has bought {int(float(args[0])):,} shares for :star2: {5612*int(float(args[0])):,}.'%ctx.message.author))
        else:
            await ctx.send(f'You don\'t have enough credits to buy {int(float(args[0])):,} shares!')
      else:
          await ctx.send('You must provide a positive number.')
@bot.command()
async def sell_shares(ctx, *args):
    global saved_data
    if len(args) == 0:
        if saved_data[ctx.message.author.id][9][8] >= 1:
            chanced = random.randint(1,1000)
            priced = 5612 if chanced < 96 else 5612
            if saved_data[ctx.message.author.id][9][3]:
                priced = priced
            else:
                priced = 5612
            saved_data[ctx.message.author.id][0] += priced
            saved_data[ctx.message.author.id][9][8] -= 1
            await ctx.send(embed=discord.Embed(description=f'%s has sold 1 shares for :star2: {priced}.'%ctx.message.author))
        else:
            await ctx.send('You don\'t have 1 shares!')
    elif len(args) >= 1:
      if int(float(args[0])) >= 0:
        if saved_data[ctx.message.author.id][9][8] >= int(float(args[0])):
            chanced = random.randint(1,1000)
            priced = 5612 if chanced > 900 else 5612
            if saved_data[ctx.message.author.id][9][3]:
                priced = priced
            else:
                priced = 5612
            saved_data[ctx.message.author.id][0] += priced*int(float(args[0]))
            saved_data[ctx.message.author.id][9][8] -= int(float(args[0]))
            await ctx.send(embed=discord.Embed(description=f'%s has sold {int(float(args[0])):,} shares for :star2: {priced*int(float(args[0])):,}.'%ctx.message.author))
        else:
            await ctx.send(f'You don\'t have {int(float(args[0])):,} shares!')
      else:
          await ctx.send('You must provide a positive number.')
@bot.command()
async def shares(ctx,*args):
    global saved_data
    startcheck(ctx.message.author.id)
    id = ctx.message.author.id
    name = ctx.message.author
    if len(args)==0:
        id = ctx.message.author.id
        name = ctx.message.author
    elif len(args) >= 1:
     if len(ctx.message.mentions) == 0:
        try:
            f_user = await bot.fetch_user(int(args[0]))
            name = f_user
            id = int(args[0])
            del f_user
        except:
            name = ctx.message.author
            id = ctx.message.author.id
     else:
         try:
             g_user = ctx.message.mentions[0]
         except:
             g_user = await bot.fetch_user(ctx.message.author.id)
         name = g_user
         id = g_user.id
    startcheck(id)
    em = discord.Embed(title=r'%s\'s Shares'%name, description='`f!buy_shares <amount>` to buy shares'
'\n`f!sell_shares <amount>` to sell shares', color=0x002389)
    em.add_field(name='Shares', value=f'<:share:964777716597538816> {saved_data[id][9][8]:,}', inline=0)
    em.add_field(name='Total Amount in Credits', value=f':star2: {saved_data[id][9][8]*5612:,}', inline=0)
    em.set_footer(text='TIP: Shares are worth 5,612 credits each!')
    await ctx.send(embed=em)
@bot.command(aliases=['gen','gener', 'generat'])
async def generator(ctx, *args):
    startgencheck(ctx.message.author.id)
    id = ctx.message.author.id
    name = ctx.message.author
    if len(args)==0:
        id = ctx.message.author.id
        name = ctx.message.author
    elif len(args) >= 1:
     if len(ctx.message.mentions) == 0:
        try:
            f_user = await bot.fetch_user(int(args[0]))
            name = f_user
            id = int(args[0])
            del f_user
        except:
            name = ctx.message.author
            id = ctx.message.author.id
     else:
         try:
             g_user = ctx.message.mentions[0]
         except:
             g_user = await bot.fetch_user(ctx.message.author.id)
         name = g_user
         id = g_user.id
    startgencheck(id)
    if gens[id][0] == 0 and id == ctx.message.author.id:
        await ctx.send('You don\'t have a generator; `f!build` to get one for :star2: 30,000')
    elif gens[id][0] == 0 and id != ctx.message.author.id:
        await ctx.send('This user doesn\'t even have a generator.')
    else:
        em = discord.Embed(title='{0}\'s <:gen:961289293001785394> Credit Generator'.format(name),
                           description='`f!dispense` to collect credits\n'
                           '`f!improve <stat> <amount>` to spend :rosette: on improving stats\n'
                           '`f!rollback <stat> <amount>` to lower stats and earn :rosette: back\n\n')
        em.add_field(name='Stats and Credits', value=f':rosette: Generator Credits - {gens[id][4]:,}\n:moneybag: Interest Boost - {gens[id][3]:,}'
                        f' (%.2fx multi)'%((gens[ctx.message.author.id][3]/100)+1)+f'\n:arrow_heading_up: Credit Boost - {gens[id][5]:,} _(+:star2: {(gens[id][5]*100):,})_')
        em.set_thumbnail(url='https://cdn.discordapp.com/emojis/961289293001785394.web'
                         'p?size=96&quality=lossless')
        await ctx.send(embed=em) #yee yee
@bot.command()
async def fund(ctx, *args):
  global saved_data, gens
  startgencheck(ctx.message.author.id)
  startcheck(ctx.message.author.id)
  if gens[ctx.message.author.id][0] == 1:
    if len(args) == 0:
        em = discord.Embed(title='Hmm...', description='I can\'t let you spend'
            ' your credits on funding your <:gen:961289293001785394> if you don\x27'
                't specify the amount of :star2: you\x27re spending!')
        em.set_thumbnail(url='https://i.ibb.co/HgGk7bn/mariono.png')
        await ctx.send(embed=em)
    elif len(args) >= 1:
        # 1/3 #
        if args[0].lower() != 'allmoney':
          try:
            fundamount = int(float(args[0]))
          except:
            fundamount = None
        else:
            fundamount=saved_data[ctx.message.author.id][0]
        if fundamount == None:
            em = discord.Embed(title='Invalid Amount!', description=''
            'I\x27m not letting you fund your generator if you specify an invalid amount!'
            ' Try specifying a valid number e.g. `5000`, `5k` or `5,000`', color=0xFF5700)
            em.set_thumbnail(url='https://i.ibb.co/HgGk7bn/mariono.png')
            await ctx.send(embed=em)
        elif fundamount != None:
            if saved_data[ctx.message.author.id][0] >= fundamount:
                if fundamount > 0:
                        em = em = discord.Embed(description='Funding...')
                        m = await ctx.send(embed=em)
                        em = discord.Embed(color=(0x990100 if fundamount < 2000 else 0x00a100),
                        title='Successful Fund!', description='You have successfully spent :star2: '
                        f'{fundamount:,} on funding your generator! You have gained :rosette:'
                        f' {(fundamount//1000):,}!')
                        if fundamount < 2000:
                            em.add_field(name=':warning: WARNING',value='You have spent too less and did not gain any :rosette:.'
                                ' Fund at least :star2: 2,000 to get at least one :rosette:.')
                        time.sleep(0.7)
                        saved_data[ctx.message.author.id][0]-=fundamount
                        gens[ctx.message.author.id][4]+=(fundamount//2000)
                        gens[ctx.message.author.id][1]+=(fundamount)
                        await m.edit(embed=em)
                        
                elif fundamount == 0:
                  em = discord.Embed(title='Invalid Amount!', description=''
                 'You must provide a positive number, but you provided 0! You can\'t fund 0!', color=0xFF5700)
                  em.set_thumbnail(url='https://i.ibb.co/HgGk7bn/mariono.png')
                  await ctx.send(embed=em)
                else:
                    em = discord.Embed(title='Invalid Amount!', description=''
                 'You must provide a positive number, but you provided a negative number!', color=0xFF5700)
                    em.set_thumbnail(url='https://i.ibb.co/HgGk7bn/mariono.png')
                    await ctx.send(embed=em)  
            else:
                em = discord.Embed(title='Not Enough Credits!', description=''
            'You don\'t have enough credits to fund! You only'
            f' have :star2: {saved_data[ctx.message.author.id][0]:,}.', color=0xFF1500)
                em.set_thumbnail(url='https://i.ibb.co/HgGk7bn/mariono.png')
                await ctx.send(embed=em)
  else:
      em = discord.Embed(title='You don\x27t even have a generator!',
                description='Get one generator by `f!build`')
      await ctx.send(embed=em)

@bot.command(aliases=['im'])
async def improve(ctx, *args):
    global gens
    startgencheck(ctx.message.author.id)
    if gens[ctx.message.author.id][0]:
      if len(args) == 0:
        await ctx.reply('The valid generator boosts are `interest`, and `credit`.')
      elif len(args) == 1:
        if args[0][0].lower() in 'ic':
            if gens[ctx.message.author.id][4] >= 1:
                if args[0][0].lower() == 'i':
                    gens[ctx.message.author.id][4] -= 1
                    gens[ctx.message.author.id][3] += 1
                    await ctx.reply('You have successfully improved your generator\'s interest boost by 1 points and lost :rosette: 1')
                elif args[0][0].lower() == 'c':
                    gens[ctx.message.author.id][4] -= 1
                    gens[ctx.message.author.id][5] += 1
                    await ctx.reply('You have successfully improved your generator\'s credit boost by 1 points and lost :rosette: 1')
            else:
                await ctx.reply('You don\'t have :rosette: 1 to spend on improving boosts')
        else:
            await ctx.reply('The valid generator boosts are `interest`, and `credit`.')
      elif len(args) >= 2:
        if args[0][0].lower() in 'ic':
          if int(float(args[1])) >= 0:
            if gens[ctx.message.author.id][4] >= int(float(args[1])):
                if args[0][0].lower() == 'i':
                    gens[ctx.message.author.id][4] -= int(float(args[1]))
                    gens[ctx.message.author.id][3] += int(float(args[1]))
                    await ctx.reply(f'You have successfully improved your generator\'s interest boost by {int(float(args[1])):,} points and lost :rosette: {int(float(args[1])):,}')
                elif args[0][0].lower() == 'c':
                    gens[ctx.message.author.id][4] -= int(float(args[1]))
                    gens[ctx.message.author.id][5] += int(float(args[1]))
                    await ctx.reply(f'You have successfully improved your generator\'s credit boost by {int(float(args[1])):,} points and lost :rosette: {int(float(args[1])):,}')
            else:
                await ctx.reply(f'You don\'t have :rosette: {int(float(args[1])):,} to spend on improving boosts')
          else:
              await ctx.reply(f'You must provide a positive number.')
        else:
            await ctx.reply('The valid generator boosts are `interest`, and `credit`.')
    else:
        await ctx.reply('You don\'t even have a generator???')
@bot.command(aliases=['rlb'])
async def rollback(ctx, *args):
    global gens
    startgencheck(ctx.message.author.id)
    if gens[ctx.message.author.id][0]:
      if len(args) == 0:
        await ctx.reply('The valid generator boosts are `interest`, and `credit`.')
      elif len(args) == 1:
        if args[0][0].lower() in 'ic':
            if args[0][0].lower() == 'i':
                if gens[ctx.message.author.id][3] >= 1:
                    gens[ctx.message.author.id][3] -= 1
                    gens[ctx.message.author.id][4] += 1
                    await ctx.reply('You\'ve rolled back your generator\'s interest boost by 1 points and received :rosette: 1!')
                else: await ctx.reply('Your generator\'s stats must have at least 0 points')
            elif args[0][0].lower() == 'c':
                if gens[ctx.message.author.id][5] >= 1:
                    gens[ctx.message.author.id][5] -= 1
                    gens[ctx.message.author.id][4] += 1
                    await ctx.reply('You\'ve rolled back your generator\'s credit boost by 1 points and received :rosette: 1!')
                else: await ctx.reply('Your generator\'s stats must have at least 0 points') 
        else:
            await ctx.reply('The valid generator boosts are `interest`, and `credit`.')
      elif len(args) >= 2:
        if args[0][0].lower() in 'ic':
          if int(float(args[1])) >= 0:
            if args[0][0].lower() == 'i':
                if gens[ctx.message.author.id][3] >= int(float(args[1])):
                    gens[ctx.message.author.id][3] -= int(float(args[1]))
                    gens[ctx.message.author.id][4] += int(float(args[1]))
                    await ctx.reply(f'You\'ve rolled back your generator\'s interest boost by {int(float(args[1])):,} points and received :rosette: {int(float(args[1])):,}!')
                else: await ctx.reply('Your generator\'s stats must have at least 0 points')
            elif args[0][0].lower() == 'c':
                if gens[ctx.message.author.id][5] >= int(float(args[1])):
                    gens[ctx.message.author.id][5] -= int(float(args[1]))
                    gens[ctx.message.author.id][4] += int(float(args[1]))
                    await ctx.reply(f'You\'ve rolled back your generator\'s credit boost by {int(float(args[1])):,} points and received :rosette: {int(float(args[1])):,}!')
                else: await ctx.reply('Your generator\'s stats must have at least 0 points')
          
          else: await ctx.reply('You must enter a positive number.')
        else:
            await ctx.reply('The valid generator boosts are `interest`, and `credit`.')
        
    else:
        await ctx.reply('You don\'t even have a generator???')
@bot.command()
async def dispense(ctx,*args):
    global saved_data, gens
    startcheck(ctx.message.author.id)
    startgencheck(ctx.message.author.id)
    if gens[ctx.message.author.id][0]:
        if gens[ctx.message.author.id][6] <= time.time():
            msg = await ctx.reply('Dispensing...', mention_author=False)
            credited = 200*gens[ctx.message.author.id][5]
            interested = int(gens[ctx.message.author.id][3] * (credited/100))
            if (interested + credited) <= 0:
                em = discord.Embed(title='Dispensed!', description=f'You didn\'t collect anything, sad. :cry:', color=0x930000)
            elif (interested + credited) >= 96000:
                em = discord.Embed(title='Dispensed!', description=f'You\'ve collected a total of :star2: {interested+credited:,}!', color=0x009324)
            else:
                em = discord.Embed(title='Dispensed!', description=f'You\'ve collected a total of :star2: {interested+credited:,}!', color=0x939301)
            em.add_field(name=':chart_with_upwards_trend: Interest Credits Collected',value=(''
            f':star2: {interested:,} _(%.2fx multi)')%((gens[ctx.message.author.id][3]/100)+1)+'_', inline=1)
            em.add_field(name=':credit_card: Credit Card Credits Collected',value=''
            f':star2: {credited:,}', inline=1)
            if (interested+credited) <= 0:
                em.set_footer(text='not stonks')
            elif (interested+credited) >= 100000:
                em.set_footer(text='stonks')
            time.sleep(0.8)
            gens[ctx.message.author.id][6] = time.time()+ 2222
            saved_data[ctx.message.author.id][0]+=interested+credited
            
            await msg.edit(content='', embed=em)
        else:
            await ctx.reply(embed=discord.Embed(description='You can generate credits again <t:%i:R>'%gens[ctx.message.author.id][6]))
    else:
        await ctx.reply('You don\'t even have a generator, how would you generate credits lol. Get one generator by `f!build`', mention_author=False)
@bot.command()
async def build(ctx, *args):
    global saved_data, gens
    startgencheck(ctx.message.author.id)
    if gens[ctx.message.author.id][0] == 0:
      if saved_data[ctx.message.author.id][0] >= 30000:
        saved_data[ctx.message.author.id][0] -= 30000
        gens[ctx.message.author.id][0] = 1
        em = discord.Embed(color=0x888888, title='Building Generator... <a:loading:961321548868882552>',
                           description='{0} pays Mario :star2: 30,000 and tells '
                           'him to build a <:gen:961289293001785394> generator...'.format(ctx.message.author))
        em.set_thumbnail(url='https://emojipedia-us.s3.dualstack.us-west-1.amaz'
                         'onaws.com/thumbs/72/twitter/322/hammer-and-pick_2692-fe0f.png')
        em.set_footer(text='TIP: Generators can give you credits!')
        msg_01 = await ctx.send(embed=em)
        em = discord.Embed(color=0x889988, title='Building Generator... <a:loading:961321548868882552>',
                           description='Mario makes a gray wooden cube from :wood: wood')
        em.set_thumbnail(url='https://emojipedia-us.s3.dualstack.us-west-1.'
                         'amazonaws.com/thumbs/72/twitter/322/hammer_1f528.png')
        time.sleep(1)
        em.set_footer(text='TIP: Generators can give you credits!')
        await msg_01.edit(embed=em)
        em = discord.Embed(color=0x88AA88, title='Building Generator... <a:loading:961321548868882552>',
                           description='Mario constructs the generator\'s credit generating system')
        em.set_thumbnail(url='https://emojipedia-us.s3.dualstack.us-west-1.am'
                         'azonaws.com/thumbs/72/twitter/322/gear_2699-fe0f.png')
        em.set_footer(text='TIP: Generators can give you credits!')
        time.sleep(1)
        await msg_01.edit(embed=em)
        
        em = discord.Embed(color=0x22BD17, title='Done!',
                           description='Mario has finished creating the <:gen:961289293001785394>'
                        ' generator for {0} and gives it to them. Enjoy generating your credits! \\\U0001F4B0'
                           ''.format(ctx.message.author), icon_url='https://cdn.discordapp.com/emojis/961341639404691496.webp?size=96&quality=lossless')
        em.set_thumbnail(url='https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thum'
                         'bs/72/twitter/322/check-mark-button_2705.png')
        em.set_footer(text='TIP: Generators can give you credits!')
        em.set_author(name="Mario", url="https://discord.com/channels/0/0/0", icon_url="https://cdn.discordapp.com/emojis/961341639404691496.webp")
        time.sleep(1)
        await msg_01.edit(embed=em)
      else:
          em = discord.Embed(color=0xFF5734, title='<:nomark:960527955988193360> Not Enough Credits!',
                           description='Mario refuses to give {0} a generator because they'
                             ' don\'t have enough credits to pay! They need :star2: 30,000.'.format(ctx.message.author))
          em.set_thumbnail(url='https://emojipedia-us.s3.dualstack.us-west-1.amaz'
                           'onaws.com/thumbs/72/twitter/322/cross-mark-button_274e.png')
          em.set_footer(text='Get your own 30,000 credits!')
          msg_02 = await ctx.send(embed=em)
    else:
        await ctx.send('You already have a <:gen:961289293001785394> generator!')
@bot.command(aliases=['lb'])
async def leaderboard(ctx):
     members = ctx.message.guild.members
     list_of_member_ids = list(map(lambda member: member.id, members))
     await ctx.channel.trigger_typing()
     class IterableNoneType(type(0)):
          def __int__(self):
               return None
          def __float__(self):
               return None
     def check(user):
          if user in saved_data:
               return saved_data[user][0]
          else:
               return IterableNoneType()
     full_leaderboard = sorted(list_of_member_ids, key=check, reverse=True)
     View = []
     L1 = full_leaderboard[0:10]
     while 0 < len(L1):
       for m in L1:
          if check(m) == max(list(map(check, L1))):
               User = await bot.fetch_user(m)
               if User.bot == True:
                   L1.remove(m)
                   break
               View += ['**{0}** - :star2: {1:,}'.format(User, check(m))]
               L1.remove(m)
               break
          else:
               continue
     await ctx.send(embed=discord.Embed(title=f'Richest people in {ctx.guild.name}',
          description='\n'.join(View)))
          
@bot.command()
async def done(ctx, *args):
    global saved_data
    startcheck(ctx.message.author.id)
    if saved_data[ctx.message.author.id][0] < 5612:
        await ctx.send('You don\'t have enough credits to buy all possible shares')
    else:
        saved_data[ctx.message.author.id][9][8] += (saved_data[ctx.message.author.id][0]//5612)
        bought = saved_data[ctx.message.author.id][0]//5612
        saved_data[ctx.message.author.id][0] %= 5612
        await ctx.send(embed=discord.Embed(description=f'%s has spent :star2: {bought*5612:,} on purchasing '
                f'all possible shares (<:share:964777716597538816> {bought:,})' % ctx.message.author))
        del bought
@bot.command()
async def stonks(ctx, *args):
    global saved_data
    startcheck(ctx.message.author.id)
    if not saved_data[ctx.message.author.id][9][3]:
        if saved_data[ctx.message.author.id][9][8] < 1:
            await ctx.send('You don\'t have any shares!')
        else:
            saved_data[ctx.message.author.id][0] += (saved_data[ctx.message.author.id][9][8]*5612)
            sold = saved_data[ctx.message.author.id][9][8]
            saved_data[ctx.message.author.id][9][8] = 0
            await ctx.send(embed=discord.Embed(description=f'%s has sold all their shares (<:share:964777716597538816> {sold:,})'
                                           f' for :star2: {sold*5612:,}. <:mariostonks:969953552816537690>' % ctx.message.author))
            del sold
    else:
        if saved_data[ctx.message.author.id][9][8] < 1:
            await ctx.send('You don\'t have any shares!')
        else:
            chanced = random.randint(1,1000)
            pricee = 5612 if chanced > 900 else 5612
            saved_data[ctx.message.author.id][0] += (saved_data[ctx.message.author.id][9][8]*pricee)
            sold = saved_data[ctx.message.author.id][9][8]
            saved_data[ctx.message.author.id][9][8] = 0
            await ctx.send(embed=discord.Embed(description=f'%s has sold all their shares (<:share:964777716597538816> {sold:,})'
                                           f' for :star2: {sold*pricee:,}. <:mariostonks:969953552816537690>' % ctx.message.author))
            del sold
@bot.command()
async def ping(ctx, *args):
    t1 = time.time()
    em = discord.Embed(color=0x50ABC3)
    t2 = time.time()
    em.add_field(name='Latency', value=f'{int(bot.latency*1000):,}ms')
    t3 = t2 - t1
    em.add_field(name='API', value=f'{int(1000*t3):,}ms')
    await ctx.send(':ping_pong: Pong!', embed=em)
@bot.command()
async def petinv(ctx, *args):
    global saved_data,pets
    id = ctx.message.author.id
    name = ctx.message.author
    startpetcheck(ctx.message.author.id)
    startcheck(ctx.message.author.id)
    if len(args)==0:
        id = ctx.message.author.id
        name = ctx.message.author
    elif len(args) >= 1:
     if len(ctx.message.mentions) == 0:
        try:
            f_user = await bot.fetch_user(int(args[0]))
            name = f_user
            id = name.id
            del f_user
        except:
            name = ctx.message.author
            id = ctx.message.author.id
     else:
         try:
             g_user = ctx.message.mentions[0]
             name = g_user
             id = name.id
         except:
             name = ctx.message.author
             id = ctx.message.author.id
    startpetcheck(id)
    startcheck(id)
    extrastartcheck1(id)
    embed=discord.Embed(title='%s\'s pet inventory' % name)
    embed.add_field(name='Fish', value=''
f''':fish: Fish | {saved_data[id][9][7][0]:,}
:tropical_fish: Tropical Fish | {saved_data[id][9][7][1]:,}
:dolphin: Dolphin | {saved_data[id][9][7][2]:,}
:shark: Shark | {saved_data[id][9][7][3]:,}''')
    embed.add_field(name='Refreshments & Potions', value=''
f''':cup_with_straw: Water | {pets[id][10][15]:,}
:coffee: Coffee | {pets[id][10][16]:,}
<:potionofdarkness:971863500429328445> Potion of Darkness | {e1s[id][0]:,}
:milk: Milk | {e1s[id][1]:,}''')
    await ctx.send(embed=embed)
################# ADVENTURE UPDATE #################################
def startadvcheck(id):
    global advs
    if id not in advs:
        advs[id] = [{'swan':    0, 'beetle':    0, 'crocodile': 0,
                 'worm':     0, 'duck':      0, 'whale2':    0,
                 'rabbit2':  0, 'sheep':     0, 'tiger':     0},
                {'balloon':  0, 'football':  0,
                 'coin':     0, 'hamburger': 0,
                 'wrench':   0, 'shamrock':  0, 'shell': 0,
                 'onion':    0, 'anchor':    0, 'hibiscus': 0,
                 'pineapple':0, 'euro':      0},
                {'medal':    0, 'trophy':    0}, 0]

@bot.command(aliases=['inv'])
async def inventory(ctx, *args):
    global advs
    id = ctx.message.author.id
    name = ctx.message.author
    if len(args)==0:
        id = ctx.message.author.id
        name = ctx.message.author
    elif len(args) >= 1:
     if len(ctx.message.mentions) == 0:
        try:
            f_user = await bot.fetch_user(int(args[0]))
            name = f_user
            id = int(args[0])
            del f_user
        except:
            name = ctx.message.author
            id = ctx.message.author.id
     else:
         try:
             g_user = ctx.message.mentions[0]
         except:
             g_user = await bot.fetch_user(ctx.message.author.id)
         name = g_user
         id = g_user.id
    startadvcheck(id)
    startadvcheck(ctx.message.author.id)
    em=discord.Embed(title='%s\'s inventory' % name, description='`f!sell <item> <amount>` to sell items')
    D_animals = dict(advs[id][0])
    L_animals = list(advs[id][0])
    animals = []
    itemnames1 = {'swan': 'Swan', 'beetle': 'Beetle', 'crocodile': 'Crocodile',
                 'worm': 'Worm', 'duck': 'Duck', 'whale2': 'Whale', 'rabbit2':
                 'Rabbit', 'sheep': 'Sheep', 'tiger': 'Tiger'}
    for j in L_animals:
      if D_animals[j] >= 1:
        animals += [f':{j}: {itemnames1[j]} ({D_animals[j]:,} owned)']
    if len(animals) != 0:
        em.add_field(name='Animals', value=('\n'.join(animals)))
    else:
        em.add_field(name='Animals', value=('No animals!'))
    D_cols = dict(advs[id][1])
    L_cols = list(advs[id][1])
    cols = []
    itemnames2 = {'balloon': 'Balloon', 'football': 'Brown Football', 'coin': 'Coin',
                 'hamburger': 'Burger', 'wrench': 'Wrench', 'shamrock':
                 'Shamrock', 'shell': 'Seashell', 'onion': 'Onion',
                  'anchor': 'Anchor', 'hibiscus': 'Hibiscus', 'pineapple': 'Pineapple',
                  'euro': 'Zhao\'s Money', 'eye': 'Mario\'s Eye'}
    for j in L_cols:
      if D_cols[j] >= 1:
        cols += [f':{j}: {itemnames2[j]} ({D_cols[j]:,} owned)']
    if len(cols) != 0:
        em.add_field(name='Collectables', value=('\n'.join(cols)))
    else:
        em.add_field(name='Collectables', value=('No collectables!'))
    D_rares = dict(advs[id][2])
    L_rares = list(advs[id][2])
    rares = []
    itemnames3 = {'medal': 'Medal', 'trophy': 'Trophy'}
    for j in L_rares:
      if D_rares[j] >= 1:
        rares += [f':{j}: {itemnames3[j]} ({D_rares[j]:,} owned)']
    if len(rares) != 0:
        em.add_field(name='Rares', value=('\n'.join(rares)))
    else:
        em.add_field(name='Rares', value=('No rares!'))
    em.add_field(name='Ores', value=('Check your ores with `f!ores`'))
    await ctx.send(embed=em)
@bot.command()
async def sell(ctx, *args):
     global advs, saved_data, e2s
     startcheck(ctx.message.author.id)
     startadvcheck(ctx.message.author.id)
     extrascheck[2](ctx.message.author.id)
     userid = ctx.message.author.id
     username = ctx.message.author
     if len(args) == 0:
          cnf = [None, 1]
     elif len(args) == 1:
          cnf = [args[0], 1]
     elif len(args) >= 2:
          try:
             cnf = [args[0], int(float(args[1]))]
          except:                                  #\#########\
               cnf = [args[1], int(float(args[0]))] # reverse |
     if cnf[1] >= 1:                               #/#########/
       if cnf[0] == None:
          await ctx.reply('The different sellables are `swan`, `beetle`, '
'`crocodile`, `worm`, `duck`, `whale`, `rabbit`, `sheep`, `tiger`, `balloon`, '
'`football`, `coin`, `hamburger`, `wrench`, `shamrock`, `shell`, `onion`, and `anchor`.')
       elif cnf[0][0:2].lower() == 'sw':
            if advs[userid][0]['swan'] >= cnf[1]:
                    advs[userid][0]['swan'] -= cnf[1]
                    saved_data[userid][0] += (cnf[1]*100)
                    await ctx.send(embed=discord.Embed(description=''
                    f'%s has successfully sold :swan: {cnf[1]:,}'
                    f' for :star2: {cnf[1]*100:,}'%username))
            else:
                 await ctx.reply(f'You don\'t have {cnf[1]:,}x :swan: Swan!')
       elif cnf[0][0:2].lower() == 'wo':
            if advs[userid][0]['worm'] >= cnf[1]:
                    advs[userid][0]['worm'] -= cnf[1]
                    saved_data[userid][0] += (cnf[1]*80)
                    await ctx.send(embed=discord.Embed(description=''
                    f'%s has successfully sold :worm: {cnf[1]:,}'
                    f' for :star2: {cnf[1]*80:,}'%username))
            else:
                 await ctx.reply(f'You don\'t have {cnf[1]:,}x :worm: Worm!')
       elif cnf[0][0:2].lower() == 'cr':
            if advs[userid][0]['crocodile'] >= cnf[1]:
                    advs[userid][0]['crocodile'] -= cnf[1]
                    saved_data[userid][0] += (cnf[1]*2500)
                    await ctx.send(embed=discord.Embed(description=''
                    f'%s has successfully sold :crocodile: {cnf[1]:,}'
                    f' for :star2: {cnf[1]*2500:,}'%username))
            else:
                 await ctx.reply(f'You don\'t have {cnf[1]:,}x :crocodile: Crocodile!')
       elif cnf[0][0:2].lower() == 'be':
            if advs[userid][0]['beetle'] >= cnf[1]:
                    advs[userid][0]['beetle'] -= cnf[1]
                    saved_data[userid][0] += (cnf[1]*1000)
                    await ctx.send(embed=discord.Embed(description=''
                    f'%s has successfully sold :beetle: {cnf[1]:,}'
                    f' for :star2: {cnf[1]*1000:,}'%username))
            else:
                 await ctx.reply(f'You don\'t have {cnf[1]:,}x :beetle: Beetle!')
       elif cnf[0][0:3].lower() == 'duc':
            if advs[userid][0]['duck'] >= cnf[1]:
                    advs[userid][0]['duck'] -= cnf[1]
                    saved_data[userid][0] += (cnf[1]*2500)
                    await ctx.send(embed=discord.Embed(description=''
                    f'%s has successfully sold :duck: {cnf[1]:,}'
                    f' for :star2: {cnf[1]*2500:,}'%username))
            else:
               await ctx.reply(f'You don\'t have {cnf[1]:,}x :duck: Duck!')
       elif cnf[0][0:2].lower() == 'wh':
            if advs[userid][0]['whale2'] >= cnf[1]:
                    advs[userid][0]['whale2'] -= cnf[1]
                    saved_data[userid][0] += (cnf[1]*15000)
                    await ctx.send(embed=discord.Embed(description=''
                    f'%s has successfully sold :whale2: {cnf[1]:,}'
                    f' for :star2: {cnf[1]*15000:,}'%username))
            else:
               await ctx.reply(f'You don\'t have {cnf[1]:,}x :whale2: Whale!')
       elif cnf[0][0:3].lower() == 'rab':
            if advs[userid][0]['rabbit2'] >= cnf[1]:
                    advs[userid][0]['rabbit2'] -= cnf[1]
                    saved_data[userid][0] += (cnf[1]*4500)
                    await ctx.send(embed=discord.Embed(description=''
                    f'%s has successfully sold :rabbit2: {cnf[1]:,}'
                    f' for :star2: {cnf[1]*4500:,}'%username))
            else:
               await ctx.reply(f'You don\'t have {cnf[1]:,}x :rabbit2: Rabbit!')
       elif cnf[0][0:3].lower() == 'shee':
            if advs[userid][0]['sheep'] >= cnf[1]:
                    advs[userid][0]['sheep'] -= cnf[1]
                    saved_data[userid][0] += (cnf[1]*5500)
                    await ctx.send(embed=discord.Embed(description=''
                    f'%s has successfully sold :sheep: {cnf[1]:,}'
                    f' for :star2: {cnf[1]*5500:,}'%username))
            else:
               await ctx.reply(f'You don\'t have {cnf[1]:,}x :sheep: Sheep!')
       elif cnf[0][0:3].lower() == 'tig':
            if advs[userid][0]['tiger'] >= cnf[1]:
                    advs[userid][0]['tiger'] -= cnf[1]
                    saved_data[userid][0] += (cnf[1]*21500)
                    await ctx.send(embed=discord.Embed(description=''
                    f'%s has successfully sold :tiger: {cnf[1]:,}'
                    f' for :star2: {cnf[1]*21500:,}'%username))
            else:
               await ctx.reply(f'You don\'t have {cnf[1]:,}x :tiger: Tiger!')
       elif cnf[0][0:3].lower() == 'bal':
            if advs[userid][1]['balloon'] >= cnf[1]:
                    advs[userid][1]['balloon'] -= cnf[1]
                    saved_data[userid][0] += (cnf[1]*6500)
                    await ctx.send(embed=discord.Embed(description=''
                    f'%s has successfully sold :balloon: {cnf[1]:,}'
                    f' for :star2: {cnf[1]*6500:,}'%username))
            else:
               await ctx.reply(f'You don\'t have {cnf[1]:,}x :balloon: Balloon!')
       elif cnf[0][0:4].lower() == 'foot':
            if advs[userid][1]['football'] >= cnf[1]:
                    advs[userid][1]['football'] -= cnf[1]
                    saved_data[userid][0] += (cnf[1]*25000)
                    await ctx.send(embed=discord.Embed(description=''
                    f'%s has successfully sold :football: {cnf[1]:,}'
                    f' for :star2: {cnf[1]*25000:,}'%username))
            else:
               await ctx.reply(f'You don\'t have {cnf[1]:,}x :football: Brown Football!')
       elif cnf[0][0:4].lower() == 'coin':
            if advs[userid][1]['coin'] >= cnf[1]:
                    advs[userid][1]['coin'] -= cnf[1]
                    saved_data[userid][0] += (cnf[1]*75000)
                    await ctx.send(embed=discord.Embed(description=''
                    f'%s has successfully sold :coin: {cnf[1]:,}'
                    f' for :star2: {cnf[1]*75000:,}'%username))
            else:
               await ctx.reply(f'You don\'t have {cnf[1]:,}x :coin: Coin!')
       elif cnf[0][0:4].lower() == 'hamb' or cnf[0][0:3].lower() == 'bur':
            if advs[userid][1]['hamburger'] >= cnf[1]:
                    advs[userid][1]['hamburger'] -= cnf[1]
                    saved_data[userid][0] += (cnf[1]*8000)
                    await ctx.send(embed=discord.Embed(description=''
                    f'%s has successfully sold :hamburger: {cnf[1]:,}'
                    f' for :star2: {cnf[1]*8000:,}'%username))
            else:
               await ctx.reply(f'You don\'t have {cnf[1]:,}x :hamburger: Burger!')
       elif cnf[0][0:2].lower() == 'wr':
            if advs[userid][1]['wrench'] >= cnf[1]:
                    advs[userid][1]['wrench'] -= cnf[1]
                    saved_data[userid][0] += (cnf[1]*25000)
                    await ctx.send(embed=discord.Embed(description=''
                    f'%s has successfully sold :wrench: {cnf[1]:,}'
                    f' for :star2: {cnf[1]*25000:,}'%username))
            else:
               await ctx.reply(f'You don\'t have {cnf[1]:,}x :wrench: Wrench!')
       elif cnf[0][0:4].lower() == 'sham':
            if advs[userid][1]['shamrock'] >= cnf[1]:
                    advs[userid][1]['shamrock'] -= cnf[1]
                    saved_data[userid][0] += (cnf[1]*12000)
                    await ctx.send(embed=discord.Embed(description=''
                    f'%s has successfully sold :shamrock: {cnf[1]:,}'
                    f' for :star2: {cnf[1]*12000:,}'%username))
            else:
               await ctx.reply(f'You don\'t have {cnf[1]:,}x :shamrock: Shamrock!')
       elif cnf[0][0:4].lower() == 'shel':
            if advs[userid][1]['shell'] >= cnf[1]:
                    advs[userid][1]['shell'] -= cnf[1]
                    saved_data[userid][0] += (cnf[1]*4000)
                    await ctx.send(embed=discord.Embed(description=''
                    f'%s has successfully sold :shell: {cnf[1]:,}'
                    f' for :star2: {cnf[1]*4000:,}'%username))
            else:
               await ctx.reply(f'You don\'t have {cnf[1]:,}x :shell: Shell!')
       elif cnf[0][0:3].lower() == 'oni':
            if advs[userid][1]['onion'] >= cnf[1]:
                    advs[userid][1]['onion'] -= cnf[1]
                    saved_data[userid][0] += (cnf[1]*6000)
                    await ctx.send(embed=discord.Embed(description=''
                    f'%s has successfully sold :onion: {cnf[1]:,}'
                    f' for :star2: {cnf[1]*6000:,}'%username))
            else:
               await ctx.reply(f'You don\'t have {cnf[1]:,}x :onion: Onion!')
       elif cnf[0][0:3].lower() == 'anc':
            if advs[userid][1]['anchor'] >= cnf[1]:
                    advs[userid][1]['anchor'] -= cnf[1]
                    saved_data[userid][0] += (cnf[1]*125000)
                    await ctx.send(embed=discord.Embed(description=''
                    f'%s has successfully sold :anchor: {cnf[1]:,}'
                    f' for :star2: {cnf[1]*125000:,}'%username))
            else:
               await ctx.reply(f'You don\'t have {cnf[1]:,}x :anchor: Anchor!')
       elif cnf[0][0:3].lower() == 'hib':
            if advs[userid][1]['hibiscus'] >= cnf[1]:
                    advs[userid][1]['hibiscus'] -= cnf[1]
                    saved_data[userid][0] += (cnf[1]*2700000)
                    await ctx.send(embed=discord.Embed(description=''
                    f'%s has successfully sold :hibiscus: {cnf[1]:,}'
                    f' for :star2: {cnf[1]*2700000:,}'%username))
       elif cnf[0][0:3].lower() == 'pin':
            if advs[userid][1]['pineapple'] >= cnf[1]:
                    advs[userid][1]['pineapple'] -= cnf[1]
                    saved_data[userid][0] += (cnf[1]*5400000)
                    await ctx.send(embed=discord.Embed(description=''
                    f'%s has successfully sold :pineapple: {cnf[1]:,}'
                    f' for :star2: {cnf[1]*5400000:,}'%username))
            else:
               await ctx.reply(f'You don\'t have {cnf[1]:,}x :pineapple: Pineapple!')
       elif cnf[0][0:3].lower() == 'med':
            if advs[userid][2]['medal'] >= cnf[1]:
                    advs[userid][2]['medal'] -= cnf[1]
                    saved_data[userid][0] += (cnf[1]*600000)
                    await ctx.send(embed=discord.Embed(description=''
                    f'%s has successfully sold :medal: {cnf[1]:,}'
                    f' for :star2: {cnf[1]*600000:,}'%username))
            else:
               await ctx.reply(f'You don\'t have {cnf[1]:,}x :medal: Medal!')
       elif cnf[0].lower().startswith('ir'):
            if e2s[userid][1][0] >= cnf[1]:
                    e2s[userid][1][0] -= cnf[1]
                    saved_data[userid][0] += (cnf[1]*450)
                    await ctx.send(embed=discord.Embed(description=''
                    f'%s has successfully sold <:iron:982682170340544532> {cnf[1]:,}'
                    f' for :star2: {cnf[1]*450:,}'%username))
            else:
               await ctx.reply(f'You don\'t have {cnf[1]:,}x <:iron:982682170340544532> Iron Ore!')
       elif cnf[0].lower().startswith('sil'):
            if e2s[userid][1][1] >= cnf[1]:
                    e2s[userid][1][1] -= cnf[1]
                    saved_data[userid][0] += (cnf[1]*800)
                    await ctx.send(embed=discord.Embed(description=''
                    f'%s has successfully sold <:silver:982682172462866462> {cnf[1]:,}'
                    f' for :star2: {cnf[1]*800:,}'%username))
            else:
               await ctx.reply(f'You don\'t have {cnf[1]:,}x <:silver:982682172462866462> Silver Ore!')
       elif cnf[0].lower().startswith('gol'):
            if e2s[userid][1][2] >= cnf[1]:
                    e2s[userid][1][2] -= cnf[1]
                    saved_data[userid][0] += (cnf[1]*2000)
                    await ctx.send(embed=discord.Embed(description=''
                    f'%s has successfully sold <:gold:982682167891083306> {cnf[1]:,}'
                    f' for :star2: {cnf[1]*2000:,}'%username))
            else:
               await ctx.reply(f'You don\'t have {cnf[1]:,}x <:gold:982682167891083306> Gold Ore!')
       elif cnf[0].lower().startswith('dia'):
            if e2s[userid][1][3] >= cnf[1]:
                    e2s[userid][1][3] -= cnf[1]
                    saved_data[userid][0] += (cnf[1]*4500)
                    await ctx.send(embed=discord.Embed(description=''
                    f'%s has successfully sold <:diamond:992415718438097068> {cnf[1]:,}'
                    f' for :star2: {cnf[1]*4500:,}'%username))
            else:
               await ctx.reply(f'You don\'t have {cnf[1]:,}x <:diamond:992415718438097068> Diamond Ore!')
       elif cnf[0][0:3].lower() in ['tro']:
            await ctx.reply(f'You can\'t sell this item.')
       elif cnf[0].lower().startswith('zha') or cnf[0].lower().startswith('mon') or cnf[0].lower().endswith('ney'):
            if advs[userid][1]['euro'] >= cnf[1]:
                    advs[userid][1]['euro'] -= cnf[1]
                    saved_data[userid][0] += (cnf[1]*1200000)
                    await ctx.send(embed=discord.Embed(description=''
                    f'%s has successfully sold :euro: {cnf[1]:,}'
                    f' for :star2: {cnf[1]*1200000:,}'%username))
            else:
               await ctx.reply(f'You don\'t have {cnf[1]:,}x :euro: Zhao\'s Money!')
       else:
          await ctx.reply('The different sellables are `swan`, `beetle`, '
'`crocodile`, `worm`, `duck`, `whale`, `rabbit`, `sheep`, `tiger`, `balloon`, '
'`football`, `coin`, `hamburger`, `wrench`, `shamrock`, `shell`, `onion`, `medal`, and `anchor`.'
          ' The sellable ores are `iron`, `silver`, `gold`, and `diamond`.')

               
     else:
          await ctx.reply('You must provide a positive number!')
       


@bot.command(aliases=['adventure'])
async def adv(ctx, *args):
     startadvcheck(ctx.message.author.id)
     global advs
     if advs[ctx.message.author.id][3] <= time.time():
          pass
     else:
          timeleft = ''
          secsleft=advs[ctx.message.author.id][3]-time.time()
          secsleft = int(secsleft)
          if secsleft >= 60:
               timeleft+='%i minutes and '%(secsleft/60)
          timeleft += '%i seconds' % (secsleft % 60)
          await ctx.reply('You must wait another {0} before going on adventure again!'.format(timeleft))
          return
     if len(args) == 0:
          await ctx.reply(embed=discord.Embed(title='Select a number',description=''
               '`f!adv 1` to get animals in the woods'
               '\n`f!adv 2` to get animals on water i.e. swan\n`f!adv 3` to find'
                              ' a chest to get a collectable'))
     elif len(args) >= 1:
          if args[0][0] == '1':
               advs[ctx.message.author.id][3]=time.time()+100
               msg = await ctx.reply('Hunting... :evergreen_tree:', mention_author=0)
               await asyncio.sleep(1.2)
               possible_animals = ['beetle','beetle','duck',
                                    None ,'sheep', 'tiger',
                                   'crocodile', 'sheep', 'worm',
                                   'duck', 'duck', None, None,
                                   'beetle','beetle','duck',
                                   'worm'  ,'sheep', 'tiger',
                                   'crocodile', 'sheep', 'worm',
                                   'duck', None, None, None]
               got_animal = random.choice(possible_animals)
               if got_animal == None:
                    await msg.edit(content='', embed=discord.Embed(title='You brought back... NOTHING!',
                    description='You went hunting in the :wood: woods and brought back nothi'
                                        'ng. Better luck next time!', color=0xaa0000))
               elif got_animal == 'duck':
                    advs[ctx.message.author.id][0][got_animal] += 1
                    await msg.edit(content='', embed=discord.Embed(title='Succesful hunt!',
                    description='You went hunting in the woods and brought back a :duck: Duck. '
                    'It walked away from the pond and wanted to find some :bread: bread.',
          color=0x00aa00))
               elif got_animal == 'beetle':
                    advs[ctx.message.author.id][0][got_animal] += 1
                    await msg.edit(content='', embed=discord.Embed(title='Succesful hunt!',
                    description='You went hunting in the woods and brought back a :beetle: Beetle. '
                    'It was on the :wood: wooden log.',color=0x00aa00))
               elif got_animal == 'worm':
                    advs[ctx.message.author.id][0][got_animal] += 1
                    await msg.edit(content='', embed=discord.Embed(title='Succesful hunt!',
                    description='You went hunting in the woods and brought back a :worm: Worm. '
                    'It was in an :apple: apple, then it crawled onto the wooden stick',color=0x00aa00))
               elif got_animal == 'sheep':
                    advs[ctx.message.author.id][0][got_animal] += 1
                    await msg.edit(content='', embed=discord.Embed(title='Succesful hunt!',
                    description='You went hunting in the woods and brought back a '
                    ':sheep: Sheep. _\*sheep baahs\*_',color=0x00aa00))
               elif got_animal == 'crocodile':
                    advs[ctx.message.author.id][0][got_animal] += 1
                    await msg.edit(content='', embed=discord.Embed(title='Succesful hunt!',
                    description='You went hunting in the woods and brought back a '
                    ':crocodile: Crocodile. ***RAWR!*** `XD`',color=0x00aa00))
               elif got_animal == 'tiger':
                    advs[ctx.message.author.id][0][got_animal] += 1
                    await msg.edit(content='', embed=discord.Embed(title='Succesful hunt!',
                    description='You went hunting in the woods and brought back a '
                    ':tiger: Tiger. It was fighting against a :lion: Lion. The tiger won.',color=0x00aa00))
          elif args[0][0]=='2':
               advs[ctx.message.author.id][3]=time.time()+100
               possible_fish = ['whale2', 'crocodile', 'swan', 'duck', 'shell',
                                'swan', 'crocodile', 'swan', 'duck', 'shell',
                                'crocodile', 'football', 'swan', 'swan', 'swan', None,
                                None,  None, None, 'football', 'football']
               got_animal = random.choice(possible_fish)
               got_fish = got_animal
               msg = await ctx.reply('Fishing... :fishing_pole_and_fish:', mention_author=0)
               await asyncio.sleep(1.3)
               if got_fish == None:
                    await msg.edit(content='', embed=discord.Embed(title='You found nothing!',
                    description='You cast out your line, but nothing caught it!', color=0xaa0000))
               elif got_fish == 'swan':
                    advs[ctx.message.author.id][0][got_animal] += 1
                    await msg.edit(content='', embed=discord.Embed(title='Successful fishing!',
                    description='You cast out your line and brought back a :swan: Swan!', color=0x00aa00))
               elif got_fish == 'shell':
                    advs[ctx.message.author.id][1][got_animal] += 1
                    await msg.edit(content='', embed=discord.Embed(title='Successful fishing!',
                    description='You cast out your line and brought back a :shell: Shell!', color=0x00aa00))
               elif got_fish == 'football':
                    advs[ctx.message.author.id][1][got_animal] += 1
                    await msg.edit(content='', embed=discord.Embed(title='Successful fishing!',
                    description='You cast out your line... and... brought back...'
                              ' a... :football: Brown Football... someone kicked the football'
                                                  ' too far.', color=0x00aa00))
               elif got_fish == 'duck':
                    advs[ctx.message.author.id][0][got_animal] += 1
                    await msg.edit(content='', embed=discord.Embed(title='Successful fishing!',
                    description='You cast out your line and brought back a :duck: Duck!'
                                                       ' \*QUACK QUACK\*', color=0x00aa00))
               elif got_fish == 'whale2':
                    advs[ctx.message.author.id][0][got_animal] += 1
                    await msg.edit(content='', embed=discord.Embed(title='Successful fishing!',
                    description='You cast out your line and brought back a :whale2: Whale, nice!'
                                   ' Was that the largest whale?', color=0x00aa00))
               elif got_fish == 'crocodile':
                    advs[ctx.message.author.id][0][got_animal] += 1
                    await msg.edit(content='', embed=discord.Embed(title='Successful fishing!',
                    description='You cast out your line and brought back a :crocodile: Crocodile!', color=0x00aa00))
          elif args[0][0]=='3':
                    advs[ctx.message.author.id][3]=time.time()+102
                    possible_items = [
                    'balloon','balloon','balloon','balloon','balloon',
                    'shamrock','shamrock','coin','anchor','hamburger','hamburger',
                    'onion','onion','hamburger','balloon','balloon','balloon','coin',
                    'wrench','wrench','medal',
                    'balloon','balloon','balloon','balloon','balloon',
                    'shamrock','shamrock','coin','anchor','hamburger','hamburger',
                    'onion','onion','hamburger','balloon','balloon','balloon','coin',
                    'wrench','wrench','medal','trophy','trophy', 
                    None, None, None, None, None, None, None, None, None, None, None,
                    None, None, 'trophy', None, None, 'trophy', None, None, None,
                    None, None, 'balloon', 'balloon']
                    gotitem = random.choice(possible_items)
                    msg = await ctx.reply('Searching for a <:chest:966057532693033022> chest...')
                    await asyncio.sleep(2)
                    itemlist = ['balloon', 'shamrock', 'coin', 'anchor', 'hamburger', 'onion', 'wrench', 'medal', 'trophy', None]
                    if gotitem == 'balloon':
                         advs[ctx.message.author.id][1][gotitem] += 1
                         await msg.edit(content='', embed=discord.Embed(title='Successful loot!',
                    description='You opened a <:chest:966057532693033022> and found a :balloon: Balloon!', color=0x00aa00))
                    elif gotitem == 'shamrock':
                         advs[ctx.message.author.id][1][gotitem] += 1
                         await msg.edit(content='', embed=discord.Embed(title='Successful loot!',
                    description='You opened a <:chest:966057532693033022> and found a :shamrock: Shamrock!', color=0x00aa00))
                    elif gotitem == 'coin':
                         advs[ctx.message.author.id][1][gotitem] += 1
                         await msg.edit(content='', embed=discord.Embed(title='Successful loot!',
                    description='You opened a <:chest:966057532693033022> and found a :coin: Coin, nice!', color=0x00aa00))
                    elif gotitem == 'anchor':
                         advs[ctx.message.author.id][1][gotitem] += 1
                         await msg.edit(content='', embed=discord.Embed(title='Successful loot!',
                    description='You opened a <:chest:966057532693033022> and found an :anchor: Anchor, nice!', color=0x00aa00))
                    elif gotitem == 'hamburger':
                         advs[ctx.message.author.id][1][gotitem] += 1
                         await msg.edit(content='', embed=discord.Embed(title='Successful loot!',
                    description='You opened a <:chest:966057532693033022> and found a :hamburger: Burger!', color=0x00aa00))
                    elif gotitem == 'onion':
                         advs[ctx.message.author.id][1][gotitem] += 1
                         await msg.edit(content='', embed=discord.Embed(title='Successful loot!',
                    description='You opened a <:chest:966057532693033022> and found an :onion: Onion!', color=0x00aa00))
                    elif gotitem == 'wrench':
                         advs[ctx.message.author.id][1][gotitem] += 1
                         await msg.edit(content='', embed=discord.Embed(title='Successful loot!',
                    description='You opened a <:chest:966057532693033022> and found a :wrench: Wrench!', color=0x00aa00))
                    elif gotitem == 'medal':
                         advs[ctx.message.author.id][2][gotitem] += 1
                         await msg.edit(content='', embed=discord.Embed(title='Nice loot!',
                    description='You opened a <:chest:966057532693033022> and found a :medal: Medal, nice!!!', color=0x00aa00))
                    elif gotitem == 'trophy':
                         advs[ctx.message.author.id][2][gotitem] += 1
                         await msg.edit(content='', embed=discord.Embed(title='OP loot!!!',
                    description='You opened a <:chest:966057532693033022> and found a :trophy: Trophy (wth how did you do dis)', color=0x00aa00))
                    elif gotitem == None:
                         await msg.edit(content='', embed=discord.Embed(title='Unsuccessful loot!',
                    description='You opened a <:chest:966057532693033022>... but you found nothing. Better luck next time!', color=0xaa0000))
                    
                         


[{'swan':    0, 'beetle':    0, 'crocodile': 0,
                 'worm':    0, 'duck':      0, 'whale2':    0,
                 'rabbit2': 0, 'sheep':     0, 'tiger':     0},
                {'balloon': 0, 'football':  0,
                 'coin':    0, 'hamburger': 0,
                 'wrench':  0, 'shamrock':  0, 'shell': 0,
                 'onion':   0, 'anchor':    0},
                {'medal':   0, 'trophy':    0}, 0]








#################################################################
########################################################################
def startbmcheck(id):
  if id not in bms:
    bms[id] = [0, 0, 0, 0]
    #[drug1, drug1cd, permit, hexcd]#
  else:
      pass
@bot.command(aliases=['blackmarket'])
async def bm(ctx, *args):
    global bms
    startbmcheck(ctx.message.author.id)
    em=discord.Embed(title='Black Market',
     color=15, description='`f!exch <id> <amount (optional)>` to buy from here,'
                    ' be careful, there is a chance of getting scammed...\n')
    em.add_field(name='Drugs & Permit', value='[1] <:weed:967418854697476179> Weed - similar to `f!drink`, but con'
     'sumed with `f!smoke`, beer cooldown included | Price: :star2: 5,000\n'
     '[2] {0}:scroll: Seller\x27s Permit - Allows you to sell weed | Price: '
     '<:weed:967418854697476179> 12\n'
     '[3] {1}:star2: 6,000 credits - Sell your weed'
     ' to someone else | Price: <:weed:967418854697476179> 1'.format('<:yesmark:960527955833020456> **BOUGHT** - ' if bms[ctx.message.author.id][2] else str(),
                 '<:nomark:960527955988193360> **LOCKED** - ' if not bms[ctx.message.author.id][2] else str()))
    await ctx.send(embed=em)
@bot.command(aliases=['excha','exchan','exchang','exchange','exchangee'])
async def exch(ctx, *args):
     startbmcheck(ctx.message.author.id)
     global bms, saved_data
     if len(args) == 0:
          await ctx.send('Format is `f!exch <id> <amount>`')
     elif len(args) == 1:
          try:
               id_ = int(args[0])
               assert id_ in (1,2,3,)
          except:
               id_ = -1
          if id_ == -1:
               await ctx.send('The ID you entered doesn\x27t seem to be valid')
          elif id_ == 1:
               if saved_data[ctx.message.author.id][0] >= 5000:
                    c = random.randint(0,999)
                    saved_data[ctx.message.author.id][0] -= 5000
                    if c <= 750:
                       bms[ctx.message.author.id][0] += 1
                       await ctx.send(embed=discord.Embed(
                            color=1,description=''
                            '%s has successfully purchased <:weed:967'
                            '418854697476179> 1'%ctx.message.author))
                    else:
                       bms[ctx.message.author.id][0] += 0
                       await ctx.send(embed=discord.Embed(
                            color=1,description=''
                            '%s has paid :star2: 5,000 and gotten scammed rip'%ctx.message.author))
               else:
                    await ctx.send('You don\'t have enough credits'
                    ' to buy <:weed:967418854697476179> 1!')
          elif id_ == 2:
            if not bms[ctx.message.author.id][2]:
               if bms[ctx.message.author.id][0] >= 12:
                    c = random.randint(0,999)
                    bms[ctx.message.author.id][0] -= 12
                    if c <= 750:
                       bms[ctx.message.author.id][2] = 1
                       await ctx.send(embed=discord.Embed(
                            color=1,description=''
                            '%s has successfully purchased a '
                            ':scroll:'%ctx.message.author))
                    else:
                       await ctx.send(embed=discord.Embed(
                            color=1,description=''
                            '%s has paid <:weed:967418854697476179> 12 and gotten scammed rip'%ctx.message.author))
               else:
                    await ctx.send('You don\'t have enough weed'
                    ' to buy a :scroll:!')
            else:
                 await ctx.send('<:nomark:960527955988193360> You already have a :scroll:!')
          elif id_ == 3:
            try: assert 0
            except: amt = 1
            if bms[ctx.message.author.id][2]:
               if bms[ctx.message.author.id][0] >= amt:
                    c = random.randint(0,999)
                    bms[ctx.message.author.id][0] -= amt
                    if c <= 750:
                       saved_data[ctx.message.author.id][0] += amt*6000
                       await ctx.send(embed=discord.Embed(
                            color=1,description=''
                            f'%s has successfully sold <:weed:967418854697476179> {amt:,}'%ctx.message.author))
                    else:
                       await ctx.send(embed=discord.Embed(
                            color=1,description=''
                            f'%s has paid <:weed:967418854697476179> {amt:,} and gotten scammed rip'%ctx.message.author))
               else:
                    await ctx.send(f'You don\'t have <:weed:967418854697476179> {amt:,}!')
            else:
                 await ctx.send('<:nomark:960527955988193360> You must own a :scroll: **Seller\x27s Permit** '
                                'in order to sell weed!')
     elif len(args) >= 2:
          try:
               id_ = int(args[0])
               assert id_ in (1,2,3,)
          except:
               id_ = -1
          if id_ == -1:
               await ctx.send('The ID you entered doesn\x27t seem to be valid lol')
          elif id_ == 1:
               try: amt = type(1)(float(args[1]))
               except: amt = 1
               if amt < 0:
                 amt = abs(amt)
               if saved_data[ctx.message.author.id][0] >= amt*5000:
                    c = random.randint(0,979)
                    saved_data[ctx.message.author.id][0] -= amt*5000
                    if c <= 750:
                       bms[ctx.message.author.id][0] += amt
                       await ctx.send(embed=discord.Embed(
                            color=1,description=''
                            '%s has successfully purchased <:weed:967'
                            f'418854697476179> {amt:,}'%ctx.message.author))
                    else:
                       bms[ctx.message.author.id][0] += 0
                       await ctx.send(embed=discord.Embed(
                            color=1,description=''
                            f'%s has paid :star2: {amt*5000:,} and gotten scammed rip'%ctx.message.author))
               else:
                    await ctx.send('You don\'t have enough credits'
                    f' to buy <:weed:967418854697476179> {amt:,}!')
          elif id_ == 2:
            if not bms[ctx.message.author.id][2]:
               if bms[ctx.message.author.id][0] >= 12:
                    c = random.randint(0,999)
                    bms[ctx.message.author.id][0] -= 12
                    if c <= 750:
                       bms[ctx.message.author.id][2] = 1
                       await ctx.send(embed=discord.Embed(
                            color=1,description=''
                            '%s has successfully purchased a '
                            ':scroll:'%ctx.message.author))
                    else:
                       await ctx.send(embed=discord.Embed(
                            color=1,description=''
                            '%s has paid <:weed:967418854697476179> 12 and gotten scammed rip'%ctx.message.author))
               else:
                    await ctx.send('You don\'t have enough weed'
                    ' to buy a :scroll:!')
            else:
                 await ctx.send('<:nomark:960527955988193360> You already have a :scroll:!')
          elif id_ == 3:
            try: amt = type(1)(float(args[1]))
            except: amt = 1
            if amt < 0:
                 amt = abs(amt)
            if bms[ctx.message.author.id][2]:
               if bms[ctx.message.author.id][0] >= amt:
                    c = random.randint(0,999)
                    bms[ctx.message.author.id][0] -= amt
                    if c <= 550:
                       saved_data[ctx.message.author.id][0] += amt*6000
                       await ctx.send(embed=discord.Embed(
                            color=1,description=''
                            f'%s has successfully sold <:weed:967418854697476179> {amt:,}'%ctx.message.author))
                    else:
                       await ctx.send(embed=discord.Embed(
                            color=1,description=''
                            f'%s has paid <:weed:967418854697476179> {amt:,} and gotten scammed rip'%ctx.message.author))
               else:
                    await ctx.send(f'You don\'t have <:weed:967418854697476179> {amt:,}!')
            else:
                 await ctx.send('<:nomark:960527955988193360> You must own a :scroll: **Seller\x27s Permit** '
                                'in order to sell weed!')
               
@bot.command()
async def weed(ctx, *args):
    global bms
    id = ctx.message.author.id
    name = ctx.message.author
    startbmcheck(ctx.message.author.id)
    if len(args)==0:
        id = ctx.message.author.id
        name = ctx.message.author
    elif len(args) >= 1:
     if len(ctx.message.mentions) == 0:
        try:
            f_user = await bot.fetch_user(int(args[0]))
            name = f_user
            id = int(args[0])
            del f_user
        except:
            name = ctx.message.author
            id = ctx.message.author.id
     else:
         try:
             g_user = ctx.message.mentions[0]
         except:
             g_user = await bot.fetch_user(ctx.message.author.id)
         name = g_user
         id = g_user.id
    startbmcheck(id)
    weeds = bms[id][0]
    em=discord.Embed(description='%s has <:weed:96'
                                       '7418854'f'697476179> {weeds:,}'%name, color=0x009102)
    if random.randint(1,100) > 50:
         em.set_footer(text='TIP: Weed is consumable by f!smoke!')
    elif random.randint(1,100) < 30:
         em.set_footer(text='TIP: Weed removes drinking cooldown!')
    else:
         em.set_footer(text='TIP: Weed is purchaseable by f!exch 1 <amount>!')
    await ctx.send(embed=em)
@bot.command()
async def smoke(ctx, *args):
    global weapons,pets,gens,saved_data,advs,bms
    startweaponcheck(ctx.message.author.id)
    startcheck(ctx.message.author.id)
    startpetcheck(ctx.message.author.id)
    startgencheck(ctx.message.author.id)
    startadvcheck(ctx.message.author.id)
    startbmcheck(ctx.message.author.id)
    if bms[ctx.message.author.id][1] <= time.time():
        if bms[ctx.message.author.id][0] >= 1:
            saved_data[ctx.message.author.id][1]=0
            saved_data[ctx.message.author.id][3][1]=0
            saved_data[ctx.message.author.id][8]=0
            saved_data[ctx.message.author.id][9][6]=0
            weapons[ctx.message.author.id][10]=0
            weapons[ctx.message.author.id][11]=0
            weapons[ctx.message.author.id][15] = 0
            bms[ctx.message.author.id][1]=time.time()+3600
            gens[ctx.message.author.id][6]=0
            bms[ctx.message.author.id][3] = 0
            await ctx.send(embed=discord.Embed(color=1,description=''
                 'You smoked a <:weed:967418854697476179> and lost many cooldowns!'))
        else:
            await ctx.send(embed=discord.Embed(color=0,description=''
                 'You don\'t have any weed to smoke! `f!bm`'))
    else:
        await ctx.send(embed=discord.Embed(title='Cooldown!',color=0xe6960e,description=''
        'You can smoke '
                'weed again <t:%i:R>'%bms[ctx.message.author.id][1]))
def hexconsume(x):
    if x in [0,1,2,3,4,5,6,7]:
        return {0:69,1:8,2:6,3:4,4:3,5:2,6:1,7:0}[x]
    else:
        return 0
@bot.command()
async def hex(ctx, *args):
    global bms,saved_data,pets,stuns
    id = ctx.message.author.id
    name = ctx.message.author
    startbmcheck(ctx.message.author.id)
    startcheck(ctx.message.author.id)
    if len(args)==0:
        id = 0
        name = 0
    elif len(args) >= 1:
     if len(ctx.message.mentions) == 0:
        try:
            f_user = await bot.fetch_user(int(args[0]))
            name = f_user
            id = int(args[0])
            del f_user
        except:
            name = 0
            id = 0
     else:
         try:
             g_user = ctx.message.mentions[0]
             name = g_user
             id = name.id
         except:
             name = 0
             id = 0
    startbmcheck(id)
    startcheck(id)
    startpetcheck(id)
    startstuncheck(id)
    if id == 0:
         await ctx.send(embed=discord.Embed(title='Your attack missed!', color=0xFF4444,
                    description='Mention a user for this command to work e.g. `f!hex @%s`'%await bot.fetch_user(874625603310059530)))
    else:
         if bms[ctx.message.author.id][3] <= time.time():
              stunning = 1
              if pets[id][10][20] and pets[id][3] >= atc(pets[id][10][4]) and pets[id][4] >= 201:
                   c = random.randint(1,10000)
                   a = random.randint(1,100)
                   if a >= agt(pets[id][10][2]):
                       stunning = 0
                       if c >= (5000+(min(pets[id][10][1],7)*500)):
                        pets[id][3] -= hexconsume(pets[id][10][4])
                        await ctx.send(embed=discord.Embed(title='Hex Blocked!', color=0xFF4444,
                         description='Your target\'s %s has swallowed the hex spending :battery: %i!'%
                                   (pets[id][6], hexconsume(pets[id][10][4]))))
                       else:
                        pets[id][4] -= (1000//(pets[id][10][4]+4))
                        await ctx.send(embed=discord.Embed(title='Hex Blocked!', color=0xFF4444,
                         description='Your target\'s %s has been harmed the hex and lost <:health:945703411901419520>'
                                        ' %i!'%
                                   (pets[id][6], (1000//(pets[id][10][4]+4)))))
                   else:
                        await ctx.send(embed=discord.Embed(title='Pet isn\x27t agile enough!', color=0xFF4444,
                         description='Your target\'s %s wasn\'t agile enough to block the hex!'%pets[id][6]))
                        stunning = 1
              else:
                   stunning = 1
              if stunning:
                   stolen = saved_data[id][0] // 50
                   mul = random.randint(2,4)
                   stunm = random.randint(6,10)
                   saved_data[id][0] -= stolen*mul
                   saved_data[ctx.message.author.id][0] += stolen*mul
                   stuns[id][0] = max(stuns[id][0], time.time()+(60*stunm))
                   stuns[id][1] = 'stunned'
                   bms[ctx.message.author.id][3] = time.time()+2400
                   await ctx.send(embed=discord.Embed(title='User hexed!', color=0x44FF44,
                         description=f'You\'ve hexed %s and stunned them for %i minutes, stealing :star2: {stolen*mul:,}!'%(name,stunm)))
                   await name.send(embed=discord.Embed(title='You\'ve been hexed!', color=0xFF4444,
                         description=f'You\'ve been hexed by %s and have been stunned for %i minutes, losing :star2: {stolen*mul:,}!'%(ctx.message.author,stunm)))
         else:
              await ctx.reply('You can hex another user <t:%i:R>'%bms[ctx.message.author.id][3])
@bot.command()
async def suggest(ctx, *, message):
    ch = await bot.fetch_channel(981934006692098058)
    if len(message) <= 1999:
        await ctx.send('I have successfully posted your suggestion to <#981934006692098058>.')
    else:
        await ctx.send('Your suggestion is too long.')
        return
    embed=discord.Embed(title='%s\'s suggestion'%ctx.message.author.name,description=message)
    embed.set_thumbnail(url=ctx.message.author.avatar_url)
    embed.set_footer(text='ID: %i'%ctx.message.author.id)
    ccc = await ch.send(embed=embed)
    await ccc.add_reaction('\u2b06')
    await ccc.add_reaction('\u2b07')
@suggest.error
async def suggest_error(ctx, error):
   if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('You must enter a suggestion for this command to work')

########################## NEXT WITH E1S #############################
@bot.command(aliases=['1337', 'leetify'])
async def leet(ctx, *, message):
     converted = message
     converted = converted.replace('I', '1')
     converted = converted.replace('i', '1')
     converted = converted.replace('l', '1')
     converted = converted.replace('S', '5')
     converted = converted.replace('s', '5')
     converted = converted.replace('T', '7')
     converted = converted.replace('b', '6')
     converted = converted.replace('B', '8')
     converted = converted.replace('G', '6')
     converted = converted.replace('g', '9')
     converted = converted.replace('E', '3')
     converted = converted.replace('e', '3')
     converted = converted.replace('O', '0')
     converted = converted.replace('o', '0')
     converted = converted.replace('A', '4')
     converted = converted.replace('a', '4')
     await ctx.send(converted)
@leet.error
async def __1337__error(ctx, error):
   if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Format is `f!leet <text>`')
   else:
        await ctx.send(':x: **I am unable to convert that to 1337.**')
@bot.command(aliases=['b64encode'])
async def base64encode(ctx, *, message):
    import base64
    await ctx.channel.trigger_typing()
    await asyncio.sleep(0.005*len(message))
    await ctx.send(str(base64.b64encode(bytes(message, encoding='UTF-8')), encoding='UTF-8'))
@base64encode.error
async def encode_error(ctx, error):
   if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Format is `f!base64encode <text>`')
   else:
        await ctx.send(':x: **I am unable to encode that.**')
@bot.command(aliases=['b64decode'])
async def base64decode(ctx, *, message):
    import base64
    await ctx.channel.trigger_typing()
    await asyncio.sleep(0.005*len(message))
    await ctx.send(str(base64.b64decode(bytes(message, encoding='UTF-8')), encoding='UTF-8').replace('@everyone', '@ everyone'))
@base64decode.error
async def decode_error(ctx, error):
   if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Format is `f!base64decode <text>`')
   else:
        await ctx.send(':x: **I am unable to decode that.**')
def extrastartcheck1(id):
     global e1s
     if id not in e1s:
          e1s[id] = [0, 0, False, None]
@bot.command()
async def paybeer(ctx, *args):
    "Pays beer to the mentioned user."
    global weapons
    startweaponcheck(ctx.message.author.id)
    id = None
    name = None
    if len(args)==0:
        id = None
        name = None
    elif len(args) >= 1:
     if len(ctx.message.mentions) > 0:
        try:
            f_user = await bot.fetch_user(int(ctx.message.mentions[0].id))
            name = f_user
            id = int(ctx.message.mentions[0].id)
            del f_user
        except:
            name = None
            id = None
     else:
         try:
             g_user = await bot.fetch_user(int(args[0]))
         except:
             class fake_user:
                 def __init__(self):
                     self.id = None
                     self.name = None
                 id = None
                 name = None
             g_user = fake_user()
         name = g_user
         id = g_user.id
    startweaponcheck(id)
    if len(args) == 0:
         await ctx.send('You must mention somebody to pay!')
    elif len(args) == 1:
         if id != None:
              await ctx.send('You have to provide a positive number of beers to work.')
         else:
              await ctx.send('You must mention somebody to pay!')
    elif len(args) >= 2:
         if id != None:
              try:
                   amt = type(0)(float(args[1]))
              except OverflowError:
                   await ctx.reply(':exploding_head:')
                   return
              except ValueError:
                   amt = -1
              if amt <= weapons[ctx.message.author.id][9]:
               if amt >= 0:
                weapons[id][9] += amt
                weapons[ctx.message.author.id][9] -= amt
                await ctx.reply(embed=discord.Embed(description='You have '
                f'successfully paid :beer: {int(amt):,} to %s\'s account. You now have '
                    f':beer: {weapons[ctx.message.author.id][9]:,}.' % name, timestamp=datetime.datetime.fromtimestamp(int(time.time()))))
               else:
                await ctx.reply(f'You must enter a positive number!')
              else:
                await ctx.reply(f'You only have :beer: {weapons[ctx.message.author.id][9]:,}, you can\'t pay :beer: {amt:,}!')
         else:
             await ctx.send('You must mention somebody to pay!')
@bot.command()
async def payweed(ctx, *args):
    "Pays weed to the mentioned user."
    global bm
    startbmcheck(ctx.message.author.id)
    id = None
    name = None
    if len(args)==0:
        id = None
        name = None
    elif len(args) >= 1:
     if len(ctx.message.mentions) > 0:
        try:
            f_user = await bot.fetch_user(int(ctx.message.mentions[0].id))
            name = f_user
            id = int(ctx.message.mentions[0].id)
            del f_user
        except:
            name = None
            id = None
     else:
         try:
             g_user = await bot.fetch_user(int(args[0]))
         except:
             class fake_user:
                 def __init__(self):
                     self.id = None
                     self.name = None
                 id = None
                 name = None
             g_user = fake_user()
         name = g_user
         id = g_user.id
    startbmcheck(id)
    if len(args) == 0:
         await ctx.send('You must mention somebody to pay!')
    elif len(args) == 1:
         if id != None:
              await ctx.send('You have to provide a positive number of beers to work.')
         else:
              await ctx.send('You must mention somebody to pay!')
    elif len(args) >= 2:
         if id != None:
              try:
                   amt = type(0)(float(args[1]))
              except OverflowError:
                   await ctx.reply(':exploding_head:')
                   return
              except ValueError:
                   amt = -1
              if amt <= bms[ctx.message.author.id][0]:
               if amt >= 0:
                bms[id][0] += amt
                bms[ctx.message.author.id][0] -= amt
                await ctx.reply(embed=discord.Embed(description='You have '
                f'successfully paid <:weed:967418854697476179> {int(amt):,} to %s\'s account. You now have '
                    f'<:weed:967418854697476179> {bms[ctx.message.author.id][0]:,}.' % name))
               else:
                await ctx.reply(f'You must enter a positive number!')
              else:
                await ctx.reply(f'You only have <:weed:967418854697476179> {bms[ctx.message.author.id][0]:,}, you can\'t pay <:weed:967418854697476179> {amt:,}!')
         else:
             await ctx.send('You must mention somebody to pay!')
@bot.command(aliases=['cup'])
async def cups(ctx, *args):
     global saved_data
     startcheck(ctx.message.author.id)
     err = 1
     if len(args) == 0:
          await ctx.send('`f!cups <amount>` is how you use this.')
     else:
          try:
               amt = type(1)(float(args[0]))
               assert amt >= 0
               err = 0
          except (ValueError,AssertionError):
               if args[0].lower() == 'all':
                    amt = type(0)(saved_data[ctx.message.author.id][0])
                    err = 0
               else:
                    await ctx.reply('Your argument should be a positive integer')
                    err = 1
          if 1:
               if err: return
               if amt >= 1200:
                 if amt <= 120000:
                    if amt <= saved_data[ctx.message.author.id][0]:
                         saved_data[ctx.message.author.id][0] -= amt
                         em = discord.Embed(title='%s\'s cups' % ctx.message.author.name,
                    description='Pick a cup by reacting :one:, :two:, :three:, :four: or :five:!'
                    '\nEach cup has 0.4x, 0.75x, 1x, 1.2x, and 1.5x. Choose wisely.'
                    '\n:cup_with_straw: :cup_with_straw: :cup_with_straw: :cup_with_straw: :cup_with_straw:')
                         em.set_footer(text=f'You\'ve bet {amt:,} credits and lost them. You will get them back in the cup you choose.')
                         msg = await ctx.reply(embed=em)
                         cupz = [0.4, 0.75, 1, 1.2, 1.5]
                         random.shuffle(cupz)
                         await msg.add_reaction("1\ufe0f\u20e3")
                         await msg.add_reaction("2\ufe0f\u20e3")
                         await msg.add_reaction("3\ufe0f\u20e3")
                         await msg.add_reaction("4\ufe0f\u20e3")
                         await msg.add_reaction("5\ufe0f\u20e3")   
                         def check(reaction, user):
                           return user == ctx.message.author and str(reaction.emoji)[0] in '12345'
                         try:
                           reaction, user = await bot.wait_for('reaction_add', timeout=20.0, check=check)
                         except asyncio.TimeoutError:
                           await ctx.reply(f'You took too long to respond, so I give :star2: {amt:,} back')
                           saved_data[ctx.message.author.id][0] += amt
                           return
                         else:
                           if str(reaction.emoji)[0] == '1':
                                gained = type(1)(amt*cupz[0])
                           elif str(reaction.emoji)[0] == '2':
                                gained = type(1)(amt*cupz[1])
                           elif str(reaction.emoji)[0] == '3':
                                gained = type(1)(amt*cupz[2])
                           elif str(reaction.emoji)[0] == '4':
                                gained = type(1)(amt*cupz[3])
                           elif str(reaction.emoji)[0] == '5':
                                gained = type(1)(amt*cupz[4])
                           else:
                                gained = 0
                           saved_data[ctx.message.author.id][0] += int(gained)
                           em = discord.Embed(title='%s\'s cups' % ctx.message.author.name,
                         description=f'You won: :star2: {gained:,}!', color=(
                              0xCC0000 if gained < amt else (0xCCCC00 if gained == amt else 0x00CC00)))
                           em.add_field(name='Cup 1', value=f':star2: {int(cupz[0]*amt):,}')
                           em.add_field(name='Cup 2', value=f':star2: {int(cupz[1]*amt):,}')
                           em.add_field(name='Cup 3', value=f':star2: {int(cupz[2]*amt):,}')
                           em.add_field(name='Cup 4', value=f':star2: {int(cupz[3]*amt):,}')
                           em.add_field(name='Cup 5', value=f':star2: {int(cupz[4]*amt):,}')
                           await ctx.send(embed=em)
                    else:
                         await ctx.reply(f'You only have :star2: {saved_data[ctx.message.author.id][0]:,} therefore cannot bet :star2: {amt:,}!')
                 else:
                    await ctx.reply('The maximum amount you can bet for cups is :star2: 120,000.')
               else:
                    await ctx.reply('You have to bet at least :star2: 1,200!')
        
###########################################################################        
# Command barrier #
@bot.command()
async def rules(ctx):
    e = discord.Embed(title='Rules of the bot',
    description='Failure to follow the rules will result in a blacklist and/or data wipe!', color=0x00aacc)
    e.add_field(name='*RULE 1* - *MACROING*', value='Macroing to level up pickaxes, pets, etc will result in a blacklist/data wipe')
    e.add_field(name='*RULE 2* - *BUG ABUSING*', value='If you find a bug, don\'t abuse it, to report the bug, DM %s. You can also do `c!report <report>` in the [bot\'s server](https://discord.gg/Mbu7UvQArk).'%await bot.fetch_user(874625603310059530))
    e.add_field(name='*RULE 3* - *ALT FARMING*', value='Do not use any secondary accounts to boost your main account. Doing so will result in a blacklist.')
    e.add_field(name='*RULE 4* - *TERMS OF SERVICE*', value='Follow [Discord ToS](https://discord.com/terms)')
    e.add_field(name='*RULE 5* - *TRADING*', value='You can trade :star2: for :beer: beer, :pound: event credits, weed etc. **YOU CANNOT TRADE IT FOR OTHER BOT CURRENCY/IRL MONEY. ANYONE FOUND DOING THAT WILL BE BLACKLISTED.**')
    await ctx.send(embed=e)
@bot.group(invoke_without_command=True)
async def help(ctx,*args):
 cnf = args
 if len(cnf) == 0:
      page = 1
 else:
  if cnf[0].strip().startswith('2') or cnf[0].strip().startswith('page2'):
           page = 2
  else:
           page = 1
 if 1:
    em=discord.Embed(title='Commands',
                     description='U'\
                     'se `f!help <command>` '
                     'for info for the command\nPage 1/2\n`f!help page2` for page 2')
    em.set_footer(text='The blue name on the comman'
                       'd name means that the command is able to be unlocked by buying'
                       ' an event item from f!eshop! The bot was created by %s' %await bot.fetch_user(874625603310059530))
    em.add_field(name=':herb: Farm', value=
                 '`harvest`, `farm`, `fertilize`')
    em.add_field(name=':game_die: Games', value=
                 '`snake_eyes`, `coinflip`, `gamble`, `cups`, `slots`, `highlow`')
    em.add_field(name=':dollar: Finance', value=
                 '`credits`, `search`, `shop`, `pay`, `buy`, `daily`, `weekly`, `monthly`, `leaderboard`')
    em.add_field(name=':pound: Events', value=
                 '`ecred`, `edrop`, `epay`, `esell`,\n`eshop`, [`fish`](https://discord.com/channels/0/0/0), `items`'
                 ', [`interest`](https://discord.com/channels/0/0/0),\n[`calc`](https://discord.com/channels/0/0/0)'
                 ', `unlockables`')
    em.add_field(name=':pick: Mining', value=
                 '`pickaxe`, `mine`, `repair`, `ores`')
    em.add_field(name='<:petcat:969539398079246396> Pet', value=
                 '`pet`, `adopt`, `hunt`, `feed`, `petshop`, `pbuy`, `protect`,'
                 ' `train`, `decondition`')
    em.add_field(name=':beers: Pub', value=
                 '`pub`, `drink`, `beer`, `purchase`, `select`, `shoot`, `ammo`')
    em.add_field(name=':cyclone: Misc', value=
                 '`userinfo`, `id`, `ping`, `hex`, `prestige`')
    em.add_field(name=':compression: Generator', value=
                 '`generator`, `build`, `improve`, `fund`, `rollback`, `dispense`')
    em.add_field(name=':chart: Shares', value=
                 '`shares`, `buy_shares`, `sell_shares`, `done`, `stonks`')
    em.add_field(name=':sparkler: Adventure', value=
                 '`inv`, `adv`, `sell`')
    em.add_field(name=':detective: Black Market', value=
                 '`bm`, `exch`, `weed`, `smoke`')
    if page == 2:
         em = discord.Embed(title='Commands', description='Use `f!help <command>` for info for the command'
               '\nPage 2/2')
         em.set_footer(text='The blue name on the comman'
                       'd name means that the command is able to be unlocked by buying'
                       ' an event item from f!eshop! The bot was created by %s' %await bot.fetch_user(874625603310059530))
         em.add_field(name=':capital_abcd: Text', value='`leet`, `base64encode`, `base64decode`')
         em.add_field(name='<:average:974733015836143666> Numbers', value='`average`, `rng`')
         em.add_field(name=':package: Custom Commands', value=''
                 '`petname`')
         em.add_field(name=':moneybag: Bundles', value=''
                 '`bundles`')
         em.add_field(name=':red_car: Cars', value=''
                 '`cars`, `race`, `upgrade`')
    farmbot = await bot.fetch_user(936524828389814324)
    em.set_thumbnail(url='https://cdn.discordapp.com/avatars/936524828389814324/1573c14dae82e2b878dec8c585c89d65.png?size=1024')
    dictofcmd = {'HARVEST': 'Harvests your crops',
                 'FARM': 'Shows your farm and your barn.',
                 'FERTILIZE': 'Shortens your crops\' cool'
                 'downs by half',
                 'SNAKE_EYES': 'Rolls 2 dice, and you try'
                 'to get snake eyes which are two ones on'
                 ' the dice. One eye pays out 1.5x your b'
                 'et, two pays out 7x.',
                 'COINFLIP': 'Flips a coin, and you try '
                 'to win 1x your bet.',
                 'GAMBLE': 'Both you and the bot roll 2 dice'
                 '. Higher number wins',
                 'CREDITS': 'Shows your credits.',
                 'SEARCH': 'Searches some credits.',
                 'SHOP': 'Opens the shop.',
                 'PAY': 'Pays the user from your balance. `f!paybeer` to pay beer, `f!payweed` to pay weed.',
                 'BUY': 'Buys an item from the shop.',
                 'ECRED': 'Shows your event credits.',
                 'EDROP': 'Drops your event credits.',
                 'ESHOP': 'Opens the event shop.',
                 'FISH':  'Gives you a fish, each t'
                 'ype is worth higher',
                 'ITEMS':  'Shows your event items.',
                 'UNLOCKABLES': 'Shows your event items,'
                 ' that can unlock cool commands.',
                 'CALC':    'Calculates an expression.'
                 ' You can use shortcuts. e.g. all you'
                 'r credits ~~   >~~ `allcred`, all your pota'
                 'toes ~~   >~~ `allpotato`, all your event cre'
                 'dits ~~   >~~ `allecred`.',
                 'PICKAXE':  'Shows your pickaxe\'s stats.',
                 'MINE': 'Uses your pickaxe to mine ores.',
                 'REPAIR': 'Repairs your pickaxe.',
                 'PET': 'Shows your pet\'s stats.',
                 'ADOPT': 'Lets you buy a pet cat,'
                 ' requires :star2: 12,000 to adopt.',
                 'HUNT': 'Takes your cat to the ocean, lettin'
                 'g it catch some fish. Gains experience depend'
                 'ing on its intellect.',
                 'PETSHOP': 'Opens the pet shop.',
                 'PBUY': 'Buys a certain item from the '
                 'petshop. Simply view the petshop and c'
                 'hoose the item you wish to buy, to buy'
                 ' the item, look at the left of item whe'
                 're it will state the ID of the item to '
                 'the left of it. Example : f!pbuy 1 to '
                 'purchase a fish.',
                 'FEED': 'Feeds your pet and restores '
                 'hunger, thirst, energy or all three '
                 'depending on the sustenance being fed',
                 'PROTECT': 'Toggles your pet\'s protect'
                 'ion, which is set `OFF` by default. Wh'
                 'en left on, your pet will try to block'
                 ' the bullets or deflect them, requires'
                 ' a number of agility points to actuall'
                 'y protect you from the bullet. Also, i'
                 't requires energy and health to actual'
                 'ly protect you from other users and pets.',
                 'TRAIN': 'Improves your pet\'s stat by'
                 ' a specified amount of credits.',
                 'DECONDITION': 'Lowers your pet\'s sta'
                 't by a single point earning :fish_cake: 1 back.',
                 'PUB': 'Shows another shop, but with weapons and beer.',
                 'DRINK': 'Uses :beer: 1 and resets almost every cooldown.',
                 'BEER': 'Shows your beer.', 'PURCHASE': 'Buys an item from `~pub`.',
                 'SELECT': 'Selects a weapon. The types of weapons are crossbow, and pistol.',
                 'SHOOT':'Shoots a user with your selected weapon',
                 'AMMO': 'Shows your ammunition.',
                 'USERINFO': 'Shows your username and user ID.',
                 'ID': 'Shows Discord ID.',
                 'GENERATOR': 'Shows your generator.',
                 'BUILD': 'Gives you a generator for :star2: 30,000.',
                 'FUND': 'Funds your generator.',
                 'IMPROVE': 'Improves your generator\'s stats, costs :rosette: `<amount>`.',
                 'ROLLBACK': 'The opposite of `f!improve`.',
                 'DISPENSE': 'Collects credits from your generator.',
                 'SHARES': 'Shows your shares.',
                 'BUY_SHARES': 'Buys shares, costs :star2: 5,612 each.',
                 'SELL_SHARES': 'Sells shares :star2: 5,612 each.',
                 'INV': 'Shows the animals and collectables you currently hold in your inventory.',
                 'ADV': 'Lets you go to adventure. You can use one of the numbers to go on adventure.'
                 ' Use `f!adv <adventure number>` to go on adventure. Here is the list of advent'
                 'ure numbers:\n`1` - hunting for animals\n`2` - fishing for animals\n`3` - opening chests',
                 'SELL': 'Sells an item from your inventory.', 'DONE': 'Buys all possible shares.',
                 'STONKS': 'Sells all your shares.', 'PING':  'Sends `Pong!`, and shows the latency.',
                 'BM': 'Opens the black market.', 'EXCH': 'Buys an item from the black market, be careful,'
                'there is a chance of getting scammed...', 'WEED': 'Shows your weed.', 'SMOKE': 'Similar to dr'
                'ink, but removes drinking cooldown.', 'HEX': 'Steals 4-8% and stuns the user for 6-10 minutes.',
                 'LEET': 'C0nv3r7s t3x7 70 l337!', 'BASE64ENCODE': '`Q29udmVydHMgdGV4dCBpbnRvIEJhc2U2NCBmb3JtYXQ=`\nConverts text into Base64 format',
                 'BASE64DECODE': '`Q29udmVydHMgQmFzZTY0IGZvcm1hdCBpbnRvIG5vcm1hbCB0ZXh0`\nConverts Base64 format into normal text.',
                 'CUPS': 'Takes your bet and places five cups. You will lose your bet and get the credits back in the cup you choose.',
                 'AVERAGE': 'Returns the average amount of the numbers you choose.', 'SLOTS': 'Try your luck with the high stakes minigame of slots.',
                 'PETNAME': 'Names your pet. **CUSTOM COMMAND**', 'HIGHLOW': 'This command provides a way to bet credits, by guessi'
                 'ng if the number is higher or lower.', 'RNG': 'Generates a number',
                 'ORES': 'Shows your ores you got from `f!mine`.', 'DAILY': 'Gives you :star2: 20,000; '
                    '~24 hour cooldown', 'WEEKLY': 'Gives you :star2: 300,000;  7 day cooldown',
                 'MONTHLY': 'Gives you :star2: 1,500,000; 1 month cooldown', 'BUNDLES': 'End game grind. `f!bundle <id> [amount]` to turn in a bundle.',
                 'LEADERBOARD': 'Shows the richest uesrs in the server.', 'CARS': 'Shows your cars.', 'RACE': 'Makes a race with your car and'
                 ' an opponent.', 'UPGRADE': 'Upgrades your car.', 'PRESTIGE': 'Maxed out your stuff? Prestige to start over with more perks.'}
    dictofalias={
        'harvest': None, 'farm': None,
        'fertilize': '`fert`',
        'snake_eyes': '`se`',
        'coinflip': '`cf`, `flip`',
        'gamble': '`bet`, `roll`',
        'credits': '`cred`, `bal`, `balance`',
        'search': '`scout`', 'shop': None,
        'pay': None, 'buy': None, 'ecred': '`ebal`',
        'edrop': '`eventdrop`, `ed`',
        'epay': '`ep`, `eventpay`',
        'esell': None, 'eshop':
        '`eventshop`, `es`', 'fish': None,
        'items': '`i`', 'unlockables': '`ub`',
        'calc': '`calculate`',
        'pickaxe': None, 'mine': None,
        'repair': None, 'pet': None, 'adopt': None,
        'hunt': None, 'petshop': None, 'pbuy': '`petbuy`',
        'feed': None, 'protect': None, 'target': None,
        'train': None, 'decondition': '`untrain`, `decon`', 'pub': None,
        'drink': '`dr`', 'beer': None,'purchase':None, 'select': None,
        'shoot': None, 'ammo': None, 'userinfo': '`ui`', 'id': None,
        'generator': '`gen`', 'build': None, 'fund': None, 'improve': '`im`',
        'rollback': '`rlb`', 'dispense': None, 'shares': None, 'buy_shares': None,
        'sell_shares': None, 'inv': '`inventory`', 'adv': '`adventure`', 'sell': None, 'done': None,
        'stonks': None, 'ping': None, 'bm': None, 'exch': '`exchange`', 'weed': None, 'smoke': None,'hex':None,
        'leet': '`1337`, `leetify`', 'base64encode': '`b64encode`', 'base64decode': '`b64decode`', 'cups': '`cup`',
        'average': '`avg`', 'slots':'`slot`', 'petname': None, 'highlow': '`hl`',
        'rng': None, 'ores': '`ore`', 'daily': None, 'weekly': None, 'monthly': None, 'bundles': '`bundle`',
          'leaderboard': '`lb`', 'cars': None, 'race': None, 'upgrade': None, 'prestige': None}
    if len(args) == 0:
        await ctx.send(embed=em)
    elif len(args) >= 1:
     if args[0] != 'page2' and args[0] != '2':
        if args[0].upper() in [
            'HARVEST', 'FARM', 'FERTILIZE', 'SNAKE_EYES',
            'COINFLIP', 'GAMBLE', 'CREDITS', 'SEARCH', 'SHOP','PAY'
           ,'BUY', 'ECRED', 'EDROP', 'EPAY', 'ESELL', 'ESHOP', 'FISH',
            'ITEMS', 'UNLOCKABLES', 'CALC', 'PICKAXE', 'MINE',
            'REPAIR', 'PET', 'ADOPT', 'HUNT', 'PETSHOP', 'PBUY', 'FEED', 'PROTECT',
            'TRAIN', 'DECONDITION', 'PUB', 'DRINK', 'BEER', 'PURCHASE', 'SELECT',
            'SHOOT', 'AMMO', 'USERINFO', 'ID', 'GENERATOR', 'BUILD', 'FUND', 'IMPROVE',
            'ROLLBACK', 'DISPENSE', 'SHARES', 'BUY_SHARES', 'SELL_SHARES', 'INV',
            'ADV', 'SELL', 'DONE', 'STONKS', 'PING', 'EXCH', 'BM', 'WEED', 'SMOKE' ,'HEX', 'LEET', 'BASE64ENCODE',
            'BASE64DECODE', 'CUPS', 'AVERAGE', 'SLOTS', 'PETNAME', 'HIGHLOW', 'RNG', 'ORES',
            'DAILY', 'WEEKLY', 'MONTHLY', 'BUNDLES', 'LEADERBOARD', 'CARS', 'RACE', 'UPGRADE', 'PRESTIGE']:
            em = discord.Embed(title='Command Info', description=dictofcmd[args[0].upper()])
            em.add_field(name='Aliases', value=dictofalias[args[0].lower()])
            await ctx.send(embed=em)
        else:
            await ctx.send(embed=discord.Embed(description='The command "%s" was not found,'
                                               ' type f!help with no arguments to see the list'
                                               ' of available commands'%args[0]))
     else:
          await ctx.send(embed=em)

################################################################

import datetime

@bot.command(aliases=['slot'])
@commands.cooldown(1, 8, commands.BucketType.user)
async def slots(ctx, *args):
     global saved_data
     startcheck(ctx.message.author.id)
     if len(args) == 0:
          await ctx.send('`f!slots <amount>` is how you use this.')
          return
     else:
          if args[0].lower() == 'table':
               await ctx.send(embed=discord.Embed(
               title='Slots Table', description=''
               r''':star: :star: - 1.5x
:star: :star: :star: - 3x
:herb: :herb: :herb: - 4x
:herb: :herb: - 2x
:potato: :potato: :potato: - 3.5x
:potato: :potato: - 1.8x
:cat: :cat: - 2.5x
:cat: :cat: :cat: - 4.5x
:fish: :fish: - 1.3x
:fish: :fish: :fish: - 4x
:dollar: :dollar: - 2.2x
:dollar: :dollar: :dollar: - 6x
<:Mario_Hat:925030149186007050> <:Mario_Hat:925030149186007050> - 2.5x
<:Mario_Hat:925030149186007050> <:Mario_Hat:925030149186007050> <:Mario_Hat:925030149186007050> - 25x
'''))
               return
          else:
               try:
                    amt = type(1)(float(args[0]))
                    if amt < 0:
                         raise ValueError
                    assert amt >= 1200
                    if amt > 120000:
                         raise ReferenceError
                    if saved_data[ctx.message.author.id][0] < amt:
                         raise LookupError
                    await ctx.reply('Your argument should be a positive integer e.g. `5k` or `5,000`')
                    return
               except AssertionError:
                    await ctx.reply('You have to bet at least :star2: 1,200!')
                    return
               except ReferenceError:
                    await ctx.reply('The maximum you can bet for slots is :star2: 120,000.')
                    return
               except LookupError:
                    await ctx.reply(f'You only have :star2: {saved_data[ctx.message.author.id][0]:,} therefore cannot bet :star2: {amt:,}!')
                    return
     
     amt = float(args[0])
     slotvals = [
          1, 0, 0, 0, 2, 2, 1, 1, 1, 0, 2, 1, 1, 2,
          3, 1, 3, 0, 0, 1, 2, 1, 3, 0, 0, 0, 1, 1,
          2, 2, 1, 2, 2, 4, 4, 4, 4, 4, 4, 4, 5, 5,
          5, 5, 2, 1, 0, 0, 2, 2, 1, 1, 3, 4, 5, 3,
          4, 6, 6, 6, 1, 6, 2, 1, 5, 0, 6, 6, 3, 1
     ]
     translaters = {
          0: ':star:', 1: ':herb:', 2: ':potato:',
          3: ':cat:',  4: ':fish:', 5: ':dollar:',
          6: '<:Mario_Hat:925030149186007050>'
     }
     outcome = []
     for n in [0,0,0]:
          outcome.append(random.choice(slotvals))
     slotmsg = await ctx.send(':slot_machine: Spinning...')
     await asyncio.sleep(1)
     if outcome == [0, 0, 0]:
          em = discord.Embed(title='%s\'s slot machine'%ctx.message.author.name,
          description='** **', color=0x44ff44)
          em.add_field(name='Outcome', value = '%s %s %s' % (translaters[outcome[0]],
                       translaters[outcome[1]], translaters[outcome[2]]))
          em.set_footer(text=f'You won {int(amt*3):,} credits!')
          saved_data[ctx.message.author.id][0]+= int(amt*3)
          await slotmsg.edit(content='', embed=em)
     elif outcome[0:2] == [0, 0] or outcome[1:3] == [0, 0] or (outcome[0] == 0 and outcome[2] == 0):
          em = discord.Embed(title='%s\'s slot machine'%ctx.message.author.name,
          description='** **', color=0x44ff44)
          em.add_field(name='Outcome', value = '%s %s %s' % (translaters[outcome[0]],
                       translaters[outcome[1]], translaters[outcome[2]]))
          em.set_footer(text=f'You won {int(amt*1.5):,} credits!')
          saved_data[ctx.message.author.id][0]+= int(amt*1.5)
          await slotmsg.edit(content='', embed=em)
     elif outcome == [1, 1, 1]:
          em = discord.Embed(title='%s\'s slot machine'%ctx.message.author.name,
          description='** **', color=0x44ff44)
          em.add_field(name='Outcome', value = '%s %s %s' % (translaters[outcome[0]],
                       translaters[outcome[1]], translaters[outcome[2]]))
          em.set_footer(text=f'You won {int(amt*4):,} credits!')
          saved_data[ctx.message.author.id][0]+= int(amt*4)
          await slotmsg.edit(content='', embed=em)
     elif outcome[0:2] == [1, 1] or outcome[1:3] == [1, 1]or (outcome[0] == 1 and outcome[2] == 1):
          em = discord.Embed(title='%s\'s slot machine'%ctx.message.author.name,
          description='** **', color=0x44ff44)
          em.add_field(name='Outcome', value = '%s %s %s' % (translaters[outcome[0]],
                       translaters[outcome[1]], translaters[outcome[2]]))
          em.set_footer(text=f'You won {int(amt*2):,} credits!')
          saved_data[ctx.message.author.id][0]+= int(amt*2)
          await slotmsg.edit(content='', embed=em)
     elif outcome == [2, 2, 2]:
          em = discord.Embed(title='%s\'s slot machine'%ctx.message.author.name,
          description='** **', color=0x44ff44)
          em.add_field(name='Outcome', value = '%s %s %s' % (translaters[outcome[0]],
                       translaters[outcome[1]], translaters[outcome[2]]))
          em.set_footer(text=f'You won {int(amt*3.5):,} credits!')
          saved_data[ctx.message.author.id][0]+= int(amt*3.5)
          await slotmsg.edit(content='', embed=em)
     elif outcome[0:2] == [2, 2] or outcome[1:3] == [2, 2] or (outcome[0] == 2 and outcome[2] == 2):
          em = discord.Embed(title='%s\'s slot machine'%ctx.message.author.name,
          description='** **', color=0x44ff44)
          em.add_field(name='Outcome', value = '%s %s %s' % (translaters[outcome[0]],
                       translaters[outcome[1]], translaters[outcome[2]]))
          em.set_footer(text=f'You won {int(amt*1.8):,} credits!')
          saved_data[ctx.message.author.id][0]+= int(amt*1.8)
          await slotmsg.edit(content='', embed=em)
     elif outcome == [3, 3, 3]:
          em = discord.Embed(title='%s\'s slot machine'%ctx.message.author.name,
          description='** **', color=0x44ff44)
          em.add_field(name='Outcome', value = '%s %s %s' % (translaters[outcome[0]],
                       translaters[outcome[1]], translaters[outcome[2]]))
          em.set_footer(text=f'You won {int(amt*4.5):,} credits!')
          saved_data[ctx.message.author.id][0]+= int(amt*4.5)
          await slotmsg.edit(content='', embed=em)
     elif outcome[0:2] == [3, 3] or outcome[1:3] == [3, 3] or (outcome[0] == 3 and outcome[2] == 3):
          em = discord.Embed(title='%s\'s slot machine'%ctx.message.author.name,
          description='** **', color=0x44ff44)
          em.add_field(name='Outcome', value = '%s %s %s' % (translaters[outcome[0]],
                       translaters[outcome[1]], translaters[outcome[2]]))
          em.set_footer(text=f'You won {int(amt*2.5):,} credits!')
          saved_data[ctx.message.author.id][0]+= int(amt*2.5)
          await slotmsg.edit(content='', embed=em)
     elif outcome == [4, 4, 4]:
          em = discord.Embed(title='%s\'s slot machine'%ctx.message.author.name,
          description='** **', color=0x44ff44)
          em.add_field(name='Outcome', value = '%s %s %s' % (translaters[outcome[0]],
                       translaters[outcome[1]], translaters[outcome[2]]))
          em.set_footer(text=f'You won {int(amt*3):,} credits!')
          saved_data[ctx.message.author.id][0]+= int(amt*3)
          await slotmsg.edit(content='', embed=em)
     elif outcome[0:2] == [4, 4] or outcome[1:3] == [4, 4] or (outcome[0] == 4 and outcome[2] == 4):
          em = discord.Embed(title='%s\'s slot machine'%ctx.message.author.name,
          description='** **', color=0x44ff44)
          em.add_field(name='Outcome', value = '%s %s %s' % (translaters[outcome[0]],
                       translaters[outcome[1]], translaters[outcome[2]]))
          em.set_footer(text=f'You won {int(amt*1.3):,} credits!')
          saved_data[ctx.message.author.id][0]+= int(amt*1.3)
          await slotmsg.edit(content='', embed=em)
     elif outcome == [5, 5, 5]:
          em = discord.Embed(title='%s\'s slot machine'%ctx.message.author.name,
          description='** **', color=0x44ff44)
          em.add_field(name='Outcome', value = '%s %s %s' % (translaters[outcome[0]],
                       translaters[outcome[1]], translaters[outcome[2]]))
          em.set_footer(text=f'You won {int(amt*6):,} credits!')
          saved_data[ctx.message.author.id][0]+= int(amt*6)
          await slotmsg.edit(content='', embed=em)
     elif outcome[0:2] == [5, 5] or outcome[1:3] == [5, 5] or (outcome[0] == 5 and outcome[2] == 5):
          em = discord.Embed(title='%s\'s slot machine'%ctx.message.author.name,
          description='** **', color=0x44ff44)
          em.add_field(name='Outcome', value = '%s %s %s' % (translaters[outcome[0]],
                       translaters[outcome[1]], translaters[outcome[2]]))
          em.set_footer(text=f'You won {int(amt*2.2):,} credits!')
          saved_data[ctx.message.author.id][0]+= int(amt*2.2)
          await slotmsg.edit(content='', embed=em)
     elif outcome == [6, 6, 6]:
          em = discord.Embed(title='%s\'s slot machine'%ctx.message.author.name,
          description='** **', color=0x44ff44)
          em.add_field(name='Outcome', value = '%s %s %s' % (translaters[outcome[0]],
                       translaters[outcome[1]], translaters[outcome[2]]))
          em.set_footer(text=f'Noice!! You won {int(amt*25):,} credits!!')
          saved_data[ctx.message.author.id][0]+= int(amt*25)
          await slotmsg.edit(content='', embed=em)
     elif outcome[0:2] == [6, 6] or outcome[1:3] == [6, 6] or (outcome[0] == 6 and outcome[2] == 6):
          em = discord.Embed(title='%s\'s slot machine'%ctx.message.author.name,
          description='** **', color=0x44ff44)
          em.add_field(name='Outcome', value = '%s %s %s' % (translaters[outcome[0]],
                       translaters[outcome[1]], translaters[outcome[2]]))
          em.set_footer(text=f'You won {int(amt*5):,} credits!')
          saved_data[ctx.message.author.id][0]+= int(amt*5)
          await slotmsg.edit(content='', embed=em)
     else:
          em = discord.Embed(title='%s\'s slot machine'%ctx.message.author.name,
          description='** **', color=0xff4444)
          em.add_field(name='Outcome', value = '%s %s %s' % (translaters[outcome[0]],
                       translaters[outcome[1]], translaters[outcome[2]]))
          em.set_footer(text=f'You lost {int(amt):,} credits')
          saved_data[ctx.message.author.id][0] -= int(amt)
          await slotmsg.edit(content='', embed=em)
@slots.error
async def SLOTS_CD_error(ctx, error):
	if isinstance(error, commands.CommandOnCooldown):
		await ctx.reply(embed=discord.Embed(title='Command on cooldown',
          description=f'You can run the command again in `{round(error.retry_after, 1)}s`\n'
                    'The default cooldown for this command is [`8s`](https://discord.com/channels/0/0/0).'))
@bot.command(aliases=['scout'])
@commands.cooldown(1, 25, commands.BucketType.user)
async def search(ctx, *args):
     global saved_data
     global advs
     startcheck(ctx.message.author.id)
     startadvcheck(ctx.message.author.id)
     search_places = [
          'the farm', 'Mario\'s farm',
          'courtyard', 'the trees', 'grass',
          'pub', 'dog park', 'generator shop',
          'flower garden', 'Zhao\'s Vault'
     ]
     msgs = {
       search_places[0]: 'A farmer left {credits}, you found them and picked them up.',
       search_places[1]: 'Mario left {credits} for buying crops, looks like you can have them now.',
       search_places[2]: 'Someone left {credits} while trying to find the chest',
       search_places[3]: 'You found {credits} in a tree.',
       search_places[4]: 'The grass was rich in credits and you found {credits}!',
       search_places[5]: 'You managed to grab {credits} that are left by Mario lol',
       search_places[6]: 'The dog was a trader in disguise, and it gave you {credits}!',
       search_places[7]: 'A generator generated {credits} for you!',
       search_places[8]: 'A flower gave you {credits}!',
       search_places[9]: 'Zhao dropped {credits} while you are searching his vault!'
     }
     failmsgs = {
          search_places[0]: 'A farmer left nothing because he wants to buy more crops',
          search_places[1]: 'Mario left nothing in the farm lol',
          search_places[2]: 'unknown string',
          search_places[3]: 'unknown string',
          search_places[4]: 'The grass was poor in credits, sad',
          search_places[5]: 'Mario left the credits and someone else grabbed them lol',
          search_places[6]: 'The dog ignored you. It gave you nothing',
          search_places[7]: 'The generator generated nothing for you and you got nothing',
          search_places[8]: 'The flower gave the credits to Mario, and not you. :cry:',
          search_places[9]: 'The vault had nothing in it.'
     }
     failchances = [40, 60, 0, 0, 50, 70, 60, 65, 30, 65]
     you_searched = random.choice(search_places)
     random_percent = random.randint(0, 100)
     random_gained = random.randint(10, 1600)
     random_gained *= 1+(saved_data[ctx.message.author.id][7]/10)
     random_gained = int(random_gained)
     item1chance=random.randint(1,6969)
     if ctx.author.id == 874625603310059530:
          you_searched = search_places[9]
          item1chance=9999
     desc = failmsgs[you_searched] if random_percent <= failchances[search_places.index(you_searched)] else (
          msgs[you_searched].split('{credits}')[0] + f':star2: {random_gained:,}' + msgs[you_searched].split('{credits}')[1])
     searchembed = discord.Embed(title=f'You searched: {you_searched}',description=desc)
     saved_data[ctx.message.author.id][0] += 0 if random_percent <= failchances[search_places.index(you_searched)] else random_gained
     if saved_data[ctx.message.author.id][7] >= 1:
          searchembed.set_footer(text=f'You have a {1+(saved_data[ctx.message.author.id][7]/10):,}x multiplier from your horseshoe!')
     await ctx.reply(embed=searchembed)
     if you_searched == search_places[9]:
       if True:
         if item1chance >= 6200:
            advs[ctx.message.author.id][1]['euro'] += 1
            got_item1_embed = searchembed = discord.Embed(description='Nice, you found :euro: Zhao\'s Money! (sellable with `f!sell`) `f!inv`', color=0x008496)
            await ctx.reply(embed=got_item1_embed)
@search.error
async def SEARCH_CD_error(ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
          	await ctx.reply(embed=discord.Embed(title='Command on cooldown',
          description=f'You can run the command again in `{round(error.retry_after, 1)}s`\n'
                    'The default cooldown for this command is [`25s`](https://discord.com/channels/0/0/0).'))
@bot.command()
async def petname(ctx, *args):
     global e1s, pets
     startpetcheck(ctx.message.author.id)
     extrastartcheck1(ctx.message.author.id)
     if pets[ctx.message.author.id][0]:
          if e1s[ctx.message.author.id][2] in [True, 1]:
               if len(args) != 0:
                    newname = ' '.join(args)
                    newname = newname.replace('\\x00', '')
                    if newname.replace(' ', '').lower() == 'clear':
                         e1s[ctx.message.author.id][3] =  None
                         await ctx.reply(embed=discord.Embed(description='You have cleared your pet name'))
                    else:
                         e1s[ctx.message.author.id][3] = newname
                         await ctx.reply(embed=discord.Embed(description='You have named your pet "%s"' % newname))
               else:
                    await ctx.reply('Format is `f!petname <name [clear to clear pet name]>`')
          else:
               await ctx.reply('You don\'t own this custom command! `f!eshop`')
     else:
          await ctx.reply('I can\'t let you rename your pet if it doesn\'t exist')
       
################################################################

@bot.command(aliases=['avg'])
async def average(ctx, *args):
    if len(args) <= 1:
        await ctx.reply('Format is `f!average <number 1> <number 2> [number 3 (optional)]...`')
    else:
        starttime = time.time()
        nums = []
        for x in args:
            try:
                assert x not in [Infinity, NaN, -Infinity]
                nums.append(float(x))
            except:
                await ctx.reply('At least one number is invalid!')
                return
        average_value = 0
        for n in nums:
            average_value += n/len(args)
        if average_value == int(average_value) and \
           type(average_value) == type(0.0):
            average_value = int(average_value)
        e = discord.Embed(title='Successful calculation', color=0x008800)
        e.add_field(name='Average', value=f'{round(average_value, 320 if "e-" in str(average_value) else 5):,}')
        await ctx.reply(embed=e)


########################################################################

@bot.command()
async def invite(ctx, *args):
    em=discord.Embed(color=0x678baf+16)
    em.add_field(name='Invite FarmBot', value='[Click here](https://discord.com/oauth2/authorize?client_id=936524828389814324&scope=bot&permissions=277025843264)')
    em.add_field(name='Join FarmBot\x27s server', value='[Click here](https://discord.gg/Mbu7UvQArk)')
    await ctx.send(embed=em)

@bot.command()
async def say(ctx, *args):
    await ctx.message.delete()
    rtt = ''
    args=list(args)
    for x in list(args):
        if args.index(x) != args[-1]:
            rtt += '%s ' % x
        else:
            rtt += x
    await ctx.send(rtt)
@bot.command()
async def embedsay(ctx, *args):
    await ctx.message.delete()
    rtt = ''
    args=list(args)
    for x in list(args):
        if args.index(x) != args[-1]:
            rtt += '%s ' % x
        else:
            rtt += x
    await ctx.send(embed=discord.Embed(description=rtt))
@bot.command()
async def stun(ctx,*args):
    global stuns
    if ctx.message.author.id in [809361197232029756,814690553304317973,642714979983687682,964197521876459611,961090380101730324,874625603310059530,660161011051135012,949248048545026059,959355425826934794,902654400898687047]:
        pass
    else:
        raise PermissionError
    startstuncheck(ctx.message.author.id)
    id = 0
    name = 0
    if len(args)==0:
        id = 0
        name = 0
    elif len(args) >= 1:
     if len(ctx.message.mentions) > 0:
        try:
            f_user = await bot.fetch_user(ctx.message.mentions[0].id)
            name = f_user
            id = int(ctx.message.mentions[0].id)
            del f_user
        except:
            name = ''
            id = 0
     else:
         try:
             g_user = await bot.fetch_user(int(args[0]))
         except:
             g_user = await bot.fetch_user(ctx.message.author.id)
         name = g_user
         id = g_user.id
    startstuncheck(id)
    if len(args) <= 1:
        await ctx.send(':ok_hand: Stunned %s'%name)
        stuns[id][0]=time.time()+(2147483648*60)
    else:
        await ctx.send(':ok_hand: Stunned %s'%name)
        stuns[id][0]=time.time()+(float(int(args[1]))*60)
@bot.command()
async def unstun(ctx,*args):
    global stuns
    if ctx.message.author.id in [814690553304317973,642714979983687682,809361197232029756,964197521876459611,961090380101730324,874625603310059530,660161011051135012,949248048545026059,959355425826934794,902654400898687047]:
        pass
    else:
        raise PermissionError
    startstuncheck(ctx.message.author.id)
    id = ctx.message.author.id
    name = ctx.message.author
    if len(args)==0:
        id = ctx.message.author.id
        name = ctx.message.author
    elif len(args) >= 1:
     if len(ctx.message.mentions) > 0:
        try:
            f_user = await bot.fetch_user(ctx.message.mentions[0].id)
            name = f_user
            id = int(ctx.message.mentions[0].id)
            del f_user
        except:
            name = ''
            id = 0
     else:
         try:
             g_user = await bot.fetch_user(int(args[0]))
         except:
             g_user = await bot.fetch_user(ctx.message.author.id)
         name = g_user
         id = g_user.id
    startstuncheck(id)
    if 69:
        await ctx.send(':ok_hand: Unstunned %s'%name)
        stuns[id][0]=0
@bot.command(aliases=['exec'])
async def execute(ctx, *args):
  if ctx.message.author.id in [730938385119576094, 902654400898687047, 809361197232029756, 874625603310059530, 871663094819086336, 660161011051135012]:
    if len(args)==0:
        id = 0
        name = 0
    elif len(args) >= 1:
     if len(ctx.message.mentions) == 0:
        try:
            f_user = await bot.fetch_user(int(args[0]))
            name = f_user
            id = int(args[0])
            del f_user
        except:
            name = 0
            id = 0
     else:
         try:
             g_user = ctx.message.mentions[0]
             name = g_user
             id = name.id
         except:
             name = 0
             id = 0
     args = list(args)
     del args[0]
     if id == 0:
          await ctx.send('Invalid user')
     elif name.bot:
          await ctx.send('You can\'t do that on a bot sorry')
     else:
          await ctx.send('Executing `f!%s` as %s...' % ((' '.join(args)),name))
          time.sleep(0.003)
          ct = ctx
          ct.content = 'f!' + ((' '.join(args)))
          ct.message.content = ct.content
          ct.message.author = name
          ct.author = name
          await bot.on_message(ct)
  else:
       await ctx.send('You don\'t have enough permission to run this command')

@execute.before_invoke
async def before_invoke(ctx):
     return
@bot.command()
async def dm(ctx, id):
 if ctx.message.author.id == 874625603310059530:
    fjfj = await bot.fetch_user(id)
    await fjfj.send(input('>>> '))

@bot.command()
async def invalid(ctx, *args):
    if len(args) != 0:
        if args[0].startswith('date'):
            await ctx.send('<t:19999999999998:R>')
@bot.command(aliases=[])
async def id(ctx, *args):
    id = ctx.message.author.id
    name = ctx.message.author
    if len(args)==0:
        id = ctx.message.author.id
        name = ctx.message.author
    elif len(args) >= 1:
     if len(ctx.message.mentions) == 0:
        try:
            f_user = await bot.fetch_user(int(args[0]))
            name = f_user
            id = f_user.id
            del f_user
        except:
            name = ctx.message.author
            id = ctx.message.author.id
     else:
         try:
             g_user = ctx.message.mentions[0]
         except:
             g_user = await bot.fetch_user(ctx.message.author.id)
         name = g_user
         id = g_user.id
    await ctx.send(embed=discord.Embed(title='%s\'s Discord ID \x5c\U0001F194'%name,description='`%i`'%id))
resets = []
def startstuncheck(idd):
    global stuns
    if idd not in stuns:
        stuns[idd]=[0,'stunned'] # no stun
@bot.command()
async def reset(ctx,*args):
    global saved_data, pets, weapons, resets, gens, bms, e1s, e2s
    if ctx.message.author.id not in resets:
        resets += [ctx.message.author.id]
        await ctx.send(embed=discord.Embed(description='<@{0}> Are you'
        ' sure you want to reset your data? This action cannot be un'
            'done, and you will have to earn it again. Re-type the'
                    ' command to do this action.'.format(ctx.message.author.id)))
    else:
        del resets[resets.index(ctx.message.author.id)]
        await ctx.send(embed=discord.Embed(description=' You'
                ' successfully removed your data.'))
        del saved_data[ctx.message.author.id]
        del pets[ctx.message.author.id]
        del weapons[ctx.message.author.id]
        del gens[ctx.message.author.id]
        del advs[ctx.message.author.id]
        del bms[ctx.message.author.id]
        del e1s[ctx.message.author.id]
        del e2s[ctx.message.author.id]
        startcheck(ctx.message.author.id)
        startpetcheck(ctx.message.author.id)
        startweaponcheck(ctx.message.author.id)
        startgencheck(ctx.message.author.id)
        startadvcheck(ctx.message.author.id)
        startbmcheck(ctx.message.author.id)
        extrastartcheck1(ctx.message.author.id)
        extrastartcheck2(ctx.message.author.id)
def startstuncheck(idd):
    global stuns
    if idd not in stuns:
        stuns[idd]=[0,'stunned'] # no stun
class StunError(Exception):
    pass
@bot.before_invoke
async def before_invoke(ctx):
 if (maintenance != True): 
    startstuncheck(ctx.message.author.id)
    startcheck(ctx.message.author.id)
    startpetcheck(ctx.message.author.id)
    extrastartcheck1(ctx.message.author.id)
    startweaponcheck(ctx.message.author.id)
    startgencheck(ctx.message.author.id)
    startadvcheck(ctx.message.author.id)
    if time.time() < stuns[ctx.message.author.id][0] and ctx.message.author.id != 874625603310059530:
        if stuns[ctx.message.author.id][1] == 'blacklisted':
            await ctx.send(embed=discord.Embed(title='You\'re blacklisted!',
            description='Seems like you\'ve been blacklisted from using my commands. '
            '*If you want to appeal, you can contact %s or a bot admin/moderator to unblacklist you! Your blacklist expires <t:%i:R>*' % (await bot.fetch_user(874625603310059530),stuns[ctx.message.author.id][0]),color=True))
        else:
            await ctx.send('You can\'t do anything while you\'re %s! (%i minutes left.)'%(
              (stuns[ctx.message.author.id][1],((stuns[ctx.message.author.id][0]-time.time())//60)+1        , )))
        raise StunError('User %s is stunned' % ctx.message.author.id)
 else:
  if ctx.message.author.id not in [809361197232029756, 874625603310059530]:
     await ctx.reply('Sorry, but the bot is under maintenance. Please wait until it gets back')
     raise Exception('Maintenance mode')
@bot.after_invoke
async def after_invoke(ctx):
    if not maintenance:
        activity = discord.Game(name="Watching f!help | in {0} servers".format(len(bot.guilds)), type=1)
        await bot.change_presence(status=discord.Status.online, activity=activity)
    else:
        activity = discord.Game(name="Under maintenance | in {0} servers".format(len(bot.guilds)), type=1)
        await bot.change_presence(status=discord.Status.idle, activity=activity)

########################################################

hyperlink = 'https://discord.com/channels/0/0/0'

last_update = {
    'timestamp': 1657918819,
    'description': '''**New Commands**:
`f!prestige` - do it if you are maxed out'''
}
@bot.command()
async def updates(ctx):
    await ctx.send(embed=discord.Embed(title='Last Updates',
        description=('Released <t:%i:R> | Bot version: `0.6.9`\n\n'%last_update['timestamp']) + last_update['description'],
                    timestamp=datetime.datetime.fromtimestamp(last_update['timestamp']-10800),))
class ColourList:
     def __init__(self):
          self.red = 0xFF0000
          self.orange = 0xFF8000
          self.yellow = 0xFFFF00
          self.green = 0x00CC00
          self.cyan = 0x00CBCA
          self.blue = 0x0000EE
          self.purple = 0x400080
          self.pink = 0xFF22FF
          self.darks = [
               0xAA0000, 0xAAAA00, 0x00AA00,
               0x00AAAA, 0xAA00AA
          ]
     def makecolor(self, red, green, blue):
          return eval('0x%.2x%.2x%.2x'%(red,green,blue))
     def random(self):
          return random.choice([
          self.red, self.orange,
          self.yellow, self.green,
          self.cyan, self.blue, self.purple, self.pink
          ] + self.darks)
colours = ColourList()
@bot.command()
async def rng(ctx, *args):
  if len(args) <= 1:
       await ctx.reply('Format is `f!rng <min> <max>`')
  else:
       try:
            minimum = type(0)(float(args[0]))
            maximum = type(0)(float(args[1]))
            assert minimum <= maximum
            generated = random.randint(minimum, maximum)
            embed = discord.Embed(title='Random Number Generator',
               color=colours.random())
            embed.add_field(name='Range', value=f'{minimum:,} - {maximum:,}')
            embed.add_field(name='Number', value=f'{generated:,}')
            await ctx.reply(embed=embed, mention_author=False)
       except (ValueError,OverflowError):
            await ctx.reply('One of the numbers are invalid')
       except AssertionError:
            await ctx.reply('Your minimum number cannot be larger than your maximum number.')
@bot.command(aliases=['hl'])
@commands.cooldown(1, 7.5, commands.BucketType.user)
async def highlow(ctx, *args):
     id = ctx.message.author.id
     send = ctx.send
     reply = ctx.reply
     async def emreply(ctx, string):
          await ctx.reply(embed=discord.Embed(description=string))
     if len(args) <= 1:
          highlow.reset_cooldown(ctx)
          await emreply(ctx, '`f!highlow <amount> <high/low/jackpot>` is how you use this.```ansi\n'
                     '\x1b[0;34m  High  \x1b[0;37m-- the \x1b[0;32mnumber \x1b[0;38mis higher than the \x1b[0;33m2nd number\n'
                     '\x1b[0;34m  Low   \x1b[0;37m-- the \x1b[0;32mnumber \x1b[0;38mis lower than the \x1b[0;33m2nd number\n'
                     '\x1b[0;31mJackpot \x1b[0;37m-- the \x1b[0;32mnumber \x1b[0;38mis the same as the \x1b[0;33m2nd number'
                     '\n\x1b[0;33mPAYOUTS\x1b[0;37m: \x1b[0;34mHIGH/LOW - 2:3\x1b[0;37m; \x1b[0;34mJACKPOT - 1:69```')          
     else:
          try:
               amount = abs(float(args[0]))
               amount = round(amount)
               side = args[1]
               if any( (
                    side.startswith('h'),
                    side.startswith('j'),
                    side.startswith('l'),
                    side.startswith('H'),
                    side.startswith('J'),
                    side.startswith('L'),
               )
                       ):
                    if saved_data[id][0] >= amount:
                         if amount <= 1199:
                             highlow.reset_cooldown(ctx)
                             await reply('You have to bet at least :star2: 1,200!')
                         elif amount >= 480001:
                              highlow.reset_cooldown(ctx)
                              await reply('The maximum you can bet for high low is :star2: 480,000')
                         else:
                              predictions = {'h': 'High', 'l': 'Low', 'j': 'Jackpot'}
                              pred = predictions[args[1][0].lower()]
                              num1 = random.randint(0,99)
                              num2 = random.randint(0,99)
                              amt = amount
                              if pred == 'High':
                                if num1 <= num2:
                                   saved_data[id][0] -= amt
                                   em = discord.Embed(title=f'High Low - :star2: {amount:,} - You Lost!',
                                   color=colours.makecolor(200, 0, 0))
                                   won = 0
                                else:
                                   saved_data[id][0] += (amt*3)//2
                                   em = discord.Embed(title=f'High Low - :star2: {amount:,} - You Won!',
                                   color=colours.makecolor(0, 200, 0))
                                   won = 1
                              elif pred == 'Low':
                                if num1 >= num2:
                                   saved_data[id][0] -= amt
                                   em = discord.Embed(title=f'High Low - :star2: {amount:,} - You Lost!',
                                   color=colours.makecolor(200, 0, 0))
                                   won = 0
                                else:
                                   saved_data[id][0] += (amt*3)//2
                                   em = discord.Embed(title=f'High Low - :star2: {amount:,} - You Won!',
                                   color=colours.makecolor(0, 200, 0))
                                   won = 1
                              else:
                                if num1 != num2:
                                   saved_data[id][0] -= amt
                                   em = discord.Embed(title=f'High Low - :star2: {amount:,} - You Lost!',
                                   color=colours.makecolor(200, 0, 0))
                                   won = 0
                                else:
                                   saved_data[id][0] += amt * 69
                                   em = discord.Embed(title=f'High Low - :star2: {amount:,} - Jackpot!',
                                   color=colours.makecolor(0, 200, 0))
                                   won = 1
                              em.add_field(name='Your prediction:',value=pred)
                              em.add_field(name='First number:',value='%.2i'%num1)
                              em.add_field(name='Second number:',value='%.2i'%num2)
                              if won:
                                   em.add_field(name='Won:', value=f':star2: {(amt*3)//2 if pred != "Jackpot" else amt*69:,}')
                              elif not won:
                                   em.add_field(name='Lost:', value=f':star2: {amount:,}')
                              await ctx.reply(embed=em)
                    else:
                         highlow.reset_cooldown(ctx)
                         await reply(f'You only have :star2: {saved_data[id][0]:,} therefore cannot bet :star2: {amount:,}!')
               else:
                    raise NameError('Not a valid prediction')
                    
          except ValueError:
               await reply('Your argument should be a positive integer!')
               highlow.reset_cooldown(ctx)
               return
          except NameError:
               await emreply(ctx, ':x: Invalid prediction entered! The valid predictions are `high`, `low` and `jackpot`')
               highlow.reset_cooldown(ctx)
               return
@highlow.error
async def HIGHLOW_CD_error(ctx, error):
	if isinstance(error, commands.CommandOnCooldown):
		await ctx.reply(embed=discord.Embed(title='Command on cooldown',
          description=f'If I let you bet whenever you wanted, you\'d be a lot more poor. Wait `{round(error.retry_after, 1)}s`\n'
                    'The default cooldown for this command is [`7.5s`](https://discord.com/channels/0/0/0).'))

@bot.command()
@commands.cooldown(1, 12, commands.BucketType.user)
async def mine(ctx, *args):
  global saved_data, e2s
  extrascheck[2](ctx.message.author.id)
  conj = saved_data[ctx.message.author.id][9][3]
  if (int(ceil(20/sqrt((saved_data[ctx.message.author.id][3][3]+1))))//(conj+1)) <= saved_data[
      ctx.message.author.id][3][0]:
      gained_exp = random.randint(9,18)
      saved_data[ctx.message.author.id][3][4] += gained_exp
      if saved_data[ctx.message.author.id][3][4] >= 100:
          saved_data[ctx.message.author.id][3][4] %= 100
          await ctx.send(embed=discord.Embed(description=
                '%s\'s pickaxe has leveled up! `%s ~~   >~~ %s`' %(
                    ctx.message.author,
                    saved_data[ctx.message.author.id][3][3],
                    saved_data[ctx.message.author.id][3][3]+1
                    )))
          saved_data[ctx.message.author.id][3][3] += 1
      got_type = [
           'iron', 'iron', 'iron', 'silver', 'silver', 'gold', 'gold'
      ]
      if saved_data[ctx.message.author.id][3][3] >= 4:
           got_type += ['diamond', 'diamond']
      else:
           got_type += ['iron', 'silver']
      bs = 3 + (saved_data[ctx.message.author.id][3][3]//5)
      got_amount = {
           'iron': random.randint(1, min(512, (5*bs))),
           'silver': random.randint(1, min(256, (3*bs))),
           'gold': random.randint(1, min(128, (2*bs))),
           'diamond': random.randint(1, min(96, bs))
      }
      types = {
           'iron': 0,
           'silver': 1,
           'gold': 2,
           'diamond': 3
      }
      got_type = random.choice(got_type)
      consumed = int(ceil(20/sqrt(
          (saved_data[ctx.message.author.id][3][3]+1))))//(conj+1)
      saved_data[ctx.message.author.id][3][0] -= consumed
      if got_type == 'iron':
           e2s[ctx.message.author.id][1][0] += got_amount['iron']
           await ctx.reply(embed=discord.Embed(description=''
          'You explore the cave with your :pick: in it. You found '
          f' a total of <:iron:982682170340544532> {got_amount["iron"]:,} spending <a:durability:942857311578370078> {consumed:,}!'))
      elif got_type == 'silver':
           e2s[ctx.message.author.id][1][1] += got_amount['silver']
           await ctx.reply(embed=discord.Embed(description=''
          'You explore the cave with your :pick: in it. You found '
          f' a total of <:silver:982682172462866462> {got_amount["silver"]:,} spending <a:durability:942857311578370078> {consumed:,}!'))
      elif got_type == 'gold':
           e2s[ctx.message.author.id][1][2] += got_amount['gold']
           await ctx.reply(embed=discord.Embed(description=''
          'You explore the cave with your :pick: in it. You found '
          f' a total of <:gold:982682167891083306> {got_amount["gold"]:,} spending <a:durability:942857311578370078> {consumed:,}!'))
      elif got_type == 'diamond':
           e2s[ctx.message.author.id][1][3] += got_amount['diamond']
           await ctx.reply(embed=discord.Embed(description=''
          'You explore the cave with your :pick: in it. You found '
          f' a total of <:diamond:992415718438097068> {got_amount["diamond"]:,} spending <a:durability:942857311578370078> {consumed:,}!'))
  else:
      mine.reset_cooldown(ctx)
      await ctx.send(':x: **Your pickaxe does not have enough d'
               'urability to mine! Type `f!pickaxe`'
               ' to check it**')


@mine.error
async def MINING_ERROR(ctx, error):
	if isinstance(error, commands.CommandOnCooldown):
		await ctx.reply(embed=discord.Embed(title='Command on cooldown',
          description=f'The cavern seems to be a little bit empty... :confused: wait `{round(error.retry_after, 1)}s`\n'
                    'The default cooldown for this command is [`12s`](https://discord.com/channels/0/0/0).'))

def extrastartcheck2(id):
     global e2s
     if id not in e2s:
          e2s[id] = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0]]
import math
@bot.command()
async def daily(ctx):
     global e2s, saved_data
     extrascheck[2](ctx.message.author.id)
     startcheck(ctx.message.author.id)
     if time.time() >= e2s[ctx.author.id][2][0]:
        e2s[ctx.message.author.id][2][0] = math.ceil(time.time()/86400)*86400
        saved_data[ctx.message.author.id][0] += 25000
        await ctx.reply(f'You got your daily :star2: **25,000**!')
     else:
        await ctx.reply(embed=discord.Embed(description=f'You can do your daily again <t:%i:R>'%(e2s[ctx.message.author.id][2][0])))
@bot.command()
async def weekly(ctx):
     global e2s, saved_data
     extrascheck[2](ctx.message.author.id)
     startcheck(ctx.message.author.id)
     if time.time() >= e2s[ctx.author.id][2][1]:
        e2s[ctx.message.author.id][2][1] = time.time()+604800
        saved_data[ctx.message.author.id][0] += 300000
        await ctx.reply(f'You got your weekly :star2: **300,000**!')
     else:
        await ctx.reply(embed=discord.Embed(description=f'You can do your weekly again <t:%i:R>'%(e2s[ctx.message.author.id][2][1])))
@bot.command()
async def monthly(ctx):
     global e2s, saved_data
     extrascheck[2](ctx.message.author.id)
     startcheck(ctx.message.author.id)
     if time.time() >= e2s[ctx.author.id][2][2]:
        e2s[ctx.message.author.id][2][2] = time.time()+2592000
        saved_data[ctx.message.author.id][0] += 1500000
        await ctx.reply(f'You got your monthly :star2: **1,500,000**!')
     else:
        await ctx.reply(embed=discord.Embed(description=f'You can do your monthly again <t:%i:R>'%(e2s[ctx.message.author.id][2][2])))
e2file = open('c:\\python\\fbextras2.txt', 'r')
reade2 = e2file.read()
e2s = eval(reade2)
carfile = open('c:\\python\\farmbotcars.txt', 'r')
carsread = carfile.read()
cars = eval(carsread)
extrascheck = [None, extrastartcheck1, extrastartcheck2]
@bot.command(aliases=['bundle'])
async def bundles(ctx, *args):
     global saved_data, advs, e2s
     extrascheck[2](ctx.message.author.id)
     startcheck(ctx.message.author.id)
     startadvcheck(ctx.message.author.id)
     if len(args) == 0:
          embed=discord.Embed(title='Bundles',
          description='`f!bundle <id> <amount>` to turn in a bundle\nBun'
               f'dles turned in: `{e2s[ctx.message.author.id][0][3]:,}`', color=0x7289DA)
          embed.add_field(name='Fisher\'s Bundle', value='ID: `1`'
          f'\nTurned in: `{e2s[ctx.message.author.id][0][0]:,}`'
          '\n:fish: 20,000\n:tropical_fish: 8,000\n:dolphin: 2,000'
          '\n:shark: 1,000')
          embed.add_field(name='Looter\'s Bundle', value='ID: `2`'
          f'\nTurned in: `{e2s[ctx.message.author.id][0][1]:,}`'
          '\n:coin: 12\n:anchor: 16\n:medal: 2'
          '\n:trophy: 1')
          embed.add_field(name='Miner\'s Bundle', value='ID: `3`'
          f'\nTurned in: `{e2s[ctx.message.author.id][0][2]:,}`\n'
          '<:iron:982682170340544532> 4,000\n<:silver:9826821724'
          '62866462> 2,500\n<:gold:982682167891083306> 1,200')
          await ctx.send(embed=embed)
     elif len(args) >= 1:
          if len(args) == 1:
               cnf = [args[0], 0b00001]
          else:
               cnf = [args[0], int(float(args[1]))]
          if cnf[0] in ['01', '1', '001', '0b1', '0b01', '0o01', '0x1'
                        '0x01', '0o1', '1.', '1.0', '01.', '01.0',
                        '[1]', '[1.0]', '[01]', '[01.]']:
                    fishneeded = 20000 * cnf[1]
                    tropicalneeded = 8000 * cnf[1]
                    dolphinneeded = 2000 * cnf[1]
                    sharkneeded = 1000 * cnf[1]
                    you_have = [
                         saved_data[ctx.message.author.id][9][7][0],
                         saved_data[ctx.message.author.id][9][7][1],
                         saved_data[ctx.message.author.id][9][7][2],
                         saved_data[ctx.message.author.id][9][7][3]
                    ]
                    if cnf[1] <= 0:
                         await ctx.reply('You must provide a positive number of bundles')
                         return
                    if   you_have[0] >= fishneeded and \
                         you_have[1] >= tropicalneeded and \
                         you_have[2] >= dolphinneeded and \
                         you_have[3] >= sharkneeded:
                         accepted = False
                         confirmation_message = await ctx.reply('Are you sure you want to'
                         f' complete **{cnf[1]}** fishing bundles? You will lose all these items:'+''
                         f'''\n:fish: {fishneeded:,}
:tropical_fish: {tropicalneeded:,}\n:dolphin: {dolphinneeded:,}\n:shark: {sharkneeded:,}''')
                         await confirmation_message.add_reaction('<:yesmark:960527955833020456>')
                         await confirmation_message.add_reaction('<:nomark:960527955988193360>')
                         def check(reaction, user):
                           return user == ctx.message.author and (reaction.emoji.id) in [
                         960527955833020456, 960527955988193360]
                         try:
                              reaction, user = await bot.wait_for('reaction_add', timeout=20.0, check=check)
                         except asyncio.TimeoutError:
                              await ctx.reply('You took too long to respond lol')
                         else:
                           if hasattr(reaction.emoji, 'id'):
                              if reaction.emoji.id != 960527955988193360:
                                   accepted = True
                              else:
                                   await ctx.reply('Guess you don\'t want to make a bundle')
                           else:
                                await ctx.reply('Guess you don\'t want to make a bundle')
                              
                         if accepted:
                              e2s[ctx.message.author.id][0][0] += cnf[1]
                              e2s[ctx.message.author.id][0][3] += cnf[1]
                              saved_data[ctx.message.author.id][9][7][0] -= fishneeded
                              saved_data[ctx.message.author.id][9][7][1] -= tropicalneeded
                              saved_data[ctx.message.author.id][9][7][2] -= dolphinneeded
                              saved_data[ctx.message.author.id][9][7][3] -= sharkneeded
                              await ctx.send(f'**{ctx.message.author.name}**, you successfully made **{cnf[1]:,}** fisher bundl'
                         f'{"es" if (cnf[1] % 100) != 1 else "e"}, nice!')
                    else:
                         embed = discord.Embed(title=f'Error!',
                         description=f'You don\'t even have enough fish to make `{cnf[1]:,}` fisher bundles!',
                         color=0xcc0000)
                         embed.add_field(name='You have', value=f''':fish: {you_have[0]:,}
:tropical_fish: {you_have[1]:,}\n:dolphin: {you_have[2]:,}\n:shark: {you_have[3]:,}''')
                         embed.add_field(name='Required', value=f''':coin: {fishneeded:,}
:tropical_fish: {tropicalneeded:,}\n:dolphin: {dolphinneeded:,}\n:shark: {sharkneeded:,}''')
                         await ctx.send(embed=embed)
          elif cnf[0] in ['02', '2', '002', '0b10', '0b010', '0o02', '0x2'
                        '0x02', '0o2', '2.', '2.0', '02.', '02.0',
                        '[2]', '[2.0]', '[02]', '[02.]']:
                    fishneeded = 12 * cnf[1]
                    tropicalneeded = 16 * cnf[1]
                    dolphinneeded = 2 * cnf[1]
                    sharkneeded = cnf[1]
                    you_have = [
                         advs[ctx.message.author.id][1]['coin'],
                         advs[ctx.message.author.id][1]['anchor'],
                         advs[ctx.message.author.id][2]['medal'],
                         advs[ctx.message.author.id][2]['trophy'],
                    ]
                    if cnf[1] <= 0:
                         await ctx.reply('You must provide a positive number of bundles')
                         return
                    if   you_have[0] >= fishneeded and \
                         you_have[1] >= tropicalneeded and \
                         you_have[2] >= dolphinneeded and \
                         you_have[3] >= sharkneeded:
                         accepted = False
                         confirmation_message = await ctx.reply('Are you sure you want to'
                         f' complete **{cnf[1]}** looter bundles? You will lose all these items:'+''
                         f'''\n:coin: {fishneeded:,}
:anchor: {tropicalneeded:,}\n:medal: {dolphinneeded:,}\n:trophy: {sharkneeded:,}''')
                         await confirmation_message.add_reaction('<:yesmark:960527955833020456>')
                         await confirmation_message.add_reaction('<:nomark:960527955988193360>')
                         def check(reaction, user):
                           return user == ctx.message.author and (reaction.emoji.id) in [
                         960527955833020456, 960527955988193360]
                         try:
                              reaction, user = await bot.wait_for('reaction_add', timeout=20.0, check=check)
                         except asyncio.TimeoutError:
                              await ctx.reply('You took too long to respond lol')
                         else:
                           if hasattr(reaction.emoji, 'id'):
                              if reaction.emoji.id != 960527955988193360:
                                   accepted = True
                              else:
                                   await ctx.reply('Guess you don\'t want to make a bundle')
                           else:
                                await ctx.reply('Guess you don\'t want to make a bundle')
                              
                         if accepted:
                              e2s[ctx.message.author.id][0][1] += cnf[1]
                              e2s[ctx.message.author.id][0][3] += cnf[1]
                              advs[ctx.message.author.id][1]['coin'] -= fishneeded
                              advs[ctx.message.author.id][1]['anchor'] -= tropicalneeded
                              advs[ctx.message.author.id][2]['medal'] -= dolphinneeded
                              advs[ctx.message.author.id][2]['trophy'] -= sharkneeded
                              await ctx.send(f'**{ctx.message.author.name}**, you successfully made **{cnf[1]:,}** looter bundl'
                         f'{"es" if (cnf[1] % 100) != 1 else "e"}, nice!')
                    else:
                         embed = discord.Embed(title=f'Error!',
                         description=f'You don\'t even have enough items to make `{cnf[1]:,}` looter bundles!',
                         color=0xcc0000)
                         embed.add_field(name='You have', value=f''':coin: {you_have[0]:,}
:anchor: {you_have[1]:,}\n:medal: {you_have[2]:,}\n:trophy: {you_have[3]:,}''')
                         embed.add_field(name='Required', value=f''':coin: {fishneeded:,}
:anchor: {tropicalneeded:,}\n:medal: {dolphinneeded:,}\n:trophy: {sharkneeded:,}''')
                         await ctx.send(embed=embed)
          elif cnf[0] in ['03', '3', '003', '0b11', '0b011', '0o03', '0x3'
                        '0x03', '0o3', '3.', '3.0', '03.', '03.0',
                        '[3]', '[3.0]', '[03]', '[03.]']:
                    fishneeded = 4000 * cnf[1]
                    tropicalneeded = 2500 * cnf[1]
                    dolphinneeded = 1200 * cnf[1]
                    you_have = [
                         e2s[ctx.message.author.id][1][0],
                         e2s[ctx.message.author.id][1][1],
                         e2s[ctx.message.author.id][1][2],
                    ]
                    if cnf[1] <= 0:
                         await ctx.reply('You must provide a positive number of bundles')
                         return
                    if   you_have[0] >= fishneeded and \
                         you_have[1] >= tropicalneeded and \
                         you_have[2] >= dolphinneeded:
                         accepted = False
                         confirmation_message = await ctx.reply('Are you sure you want to'
                         f' complete **{cnf[1]}** miner bundles? You will lose all these items:'+''
                         f'''\n<:iron:982682170340544532> {fishneeded:,}
<:silver:982682172462866462> {tropicalneeded:,}\n<:gold:982682167891083306> {dolphinneeded:,}''')
                         await confirmation_message.add_reaction('<:yesmark:960527955833020456>')
                         await confirmation_message.add_reaction('<:nomark:960527955988193360>')
                         def check(reaction, user):
                           return user == ctx.message.author and (reaction.emoji.id) in [
                         960527955833020456, 960527955988193360]
                         try:
                              reaction, user = await bot.wait_for('reaction_add', timeout=20.0, check=check)
                         except asyncio.TimeoutError:
                              await ctx.reply('You took too long to respond lol')
                         else:
                           if hasattr(reaction.emoji, 'id'):
                              if reaction.emoji.id != 960527955988193360:
                                   accepted = True
                              else:
                                   await ctx.reply('Guess you don\'t want to make a bundle')
                           else:
                                await ctx.reply('Guess you don\'t want to make a bundle')
                              
                         if accepted:
                              e2s[ctx.message.author.id][0][2] += cnf[1]
                              e2s[ctx.message.author.id][0][3] += cnf[1]
                              e2s[ctx.message.author.id][1][0] -= fishneeded
                              e2s[ctx.message.author.id][1][1] -= tropicalneeded
                              e2s[ctx.message.author.id][1][2] -= dolphinneeded
                              await ctx.send(f'**{ctx.message.author.name}**, you successfully made **{cnf[1]:,}** miner bundl'
                         f'{"es" if (cnf[1] % 100) != 1 else "e"}, nice!')
                    else:
                         embed = discord.Embed(title=f'Error!',
                         description=f'You don\'t even have enough ores to make `{cnf[1]:,}` miner bundles!',
                         color=0xcc0000)
                         embed.add_field(name='You have', value=f'''<:iron:982682170340544532> {you_have[0]:,}
<:silver:982682172462866462> {you_have[1]:,}\n<:gold:982682167891083306> {you_have[2]:,}''')
                         embed.add_field(name='Required', value=f'''<:iron:982682170340544532> {fishneeded:,}
<:silver:982682172462866462> {tropicalneeded:,}\n<:gold:982682167891083306> {dolphinneeded:,}''')
                         await ctx.send(embed=embed)
                  
@bot.command()
async def send(ctx, channel, *, message):
    ch = await bot.fetch_channel(type(1)(str(channel).replace
    ('<', '').replace('>', '').replace('#', '')))
    await ch.send(message.replace('@everyone', '[EVERYONE PING]').replace('@here', '[HERE PING]'))
@bot.command(aliases=['ore'])
async def ores(ctx, *args):
     id = ctx.message.author.id
     name = ctx.message.author
     if len(args)==0:
        id = ctx.message.author.id
        name = ctx.message.author
     elif len(args) >= 1:
      if len(ctx.message.mentions) == 0:
        try:
            f_user = await bot.fetch_user(int(args[0]))
            name = f_user
            id = f_user.id
            del f_user
        except:
            name = ctx.message.author
            id = ctx.message.author.id
      else:
         try:
             g_user = ctx.message.mentions[0]
         except:
             g_user = await bot.fetch_user(ctx.message.author.id)
         name = g_user
         id = g_user.id
     extrascheck[2](id)
     await ctx.send(embed=discord.Embed(color=0x454FBF,
     title=name.name + '\'s ores', description=''
f'''Ores can be earned through `f!mine`, can be sold with `f!sell <type>`!
`  Iron  ` - <:iron:982682170340544532> {e2s[id][1][0]:,}
` Silver ` - <:silver:982682172462866462> {e2s[id][1][1]:,}
`  Gold  ` - <:gold:982682167891083306> {e2s[id][1][2]:,}
` Diamond` - <:diamond:992415718438097068> {e2s[id][1][3]:,}'''))
def startcarcheck(id):
     global cars
     if id not in cars:
          cars[id]=[{ 
               'volvo': [
                    False, # you do not own this #
                    40,    #  speed <_>----------#
                    1,     #  level <_>----------#
                    0,     #  experience <_>-----#
               ],
               'mercedes': [
                    False, # you do not own this #
                    35,    #  speed <_>----------#
                    1,     #  level <_>----------#
                    0,     #  experience <_>-----#
               ],
               'toyota': [
                    False, # you do not own this #
                    38,    #  speed <_>----------#
                    1,     #  level <_>----------#
                    0,     #  experience <_>-----#
               ],
               'ferrari': [
                    False, # you do not own this #
                    45,    #  speed <_>----------#
                    1,     #  level <_>----------#
                    0,     #  experience <_>-----#
               ],
               'volkswagen': [
                    False, # you do not own this #
                    41,    #  speed <_>----------#
                    1,     #  level <_>----------#
                    0,     #  experience <_>-----#
               ]}, 0, 0]
@bot.command(aliases=['cars'])
async def car(ctx, *args):
     iid = ctx.message.author.id
     name = ctx.message.author
     if len(args)==0:
        iid = ctx.message.author.id
        name = ctx.message.author
     elif len(args) >= 1:
      if len(ctx.message.mentions) == 0:
        try:
            f_user = await bot.fetch_user(int(args[0]))
            name = f_user
            iid = f_user.id
            del f_user
        except:
            name = ctx.message.author
            iid = ctx.message.author.id
      else:
         try:
             g_user = ctx.message.mentions[0]
         except:
             g_user = await bot.fetch_user(ctx.message.author.id)
         name = g_user
         iid = g_user.id
     startcarcheck(iid)
     embed=discord.Embed(color=0x454FBF,
     title=name.name + '\'s cars', description=''
f'''`f!shop` to see a list of cars and items\n`f!race <car>` to race with your car
`f!upgrade <car>` to upgrade a car''')
     if cars[iid][0]['volvo'][0]:
         speed = cars[iid][0]['volvo'][1]
         level = cars[iid][0]['volvo'][2]
         experience = cars[iid][0]['volvo'][3]
         embed.add_field(name='<:Volvo:997419119475425321> Volvo', value=''
        f'**Speed**: {speed:,} km/h\n**Level**: {level:,}\n**Experience**: {experience}')
     if cars[iid][0]['ferrari'][0]:
         speed = cars[iid][0]['ferrari'][1]
         level = cars[iid][0]['ferrari'][2]
         experience = cars[iid][0]['ferrari'][3]
         embed.add_field(name='<:Ferrari:985076724293304330> Ferrari', value=''
        f'**Speed**: {speed:,} km/h\n**Level**: {level:,}\n**Experience**: {experience}')
     if cars[iid][0]['toyota'][0]:
         speed = cars[iid][0]['toyota'][1]
         level = cars[iid][0]['toyota'][2]
         experience = cars[iid][0]['toyota'][3]
         embed.add_field(name='<:Toyota:985078103388848168> Toyota', value=''
        f'**Speed**: {speed:,} km/h\n**Level**: {level:,}\n**Experience**: {experience}')
     if cars[iid][0]['volkswagen'][0]:
         speed = cars[iid][0]['volkswagen'][1]
         level = cars[iid][0]['volkswagen'][2]
         experience = cars[iid][0]['volkswagen'][3]
         embed.add_field(name='<:Volkswagen:985221821399986346> Volkswagen', value=''
        f'**Speed**: {speed:,} km/h\n**Level**: {level:,}\n**Experience**: {experience}')
     if cars[iid][0]['mercedes'][0]:
         speed = cars[iid][0]['mercedes'][1]
         level = cars[iid][0]['mercedes'][2]
         experience = cars[iid][0]['mercedes'][3]
         embed.add_field(name='<:MercedesBenz:985077274716041216> Mercedes Benz', value=''
        f'**Speed**: {speed:,} km/h\n**Level**: {level:,}\n**Experience**: {experience}')
     embed.add_field(name='<:CarToken:985218904743890974> Car Tokens', value=''
        f'{cars[iid][1]:,}', inline=0)
     await ctx.send(embed=embed)
@bot.command()
@commands.cooldown(1, 0x20, commands.BucketType.user)
async def race(ctx, *args):
  global cars,saved_data
  iid = ctx.message.author.id
  fuzzies = {
       'vlkswg': 'volkswagen',
       'mrcds':  'mercedes',
       'tyt':    'toyota',
       'vlv':    'volvo',
       'frrr':   'ferrari'
  }
  startcarcheck(iid)
  if len(args) != 0:
     carid = (' '.join(args).lower()).replace('a', '').replace('u', '').replace('e', '').replace('i', '').replace('o', '').replace(' ', '').rstrip('bnz')
     if carid in ['vlkswg', 'mrcds', 'tyt', 'vlv', 'frrr']:
               carinfo = {
                    'owned': cars[iid][0][fuzzies[carid]][0],
                    'speed': cars[iid][0][fuzzies[carid]][1],
                    'level': cars[iid][0][fuzzies[carid]][2],
                    'exp':   cars[iid][0][fuzzies[carid]][3]
               }
               def short_car(m, m2):
                    return random.randint(m,m2)+carinfo['speed'] - (cars[iid][0][fuzzies[carid]][1]//7)
               if carinfo['owned']:
                    opponents = [
                         {'<:BMW:988021536176885820> BMW M3': [short_car(-5,5)]},
                         {'<:Renault:987981273513492510> Renault Megane': [short_car(-4,10)]},
                         {'<:Renault:987981273513492510> Renault Scenic': [short_car(-6,8)]},
                         {'<:Nissan:987981792822853693> Nissan GTR': [55]},
                         {'<:Subaru:988177790018940968> Subaru XV': [short_car(-5,10)]},
                         {'<:BlueNissan:987984300421042196> Nissan Sentra': [short_car(-8,8)]},
                         {'<:Ford:988184218418966609> Ford Focus': [short_car(-8,16)]},
                         {'<:Ford:988184218418966609> Ford Mustang': [short_car(-4,12)]},
                         {':race_car: G-45': [short_car(-10,20)]},
                         {'<:Lexus:988183455626051635> Lexus SC 430': [short_car(-5, 12)]},
                         {'<:BMW:988021536176885820> BMW E5': [short_car(-2,4)]}, 
                         {'<:Porsche:988324949955600415> Porsche 911': [short_car(-6,12)]},
                         {'<:Chevrolet:987982349234999337> Chevrolet SUV': [short_car(-5,18)]},
                         {'<:FIAT:988185023461093486> FIAT 500': [short_car(-5,-2)]},
                         {'<:CryoSkoda:989604810917572658> Cryo \u0160koda': [short_car(-5, 40)]},
                         {'<:Skoda:987980732695715852> \u0160koda Octavia': [short_car(-3, 7)]},
                         {'<:MercedesBenz:985077274716041216> Mercedes Sedan': [short_car(-7, 7)]},
                         {'<:MercedesBenz:985077274716041216> Mercedes SUV': [short_car(-5, 11)]},
                         {'<:Bugatti:995650823763796049> Bugatti Chiron': [short_car(-5, 15)]},
                    ]
                    _range_ = [{
                         'you': [7, 0],
                         'opp': [7, 0]
                         }]
                    opponent = random.choice(opponents)
                    won = False
                    lost = False
                    winprize = random.randint(1,10)
                    def raceembed(__range__, __opponent__):
                         global won,lost,E
                         opponent_name = list(__opponent__)[0]
                         track1 = '<:road1:988070829915013141>' * __range__[0]['you'][0]
                         track2 = '<:road1:988070829915013141>' * __range__[0]['you'][1]
                         track3 = '<:road1:988070829915013141>' * __range__[0]['opp'][0]
                         track4 = '<:road1:988070829915013141>' * __range__[0]['opp'][1]
                         finish = '<:finish:988070824252682341>'
                         start = '<:road2:988070831693389975>'
                         woncred = winprize*random.randint(200, 800)
                         wontokens = winprize
                         yourcar, oppcar = ('<:rc1:988070825817157663>', '<:rc2:988070828228902912>')
                         if __range__[0]['opp'][0] >= 1 and __range__[0]['you'][0] <= 0:
                              won = True
                              saved_data[ctx.message.author.id][0] += woncred
                              cars[ctx.message.author.id][1] += wontokens
                              cars[ctx.message.author.id][0][fuzzies[carid]][3] += wontokens*2
                              E = discord.Embed(title='Your race', description=f'You won the race! You won :star2: {woncred:,} and '
                                                f'<:CarToken:985218904743890974> {wontokens:,}! Your car gained {wontokens*2:,} EXP!', color=0x00cc00)
                              E.set_author(name='Woohoo!', icon_url=str("https://emojipedia-us.s3.dualstack.us-west-"
                                                                        "1.amazonaws.com/thumbs/120/microsoft/310/1st-place-medal_1f947.png"))
                         elif __range__[0]['you'][0] >= 1 and __range__[0]['opp'][0] <= 0:
                              lost = True
                              E = discord.Embed(title='Your race', description='You lost the race!', color=0xcc0000)
                              E.set_author(name='Sad!', icon_url=str('https://emojipedia-us.s3.dualstack.us-west-1'
                                                                     '.amazonaws.com/thumbs/120/twitter/322/worried-face_1f61f.png'))
                         elif __range__[0]['you'][0] <= 0 and __range__[0]['opp'][0] <= 0:
                              lost = True
                              E = discord.Embed(title='Your race', description='You tied with your opponent!', color=0xccbb00)
                              E.set_author(name='Tie!', icon_url=str('https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/t'
                                                                     'humbs/72/twitter/322/face-with-raised-eyebrow_1f928.png'))
                         else:
                              winningprize = random.randint(1,5000)
                              E = discord.Embed(title='Your race', description='_ _', color=0xcccc00)
                         E.add_field(name=f'Your car ({fuzzies[carid].capitalize()})', value=''
                         f'{finish + track1 + yourcar + track2 + start}')
                         E.add_field(name=f'Opponent\'s car ({opponent_name})', value=''
                         f'{finish + track3 + oppcar + track4 + start}')
                         return E
                    __range__ = _range_
                    racemsg = await ctx.send(embed=raceembed(__range__, opponent))
                    def therange():
                         return __range__
                    def theopponentname():
                         return list(opponent)[0]
                    def lean():
                         global __range__
                         __range__ = therange()
                         lowered1 = random.randint(random.randint(0,1), min(__range__[0]['you'][0], (carinfo['speed']//22)))
                         lowered2 = random.randint(random.randint(0,1), min(__range__[0]['opp'][0], (opponent[theopponentname()][0]//22)))
                         __range__[0]['opp'][0] -= lowered2
                         __range__[0]['you'][0] -= lowered1
                         __range__[0]['opp'][1] += lowered2
                         __range__[0]['you'][1] += lowered1
                    def untie():
                         global __range__
                         if __range__[0]['opp'] == 0 and \
                            __range__[0]['you'] == 0:
                              player_chosen = random.choice(['you', 'opp'])
                              __range__[0][player_chosen][0] += 1
                              __range__[0][player_chosen][1] -= 1
                    while __range__[0]['you'][0] >= 1 and __range__[0]['opp'][0] >= 1:
                         await asyncio.sleep(0.6)
                         lean()
                         untie()
                         await racemsg.edit(embed=raceembed(__range__, opponent))
                         _range_ = __range__
                         
                          
               else:
                    race.reset_cooldown(ctx)
                    await ctx.reply(embed=discord.Embed(
     description=':x:  You do not own this car! `f!shop`', color=0xBC0010))
     else:
          race.reset_cooldown(ctx)
          await ctx.send(embed=discord.Embed(
     description='The valid cars to ra'
               'ce are `Volkswagen`, `Mercedes`, `Ferrari`, `Volvo` and `Toyota`.'))
  else:
     race.reset_cooldown(ctx)
     await ctx.send(embed=discord.Embed(title=':question: How to race?',
     description='To race, do `f!race <car>`.\n\nThe valid cars to ra'
               'ce are `Volkswagen`, `Mercedes`, `Ferrari`, `Volvo` and `Toyota`.'))
@race.error
async def RACING_ERROR(ctx, error):
	if isinstance(error, commands.CommandOnCooldown):
		await ctx.reply(embed=discord.Embed(title='Command on cooldown',
          description=f'Command on cooldown, wait `{round(error.retry_after, 1)}s`\n'
                    'The default cooldown for this command is [`32s`](https://discord.com/channels/0/0/0).'))

@bot.command()
@commands.cooldown(1, 4, commands.BucketType.user)
async def upgrade(ctx, *args):
  global cars,saved_data
  iid = ctx.message.author.id
  fuzzies = {
       'vlkswg': 'volkswagen',
       'mrcds':  'mercedes',
       'tyt':    'toyota',
       'vlv':    'volvo',
       'frrr':   'ferrari'
  }
  startcarcheck(iid)
  if len(args) != 0:
     carid = (' '.join(args).lower()).replace('a', '').replace('u', '').replace('e', '').replace('i', '').replace('o', '').replace(' ', '').rstrip('bnz')
     if carid in ['vlkswg', 'mrcds', 'tyt', 'vlv', 'frrr']:
               carinfo = {
                    'owned': cars[iid][0][fuzzies[carid]][0],
                    'speed': cars[iid][0][fuzzies[carid]][1],
                    'level': cars[iid][0][fuzzies[carid]][2],
                    'exp':   cars[iid][0][fuzzies[carid]][3]
               }
               if carinfo['owned']:
                 try:
                     cars[ctx.message.author.id][2]
                 except IndexError:
                     cars[ctx.message.author.id] += [0]
                 prestigelevel = cars[ctx.message.author.id][2]
                 sped = cars[iid][0][fuzzies[carid]][1]
                 if sped < (100 + (40 * prestigelevel)):
                    if saved_data[iid][0] >= 6000 and \
                       cars[iid][1] >= 12 and \
                       cars[iid][0][fuzzies[carid]][3] >= 40:
                         speed_increased = random.randint(1,4)
                         saved_data[iid][0] -= 6000
                         cars[iid][1] -= 12
                         cars[iid][0][fuzzies[carid]][3] -= 40
                         cars[iid][0][fuzzies[carid]][2] += 1
                         cars[iid][0][fuzzies[carid]][1] += speed_increased
                         if cars[iid][0][fuzzies[carid]][1] >= 100 + (prestigelevel * 40):
                             cars[iid][0][fuzzies[carid]][1] = 100 + (prestigelevel * 40)
                         await ctx.reply(embed=discord.Embed(
     description=f':white_check_mark: You successfully upgraded your {fuzzies[carid].capitalize()} for :star2: 6,000, '
     f'<:CarToken:985218904743890974> 12 and 40 EXP from your car!\n\nYour new car speed: {cars[iid][0][fuzzies[carid]][1]:,}', color=0x00BC25))
                    else:
                         upgrade.reset_cooldown(ctx)
                         await ctx.reply(embed=discord.Embed(
     description=':x:  You cannot afford this upgrade! You need the following things below:\n:star2: 6,000\n'
     '<:CarToken:985218904743890974> 12\n40 EXP of the car you are upgrading', color=0xBC0010))
                 else:
                         upgrade.reset_cooldown(ctx)
                         await ctx.reply(embed=discord.Embed(
     description=':x:  Your car is already at the maximum speed cap. `f!prestige car` to increase it!', color=0xBC0010))
               else:
                    upgrade.reset_cooldown(ctx)
                    await ctx.reply(embed=discord.Embed(
     description=':x:  You do not own this car therefore cannot upgrade it! `f!shop`', color=0xBC0010))
     else:
          upgrade.reset_cooldown(ctx)
          await ctx.send(embed=discord.Embed(
     description='The valid cars to upg'
               'rade are `Volkswagen`, `Mercedes`, `Ferrari`, `Volvo` and `Toyota`.'))
  else:
     upgrade.reset_cooldown(ctx)
     await ctx.send(embed=discord.Embed(title=':question: How to upgrade?',
     description='To upgrade a car, do `f!upgrade <car>`.\n\nThe valid cars to up'
               'grade are `Volkswagen`, `Mercedes`, `Ferrari`, `Volvo` and `Toyota`.'))
@upgrade.error
async def UPGRADING_ERROR(ctx, error):
	if isinstance(error, commands.CommandOnCooldown):
		await ctx.reply(embed=discord.Embed(title='Command on cooldown',
          description=f':x: You are on an upgrade cooldown! Try again in `{round(error.retry_after, 1)}s`\n'
                    'The default cooldown for this command is [`4s`](https://discord.com/channels/0/0/0).'))
@bot.command()
async def prestige(ctx, *args):
     global cars, saved_data
     iid = ctx.message.author.id
     startcarcheck(ctx.message.author.id)
     if len(args) == 0:
          await ctx.reply(embed=discord.Embed(description=':x: You need to put `car`, `help` or `levels` after `f!prestige`!', color=0xee0000), mention_author=0)
     else:
          if args[0].lower().startswith('h'):
               await ctx.reply(embed=discord.Embed(description=':information_source: **Limits**\n\nCar max speed cap formula: `100 + (car_prestige * 40)`'
                                        '\n\n:information_source: **Why should I prestige**\n\nIf you prestige your cars, you increase their max speed.\n'
                                        '\n:information_source: **Prestige Requirements**\n\nCar Token required formula: `400 + (next_prestige * 250)`\n'
                                        'Credit required formula: `500,000 + (next_prestige * 150,000)`', color=0xee0000), mention_author=0)
          if args[0].lower().startswith('l'):
              try:
                 cars[ctx.message.author.id][2]
              except IndexError:
                 cars[ctx.message.author.id] += [0]
              await ctx.reply(f'Your prestige levels:\n**Cars**: {cars[ctx.message.author.id][2]}')
          if args[0].lower().startswith('c'):
             try:
                 cars[ctx.message.author.id][2]
             except IndexError:
                 cars[ctx.message.author.id] += [0]
             p = cars[ctx.message.author.id][2]
             accepted = False
             n = p + 1
             cartokenneeded = 400 + (250 * n)
             creditneeded = 500000 + (150000 * n)
             confirmation_message = await ctx.reply('Are you sure you want to'
             f' prestige your cars'
             f'''?\nIt will cost you <:CarToken:985218904743890974> **{cartokenneeded:,}**'''
                                f''' and :star2: **{creditneeded:,}**.
If you want to, you will lose:
***Your car upgrades
Your car tokens
Your car levels***
You will get the upgrades:
***+40 km/h to the speed cap***''')
             def check(reaction, user):
               return user == ctx.message.author and (reaction.emoji.id) in [
             960527955833020456, 960527955988193360]
             await confirmation_message.add_reaction('<:yesmark:960527955833020456>')
             await confirmation_message.add_reaction('<:nomark:960527955988193360>')
             try:
                  reaction, user = await bot.wait_for('reaction_add', timeout=25.0, check=check)
             except asyncio.TimeoutError:
                  await ctx.reply('You took too long to respond lol')
             else:
               if hasattr(reaction.emoji, 'id'):
                  if reaction.emoji.id != 960527955988193360:
                       accepted = True
                  else:
                       await ctx.reply('Guess you don\'t want to prestige your cars')
               else:
                    await ctx.reply('Guess you don\'t want to prestige your cars')
                  
             if accepted:
                  iid = ctx.message.author.id
                  uhcr = cars[ctx.message.author.id][1]
                  cr = saved_data[ctx.message.author.id][0]
                  if saved_data[ctx.message.author.id][0] >= creditneeded and\
                     cars[ctx.message.author.id][1] >= cartokenneeded:
                      cars[ctx.message.author.id][2] += 1
                      cars[iid][0]['volvo'][1] = 40
                      cars[iid][0]['mercedes'][1] = 35
                      cars[iid][0]['ferrari'][1] = 45
                      cars[iid][0]['toyota'][1] = 38
                      cars[iid][0]['volkswagen'][1] = 41
                      cars[ctx.message.author.id][1] = 0
                      saved_data[ctx.message.author.id][0] -= creditneeded
                      e = discord.Embed(description='Congratulations you absolute '
                        'racer. You have raced a lot. You have earned this prestige for y'
                            'our cars and the rewards associated, and don\'t let anyone tell you otherwise.')
                      e.set_author(name=f'{ctx.message.author.name} | Prestige {n:,}', icon_url='https://cdn.dis'
                                   'cordapp.com/emojis/996843351376662558.png')
                      e.add_field(name='Earned Upgrades', value='` - ` +40 km/h to the speed cap')
                      await ctx.send(embed=e)
                  else:
                      await ctx.send(f'**{ctx.message.author.name}**, you do not have enough items to prestige!\n\n'
                        f'<:CarToken:985218904743890974> {uhcr:,}/{cartokenneeded:,}\n:star2: {cr:,}/{creditneeded:,}')


def starte3check(uid):
     global e3s
     if uid not in e3s:
          pass











@bot.command()
async def save(ctx):
     pfile = open('c:\\python\\farmbotpets.txt', 'w', encoding='utf-8')
     pfile.write(str(pets))
     pfile.close()
     wfile = open('c:\\python\\farmbotweapons.txt', 'w', encoding='utf-8')
     wfile.write(str(weapons))
     wfile.close()
     gfile = open('c:\\python\\farmbotgens.txt', 'w', encoding='utf-8')
     gfile.write(str(gens))
     gfile.close()
     sfile = open('c:\\python\\farmbotstuns.txt', 'w', encoding='utf-8')
     sfile.write(str(stuns))
     sfile.close()
     afile = open('c:\\python\\farmbotadvs.txt', 'w', encoding='utf-8')
     afile.write(str(advs))
     afile.close()
     bfile = open('c:\\python\\farmbotbm.txt', 'w', encoding='utf-8')
     bfile.write(str(bms))
     bfile.close()
     e1file = open('c:\\python\\fbextras1.txt', 'w', encoding='utf-8')
     e1file.write(str(e1s))
     e1file.close()
     e2file = open('c:\\python\\fbextras2.txt', 'w', encoding='utf-8')
     e2file.write(str(e2s))
     e2file.close()
     e3file = open('c:\\python\\fbextras3.txt', 'w', encoding='utf-8')
     e3file.write(str(e3s))
     e3file.close()
     file = open('c:\\python\\farmbotdatas.txt', 'w', encoding='utf-8')
     file.write(str(saved_data))
     file.close()
     cfile = open('c:\\python\\farmbotcars.txt', 'w', encoding='utf-8')
     cfile.write(str(cars))
     cfile.close()
     await ctx.send('yea')
########################################################

bot.run('OTQyODEzODAzNTE3NzI2ODAw.Ygp9xw.DQT0OcWrSJBVV9-OLJIVqSn156I')
file.close()
print('Closing...')
time.sleep(0.5)
print('Saving...')
time.sleep(0.5)
file = open('c:\\python\\farmbotdatas.txt', 'w', encoding='utf-8')
file.write(str(saved_data))
file.close()
pfile = open('c:\\python\\farmbotpets.txt', 'w', encoding='utf-8')
pfile.write(str(pets))
pfile.close()
wfile = open('c:\\python\\farmbotweapons.txt', 'w', encoding='utf-8')
wfile.write(str(weapons))
wfile.close()
gfile = open('c:\\python\\farmbotgens.txt', 'w', encoding='utf-8')
gfile.write(str(gens))
gfile.close()
sfile = open('c:\\python\\farmbotstuns.txt', 'w', encoding='utf-8')
sfile.write(str(stuns))
sfile.close()
afile = open('c:\\python\\farmbotadvs.txt', 'w', encoding='utf-8')
afile.write(str(advs))
afile.close()
bfile = open('c:\\python\\farmbotbm.txt', 'w', encoding='utf-8')
bfile.write(str(bms))
bfile.close()
e1file = open('c:\\python\\fbextras1.txt', 'w')
e1file.write(str(e1s))
e1file.close()
e2file = open('c:\\python\\fbextras2.txt', 'w', encoding='utf-8')
e2file.write(str(e2s))
e2file.close()
e3file = open('c:\\python\\fbextras3.txt', 'w', encoding='utf-8')
e3file.write(str(e3s))
e3file.close()
cfile = open('c:\\python\\farmbotcars.txt', 'w', encoding='utf-8')
cfile.write(str(cars))
cfile.close()
print('Successfully installed it offline')
