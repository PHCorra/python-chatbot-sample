from functools import lru_cache
from langchain_core.output_parsers import StrOutputParser


class Message:
    def __init__(self, role, content):
        self.role = role
        self.content = content


class ChatHistory():
    def __init__(self):
        self.messages = []

    def add_message(self, role, content):
        message = Message(role, content)
        self.messages.append(message)

    def get_chat_history(self):
        return [{"role": msg.role, "content": msg.content} for msg in self.messages]


@lru_cache
def get_cached_chat_history():
    return ChatHistory()


@lru_cache
def get_string_parser():
    return StrOutputParser()
