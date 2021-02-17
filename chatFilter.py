
from addict import Dict
import json
import discord
f = open("filterwords.json")
chatFilter = Dict(json.load(f))
le = open("filterignore.json")
chatFilterIgnore = Dict(json.load(le))

async def userCheck(id):
    if str(id) not in chatFilterIgnore['ignoreuser']:
        return False
    else:
        return True
       
           
async def messageCheck(message):
    for key in chatFilter['bannedWords']:
        text = message.content.lower()
        if key in text.split():
            embed = discord.Embed(title="Global Filter", description="Banned word triggered by `Wildcard`", colour=discord.Colour.from_rgb(255, 0, 242))
            embed.add_field(name="Banned Word", value=key)
            embed.add_field(name="Full Message", value=message.content, inline=False)
            embed.set_author(name=message.author.name+'#'+message.author.discriminator, icon_url=message.author.avatar_url)
            return embed 
    return False
        
async def reload(message):
    if message.author.id == 193112730943750144:
        foxtrot = open("filterwords.json", "r")
        filterList = Dict(json.load(foxtrot))
        chatFilter['bannedwords'] = filterList['bannedwords']
        foxtrot.close()
        return "Global Filter reloaded successfully!"

async def banWord(message):
    text = message.content.replace("$banword ", "", 1).lower()
    if message.author.guild_permissions.administrator == True:
        foxtrot = open("filterwords.json", "r")
        filterList = Dict(json.load(foxtrot))
        filterList['bannedWords'].setdefault(text,)
        chatFilter['bannedWords'].setdefault(text,)
        foxtrot.close()
        jsonFile = open("filterwords.json", "w+")
        json.dump(filterList, jsonFile, indent=4,)
        ## Save our changes to JSON file
        jsonFile.close()
        return(str(text)+" has been added to globalfilter")

async def unBanWord(message):
    text = message.content.replace("$unbanword ", "", 1).lower()
    if message.author.guild_permissions.administrator == True:
        foxtrot = open("filterwords.json", "r")
        filterList = Dict(json.load(foxtrot))
        foxtrot.close()
        if text in filterList['bannedWords']:
            filterList['bannedWords'].pop(text)
            chatFilter['bannedWords'].pop(text)
            jsonFile = open("filterwords.json", "w+")
            json.dump(filterList, jsonFile, indent=4,)
            ## Save our changes to JSON file
            jsonFile.close()
            return(str(text)+" has been removed from the globalfilter")
        else:
            return(str(text)+" was already unfiltered!")

