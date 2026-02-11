from groq import Groq

from settings import GROQ_API, MODEL_START


class BestPratics:
    """
    Melhores Práticas para Prompts:
    Usas prompts específicos
    Instruções Precisas e Detalhadas
    Controle o formato da resposta
    Use separadores para organizar informações
    """

    def __init__(self):
        self.__model = MODEL_START
        self.__api_key = GROQ_API
        self.client = Groq(api_key=self.__api_key)
        self.temperature = 0.7

    async def best_pratics_first(self):
        """Prompt vago"""
        system_prompt = "Você é um especialista em gastronimia."
        user_prompt = "Fale sobre café."

        response_complete = self.client.chat.completions.create(
            model=self.__model,
            temperature=self.temperature,
            max_completion_tokens=400,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )

        response = response_complete.choices[0].message.content

        print(f"Pergunta: {user_prompt}")
        print("Reponse: ")
        print(response)

        return response


async def run_main():
    best_pratics = BestPratics()
    await best_pratics.best_pratics_first()
