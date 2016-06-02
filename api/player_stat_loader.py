import os
import requests
import urllib2
import re
import models
from bs4 import BeautifulSoup

def getPlayerData(playerName):
    print "Querying player: %s" % playerName

    #initialize the web scraping parser
    html = urllib2.urlopen("https://playoverwatch.com/en-us/career/psn/" + playerName).read() #TODO: psn support only, extend this!
    soup = BeautifulSoup(html, 'html5lib')

    highlightsHtml = soup.find('section', {'id': 'highlights-section'})
    statNames = highlightsHtml.find_all('p', {'class': 'card-copy'})
    statValues = highlightsHtml.find_all('h3', {'class': 'card-heading'})

    playerStat = {}

    for index, statName in enumerate(statNames):
        playerStat[statName.string] = statValues[index].string

    return playerStat


if __name__== '__main__':
    print getPlayerData("onewaysidewalks")
