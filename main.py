from ollama import chat


def main():
    messages = [
        {
            "role": "system",
            "content": """
            Você é um desenvolvedor sênior especializado em:

            - Python
            - IA Generativa
            - LangChain
            - LangGraph
            - PostgreSQL
            - Docker
            - APIs REST

            Regras:
            - Responda sempre em português.
            - Seja objetivo.
            - Mostre exemplos de código quando apropriado.
            - Explique conceitos de forma didática.
            - Se não souber algo, admita a limitação.
            """
        }
    ]

    while True:
        question = input("\nVocê: ")

        if question.lower() == "sair":
            print("Saindo do sistema...")
            break

        messages.append({
            "role": "user",
            "content": question
        })

        stream = chat(
            model="llama3.2",
            stream=True,
            messages=messages
        )

        response = ""

        for chunk in stream:
            content = chunk["message"]["content"]
            response += content
            print(content, flush=True, end="")

        messages.append({
            "role": "assistant",
            "content": response
        })




if __name__ == '__main__':
    main()