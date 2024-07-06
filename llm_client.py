from openai import OpenAI


class LLMClient:
    def __init__(self):
        self.client = OpenAI(
            base_url="http://127.0.0.1:8080/v1", api_key="sk-no-key-required"
        )

    def chat(self, system_prompt, user_prompt, search_results):
        completion = self.client.chat.completions.create(
            model="LLaMA_CPP",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
                {"role": "assistant", "content": str(search_results)},
            ],
        )
        return completion.choices[0].message
