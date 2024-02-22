from llama_cpp import Llama

ERROR_NO_CONVERSATION = {"error": "No body in request"}

llm = Llama(
    model_path="./models/llama-2-7b-chat.Q2_K.gguf",
    chat_format="llama-2"
)


def handler(event, context):
    if "conversation" not in event:
        return ERROR_NO_CONVERSATION

    temperature = 0.5
    if "temperature" in event:
        temperature = event["temperature"]

    max_tokens = None
    if "max_tokens" in event:
        max_tokens = event["max_tokens"]

    output = llm.create_chat_completion(
        messages=event["conversation"], temperature=temperature, max_tokens=max_tokens
    )
    return output
