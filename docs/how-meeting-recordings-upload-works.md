# How automatic video upload works

Videos are being recorded using one of [zoom accounts](../assets.md#zoom-accounts) used by OpenTelemetry. OpenTelemetry zoom accounts are paid for and owned by CNCF.

## Video upload process

- All meetings are configured for automatic recording start. No host present necessary.
- Once meeting is concluded, all participants need to leave the meeting room so the recording will be uploaded to zoom cloud.
- Every recorded meeting (of length 1 minute or longer) is picked up by
  [Zapier](../assets.md#zapier-account) (https://zapier.com).
  Zapier is configured to automatically post links of the Zoom cloud recordings
  (along with the meeting name, start time and duration) to a
  [publicly viewable Google spreadsheet](https://docs.google.com/spreadsheets/d/1SYKfjYhZdm2Wh2Cl6KVQalKg_m4NhTPZqq-8SzEVO6s).
- It typically takes an hour for the video to be processed by Zapier.

## Video archival process

- Meetings older than 6 months are manually removed from the publicly viewable spreadsheet. Direct links to the recordings will still work after this. Follow these steps to archive links:
  1. Add any entries on the public spreadsheet to the ['Zoom recordings archive' spreadsheet](https://docs.google.com/spreadsheets/d/1U34Ae4D8EMhMbrFujdSRjoHBae3o9pvptLO1c6X4RPI/edit?usp=sharing). This spreadsheet is only viewable by the admin GSuite account.
  2. Remove the entries from the public spreadsheet.

## Video is missing or no longer available in spreadsheet - what to do

- Post an [issue](https://github.com/open-telemetry/community/issues/new) with the following information:
  - meeting name (e.g. Java SIG)
  - exact datetime with the timezone of the meeting
  - zoom link used
  - duration (as you remember it), approx 30 min, approx 1 hour, etc.
  - any details like meeting was back to back with other meeting and people joined for the next meeting before this one concluded. Or meeting had some strange accounts joining and zoom bombing, etc.
  - If older than 6 months, provide a rationale for requesting the meeting recording (e.g. what topic you are interested in learning more about).

### Steps to find the missing video

- If older than 6 months, check the ['Zoom recordings archive' spreadsheet](https://docs.google.com/spreadsheets/d/1U34Ae4D8EMhMbrFujdSRjoHBae3o9pvptLO1c6X4RPI/edit?usp=sharing) for the meeting link.
- Otherwise
  - Find the zoom account corresponding to the meeting link. Mapping from static rooms to the account may be found in the zoom bombing document referred from [this page](../docs/how-to-handle-public-calendar.md#zoom-abuse-prevention).
  - If non OpenTelemetry zoom account was used, there will be no recording available. Please contact the owner of the zoom account linked from the event.
  - In the zoom account, check if the meeting recording present. If recording is there, it is a Zapier integration issue.
  - If recording is missing in zoom account, check the meeting room settings. Make sure that automatic meeting recording is enabled.
  - If setting is set, likely the meeting recording was stopped using the host key and the recording doesn't exist.
