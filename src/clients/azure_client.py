from dotenv import load_dotenv
import os
from langchain_openai import AzureChatOpenAI


load_dotenv(dotenv_path='../.env')


def create_azure_client():
    print('creating Azure Chat Model')
    model = AzureChatOpenAI(
        openai_api_key=os.getenv("API_KEY"),
        azure_endpoint=os.getenv("ENDPOINT"),
        azure_deployment=os.getenv("DEPLOYMENT_NAME"),
        openai_api_version=os.getenv("OPENAI_API_VERSION")
    )
    print('Azure Chat Model Created')
    return model
