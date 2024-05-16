from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

# client = AzureOpenAI(
#     azure_endpoint="https://azureopenai-vastmindz.openai.azure.com/",
#     api_version="2023-03-15-preview",
#     api_key=os.getenv("OPENAI_API_KEY")
#     )

client = OpenAI(
  api_key=os.environ.get("OPENAI_API_KEY"),
)

def get_completion_from_messages(system_message, user_message, model="gpt-4-turbo", temperature=0, max_tokens=500) -> str:

    messages = [
        {'role': 'system', 'content': system_message},
        {'role': 'user', 'content': f"{user_message}"}
    ]

    response = client.chat.completions.create(model=model,
    messages=messages,
    temperature=temperature, 
    max_tokens=max_tokens)

    return response.choices[0].message.content

if __name__ == "__main__":
    system_message = "You are a helpful assistant"
    user_message = "Hello, how are you?"
    print(get_completion_from_messages(system_message, user_message))