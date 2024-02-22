from lambda_function import handler

conversation = [
    {"role": "system", "content": "You are a friendly chatbot."},
    {"role": "user", "content": "Hello, how are you?"},
]

event = {"conversation": conversation, "temperature": 0.5}
print(handler(event, None))
