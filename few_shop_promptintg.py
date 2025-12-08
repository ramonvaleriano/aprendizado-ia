import asyncio
from groq import Groq

from settings import groq_apy_key, model_start


class FewShopPrompt:
    """
    Técnicas Few Shot Prompting
    - Zero Shot: Sem exemplos, apenas instruções
    - One Shot: Um exemplo para instruir o modelo
    - Few Shot: Múltiplos exemplos para melhor compreensão
    """

    def __init__(self):
        self.__model = model_start
        self.__api_key = groq_apy_key
        self.client = Groq(api_key=self.__api_key)

    async def zero_shot_prompot(self):
        # Quando usamos Zero shot

        system_prompt = """
        Você é um chef renomado
        Receba o nome de um ingrediente e sugira um prato sofisticado onde ele seja protagonista
        """

        user_prompt = """
        Abacate
        """

        response_complete = self.client.chat.completions.create(
            model=self.__model,
            temperature=0.5,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ]
        )

        response = response_complete.choices[0].message.content

        print(f"Response: \n{response}")

        return response
    
async def test_few_shot_prompt():
    few_shot_prompt = FewShopPrompt()
    await few_shot_prompt.zero_shot_prompot()

asyncio.run(test_few_shot_prompt())
