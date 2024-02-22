#!/bin/bash
curl http://localhost:9000/2015-03-31/functions/function/invocations -d '{"conversation": [{"role": "system", "content": "You are a friendly chatbot."},
    {"role": "user", "content": "Hello, how are you?"}]}'
