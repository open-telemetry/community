# OpenTelemetryYoutube Tool

## Pre-requisites

* [dotnet](https://dotnet.microsoft.com/download/dotnet-core) installed to run the application
* `secret.json` from [Google Console](https://console.developers.google.com/)
* Your user need to be manager or owner of the channel

## How to use

1. Create your OAuth credential at [Google Console](https://console.developers.google.com/)
2. Download the `secret.json`
3. Build and run the application:

* `dotnet build`
* `dotnet run`

## What it does

This tool will process the private videos that we have in [OpenTelemetry channel](https://www.youtube.com/channel/UCHZDBZTIfdy94xMjMKz-_MA) and will move it to public if:

1. The length of the video is greater then 30 minutes
2. The title does not start with our current placeholder (`202x-xx-xx meeting`)

When it finds a video, it will update the title and mark as public.
