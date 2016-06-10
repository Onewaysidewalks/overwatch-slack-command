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

class Character: #an overarching class to hold all stat groups
    def __init__(self):
        self.groups = []

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)

    def __unicode__(self):
        return str(self.__dict__)

class CharacterStatGroup: #a grouping of character stats, by header
    def __init__(self, header):
        self.header = header
        self.stats = []

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)

    def __unicode__(self):
        return str(self.__dict__)

class CharacterStat:
    def __init__(self, statName, statValue):
        self.name = statName
        self.value = statValue

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)

    def __unicode__(self):
        return str(self.__dict__)
