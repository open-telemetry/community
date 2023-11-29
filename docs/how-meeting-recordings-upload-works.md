# How automatic video upload works

Videos are being recorded using one of [zoom accounts](https://github.com/open-telemetry/community/blob/main/assets.md#zoom-accounts) used by OpenTelemetry. OpenTelemetry zoom accounts are paid for and owned by CNCF.

## Video upload process

- All meetings are configured for automatic recording start. No host present necessary.
- Once meeting is concluded, all participants need to leave the meeting room so the recording will be uploaded to zoom cloud.
- Every recorded meeting (of length 1 minute or longer) is picked up by
  [Zapier](https://github.com/open-telemetry/community/blob/main/assets.md#zapier-account) (https://zapier.com).
  Zapier is configured to automatically post links of the Zoom cloud recordings
  (along with the meeting name, start time and duration) to a
  [publicly viewable Google spreadsheet](https://docs.google.com/spreadsheets/d/1SYKfjYhZdm2Wh2Cl6KVQalKg_m4NhTPZqq-8SzEVO6s).
- It typically takes an hour for the video to be processed by Zapier.

## Video is missing - what to do

- Post the [issue](https://github.com/open-telemetry/community/issues/new), provide the following information:
  - meeting name (e.g. Java SIG)
  - exact datetime with the timezone of the meeting
  - zoom link used
  - duration (as you remember it), approx 30 min, approx 1 hour, etc.
  - any details like meeting was back to back with other meeting and people joined for the next meeting before this one concluded. Or meeting had some strange accounts joining and zoom bombing, etc.

### Steps to find the missing video

- Find the zoom account corresponding to the meeting link. Mapping from static rooms to the account may be found in the zoom bombing document referred from [this page](https://github.com/open-telemetry/community/blob/main/docs/how-to-handle-public-calendar.md#zoom-bombing-prevention).
- If non OpenTelemetry zoom account was used, there will be no recording available. Please contact the owner of the zoom account linked from the event.
- In the zoom account, check if the meeting recording present. If recording is there, it is a Zapier integration issue.
- If recording is missing in zoom account, check the meeting room settings. Make sure that automatic meeting recording is enabled.
- If setting is set, likely the meeting recording was stopped using the host key and the recording doesn't exist.
