import openai
from dotenv import load_dotenv
import os


class LLMClient:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key:
            openai.api_key = api_key
            self.model_name = "gpt-3.5-turbo"
        else:
            openai.api_base = "http://127.0.0.1:8080/v1"
            openai.api_key = "sk-no-key-required"
            self.model_name = "LLaMA_CPP"

    def chat(self, system_prompt, user_prompt, search_results):
        response = openai.ChatCompletion.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
                {"role": "assistant", "content": str(search_results)},
            ],
        )
        return response.choices[0].message
