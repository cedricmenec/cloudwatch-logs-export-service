SERVICE=ExportCloudWatchLogGroup

build:
	sam build

sync:
	sam sync --stack-name $(STACK_NAME)
