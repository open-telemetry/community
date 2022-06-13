# OpenTelemetryYoutube Tool

## Pre-requisites

* [dotnet](https://dotnet.microsoft.com/download) installed to run
  the application
* Your user need to be manager or owner of the channel
* Configure access to use the [YouTube Data API](https://developers.google.com/youtube/v3/getting-started).
  Steps are roughly as follows:
  1. Create a project using the [Google Developers Console](https://console.developers.google.com/).
  2. From the [Enabled APIs page](https://console.developers.google.com/apis/enabled)
     make sure the YouTube Data API v3 is enabled for the project.
  3. Create OAuth credentials from the [Credentials page](https://console.cloud.google.com/apis/credentials).
  4. Configure the consent screen from the [OAuth consent screen page](https://console.cloud.google.com/apis/credentials/consent).

## Configuration

Running the tool requires the following environment variables to be set:

* `YOUTUBE_API_CLIENT_ID`
* `YOUTUBE_API_CLIENT_SECRET`
* `YOUTUBE_API_ACCESS_TOKEN`
* `YOUTUBE_API_REFRESH_TOKEN`

The `YOUTUBE_API_CLIENT_ID` and `YOUTUBE_API_CLIENT_SECRET` variables should be
set with the appropriate values from the OAuth credentials created when
configuring access to the [YouTube Data API](https://developers.google.com/youtube/v3/getting-started).

Generate an access and refresh token as follows:

1. The following command works on a Mac and opens a browswer window
   facilitating the generation of an authorization code:

    ```shell
    open "https://accounts.google.com/o/oauth2/auth?client_id=$YOUTUBE_API_CLIENT_ID&redirect_uri=urn:ietf:wg:oauth:2.0:oob&scope=https://www.googleapis.com/auth/youtube&response_type=code"
    ```

2. Run the following curl command using the authorization code generated in the
   previous step:

    ```shell
    curl \
    -d "client_id=$YOUTUBE_API_CLIENT_ID" \
    -d "client_secret=$YOUTUBE_API_CLIENT_SECRET" \
    -d "redirect_uri=urn:ietf:wg:oauth:2.0:oob" \
    -d "grant_type=authorization_code" \
    -d "code=PUT_AUTH_CODE_FROM_STEP_1_HERE" \
    https://accounts.google.com/o/oauth2/token
    ```

    Sample response:

    ```json
    {
      "access_token": "YOUR_ACCESS_TOKEN",
      "expires_in": 3599,
      "refresh_token": "YOUR_REFRESH_TOKEN",
      "scope": "https://www.googleapis.com/auth/youtube",
      "token_type": "Bearer"
    }
    ```

3. Set the `YOUTUBE_API_ACCESS_TOKEN` and `YOUTUBE_API_REFRESH_TOKEN`
   environment variables to the values retreived in the previous step.

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
