from dataclasses import dataclass

from tidal_dl_ng.constants import QualityVideo
from dataclasses_json import dataclass_json
from tidalapi import Quality


@dataclass_json
@dataclass
class Settings:
    skip_existing: bool = False
    album_cover_save: bool = True
    lyrics_save: bool = False
    # TODO: Implement API KEY selection.
    api_key_index: bool = 0
    album_info_save: bool = False
    video_download: bool = True
    multi_thread: bool = False
    download_delay: bool = True
    download_base_path: str = "./download/"
    quality_audio: Quality = Quality.low_320k
    quality_video: QualityVideo = QualityVideo.P480
    use_playlist_folder: bool = True
    format_album: str = "Albums/{artist_name} - {title}/{track_num}. {artist_name} - {track_title}"
    format_playlist: str = "Playlists/{playlist_name}/{artist_name} - {track_title}"
    format_mix: str = "Mix/{mix_name}/{artist_name} - {track_title}"
    format_track: str = "Tracks/{artist_name} - {track_title}"
    format_video: str = "Videos/{artist_name} - {track_title}"
    video_convert_mp4: bool = True


@dataclass_json
@dataclass
class HelpSettings:
    skip_existing: str = "Do not download, if file already exists."
    album_cover_save: str = "Safe cover to album folder."
    lyrics_save: str = "Safe lyrics to audio file."
    api_key_index: str = "Set the device API KEY."
    album_info_save: str = "Save album info to track?"
    video_download: str = "Allow download of videos."
    multi_thread: str = "Download several tracks in parallel."
    download_delay: str = "Activate randomized download delay to mimic human behaviour."
    download_base_path: str = "Where to store the downloaded media."
    quality_audio: str = (
        'Desired audio download quality: "LOW" (96kbps), "HIGH" (320kbps), '
        '"LOSSLESS" (16 Bit, 44,1 kHz), '
        '"HI_RES" (MQA 24 Bit, 96 kHz), "HI_RES_LOSSLESS" (up to 24 Bit, 192 kHz)'
    )
    quality_video: str = 'Desired video download quality: "360", "480", "720", "1080"'
    use_playlist_folder: str = (
        "Should items of playlist be downloaded to a separate playlist folder or to the tracks folder?"
    )
    # TODO: Describe possible variables.
    format_album: str = "Where to download albums and how to name the items."
    format_playlist: str = "Where to download playlists and how to name the items."
    format_mix: str = "Where to download mixes and how to name the items."
    format_track: str = "Where to download tracks and how to name the items."
    format_video: str = "Where to download videos and how to name the items."
    video_convert_mp4: str = (
        "Videos are downloaded as MPEG Transport Stream (TS) files. With this option each video "
        "will be converted to MP4. FFMPEG must be installed and added to your 'PATH' variable."
    )


@dataclass_json
@dataclass
class Token:
    token_type: str | None = None
    access_token: str | None = None
    refresh_token: str | None = None
    expiry_time: float = 0.0