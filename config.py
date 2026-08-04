import os
from dotenv import load_dotenv

load_dotenv()


# =====================
# Telegram
# =====================

TG_BOT_TOKEN = os.getenv(
    "TG_BOT_TOKEN"
)

TG_CHAT_ID = os.getenv(
    "TG_CHAT_ID"
)


# =====================
# Polymarket
# =====================

POLY_PRIVATE_KEY = os.getenv(
    "POLY_PRIVATE_KEY"
)

POLY_API_KEY = os.getenv(
    "POLY_API_KEY"
)

POLY_API_SECRET = os.getenv(
    "POLY_API_SECRET"
)

POLY_API_PASSPHRASE = os.getenv(
    "POLY_API_PASSPHRASE"
)


# =====================
# Strategy
# =====================

MIN_PROFIT = float(
    os.getenv(
        "MIN_PROFIT",
        "0.02"
    )
)


MAX_TRADE_AMOUNT = float(
    os.getenv(
        "MAX_TRADE_AMOUNT",
        "20"
    )
)


# 安全开关
# 第一阶段关闭自动交易

AUTO_TRADE = False
