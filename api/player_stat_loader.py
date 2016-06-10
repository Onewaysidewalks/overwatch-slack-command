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
    print "Querying player: %s" % requestConfig.playerName

    #initialize the web scraping parser
    html = urllib2.urlopen("https://playoverwatch.com/en-us/career/%s/%s" % (requestConfig.platform, requestConfig.playerName)).read() #TODO: psn support only, extend this!
    soup = BeautifulSoup(html, 'html5lib')

    highlightsHtml = soup.find('section', {'id': 'highlights-section'})
    statNames = highlightsHtml.find_all('p', {'class': 'card-copy'})
    statValues = highlightsHtml.find_all('h3', {'class': 'card-heading'})

    playerStat = {}

    if not requestConfig.characterInquiry or requestConfig.characterInquiry == "OVERALL":
        for index, statName in enumerate(statNames):
            playerStat[statName.string] = statValues[index].string

    return playerStat


if __name__== '__main__':
    #we skip the first argument, as that is the file name
    if sys.argv[1] == 'load':
        print getPlayerData(models.RequestConfig("psn", sys.argv[2], "OVERALL"))
    if sys.argv[1] == 'parse':
        print parseRequestConfig(sys.argv[2])
    if sys.argv[1] == 'loadAndParse':
        requestConfig = parseRequestConfig(sys.argv[2])
        print getPlayerData(requestConfig)
