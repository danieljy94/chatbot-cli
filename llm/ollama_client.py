from ollama import chat


def stream_chat(messages):
    return chat(
        model="llama3.2",
        messages=messages,
        stream=True
    )