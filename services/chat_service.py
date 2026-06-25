from llm.ollama_client import stream_chat
import re

from tools.viacep_tool import search_cep


def extract_cep(text: str):

    match = re.search(
        r"\d{5}-?\d{3}",
        text
    )

    if match:
        return match.group()

    return None

def send_message(messages, question):

    cep = extract_cep(question)

    if cep:
        result_cep = search_cep(cep)

        cep_address = (
            f"O CEP {result_cep['cep']} corresponde a "
            f"{result_cep['logradouro']}, "
            f"bairro {result_cep['bairro']}, "
            f"{result_cep['localidade']}/{result_cep['uf']}."
        )

        print(result_cep)
        return


    messages.append({
        "role": "user",
        "content": question
    })

    response = ""

    stream = stream_chat(messages)

    for chunk in stream:
        content = chunk["message"]["content"]

        response += content

        print(content, end="", flush=True)

    messages.append({
        "role": "assistant",
        "content": response
    })

    print()