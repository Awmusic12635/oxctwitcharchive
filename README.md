# oxctwitcharchive
oxctwitcharchive is a basic python script to archive all the vods of OXC's streamers.
It reaches out to twitch's API with a list of streamers to check. It looks at all their vods
and sees if there is an OXC vod available and if so it tries to download it. It currently
uses v5 of the twitch api.

## Setup Instructions

1. Rename .env.example to .env
2. Go to https://glass.twitch.tv/console/apps/ and register an application.
3. Grab the client_id and put it in the CLIENT_ID config value in .env
4. Update the BASE_DIR in .env to be the folder you want to download vods to
5. OXC_STREAMERS is a comma separated list of streamers to track. There is a default list
included but you might want to add more.
6. Install the python requirements `pip install -r requirements.txt`

This program is designed to be run in a CRON style and will exit after a run.

## How To Run
Simply call:  `python main.py`

## Example Output
```
(oxctwitcharchive) Alexs-MBP-2:oxctwitcharchive alex$ python main.py
Streamers to check
[u'swift63', u'ohcorbecmycorbec', u'skateactiondj']
Checking user: swift63
(swift63): Looking at vod: Grinding in Diamond
Not an OXC video, skipping...
(swift63): Looking at vod: Fortnite Friendly Fire
Not an OXC video, skipping...
(swift63): Looking at vod: OXC Lucio Ball Tournament
VOD missing, kicking off download
[twitch:vod] 302191197: Downloading vod info JSON
[twitch:vod] 302191197: Downloading vod access token
[twitch:vod] 302191197: Downloading m3u8 information
[download] 100% of 2.43GiB
[ffmpeg] Fixing malformed AAC bitstream in "OXC_Lucio_Ball_Tournament-v302191197.mp4"
```


## Limitations
1. This will only download streams that have "OXC" in the title.
2. It also currently offloads existing download
handling via youtube-dl, making it call this on every run no matter what.
3. There is almost no error handling

## Potential Future Improvements
1. Better error handling
2. Metadata extraction for better folder organization and file naming
3. Check for completed downloads ourselves
4. Maybe daemonize it