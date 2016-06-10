import os
import requests
import urllib2
import re
import models
import sys
from bs4 import BeautifulSoup

def parseRequestConfig(requestConfigStr):
    requestPieces = requestConfigStr.split(' ')

    #Argument Structure is {platform} {name} {inquiry}
    requestPieceCount = len(requestPieces)
    if requestPieceCount == 1:
        #if the length is one, we assume the asker is looking for a psn name, of OVERALL inquiry
        return models.RequestConfig("psn", requestPieces[0], "OVERALL")
    elif requestPieceCount == 2:
        possiblePlatform = requestPieces[0]
        if possiblePlatform in ["xbox", "psn", "pc"]:
            #the first arg is a platform, we assume the inquiry is OVERRAL, and take platform and name
            return models.RequestConfig(requestPieces[0].lower(), requestPieces[1], "OVERALL")
        else:
            #the first arg is NOT a platform, we assume the structure is {name} {inquiry}, for the psn platform
            return models.RequestConfig("psn", requestPieces[0], requestPieces[1].upper())
    else:
        return models.RequestConfig(requestPieces[0].lower(), requestPieces[1], requestPieces[2].upper())



def getPlayerData(requestConfig):
    print "Querying: %s" % requestConfig

    #initialize the web scraping parser
    html = urllib2.urlopen("https://playoverwatch.com/en-us/career/%s/%s" % (requestConfig.platform, requestConfig.playerName)).read() #TODO: psn support only, extend this!
    soup = BeautifulSoup(html, 'html5lib')

    playerStats = models.Character()

    characterKey = getCharacterKey(requestConfig.characterInquiry)

    if characterKey == "OVERALL":
        highlightsHtml = soup.find("section", {"id": "highlights-section"})
        statNames = highlightsHtml.find_all("p", {'class': 'card-copy'})
        statValues = highlightsHtml.find_all("h3", {'class': 'card-heading'})

        characterStatGroup = models.CharacterStatGroup("Overall")

        for index, statName in enumerate(statNames):
            characterStatGroup.stats.append(models.CharacterStat(statName.string, statValues[index].string))
        playerStats.groups.append(characterStatGroup)
    else:
        #this means we are in character specific mode. Load stats only relevant to that character
        #first we get a hold of the containing div via the attribute "data-category-id"
        containingDiv = soup.find("div", {"data-category-id": characterKey})

        #from the containing div, we look to get a hold of tables with the class "data-table". These will individually hold all of the stats that are shown
        dataTables = containingDiv.find_all("table", {"class": "data-table"})

        #now we iterate each table, and pull both the header for the table, as well as the key value pairs for the stats
        #the resulting structure should look like this:
        #{
        #    "{table header, i.e. Hero Specific}": {
        #         "statName": "statValue"
        #    },
        #    ....
        #}

        for dataTable in dataTables:
            header = dataTable.find("th").string
            characterStatGroup = models.CharacterStatGroup(header)

            dataBody = dataTable.find("tbody")
            for statRow in dataBody.find_all("tr"):
                cells = statRow.find_all("td")
                statName = cells[0].string
                statValue = cells[1].string

                characterStatGroup.stats.append(models.CharacterStat(statName, statValue))

            playerStats.groups.append(characterStatGroup)

    return playerStats

def getCharacterKey(characterName):
    compareStr = characterName.lower()
    if compareStr == "reaper":
        return "0x02E0000000000002"
    elif compareStr == "tracer":
        return "0x02E0000000000003"
    elif compareStr == "mercey":
        return "0x02E0000000000004"
    elif compareStr == "hanzo":
        return "0x02E0000000000005"
    elif compareStr == "torbjorn":
        return "0x02E0000000000006"
    elif compareStr == "reinhardt":
        return "0x02E0000000000007"
    elif compareStr == "pharah":
        return "0x02E0000000000008"
    elif compareStr == "winston":
        return "0x02E0000000000009"
    elif compareStr == "widowmaker":
        return "0x02E000000000000A"
    elif compareStr == "bastion":
        return "0x02E0000000000015"
    elif compareStr == "symmetra":
        return "0x02E0000000000016"
    elif compareStr == "zenyatta":
        return "0x02E0000000000020"
    elif compareStr == "genji":
        return "0x02E0000000000029"
    elif compareStr == "roadhog":
        return "0x02E0000000000040"
    elif compareStr == "mccree":
        return "0x02E0000000000042"
    elif compareStr == "junkrat":
        return "0x02E0000000000065"
    elif compareStr == "zarya":
        return "0x02E0000000000068"
    elif compareStr == "soldier76":
        return "0x02E000000000006E"
    elif compareStr == "lucio":
        return "0x02E0000000000079"
    elif compareStr == "dva":
        return "0x02E000000000007A"
    elif compareStr == "mei":
        return "0x02E00000000000DD"
    else:
        return "OVERALL"

if __name__== '__main__':
    #we skip the first argument, as that is the file name
    if sys.argv[1] == 'load':
        print getPlayerData(models.RequestConfig("psn", sys.argv[2], "OVERALL"))
    if sys.argv[1] == 'parse':
        print parseRequestConfig(sys.argv[2])
    if sys.argv[1] == 'parseAndLoad':
        requestConfig = parseRequestConfig(sys.argv[2])
        print getPlayerData(requestConfig)
