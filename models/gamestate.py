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
    ability1Current = 0
    ability2Current = 0
    ability3Current = 0
    credits = 0
    armor = 0
    health = 0
    def __init__(self, player):
        self.player = player

class TeamState:
    score = 0
    def __init__(self, name, startingSide, currentSide, playerStates):
        self.name = name
        self.startingSide = startingSide
        self.currentSide = currentSide
        self.playerStates = playerStates # list

class RoundState:
    roundStatus = RoundStatus.PRE_ROUND
    roundTime = 0 # in seconds
    def __init__(self, roundNumber):
        self.roundNumber = roundNumber

class Half(Enum):
    FIRST = 0
    SECOND = 1
    OVERTIME = 2

class GameState:
    currentRoundNumber = 1
    half = Half.FIRST
    team1State = None
    team2State = None
    currentRoundState = None
    gameFinished = False

   