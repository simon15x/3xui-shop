# region: Download
APP_IOS_LINK = "https://apps.apple.com/ru/app/happ-proxy-utility-plus/id6746188973"
APP_ANDROID_LINK = "https://play.google.com/store/apps/details?id=com.happproxy"
APP_WINDOWS_LINK = (
    "https://github.com/Happ-proxy/happ-desktop/releases/latest/download/setup-Happ.x86.exe"
)

APP_IOS_SCHEME = "happ://add/"
APP_ANDROID_SCHEME = "happ://add/"
APP_WINDOWS_SCHEME = "happ://add/"
APP_ROUTING = (
    "happ://routing/add/eyJQcm94eUlwIjpbXSwiR2xvYmFsUHJveHkiOnRydWUsIkdlb3NpdGVVcmwiOiJodHRwczpcL1wvZ2l0aHViLmNvbVwvTG95YWxzb2xkaWVyXC92MnJheS1ydWxlcy1kYXRcL3JlbGVhc2VzXC9sYXRlc3RcL2Rvd25sb2FkXC9nZW9zaXRlLmRhdCIsIlJlbW90ZUROU1R5cGUiOiJEb0giLCJEbnNIb3N0cyI6eyJjbG91ZGZsYXJlLWRucy5jb20iOiIxLjEuMS4xIiwiZG5zLmdvb2dsZSI6IjguOC44LjgifSwiTGFzdFVwZGF0ZWQiOjE3NTE4NjU0NTksIk5hbWUiOiIxIiwiRG9tZXN0aWNETlNEb21haW4iOiJodHRwczpcL1wvZG5zLmdvb2dsZVwvZG5zLXF1ZXJ5IiwiQmxvY2tTaXRlcyI6W10sIkRvbWVzdGljRE5TSXAiOiI4LjguOC44IiwiRG9tZXN0aWNETlNUeXBlIjoiRG9IIiwiUmVtb3RlRE5TSXAiOiIxLjEuMS4xIiwiRG9tYWluU3RyYXRlZ3kiOiJJUElmTm9uTWF0Y2giLCJGYWtlRG5zIjpmYWxzZSwiUmVtb3RlRE5TRG9tYWluIjoiaHR0cHM6XC9cL2Nsb3VkZmxhcmUtZG5zLmNvbVwvZG5zLXF1ZXJ5IiwiRGlyZWN0U2l0ZXMiOlsiZ2Vvc2l0ZTpjYXRlZ29yeS1ydSJdLCJEaXJlY3RJcCI6WyIxMC4wLjAuMFwvOCIsIjEwMC42NC4wLjBcLzEwIiwiMTcyLjE2LjAuMFwvMTIiLCIxOTIuMTY4LjAuMFwvMTYiLCIxNjkuMjU0LjAuMFwvMTYiLCIyMjQuMC4wLjBcLzQiLCIyNTUuMjU1LjI1NS4yNTUiLCJnZW9pcDpydSJdLCJQcm94eVNpdGVzIjpbXSwiR2VvaXBVcmwiOiJodHRwczpcL1wvZ2l0aHViLmNvbVwvTG95YWxzb2xkaWVyXC92MnJheS1ydWxlcy1kYXRcL3JlbGVhc2VzXC9sYXRlc3RcL2Rvd25sb2FkXC9nZW9pcC5kYXQiLCJCbG9ja0lwIjpbXSwiVXNlQ2h1bmtGaWxlcyI6dHJ1ZX0="
)

# endregion

# region: Keys
MAIN_MESSAGE_ID_KEY = "main_message_id"
PREVIOUS_CALLBACK_KEY = "previous_callback"

INPUT_PROMOCODE_KEY = "input_promocode"

SERVER_NAME_KEY = "server_name"
SERVER_HOST_KEY = "server_host"
SERVER_MAX_CLIENTS_KEY = "server_max_clients"

NOTIFICATION_CHAT_IDS_KEY = "notification_chat_ids"
NOTIFICATION_LAST_MESSAGE_IDS_KEY = "notification_last_message_ids"
NOTIFICATION_MESSAGE_TEXT_KEY = "notification_message_text"
NOTIFICATION_PRE_MESSAGE_TEXT_KEY = "notification_pre_message_text"
# endregion

# region: Webhook paths
TELEGRAM_WEBHOOK = "/webhook"  # Webhook path for Telegram bot updates
CONNECTION_WEBHOOK = "/connection"  # Webhook path for receiving connection requests
CRYPTOMUS_WEBHOOK = "/cryptomus"  # Webhook path for receiving Cryptomus payment notifications
HELEKET_WEBHOOK = "/heleket"  # Webhook path for receiving Heleket payment notifications
YOOKASSA_WEBHOOK = "/yookassa"  # Webhook path for receiving Yookassa payment notifications
YOOMONEY_WEBHOOK = "/yoomoney"  # Webhook path for receiving Yoomoney payment notifications
# endregion

# region: Notification tags
BOT_STARTED_TAG = "#BotStarted"
BOT_STOPPED_TAG = "#BotStopped"
BACKUP_CREATED_TAG = "#BackupCreated"
EVENT_PAYMENT_SUCCEEDED_TAG = "#EventPaymentSucceeded"
EVENT_PAYMENT_CANCELED_TAG = "#EventPaymentCanceled"
# endregion

# region: I18n settings
DEFAULT_LANGUAGE = "en"
I18N_DOMAIN = "bot"
# endregion

# region: Constants
UNLIMITED = "∞"
DB_FORMAT = "sqlite3"
LOG_ZIP_ARCHIVE_FORMAT = "zip"
LOG_GZ_ARCHIVE_FORMAT = "gz"
MESSAGE_EFFECT_IDS = {
    "🔥": "5104841245755180586",
    "👍": "5107584321108051014",
    "👎": "5104858069142078462",
    "❤️": "5044134455711629726",
    "🎉": "5046509860389126442",
    "💩": "5046589136895476101",
}
# endregion

# region: Enums
from enum import Enum
from typing import Any, Optional


class TransactionStatus(Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    CANCELED = "canceled"
    REFUNDED = "refunded"


class Currency(Enum):
    RUB = ("RUB", "₽")
    USD = ("USD", "$")
    XTR = ("XTR", "★")

    @property
    def symbol(self) -> str:
        return self.value[1]

    @property
    def code(self) -> str:
        return self.value[0]

    @classmethod
    def from_code(cls, code: str) -> "Currency":
        code = code.upper()
        for currency in cls:
            if currency.code == code:
                return currency
        raise ValueError(f"Invalid currency code: {code}")


class ReferrerRewardType(Enum):
    DAYS = "days"
    MONEY = "money"  # TODO: consider using currencies instead? depends on balance implementation

    @classmethod
    def from_str(cls, value: str) -> Optional["ReferrerRewardType"]:
        try:
            return cls[value.upper()]
        except KeyError:
            try:
                return cls(value.lower())
            except ValueError:
                return None


class ReferrerRewardLevel(Enum):
    FIRST_LEVEL = 1
    SECOND_LEVEL = 2

    @classmethod
    def from_value(cls, value: Any) -> Optional["ReferrerRewardLevel"]:
        try:
            return cls(int(value))
        except (ValueError, KeyError):
            return None


# endregion
