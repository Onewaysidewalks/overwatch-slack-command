class RequestConfig:
    def __init__(self, platform, playerName, characterInquiry):
        self.playerName = playerName
        self.platform = platform
        self.characterInquiry = characterInquiry

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)

    def __unicode__(self):
        return str(self.__dict__)
