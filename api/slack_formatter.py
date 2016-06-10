def getSlackMessage(playerData, requestConfig):

    message = "<https://playoverwatch.com/en-us/career/%s/%s|%s>\n" % (requestConfig.platform, requestConfig.playerName, requestConfig.playerName)

    for statGroup in playerData.groups:
        message = "%s%s\n" % (message, statGroup.header)
        for statEntry in statGroup.stats:
            message = "%s>%s: %s\n" % (message, statEntry.name, statEntry.value)
    return { "text": "OHAI %s" % message , "response_type": "in_channel" }
