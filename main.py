from services.chat_service import send_message
from prompts.system_prompt import SYSTEM_PROMPT


def main():

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    while True:

        question = input("\nVocê: ")

        if question.lower() == "sair":
            print("\nSaindo do sistema...")
            break

        send_message(messages, question)


if __name__ == "__main__":
    main()