# TODO

## Validation
* Create a validation function to validate the input
* List all the validation error cases (to create unit tests)

## Misc
* Configure Logging system (and set the "round/event" trace in DEBUG)

## Infrastructure / Application 
* Create a Makefile with build / deploy command
* Create SQS Queue in template.yaml
* Implement AWS CLI commands to send a message in SQS queue (document in README.md)
* Improve SAM Template to deploy Lambda Function

## Implement `cw-logs-export` Lambda Function
* Save the content to an S3 Bucket
  * Add two environment variables to the function (S3_BUCKET_NAME & S3_PATH_PREFIX)
* How one single handler can process different event source (ex: SQS / API Gateway / Simple event) ?
* Try to use CloudWatch Logs Insight instead of filter SDK
  (IMPORTANT: double check if CloudWatch Logs Insight is not limited to only one execution !)
