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

    async def best_pratics_second(self):
        """Prompt Especifico"""
        system_prompt = "Você é um especialista em gastronimia."
        user_prompt = "Liste e expique 3 métodos de preparo de café que realçam diferentes sabores."

        response_complete = self.client.chat.completions.create(
            model=self.__model,
            temperature=self.temperature,
            max_completion_tokens=800,
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

    async def best_pratics_third(self):
        """Instrução genérica"""
        system_prompt = "Você é um guia de viagens."
        user_prompt = "Esecreva sobre viagens na Europa"

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
    
    async def best_pratics_fouth(self):
        """Instrução genérica"""
        system_prompt = "Você é um guia de viagens especializado em roteiros práticos."

        user_prompt = """Monte um roteiro de 5 dias para Paris.
        Cada dia deve conter: (1) ponto turístico principal, 
        (2) atividade gastronômica e (3) sugestão de transporte."""

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
    
    async def best_pratics_fith(self):
        """Sem limite de formato para respostas"""
        system_prompt = "Você é uma nutricionista que fala de alimentos."

        user_prompt = """Quais frutas tropicais famosas"""

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
    
    async def best_pratics_sixth(self):
        """Limitando o formato de saída"""
        system_prompt = "Você é um nutricionista e deve seguir o formato solicitado."

        user_prompt = """Liste exatamente 4 frutas tropicais.
        Use o formato:
        - [Nome]: [1 benefício nutricional em uma frase]"""


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
    await best_pratics.best_pratics_sixth()
