import discord
from riotwatcher import LolWatcher
import conf
from Domain.Lol.Model.Services.RessourcesManager import RessourcesManager
from Infrastructure.Lol.Mediator import Mediator
import random

# Todo: Refactorer en objet quand comportement un peu plus défini

from discord.utils import get
import os

# You must define your own config file with key_riot.
API_KEY     = RessourcesManager().config['key_riot']
LOL_WATCHER = LolWatcher(API_KEY)
MEDIATOR    = Mediator(LOL_WATCHER)

client = discord.Client()
TOKEN  = RessourcesManager().config['token']
PREFIX = "!a"

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(PREFIX) == 0:
        return
    args = message.content.split()[1:]
    for i in range(len(args)):
        args[i].lower()

    await streamsCommands(message, args[0], args)
    await help(message, args[0], args)
    await rank(message, args[0], args)
    await match(message, args[0], args)
    await kda(message, args[0], args)


async def streamsCommands(message, command, args):

    if command == "say":
        sayMessage = args.join(" ")
        message.delete().catch()
        message.channel.send(sayMessage)

    if command == "corobizar":
        await message.channel.send("https://www.twitch.tv/corobizar")

    if command == "mv":
        await message.channel.send("https://www.twitch.tv/mistermv")

    if command == "gummy":
        await message.channel.send("https://www.twitch.tv/elgummy115")

    if command == "yukii":
        await message.channel.send("https://www.twitch.tv/suyukii")


async def help(message, command, args):

    if command == "help":
        say        = "!a say this is a random sentence : bot delete your message then write what you ask"
        hero       = "!a hero <top/middle/jungle/adc/support>: bot send informations from u.gg about the champion you asked for"
        ping       = "!a ping : a simple test of ping"
        randomrole = "!a randomrole : give you a random League of Legends role"
        twitch     = "!a <corobizar/mv/yukii/gummy> : bot send twitch channel of corobizar / mister mv / yukii or gummy"
        level      = "!a level < pseudo > : bot send level of pseudo on League of Legends"
        rank       = "!a rank < pseudo >: Send rank informations into the channel you asked for "
        match      = "!a match < pseudo >: Send match live informations into the channel you asked for"


        embed = discord.Embed(description= "Help", color=12717994)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/440116867802333186/585811500795691019/AW489065_20.gif")
        embed.add_field(name="** #Command 1 **", value=say)
        embed.add_field(name="** #Command 2 **", value=hero)
        embed.add_field(name="** #Command 3 **", value=ping)
        embed.add_field(name="** #Command 4 **", value=randomrole)
        embed.add_field(name="** #Command 5 **", value=twitch)
        embed.add_field(name="** #Command 6 **", value=level)
        embed.add_field(name="** #Command 7 **", value=rank)
        embed.add_field(name="** #Command 8 **", value=match)
        await message.channel.send(embed=embed)


async def rank(message, command, args):
    if command == "rank":
        ranks = MEDIATOR.getRiotRanking(args[1]).getRankBySummoner()
        for queue in ranks:
            embed = discord.Embed(title="Ranked Status of " + MEDIATOR.getRiotRanking(args[1]).getSummoner().name,color=discord.colour.Color.dark_blue())
            embed.set_thumbnail(url="http://pa1.narvii.com/6386/d6b473c43316280f1a0e55c456f52903b8dcefd4_00.gif")
            embed.set_image(url="https://i.imgur.com/M0BXsvb.gif")
            embed.add_field(name="** Queue Type **",value= queue.queueType)
            embed.add_field(name="** Rank **",value= queue.tier + " " + queue.rank)
            embed.add_field(name="** League Points **",value= queue.leaguePoints)
            embed.add_field(name="** Wins **",value= queue.wins)
            embed.add_field(name="** Losses **",value= queue.losses)
            embed.add_field(name="** Inactive ? **",value= queue.inactive)
            embed.add_field(name="** Veteran ? **",value= queue.veteran)
            embed.add_field(name="** Fresh Blood ? **",value= queue.freshBlood)
            embed.add_field(name="** Hotstreak ? **",value= queue.hotStreak)

            if queue.miniSeries is not None:
                embed.add_field(name="** MiniSeries Wins **",value= queue.miniSeries.wins)
                embed.add_field(name="** MiniSeries Losses **",value= queue.miniSeries.losses)
                embed.add_field(name="** MiniSeries Target **",value= queue.miniSeries.target)
                embed.add_field(name="** MiniSeries Progress (W = win, L = loose, N = not done yet) **", value=queue.miniSeries.progress)
            await message.channel.send(embed=embed)


async def match(message, command, args):
    if command == "match":
        try:
            currentActiveGame = MEDIATOR.getRiotRanking(args[1]).getActiveGame()
        except:
            await message.channel.send("This summoner isn't in game or do not exist")
            return
        bannedStr       = ""
        team       = ["", ""]
        for bans in currentActiveGame.bannedChampions:
            bannedStr += "\n" + str(bans.pickTurn) + ":" + bans.getChampion()
        i = 0
        blueId = currentActiveGame.participants[0].teamId
        for p in currentActiveGame.participants:
            j = 0 if p.teamId == blueId else 1
            team[j] += "\n" + "**" + p.summonerName + "** : ***"
            team[j] += p.getChampion()
            team[j] += "*** " + RessourcesManager().getSpellById(p.spell1Id)
            team[j] += " "    + RessourcesManager().getSpellById(p.spell2Id)
            i += 1
        await sendRank(message, args, currentActiveGame.participants)
        embed = discord.Embed(description= 'Live Match', color= discord.colour.Color.dark_purple())
        embed.add_field(name="** Game Mode **",value=currentActiveGame.gameMode)
        embed.add_field(name="**Game Type **",value=currentActiveGame.gameType)
        embed.add_field(name="**BannedChampions **",value=bannedStr, inline=False)
        embed.add_field(name="**gameLength (name=sec) **",value=currentActiveGame.gameLength)
        embed.add_field(name="**Queue type **",value=currentActiveGame.gameQueueConfigId)
        embed.add_field(name="**Blue Team**",value=team[0],inline=False)
        embed.add_field(name="**Red Team**",value=team[1],inline=False)
        await message.channel.send(embed=embed)


async def sendRank(message, args, participants):
    string = ["", ""]
    blueid = participants[0].teamId
    for p in participants:
        ranks     = MEDIATOR.getRiotRanking(p.summonerName).getRankBySummoner()
        for r in ranks:
            j = 0 if p.teamId == blueid else 1
            string[j] += "**" + p.summonerName + "** \n"
            string[j] += r.queueType + ":    **" + r.tier + "   " + r.rank + "**   \n"
            string[j] += "Points : **" + str(r.leaguePoints) + "**   Wins : **" + str(r.wins) + "**   Loose : **" + str(r.losses) + "** \n \n"

    embed = discord.Embed(title="Live Match Ranks (1/2)",color=discord.colour.Color.green())
    embed.add_field(name="** Players **", value=string[0])
    await message.channel.send(embed=embed)

    embed = discord.Embed(title="Live Match Ranks (2/2)", color=discord.colour.Color.dark_orange())
    embed.add_field(name="** Players **", value=string[1])
    await message.channel.send(embed=embed)


def embedKda(message, dict, embed):

    for kdaCs in dict:
        string = ""
        string += "\n** kills** " + str(dict[kdaCs][0])
        string += "\n** deaths** " + str(dict[kdaCs][1]) + "\n** assists** " + str(dict[kdaCs][2])
        string += "\n** cs** " + str(dict[kdaCs][3]) + "\n** cs by Min** " + str( "%.2f" % dict[kdaCs][6])
        string += "\n** nb games ** " + str(dict[kdaCs][4])
        string += "\n** time played ** " + str(dict[kdaCs][5]) + "\n"
        embed.add_field(name="**" + kdaCs + "**: ", value=string, inline=True)
    return embed


async def kda(message, command, args):
    # !a match name, nbgames, mode, champion
    mode = None
    if len(args) > 3:
        mode = args[3]
    champ = None
    if len(args) > 4:
        champ = args[4]
    if command == "kda":
        # Todo: faire nb days
        kda   = MEDIATOR.KdaCs(int(args[2]), 0, args[1], mode, champ)
        embed = discord.Embed(title="**Kda and Cs on " + args[2] + " games**", color=discord.colour.Color.dark_red())

        iconId = MEDIATOR.getProfile(args[1]).profileIconId
        embed.set_thumbnail(url=RessourcesManager().getIconUrlById(iconId))

        embed.add_field(name="**Global Mean Kda**: ", value="\n** kills** "+ str(kda.meanGlobalKda[0]) + "\n** deaths** "
                                                        + str(kda.meanGlobalKda[1]) +"\n** assists** "+ str(kda.meanGlobalKda[2]))

        embed.add_field(name="**Global Kda**: ",value="\n** kills** "+ str(kda.globalKda[0]) +
                                                  "\n** deaths** "+ str(kda.globalKda[1]) +"\n** assists** "+ str(kda.globalKda[2]))

        embed.add_field(name="**Global Mean Cs**: ", value=kda.meanGlobalCs)
        embed.add_field(name="**Global Cs**: ", value=kda.globalCs)
        embed.add_field(name="**Cs by min**: ", value="%.2f" % kda.csByMin)
        embed.add_field(name="**Total time played**: ", value=kda.totalTime)

        await message.channel.send(embed=embed)
        embed = discord.Embed(title="**Mean Global Kda and Cs on " + args[2] + " games**", color=discord.colour.Color.dark_purple())

        randomChampName = random.choice(list(kda.dictMeanKdaCs.keys()))
        embed.set_thumbnail(url=RessourcesManager().getChampIconUrlByName(randomChampName))

        embed = embedKda(message, kda.dictMeanKdaCs, embed)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title="**Global Kda and Cs on " + args[2] + " games**", color=discord.colour.Color.dark_teal())
        embed = embedKda(message, kda.dictKdaCs, embed)

        randomChampName2 = randomChampName
        if len(kda.dictKdaCs) > 1:
            while randomChampName2 == randomChampName:
                randomChampName2 = random.choice(list(kda.dictKdaCs.keys()))

        embed.set_thumbnail(url=RessourcesManager().getChampIconUrlByName(randomChampName2))

        await message.channel.send(embed=embed)


client.run(TOKEN)



