from enum import Enum
class RoundStatus(Enum):
    PRE_ROUND = 0
    ROUND_STARTED = 1
    SPIKE_PLANTED = 2
    ROUND_ENDED = 3

class AgentRole(Enum):
    DUELIST = 0
    CONTROLLER = 1
    INITIATOR = 2
    SENTINEL = 3

class Agents(Enum):
    ASTRA = 0
    BREACH = 1
    BRIMSTONE = 2
    CHAMBER = 3
    CYPHER = 4
    FADE = 5
    GEKKO = 6
    HARBOR = 7
    JETT = 8
    KAYO = 9
    KILLJOY = 10
    NEON = 11
    OMEN = 12
    PHOENIX = 13
    RAZE = 14
    REYNA = 15
    SAGE = 16
    SKYE = 17
    SOVA = 18
    VIPER = 19
    YORU = 20

class Agent:
    def __init__(self, name, type, role, ability1Name, ability1Max, ability2Name, ability2Max, ability3Name, ability3Max, ultName, ultOrbsRequired):
        self.name = name
        self.type = type
        self.role = role
        self.ability1Name = ability1Name
        self.ability1Max = ability1Max
        self.ability2Name = ability2Name
        self.ability2Max = ability2Max
        self.ability3Name = ability3Name
        self.ability3Max = ability3Max
        self.ultName = ultName
        self.ultOrbsRequired = ultOrbsRequired

class Astra(Agent): # TODO
    def __init__():
        super().__init__(name="astra", 
                         type=Agents.ASTRA, 
                         role=AgentRole.CONTROLLER, 
                         ability1Name="nebula", 
                         ability1Max=4,
                         ability2Name="TODO",
                         ability2Max=0,
                         ability3Name="TODO",
                         ability3Max=0,
                         ultName="cosmic divide",
                         ultOrbsRequired=7)
        
class Breach(Agent):
    def __init__():
        super().__init__(name="breach", 
                         type=Agents.BREACH, 
                         role=AgentRole.INITIATOR, 
                         ability1Name="aftershock", 
                         ability1Max=1,
                         ability2Name="flashpoint",
                         ability2Max=2,
                         ability3Name="fault line",
                         ability3Max=1,
                         ultName="rolling thunder",
                         ultOrbsRequired=8)
        
class Brimstone(Agent):
    def __init__():
        super().__init__(name="brimstone", 
                         type=Agents.BRIMSTONE, 
                         role=AgentRole.CONTROLLER, 
                         ability1Name="stim beacon", 
                         ability1Max=1,
                         ability2Name="incendiary",
                         ability2Max=1,
                         ability3Name="sky smoke",
                         ability3Max=3,
                         ultName="orbital strike",
                         ultOrbsRequired=7)
        
class Chamber(Agent):
    def __init__():
        super().__init__(name="chamber", 
                         type=Agents.CHAMBER, 
                         role=AgentRole.SENTINEL, 
                         ability1Name="trademark", 
                         ability1Max=1,
                         ability2Name="headhunter",
                         ability2Max=8,
                         ability3Name="rendezvous",
                         ability3Max=1,
                         ultName="tour de force",
                         ultOrbsRequired=8)
        
class Cypher(Agent):
    def __init__():
        super().__init__(name="cypher", 
                         type=Agents.CYPHER, 
                         role=AgentRole.SENTINEL, 
                         ability1Name="trapwire", 
                         ability1Max=2,
                         ability2Name="cyber cage",
                         ability2Max=2,
                         ability3Name="spycam",
                         ability3Max=1,
                         ultName="neural theft",
                         ultOrbsRequired=6)
        
class Fade(Agent):
    def __init__():
        super().__init__(name="fade", 
                         type=Agents.FADE, 
                         role=AgentRole.INITIATOR, 
                         ability1Name="prowler", 
                         ability1Max=2,
                         ability2Name="seize",
                         ability2Max=1,
                         ability3Name="haunt",
                         ability3Max=1,
                         ultName="nightfall",
                         ultOrbsRequired=8)
        
class Gekko(Agent):
    def __init__():
        super().__init__(name="gekko", 
                         type=Agents.GEKKO, 
                         role=AgentRole.INITIATOR, 
                         ability1Name="mosh pit", 
                         ability1Max=2,
                         ability2Name="wingman",
                         ability2Max=1,
                         ability3Name="dizzy",
                         ability3Max=1,
                         ultName="thrash",
                         ultOrbsRequired=7)
        
class Harbor(Agent):
    def __init__():
        super().__init__(name="harbor", 
                         type=Agents.HARBOR, 
                         role=AgentRole.CONTROLLER, 
                         ability1Name="cascade", 
                         ability1Max=2,
                         ability2Name="cove",
                         ability2Max=1,
                         ability3Name="high tide",
                         ability3Max=1,
                         ultName="reckoning",
                         ultOrbsRequired=7)
        


class PlayerState:


class TeamState:
    score = 0
    name = ""

class RoundState:
    roundStatus = RoundStatus.PRE_ROUND
    roundTime = 0 # in seconds
    team1Score = 0
    team2Score = 0

   