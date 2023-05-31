from enum import Enum


class FrameType(Enum):
    NON_GAME_FRAME = -1
    PRE_ROUND_FRAME = 0
    MID_ROUND_FRAME = 1


class PreRoundPlayerInfo:
    def __init__(self, name, agent, ability1Count, ability2Count, ability3Count, ultOrbs, creds):
        self.name = name
        self.agent = agent
        self.ability1Count = ability1Count
        self.ability2Count = ability2Count
        self.ability3Count = ability3Count
        self.ultOrbs = ultOrbs
        self.creds = creds


class MidRoundPlayerInfo:
    def __init__(self, name, agent, ability1Count, ability2Count, ability3Count, ultOrbs, creds, health, armor):
        self.name = name
        self.agent = agent
        self.ability1Count = ability1Count
        self.ability2Count = ability2Count
        self.ability3Count = ability3Count
        self.ultOrbs = ultOrbs
        self.creds = creds
        self.health = health
        self.armor = armor


class PreRoundInfo:
    def __init__(self, team1, team1Score, team1PlayerInfoList, team2, team2Score, team2PlayerInfoList, roundTimer, roundNumber):
        self.team1 = team1
        self.team1Score = team1Score
        self.team1PlayerInfoList = team1PlayerInfoList
        self.team2 = team2
        self.team2Score = team2Score
        self.team2PlayerInfoList = team2PlayerInfoList
        self.roundTimer = roundTimer
        self.roundNumber = roundNumber


class RoundInfo:
    def __init__(self, team1, team1Score, team1PlayerInfoList, team2, team2Score, team2PlayerInfoList, roundTimer, roundNumber):
        self.team1 = team1
        self.team1Score = team1Score
        self.team1PlayerInfoList = team1PlayerInfoList
        self.team2 = team2
        self.team2Score = team2Score
        self.team2PlayerInfoList = team2PlayerInfoList
        self.roundTimer = roundTimer
        self.roundNumber = roundNumber


class Frame():
    def __init__(self, frameType):
        self.frameType = frameType
        self.frameID = None  # TODO: some cryptographic hash


class NonGameFrame(Frame):
    def __init__(self, frameNumber):
        self.frameNumber = frameNumber
        super().__init__(self, FrameType.NON_GAME_FRAME)


class PreroundFrame(Frame):
    def __init__(self, frameNumber, frameInfo):
        self.frameNumber = frameNumber
        self.frameInfo = frameInfo
        super().__init__(self, FrameType.PRE_ROUND_FRAME)


class MidRoundFrame(Frame):
    def __init__(self, frameNumber, frameInfo):
        self.frameNumber = frameNumber
        self.frameInfo = frameInfo
        super().__init__(self, FrameType.MID_ROUND_FRAME)
