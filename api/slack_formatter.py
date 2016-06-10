def getSlackMessage(playerData, requestConfiguration):
    return { "text": "OHAI " + playerName + ": " + str(playerData), "response_type": "in_channel" }
