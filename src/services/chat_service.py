from clients.azure_client import create_azure_client
from entities.chat_history import get_cached_chat_history, get_string_parser
from langchain_core.prompts import ChatPromptTemplate


async def send_message(message: str):
    chatHistory = get_cached_chat_history()
    chatHistory.add_message("user", message)

    chat_template = [
        ("system", "You are an AI Assistant that helps codes in python, your name is PYAI")
    ]
    chat_template.extend((msg["role"], msg["content"])
                         for msg in chatHistory.get_chat_history())

    prompt_template = ChatPromptTemplate.from_messages(chat_template)
    model = create_azure_client()
    parser = get_string_parser()

    chain = prompt_template | model | parser

    response = chain.invoke({"text": message})
    chatHistory.add_message("assistant", response)

    return response
