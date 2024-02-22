#!/bin/bash
docker run --platform linux/amd64 -d -v /Users/simon/.aws-lambda-rie:/aws-lambda -p 9000:8080 --entrypoint /aws-lambda/aws-lambda-rie lambda-llama:test /usr/local/bin/python -m awslambdaric lambda_function.handler
