"""VELOCITY HUNGARIAN - language pack, brand and motion design constants."""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

OUTPUT_DIR = BASE_DIR / "output"
LESSONS_DIR = OUTPUT_DIR / "lessons"
HISTORY_DIR = OUTPUT_DIR / "history"
SCENE_DIR = BASE_DIR / "scene"

VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920
FPS = 30

# ---------------------------------------------------------------- brand

BRAND = "VELOCITY HUNGARIAN"
BRAND_LOCKUP_TOP = "VELOCITY"
BRAND_LOCKUP_BOTTOM = "HUNGARIAN"
HANDLE = "@velocityhungarian"
MASCOT_NAME = "Velo"

# ==== LANGUAGE PACK START ====
LANGUAGE = {
    "code": "hu",
    "name": "Hungarian",
    "native_name": "Magyar",
    "history_key": "hungarian",
    "english_voice": "en-US-AvaNeural",
    "english_fallback_voice": "en-US-GuyNeural",
    "native_voice": "hu-HU-TamasNeural",
    "native_fallback_voice": "hu-HU-NoemiNeural",
    "native_engine": "edge",
    "native_lang_code": "hu",
    "english_rate": "-2%",
    "native_rate": "-6%",
    "english_pitch": "+0Hz",
    "native_pitch": "+0Hz",
    "native_label": "MAGYAR",
    "translit_label": "SAY IT LIKE",
    "greeting": "Szia!",
    "encouragement": "Kiváló!",
    "rtl": False,
    "char_tiles": False,
    "script_font": "",
}
# ==== LANGUAGE PACK END ====

AI_MODEL = os.getenv("AI_MODEL", "gemini-fast")
POLLINATIONS_API_KEY = os.getenv("POLLINATIONS_API_KEY", "")

# ---------------------------------------------------------------- timing (seconds)

INTRO_DURATION = 4.0
OUTRO_DURATION = 5.2
EN_CARD_IN = 0.55
GAP_EN_NATIVE = 0.5
NATIVE_CARD_LEAD = 0.35
GAP_BEFORE_REPEAT = 0.8
TAIL_HOLD = 1.4
MAX_REEL_DURATION = 88.0

# ---------------------------------------------------------------- palette

INK = "#3C3C3C"
MUTED = "#8A8A8A"
CREAM = "#FFF8E7"
GREEN = "#58CC02"
GREEN_DARK = "#46A302"
GREEN_DEEP = "#3D8F00"
BLUE = "#1CB0F6"
PURPLE = "#A560E8"
ORANGE = "#FF7A00"
RED = "#FF4B4B"
YELLOW = "#F5A700"
TEAL = "#00A889"
PINK = "#E056A0"

PALETTE = [GREEN, BLUE, PURPLE, ORANGE, RED, YELLOW, TEAL, PINK]

# ---------------------------------------------------------------- categories
# (english, native, icon, accent)

# ==== CATEGORY TABLE START ====
CATEGORY_TABLE = [
    ("Greetings", "Köszöntések", "hand", "#1CB0F6"),
    ("Basic Phrases", "Alapvető Kifejezések", "chat", "#58CC02"),
    ("Common Expressions", "Gyakori Kifejezések", "chat", "#1CB0F6"),
    ("Travel", "Utazás", "plane", "#1CB0F6"),
    ("Restaurant", "Étterem", "fork", "#FF7A00"),
    ("Shopping", "Vásárlás", "bag", "#E056A0"),
    ("Emergency", "Vészhelyzet", "siren", "#FF4B4B"),
    ("Family Terms", "Családi Kifejezések", "heart", "#E056A0"),
    ("Numbers", "Számok", "hash", "#A560E8"),
    ("Time", "Idő", "clock", "#00A889"),
    ("Motivation", "Motiváció", "rocket", "#A560E8"),
    ("Love", "Szerelem", "heart", "#FF4B4B"),
    ("Success", "Siker", "trophy", "#F5A700"),
    ("Wisdom", "Bölcsesség", "book", "#A560E8"),
    ("Happiness", "Boldogság", "smile", "#F5A700"),
    ("Self Improvement", "Önfejlesztés", "leaf", "#58CC02"),
    ("Gratitude", "Hála", "heart", "#FF7A00"),
    ("Friendship", "Barátság", "users", "#00A889"),
    ("Hope", "Remény", "sun", "#FF7A00"),
    ("Creativity", "Kreativitás", "palette", "#E056A0"),
    ("Inner Peace", "Belső Béke", "lotus", "#00A889"),
    ("Confidence", "Magabiztosság", "shield", "#1CB0F6"),
    ("Perseverance", "Kitartás", "mountain", "#FF7A00"),
    ("Inspiration", "Inspiráció", "sparkles", "#A560E8"),
    ("Positive Life", "Pozitív Élet", "sun", "#58CC02"),
    ("Courage", "Bátorság", "shield", "#FF4B4B"),
    ("Kindness", "Kedvesség", "heart", "#E056A0"),
    ("Patience", "Türelem", "hourglass", "#00A889"),
    ("Forgiveness", "Megbocsátás", "hands", "#FF7A00"),
    ("Strength", "Erő", "dumbbell", "#FF4B4B"),
    ("Joy", "Öröm", "smile", "#F5A700"),
    ("Balance", "Egyensúly", "scale", "#00A889"),
    ("Growth", "Növekedés", "sprout", "#58CC02"),
    ("Purpose", "Cél", "target", "#A560E8"),
    ("Mindfulness", "Tudatos Jelenlét", "lotus", "#00A889"),
    ("Daily Routine", "Napi rutin", "calendar", "#1CB0F6"),
    ("Weather", "Időjárás", "cloud", "#1CB0F6"),
    ("Feelings", "Érzések", "smile", "#E056A0"),
    ("Food", "Étel", "fork", "#FF7A00"),
    ("Health", "Egészség", "heart", "#58CC02"),
    ("Work", "Munka", "briefcase", "#1CB0F6"),
    ("Technology", "Technológia", "chip", "#A560E8"),
    ("Nature", "Természet", "leaf", "#58CC02"),
    ("Animals", "Állatok", "paw", "#FF7A00"),
    ("Colors", "Színek", "palette", "#E056A0"),
    ("Directions", "Irányok", "compass", "#1CB0F6"),
    ("Body Parts", "Testrészek", "hand", "#00A889"),
    ("Clothes", "Ruházat", "shirt", "#E056A0"),
    ("Music", "Zene", "music", "#A560E8"),
    ("Sports", "Sport", "ball", "#FF7A00"),
    ("Holidays", "Ünnepek", "gift", "#FF4B4B"),
    ("Education", "Oktatás", "book", "#1CB0F6"),
    ("Culture", "Kultúra", "globe", "#00A889"),
    ("Finance", "Pénzügyek", "coin", "#58CC02"),
    ("Relationships", "Kapcsolatok", "users", "#E056A0"),
]
# ==== CATEGORY TABLE END ====

CATEGORIES = [c[0] for c in CATEGORY_TABLE]
CATEGORIES_NATIVE = {c[0]: c[1] for c in CATEGORY_TABLE}
CATEGORY_META = {c[0]: {"native": c[1], "icon": c[2], "accent": c[3]} for c in CATEGORY_TABLE}
MAX_RECENT_CATEGORIES = 25

# ==== HASHTAGS START ====
HASHTAGS = [
    "#learnhungarian",
    "#hungarianlessons",
    "#hungarianforbeginners",
    "#languagelearning",
    "#hungarianvocabulary",
    "#velocityhungarian",
    "#dailyhungarian",
    "#hungarian",
    "#learnlanguages",
    "#speakhungarian",
    "#bilingual",
    "#languagetips",
]
# ==== HASHTAGS END ====
