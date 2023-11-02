# Spotify sync client

This script is created to sync a list of playlists or albums from Spotify to a USB device or a local folder.

## Usage

### Install

```shell
pip install poetry
poetry install
poetry shell
```

## Configure env

You can place your configuration in `.env` file in the root of the project.

There are currently 4 environment variables used in the project:

`SYNC_TO_USB` (default `False`): if set to `True`, it will try to find a USB device connected
to the computer and sync the music to it. If set to `False`, it will sync music to the 
`MUSIC_FOLDER` directory.

`MUSIC_FOLDER`: a path to the folder where the music should be synced to.

`USB_DEVICE_NAME`: a name of the USB device that will be used for syncing.

`SYNC_FILE_NAME` (default: `sync.spotdl`): a name of the file that will be created in each sub-folder for synchronization.


# Configure playlists

You can configure playlists in `config.json` file in the root of the project.

This file should contain a following structure:
```json
{
  "LoFi": "https://example.com/playlist/1",
  "Chill": "https://example.com/playlist/2"
}
```

Where the keys are the folder names (for each item in a json a separate sub-folder will be created in a sync folder),
and the values are the links to the albums or playlists in a format that
[spotify-downloader](https://github.com/spotDL/spotify-downloader) supports.

## Run

```shell
./sync.py
```
