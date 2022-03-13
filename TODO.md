# TODO

## Validation
* Create a validation function to validate the input
* List all the validation error cases (to create unit tests)

## Misc
* Configure Logging system (and set the "round/event" trace in DEBUG)

## Infrastructure / Application 
* Test triggering Lambda Function using SQS
* Implement AWS CLI commands to send a message in SQS queue
* Create SQS Queue in template.yaml
* Improve SAM Template to deploy Lambda Function

## Implement `cw-logs-export` Lambda Function
* Try to use CloudWatch Logs Insight instead of filter SDK
  (IMPORTANT: double check if CloudWatch Logs Insight is not limited to only one execution !)
* How one handler can process different event source (ex: SQS / API Gateway / Simple event) ?
