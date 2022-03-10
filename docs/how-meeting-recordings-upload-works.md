# How automatic video upload works

Videos are being recorded using one of [zoom accounts](https://github.com/open-telemetry/community/blob/main/assets.md#zoom-accounts) used by OpenTelemetry. OpenTelemetry zoom accounts are paid for and owned by CNCF.

## Video upload process

- All meetings are configured for automatic recording start. No host present necessary.
- Once meeting is concluded, all participants need to leave the meeting room so the recording will be uploaded to zoom account.
- Every recorded meeting is picked up by [Splain](https://github.com/open-telemetry/community/blob/main/assets.md#splain-account) (https://splain.io/). Splain is configured to automatically copy meetings from zoom to Youtube. It typically takes an hour for the video to be processed by Splain.
- Splain uploads all meetings as private (not published). People with the access to OpenTelemetry [Youtube channel](https://github.com/open-telemetry/community/blob/main/assets.md#youtube-channel-opentelemetry) can see both - private and public videos.
- A custom built tool [OpenTelemetryYoutube](https://github.com/open-telemetry/community/tree/main/tools/OpenTelemetryYoutube) is designed to fix up the title of the video by including it's date into the title and marking video as public.
- The tool is manually run by volunteer. The frequency of the run depends on this volunteer availability. The work to improve situation is tracked here: https://github.com/open-telemetry/community/issues/863.
- Note, short videos are not processed by the tool as they typically are accidental meeting link clicks, not a real meetings.

## Video is missing - what to do

- Post the [issue](https://github.com/open-telemetry/community/issues/new), provide the follwowing information:
  - exact datetime with the timezone of the meeting
  - meeting room (zoom link used)
  - duration (as you remember it), approx 30 min, approx 1 hour, etc.
  - any details like meeting was back to back with other meeting and people joined for the next meeting before this one concluded. Or meeting had some strange accounts joining and zoom bombing, etc.

### Steps to find the missing video

- Check the YouTube account. If meeting recording is there, but not private, make sure the OpenTelemetryYoutube tools is running. Video can be made public manually if urgent.
- Find the zoom account corresponding to the meeting link. Mapping from static rooms to the account may be found in the zoom bombing document referred from [this page](https://github.com/open-telemetry/community/blob/main/docs/how-to-handle-public-calendar.md#zoom-bombing-prevention).
- If non Opentelemetry zoom account was used, there will be no recording available. Please contact the owner of the zoom account linked from the event.
- In the zoom account, check if the meeting recording present. If recording is there, but missing on Youtue, it is a Splain issue. Contact CNCF rep listed on [assets page](https://github.com/open-telemetry/community/blob/main/assets.md##splain-account) to file a support ticket with Splain. Video can be downloaded and manually uploaded to YouTube if urgent.
- If recording is missing in zoom account, check the meeting room settings. Make sure that automatic meeting recording is enabled.
- If setting is set, likely the meeting recording was stopped using the host key and the recording doesn't exist.
