from groq import Groq

from settings import groq_apy_key, model_start

class BestPraticsOfPrompts:
    """
        Use Prompts especificos
        Instruções Precisas e Detalhadas
        Controle o formato da resposta
        Use separadores para organizar informações
    """
    def __init__(self):
        self.__api_key = groq_apy_key
        self.__model = model_start
        self.client = Groq(api_key=self.__api_key)

    def first_prompt(self):
        # Prompt vem vago, sem especificidade.
        prompt_vago = "Fale Sobre café"
        response_vago = self.client.chat.completions.create(
            model=self.__model,
            temperature=0.7,
            max_completion_tokens=400,
            messages=[
                {
                    "role": "system",
                    "content": "Você é um especialista em gastronomia"
                },
                {
                    "role": "user",
                    "content": prompt_vago
                }
            ]
        )

        response = response_vago.choices[0].message.content

        print(f"Reponse: {response}")

        return response
    
    def second_prompt(self):
        # Prompt especifico
        prompt_especifc = "liste e explique 3 métodos de preparo de café que realcam diferentes sabores."
        response_especifc = self.client.chat.completions.create(
            model=self.__model,
            temperature=0.7,
            max_completion_tokens=400,
            messages=[
                {
                    "role": "system",
                    "content": "Você é um especilista em grastronomia."
                },
                {
                    "role": "user",
                    "content": prompt_especifc
                }
            ]
        )

        response = response_especifc.choices[0].message.content

        print(f"Reponse: {response}")

        return response
    
    def third_prompt(self):
        # Prompt Genérico
        prompt_generico = "Escreva sobre viagens na Europa"

        response_generic = self.client.chat.completions.create(
            model=self.__model,
            temperature=0.7,
            max_completion_tokens=400,
            messages=[
                {
                    "role": "system",
                    "content": "Você um guia de viagens"
                },
                {
                    "role": "user",
                    "content": prompt_generico
                }
            ]
        )

        response = response_generic.choices[0].message.content

        print(f"Reponse: {response}")

        return response
    
    def fouth_prompt(self):
        # Prompt detalhado
        prompt_detalhadao = """Monte um roteiro de 5 dias para Paris.
        Cada dia deve conter: (1) ponto turístico principal,
        (2) atividade gastronômica e (3) sugestão de transporte.
        """
        response_detalhado = self.client.chat.completions.create(
            model=self.__model,
            temperature=0.7,
            max_completion_tokens=400,
            messages=[
                {
                    "role": "system",
                    "content": "Você é um guia de viagens especializado em roteiros práticos."
                },
                {
                    "role": "user",
                    "content": prompt_detalhadao
                }
            ]
        )

        response = response_detalhado.choices[0].message.content

        print(f"Reponse: {response}")

        return response

test_best_pratics = BestPraticsOfPrompts()
test_best_pratics.fouth_prompt()