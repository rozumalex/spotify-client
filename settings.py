import os
from dotenv import load_dotenv
import orjson

__all__ = ["SYNC_CONFIG", "SYNC_FILE_NAME", "MUSIC_FOLDER", "SYNC_TO_USB", "USB_DRIVE_NAME"]


load_dotenv()


def load_boolean_env(name: str, default: bool) -> bool:
    env_value = os.getenv(name, default)

    if isinstance(env_value, bool):
        return env_value

    if env_value.lower() in ["false", "0"]:
        return False

    return True


# If set to True, will try to sync to a USB drive
SYNC_TO_USB = load_boolean_env("SYNC_TO_USB", False)

# Name of the USB drive to sync music to
USB_DRIVE_NAME = os.getenv("USB_DRIVE_NAME")

# Folder to sync music to that will be used if SYNC_TO_USB is set to False
# or no USB drive is connected
MUSIC_FOLDER = os.getenv("MUSIC_FOLDER")

# Name of the file that will be created in every folder
# for synchronization purposes
SYNC_FILE_NAME = os.getenv("SYNC_FILE_NAME", "sync.spotdl")

with open("config.json", "r") as f:
    SYNC_CONFIG = orjson.loads(f.read())
