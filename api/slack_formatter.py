def getSlackMessage(playerData, requestConfig):
    return { "text": "OHAI " + requestConfig.playerName + ": " + str(playerData), "response_type": "in_channel" }
