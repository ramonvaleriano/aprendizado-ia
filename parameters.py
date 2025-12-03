from groq import Groq
from settings import groq_apy_key, model_start

class Parameters:
    """
        temperature: Controla a alatoridade das respostas. Valores entre 0.0 e 1.0 são aceitos.
        max_completion_tokens: define o número máximo de tokens que podem ser gerados pelo modelo.
                               Esse parâmetro substitui o max_tokens em desuso.
        top_p: Controla a diversidade via "nucleus sampling" -- em torno de 0.5 significa considerar
               apenas tokens que somam 50% da probabilidade. 
    """
    def __init__(self):
        self.__api_key = groq_apy_key
        self.__model = model_start
        self.client = Groq(api_key=self.__api_key)

    def firt_chat_parameters(self, prompt="Escreva uma frase poética sobre o anoitecer"):
        "Usando temperature baixa, sendo mais deterministico. (0.0)"
        
        response_low = self.client.chat.completions.create(
            model=self.__model,
            temperature=0.0,
            messages=[
                {
                    "role": "system",
                    "content": "Você é um poeta minimalista que descreve a natureza de forma simples e direta"
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        response = response_low.choices[0].message.content

        print(f"Response: {response}")

        return response
    
    def second_chat_parameters(self, prompt="Escreva uma frase poética sobre o anoitecer"):
        "Usando uma temperatura mais equilibrada, 0.7"

        response_medium = self.client.chat.completions.create(
            model=self.__model,
            temperature=0.7,
            messages=[
                {
                    "role": "system",
                    "content": "Você é um poeta classico que mistura a imagens da natureza."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        response = response_medium.choices[0].message.content

        print(f"Response: {response}")

        return response
    
    def thrith_chat_parameters(self, prompt="Escreva uma frase poética sobre o anoitecer"):
        "Usando uma temparatura mais criativa, 1.5"

        response_high = self.client.chat.completions.create(
            model=self.__model,
            temperature=1.5,
            messages=[
                {
                    "role": "system",
                    "content": "Você é um poeta surrealista que usa imagens improváveis e linguagem ousada."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        response = response_high.choices[0].message.content

        print(f"Response: {response}")

        return response
    
    def fouth_chat_parameters(self, prompt="Complete a frase: 'A inteligência artifical será...'"):
        "Modelo focado, top_p 0.1"
        response_focused = self.client.chat.completions.create(
            model=self.__model,
            temperature=1.0,
            top_p=0.1,
            messages=[
                {
                    "role": "system",
                    "content": "Você é um futurista que faz previsões sérias e objetivas sobre tecnologia"
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        response = response_focused.choices[0].message.content

        print(f"Response: {response}")

        return response

    
test_parameters = Parameters()
test_parameters.fouth_chat_parameters()