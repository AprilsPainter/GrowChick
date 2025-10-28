# config.py

import os

DEFAULT_STATS = {
    "매력": 0,
    "포만감": 50,
    "행복도": 50,
    "청결도": 30
}

STAT_BAR_COLORS = {
    "매력": (249, 36, 114),
    "포만감": (243, 104, 11),
    "행복도": (57, 197, 6),
    "청결도": (2, 197, 227)
        }

FONT_PATH = os.path.join("assets", "ui", "fonts", "NeoDunggeunmoPro-Regular.ttf")
