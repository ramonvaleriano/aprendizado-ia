from groq import Groq
from settings import GROQ_API, MODEL_START


class Parameters:
    """
    Temperature: Controla a aleatoriedade das respostas. Valores entre 0.0 e 1.0 são aceitos.
    max_competion_tokens: Define um número mázimo de tokens que podem ser gerados pelo modelo.
                        Esse parâmetro substitui o max_tokens em desuso.
    top_p: Controle diversidade via "nucleus sampling" -  em torno de 0.5 significa considerar
          apeans os tokens que somam 50% da probabilidade.
    """

    def __init__(self):
        self.__model = MODEL_START
        self.__api_key = GROQ_API
        self.client = Groq(api_key=self.__api_key)
        self.temperature = 0.0

    async def parameters_first(self):
        system_prompt = "Você é um poéta minimalista que descreve a natureza de forma simples e direta"
        user_prompt = "Escreva uma frase poética sobre o anoitecer."

        response_complete = self.client.chat.completions.create(
            temperature=self.temperature,
            model=self.__model,
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
    
    async def parameters_second(self):
        system_prompt = "Você é um poéta um poeta clássico que mistura metáforas e imagens da natureza."
        user_prompt = "Escreva uma frase poética sobre o anoitecer."

        self.temperature = 0.7

        response_complete = self.client.chat.completions.create(
            temperature=self.temperature,
            model=self.__model,
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

    async def parameters_third(self):
        system_prompt = "Você é um poéta um poeta clássico que mistura metáforas e imagens da natureza."
        user_prompt = "Escreva uma frase poética sobre o anoitecer."

        self.temperature = 0.7

        response_complete = self.client.chat.completions.create(
            temperature=self.temperature,
            model=self.__model,
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
    parameters_groq = Parameters()
    await parameters_groq.parameters_second()
