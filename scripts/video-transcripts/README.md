# YouTube Transcripts

This directory contains a small script which fetches transcripts from the YouTube API, so that we can 
keep text/markdown corresponding to the transcripts of the videos that the community produces.

## Setup

* `python3 -m venv venv`
* `source venv/bin/activate`
* `pip3 install -r requirements.txt`

## Configure Environment

Edit `.env` file and set `API_KEY` to the correct value for YouTube
Optionally, add `OPENAI_API_KEY` if you intend to use the categorizer

## Run & Pull Transcripts!

Typical usage will involve a YouTube Channel ID, which is in the [URL for the channel](https://www.youtube.com/channel/UCHZDBZTIfdy94xMjMKz-_MA)

From within this directory, we'd place transcripts in that directory off of the root.

```
python3 transcripts.py \
    --channel UCHZDBZTIfdy94xMjMKz-_MA \
    --path ../../transcripts
```

## Need a YouTube Key?

* Have a GCP project
* Go to a GCP project, make sure YouTube Data API v3 is enabled
* Create an API key in that project and use that for this value.

