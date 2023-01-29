from pytube import YouTube
import ssl
from pytube.cli import on_progress

ssl._create_default_https_context = ssl._create_unverified_context


def download_audio_song(output_path, link):
    youtubeObject = YouTube(link, on_progress_callback=on_progress)
    print(f"Downloading | {youtubeObject.title}")
    try:
        downloaded_path = youtubeObject.\
            streams.\
            get_audio_only().\
            download(output_path=output_path)
        print(f"Download is completed successfully | {downloaded_path}")
    except Exception as e:
        print(f"An error has occurred | {e}")


if __name__ == "__main__":
    file_path = input("Enter youtube link file path: ")
    output_path = input("Enter download location: ")
    with open(file_path, 'r') as f:
        links = f.readlines()

    for link in links:
        download_audio_song(output_path=output_path, link=link)
