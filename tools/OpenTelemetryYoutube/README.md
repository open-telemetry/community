# OpenTelemetryYoutube Tool

## Pre-requisites

* [dotnet](https://dotnet.microsoft.com/download/dotnet-core) installed to run
  the application
* `secret.json` from [Google Console](https://console.developers.google.com/)
* Your user need to be manager or owner of the channel

## How to use

1. Create your OAuth credential at [Google
   Console](https://console.developers.google.com/)
2. Download the `secret.json`
3. Build and run the application:

* `dotnet build`
* `dotnet run path_to_secrets.json`

This will filter the total video duration to be deleted (if time less then 5
minutes, it will automatically delete):

* `dotnet run path_to_secrets.json 5`

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
