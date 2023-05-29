from enum import Enum
class RoundStatus(Enum):
    PRE_ROUND = 0
    ROUND_STARTED = 1
    SPIKE_PLANTED = 2
    ROUND_ENDED = 3 # also basically a "postround started status"

class Side(Enum):
    ATTACKER = 0
    DEFENDER = 1

class Player:
    def __init__(self, name, agent, team):
        self.name = name
        self.agent = agent
        self.team = team


class PlayerState:
    def __init__(self, player):
        self.player = player
        self.ability1Current = 0
        self.ability2Current = 0
        self.ability3Current = 0
        self.credits = 0
        self.armor = 0
        self.health = 0

class TeamState:
    def __init__(self, name, startingSide, currentSide, playerStates):
        self.name = name
        self.score = 0
        self.startingSide = startingSide
        self.currentSide = currentSide
        self.playerStates = playerStates # list

class RoundState:
    roundStatus = RoundStatus.PRE_ROUND
    roundTime = 0 # in seconds
    def __init__(self, roundNumber):
        self.roundStatus = RoundStatus.PRE_ROUND
        self.roundTime = 0 # in seconds
        self.roundNumber = roundNumber

class Half(Enum):
    FIRST = 0
    SECOND = 1
    OVERTIME = 2

class GameState:
    def __init__(self):
        self.currentRoundNumber = 1
        self.half = Half.FIRST
        self.team1State = None
        self.team2State = None
        self.currentRoundState = None
        self.gameFinished = False

   