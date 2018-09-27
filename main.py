from __future__ import unicode_literals
from twitch.client import TwitchClient
import os
import youtube_dl
from dotenv import load_dotenv, find_dotenv
load_dotenv('.env')

# List of users to track

oxc_streamer_list = os.getenv("OXC_STREAMERS").split(',')
BASE_DIR = os.getenv("BASE_DIR")
CLIENT_ID = os.getenv("CLIENT_ID")


def download_vod(url, video_name, username):
    if os.path.isdir(BASE_DIR + username):
        os.chdir(BASE_DIR + username)
    else:
        os.mkdir(BASE_DIR + username)
        os.chdir(BASE_DIR + username)

    ydl_opts = {
        'restrictfilenames': True
    }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception:
        print("Download error, will come back to it")


def check_completed_download(video_name, streamer):
    pass


def extract_metadata(vod):
    pass


def main():
    print("Streamers to check")
    print(oxc_streamer_list)
    try:
        client = TwitchClient(client_id=CLIENT_ID)

        users = client.users.translate_usernames_to_ids(oxc_streamer_list)

        for user in users:
            print("Checking user: {username}".format(username=user.name))
            # now that we have the userid we can look at their videos
            videos = client.channels.get_videos(user.id, broadcast_type='archive')
            for video in videos:
                print("({username}): Looking at vod: {vodname}".format(username=user.name, vodname=video.title))
                # for each video check to see if it is an OXC video
                if 'OXC' in video.title or 'OWXC' in video.title or 'OWXL' in video.title:
                    if video.status == 'recorded':
                        #if not check_completed_download(video.url):
                        print("VOD missing, kicking off download")
                        download_vod(video.url, video.title, user.name)
                        #else:
                         #   print("VOD already downloaded, skipping...")
                    else:
                        print("VOD creation still in progress, will get to this later")
                else:
                    print("Not an OXC video, skipping...")
    except Exception:
        print("oops, we hit a bug")


main()