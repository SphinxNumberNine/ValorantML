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

class Jett(Agent):
    def __init__():
        super().__init__(name="jett", 
                         type=Agents.JETT, 
                         role=AgentRole.DUELIST, 
                         ability1Name="cloudburst", 
                         ability1Max=2,
                         ability2Name="updraft",
                         ability2Max=2,
                         ability3Name="tailwind",
                         ability3Max=1,
                         ultName="bladestorm",
                         ultOrbsRequired=7)

class Kayo(Agent):
    def __init__():
        super().__init__(name="kayo", 
                         type=Agents.KAYO, 
                         role=AgentRole.INITIATOR, 
                         ability1Name="frag/ment", 
                         ability1Max=1,
                         ability2Name="flash/drive",
                         ability2Max=2,
                         ability3Name="zero/point",
                         ability3Max=1,
                         ultName="null/cmd",
                         ultOrbsRequired=8)

class Killjoy(Agent):
    def __init__():
        super().__init__(name="killjoy", 
                         type=Agents.KILLJOY, 
                         role=AgentRole.SENTINEL, 
                         ability1Name="nanoswarm", 
                         ability1Max=2,
                         ability2Name="alarmbot",
                         ability2Max=1,
                         ability3Name="turret",
                         ability3Max=1,
                         ultName="lockdown",
                         ultOrbsRequired=8)

class Neon(Agent):
    def __init__():
        super().__init__(name="neon", 
                         type=Agents.NEON, 
                         role=AgentRole.DUELIST, 
                         ability1Name="fast lane", 
                         ability1Max=1,
                         ability2Name="relay bolt",
                         ability2Max=2,
                         ability3Name="high gear",
                         ability3Max=1,
                         ultName="overdrive",
                         ultOrbsRequired=7)
        
class Omen(Agent):
    def __init__():
        super().__init__(name="omen", 
                         type=Agents.OMEN, 
                         role=AgentRole.CONTROLLER, 
                         ability1Name="shrouded step", 
                         ability1Max=2,
                         ability2Name="paranoia",
                         ability2Max=1,
                         ability3Name="dark cover",
                         ability3Max=2,
                         ultName="from the shadows",
                         ultOrbsRequired=7)

class Phoenix(Agent):
    def __init__():
        super().__init__(name="phoenix", 
                         type=Agents.PHOENIX, 
                         role=AgentRole.DUELIST, 
                         ability1Name="blaze", 
                         ability1Max=1,
                         ability2Name="curveball",
                         ability2Max=2,
                         ability3Name="hot hands",
                         ability3Max=1,
                         ultName="run it back",
                         ultOrbsRequired=6)

class Raze(Agent):
    def __init__():
        super().__init__(name="raze", 
                         type=Agents.RAZE, 
                         role=AgentRole.DUELIST, 
                         ability1Name="boom bot", 
                         ability1Max=1,
                         ability2Name="blast pack",
                         ability2Max=2,
                         ability3Name="paint shells",
                         ability3Max=1,
                         ultName="showstopper",
                         ultOrbsRequired=8)

class Reyna(Agent):
    def __init__():
        super().__init__(name="reyna", 
                         type=Agents.REYNA, 
                         role=AgentRole.DUELIST, 
                         ability1Name="leer", 
                         ability1Max=2,
                         ability2Name="devour",
                         ability2Max=2,
                         ability3Name="dismiss",
                         ability3Max=2,
                         ultName="empress",
                         ultOrbsRequired=8)

class Sage(Agent):
    def __init__():
        super().__init__(name="sage", 
                         type=Agents.SAGE, 
                         role=AgentRole.SENTINEL, 
                         ability1Name="barrier orb", 
                         ability1Max=1,
                         ability2Name="slow orb",
                         ability2Max=2,
                         ability3Name="healing orb",
                         ability3Max=1,
                         ultName="resurrection",
                         ultOrbsRequired=8)

class Skye(Agent):
    def __init__():
        super().__init__(name="skye", 
                         type=Agents.SKYE, 
                         role=AgentRole.INITIATOR, 
                         ability1Name="regrowth", 
                         ability1Max=1,
                         ability2Name="trailblazer",
                         ability2Max=1,
                         ability3Name="guiding light",
                         ability3Max=2,
                         ultName="seekers",
                         ultOrbsRequired=7)

class Sova(Agent):
    def __init__():
        super().__init__(name="sova", 
                         type=Agents.SOVA, 
                         role=AgentRole.INITIATOR, 
                         ability1Name="owl drone", 
                         ability1Max=1,
                         ability2Name="shock bolt",
                         ability2Max=2,
                         ability3Name="recon bolt",
                         ability3Max=1,
                         ultName="hunter's fury",
                         ultOrbsRequired=8)

class Viper(Agent):
    def __init__():
        super().__init__(name="viper", 
                         type=Agents.VIPER, 
                         role=AgentRole.CONTROLLER, 
                         ability1Name="snake bite", 
                         ability1Max=2,
                         ability2Name="poison cloud",
                         ability2Max=1,
                         ability3Name="toxic screen",
                         ability3Max=1,
                         ultName="viper's pit",
                         ultOrbsRequired=8)

class Yoru(Agent):
    def __init__():
        super().__init__(name="yoru", 
                         type=Agents.YORU, 
                         role=AgentRole.DUELIST, 
                         ability1Name="fakeout", 
                         ability1Max=1,
                         ability2Name="blindside",
                         ability2Max=2,
                         ability3Name="gatecrash",
                         ability3Max=2,
                         ultName="dimensional drift",
                         ultOrbsRequired=7)

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
    currentRoundNumber = 0
    half = Half.FIRST
    team1State = None
    team2State = None
    currentRoundState = None

   