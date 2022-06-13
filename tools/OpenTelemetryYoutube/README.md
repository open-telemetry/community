# OpenTelemetryYoutube Tool

## Pre-requisites

* [dotnet](https://dotnet.microsoft.com/download) installed to run
  the application
* Your user need to be manager or owner of the channel
* OAuth credentials from [Google Console](https://console.developers.google.com/)

## Configuration

Running the tool requires the following environment variables to be set:

* `YOUTUBE_API_CLIENT_ID`
* `YOUTUBE_API_CLIENT_SECRET`
* `YOUTUBE_API_ACCESS_TOKEN`
* `YOUTUBE_API_REFRESH_TOKEN`

## How to use

Build and run the application:

* `dotnet build`
* `dotnet run`

This will filter the total video duration to be deleted (if time less then 5
minutes, it will automatically delete):

* `dotnet run 5`

## What it does

This tool will process the private videos that we have in [OpenTelemetry
channel](https://www.youtube.com/channel/UCHZDBZTIfdy94xMjMKz-_MA) and will move
it to public if:

1. The length of the video is greater then 20 minutes
2. The title does not start with our current placeholder (`202x-xx-xx meeting`)

If the tool encounters a video with the title "Governance Committee", it will
process as well, adding the processed date in the beggining of the title and
updating to public.

If the tool encounters a video with total time less then a configured value, it
will automatically delete. The default value is 3 minutes.
