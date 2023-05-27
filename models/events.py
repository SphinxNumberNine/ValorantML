from enum import Enum

class EventType(Enum):
    GAME_STARTED = 0
    ROUND_STARTED = 1
    SPIKE_PLANTED = 2
    ROUND_ENDED = 3
    KILL = 4
    DAMAGE = 5
    HEAL = 6
    ABILITY_USED = 7
    ABILITY_GAINED = 8
    ULT_USED = 9
    ULT_GAINED = 10
    KAYO_DOWNED = 11
    KAYO_RES = 12
    SAGE_RES = 13
    PHOENIX_ULT_DEATH = 14

class RoundEndReason(Enum):
    ELIMINATIONS = 0
    SPIKE_EXPLOSION = 1
    SPIKE_DEFUSE = 2
    TIMEOUT = 3

class Event():
    def __init__(self, eventType):
        self.eventType = eventType
        self.eventID = None # TODO: some cryptographic hash

class GameStartedEvent(Event):
    def __init__(self, frameID, teamState1, teamState2, gameMap):
        self.teamState1 = teamState1
        self.teamState2 = teamState2
        self.map = gameMap
        self.frameID = frameID
        super().__init__(self, EventType.GAME_STARTED)

class RoundStartedEvent(Event):
    def __init__(self, frameID, teamState1, teamState2, roundNumber):
        self.teamState1 = teamState1
        self.teamState2 = teamState2
        self.roundNumber = roundNumber
        self.frameID = frameID
        super().__init__(self, EventType.ROUND_STARTED)

class SpikePlantedEvent(Event):
    def __init__(self, frameID, roundTime):
        self.roundTime = roundTime
        self.frameID = frameID
        super().__init__(self, EventType.SPIKE_PLANTED)

class RoundEndedEvent(Event):
    def __init__(self, frameID, roundEndReason):
        self.roundEndReason = roundEndReason
        self.frameID = frameID
        super.__init__(self, EventType.ROUND_ENDED)

class KillEvent(Event):
    def __init__(self, frameID, killingPlayer, dyingPlayer):
        self.frameID = frameID
        self.killingPlayer = killingPlayer
        self.dyingPlayer = dyingPlayer
        super().__init__(EventType.KILL)

class DamageEvent(Event):
    def __init__(self, frameID, player, damageTaken, newHP):
        self.frameID = frameID
        self.player = player
        self.damageTaken = damageTaken
        self.newHP = newHP
        super().__init__(EventType.DAMAGE)

class HealEvent(Event):
    def __init__(self, frameID, player, hpRecieved, newHP):
        self.frameID = frameID
        self.player = player
        self.hpRecieved = hpRecieved
        self.newHP = newHP
        super().__init__(EventType.HEAL)

class AbilityUsedEvent(Event):
    def __init__(self, frameID, player, abilityUsed):
        self.frameID = frameID
        self.player = player
        self.abilityUsed = abilityUsed
        super().__init__(EventType.ABILITY_USED)

class AbilityGainedEvent(Event):
    def __init__(self, frameID, player, abilityGained):
        self.frameID = frameID
        self.player = player
        self.abilityGained = abilityGained
        super().__init__(EventType.ABILITY_GAINED)

class UltUsedEvent(Event):
    def __init__(self, frameID, player, ultUsed):
        self.frameID = frameID
        self.player = player
        self.abilityUsed = abilityUsed
        super().__init__(EventType.ULT_USED)

class UltGainedEvent(Event):
    def __init__(self, frameID, player, ultGained):
        self.frameID = frameID
        self.player = player
        self.abilityGained = abilityGained
        super().__init__(EventType.ULT_GAINED)

    
class KayoDownedEvent(Event):
    def __init__(self, frameID, player):
        self.frameID = frameID
        self.player = player
        super().__init__(EventType.KAYO_DOWNED)

class KayoResEvent(Event):
    def __init__(self, frameID, player):
        self.frameID = frameID
        self.player = player
        super().__init__(EventType.KAYO_RES)

class SageResEvent(Event):
    def __init__(self, frameID, player):
        self.frameID = frameID
        self.player = player
        super().__init__(EventType.SAGE_RES)

class PhoenixUltDeathEvent(Event):
    def __init__(self, frameID, player):
        self.frameID = frameID
        self.player = player
        super().__init__(EventType.PHOENIX_ULT_DEATH)


