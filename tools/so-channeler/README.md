# StackOverflow -> Slack Question Channeler

This is a Lambda function designed to channel questions from StackOverflow
tagged with `#open-telemetry` into a designated Slack channel.

## Packaging and Deployment

1. Run `pip3 install requests -t ./package` to install the `requests` library
   into the `package` directory.
2. Copy `lambda_function.py` into the `package` directory.
3. Zip the contents of the `package` directory into a zip file named
   `lambda_function.zip`. **Do not zip the `package` directory itself, zip its
   contents**.
4. Upload the zip file to AWS Lambda. Deploy the function.
5. Adjust the timeout to ~1 minute (adjust as needed) and set environment
   variables.
6. Create an EventBridge trigger with the desired schedule (hourly would be
   `cron(0 * * * ? *)`) and set the target to the Lambda function.

## Requirements

The Lambda function requires the following environment variables to be set:

- `SLACK_WEBHOOK_URL`: The URL of the Slack webhook to post to.
- `S3_BUCKET_NAME`: The name of the S3 bucket to store the last timestamp in.

It also requires an IAM Policy and Role. The policy is below (replace
`your-bucket-name` with the name of the bucket created):

``` json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:PutObject"
            ],
            "Resource": "arn:aws:s3:::your-bucket-name/*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "arn:aws:logs:*:*:*"
        }
    ]
}
```

Attach this policy to a role and attach the role to the Lambda function.

You will also need a Slack App with Incoming Webhooks enabled. Set the webook
environment variable to the URL given to you by this app.
