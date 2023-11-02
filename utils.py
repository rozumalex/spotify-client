import os
from typing import Optional

import settings

__all__ = ["get_sync_args"]


def format_folder_path(folder_path: str) -> str:
    """Wraps folder path with single quotes, so it can be used as a parameter in the command line."""
    return f"'{folder_path}'"


def get_usb_path() -> Optional[str]:
    """Get path to the USB drive if connected."""
    for volume in os.listdir("/Volumes"):
        if volume == settings.USB_DRIVE_NAME:
            return os.path.join("/Volumes", volume)

    return


def get_folder_path(folder_name: str) -> str:
    """
    Get path to the folder with given name.
    
    If `SYNC_TO_USB` is set to `True`, will try to get path to the USB drive
    if connected.
    
    Otherwise, will return path to the folder in `MUSIC_FOLDER`.
    """
    if settings.SYNC_TO_USB:
        folder_path = get_usb_path() or settings.MUSIC_FOLDER
    else:
        folder_path = settings.MUSIC_FOLDER

    return os.path.join(folder_path, folder_name)


def folder_exists(folder_path: str) -> bool:
    """Return `True` if folder with given path exists."""
    return os.path.isdir(folder_path)


def get_sync_file_path(folder_path: str) -> str:
    """Get path to the file that is used for synchronization."""
    return os.path.join(folder_path, settings.SYNC_FILE_NAME)


def file_exists(file_path: str) -> bool:
    """Return `True` if file with given path exists."""
    return os.path.isfile(file_path)


def create_folder(folder_path: str) -> None:
    """Creates folder with given path."""
    os.mkdir(folder_path)


def get_sync_args() -> list[str]:
    for folder_name, url in settings.SYNC_CONFIG.items():
        folder_path = get_folder_path(folder_name)
        sync_file_path = get_sync_file_path(folder_path)

        args = [format_folder_path(sync_file_path), "--output", format_folder_path(folder_path)]

        if not file_exists(sync_file_path):
            if not folder_exists(folder_path):
                create_folder(folder_path)

            args = [url, "--save-file"] + args

        args = ["spotdl", "sync"] + args

        yield args
