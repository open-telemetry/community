#!/bin/bash

file=${VOTERS_ROLL_PATH:-"./voters-roll.csv"}
dryrun="true"

command -v gh 1>/dev/null 2>&1
if [ $? != 0 ]; then
    echo "The command 'gh' is expected to exist and be configured in order to make comments to GitHub issues."
    exit 1
fi

while getopts f:i:d: flag
do
    case "${flag}" in
        i) issue=${OPTARG};;
        d) dryrun=${OPTARG};;
    esac
done

if [[ -z $issue ]]; then
    echo "Please, specify the issue URL. Ex.: $0 -i https://github.com/open-telemetry/community/issues/1173"
    exit 0
fi

if [ ! -f $file ]; then
    echo "Please, specify an existing input file as a VOTERS_ROLL_PATH env variable"
    exit 0
fi

header="We invite the people mentioned in this comment to vote in the OpenTelemetry Governance Committee, as they have provided more than 20 contributions to the project over the last year via GitHub. Your contributions were comments, code reviews, pull requests, among others. Thank you!\n"
msg=${header}
counter=0

echo -e "Reading the file ${file} and creating comments for the issue ${issue}\n"
while read -r line;
do
    re="^(.+)\,(.+)$"
    [[ $line =~ $re ]]
    handle="${BASH_REMATCH[1]}"
    contributions="${BASH_REMATCH[2]//[$'\r\n']}"

    if [[ -z $handle ]]; then
        continue
    fi

    msg="${msg}\\n* @${handle}"
    ((counter++))

    if (( counter >= 50 )); then
        # reached 50 mentions, create the comment
        if [ "$dryrun" = true ]; then
            echo -e $msg
        else
            echo -e $msg | gh issue comment "${issue}" -F -
        fi

        # reset
        msg=${header}
        counter=0
    fi
done < ${file}

if (( counter > 0 )); then
    if [ "$dryrun" = true ]; then
        echo -e $msg
    else
        echo -e $msg | gh issue comment "${issue}" -F -
    fi
fi