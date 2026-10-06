"""The approved P0 content inventory (GDD G04, G05, G07; Story 1.4).

Validation accepts exactly this set so later-stage or extra content cannot slip in.
"""

SUPPORTED_CONTENT_SCHEMA_VERSION = 1
SUPPORTED_PACKAGE_ID = "package:brackenford-p0"
SUPPORTED_PACKAGE_MAJOR_VERSION = 1

MARKET_SQUARE = "location:brackenford:market-square"
MARAS_STALL = "location:brackenford:maras-stall"
COMMON_ROOM = "location:brackenford:common-room"
APPROVED_LOCATION_IDS = frozenset({MARKET_SQUARE, MARAS_STALL, COMMON_ROOM})

MARA = "npc:brackenford:mara"
OREN = "npc:brackenford:oren"
TESSA = "npc:brackenford:tessa"
IVO = "npc:brackenford:ivo"
APPROVED_NPC_IDS = frozenset({MARA, OREN, TESSA, IVO})

APPROVED_ROUTE_ENDPOINTS = frozenset(
    {frozenset({MARKET_SQUARE, MARAS_STALL}), frozenset({MARKET_SQUARE, COMMON_ROOM})}
)
APPROVED_MOVEMENT_MODE_IDS = frozenset(
    {"movement:walk", "movement:jog", "movement:sprint", "movement:crawl"}
)

DRINK = "item:brackenford:drink"
DRINK_PRICE_GOLD = 1
DRINK_STOCK = 5
PREPARED_POUCH_GOLD = 10_000

APPROVED_KIND_COUNTS = {
    "manifest": 1,
    "movement_rules": 1,
    "world": 1,
    "location": 3,
    "npc": 4,
    "item": 1,
    "social_conflict": 1,
    "check": 1,
    "starting_state": 1,
}

INTRODUCTION_MIN_WORDS = 60
INTRODUCTION_MAX_WORDS = 120

APPROVED_ROUTE_LENGTHS = (
    (frozenset({MARKET_SQUARE, MARAS_STALL}), 7000),
    (frozenset({MARKET_SQUARE, COMMON_ROOM}), 140000),
)
APPROVED_MOVEMENT_SPEEDS = (
    ("movement:walk", 1400),
    ("movement:jog", 2800),
    ("movement:sprint", 5600),
    ("movement:crawl", 500),
)
OBLIGATION_GOLD = 20
OBLIGATION_DUE_SECOND = 115200
PAYMENT_EXTENSION_DIFFICULTY = 12
PAYMENT_EXTENSION_SECONDS = 86400
