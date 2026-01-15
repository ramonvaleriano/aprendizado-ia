import asyncio
from groq import Groq
from settings import groq_apy_key, model_start


class ComplementText:
    def __init__(self):
        self.__model = model_start
        self.__key = groq_apy_key
        self.client = Groq(api_key=self.__key)

    async def start_client(self):
        system_prompt = "Você é um especialista em melhoria continua."
        user_prompt = "O que é PDCA?"
        response_complete = self.client.chat.completions.create(
            temperature=1.0,
            model=self.__model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )

        response = response_complete.choices[0].message.content

        print(f"Pergunta: {user_prompt}")
        print(f"Resposta: {response}")

        return response


async def run_main():
    complement_text = ComplementText()
    await complement_text.start_client()


asyncio.run(run_main())
