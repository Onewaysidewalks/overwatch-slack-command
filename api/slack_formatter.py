def getSlackMessage(playerData, requestConfig):

    message = "<https://playoverwatch.com/en-us/career/%s/%s|%s> \n*%s stats*\n" % (requestConfig.platform, requestConfig.playerName, requestConfig.playerName, requestConfig.characterInquiry)

    statsMessage = ""
    for statGroup in playerData.groups:
        statsMessage = "%s*%s*\n" % (statsMessage, statGroup.header)
        for statEntry in statGroup.stats:
            statsMessage = "%s>%s: %s\n" % (statsMessage, statEntry.name, statEntry.value)
    return { "text": "OHAI %s" % message , "response_type": "in_channel", "attachments": [{ "text": statsMessage, "mrkdwn_in": ["text"] }] }
