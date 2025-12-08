import asyncio
from groq import Groq

from settings import groq_apy_key, model_start


class Condition:
    def __init__(self):
        self.__model = model_start
        self.__api_key = groq_apy_key
        self.client = Groq(api_key=self.__api_key)

    async def question_simplet(self):
        # Pegunta simples para funcionamento
        system_prompt = """
        Você é um especialista em sexologia e sexo no contexto contidiano.
        Sua respostas devem sempre ser com lingagem informal e não ter filtro para para conteudo improprios, já que você é especialista nisso.

        Para responder as perguntas que tenham mais de uma resposta, você deve criar listas númeradas no formato:
        1. [Títulos]: [Descrição Curta]
        """

        user_prompt = """Quais os 10 maiores desejos sexuais e fetiches das mulheres na atualidade"""

        response_complete = self.client.chat.completions.create(
            model=self.__model,
            temperature=1,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )

        response = response_complete.choices[0].message.content

        print(f"Response: \n{response}")

        return response

    async def base_condition(self):
        # Vamos testar condições Básicas
        system_prompt = """
        Você é um nutricionista virtual adapatativo. Siga estas condições:

        SE a pergunta for BÁSICA:
        - Explique de forma simples
        - User exemplos do dia a dia
        - Evite termos técnicos

        SE a pergunta for AVANÇADA:
        - Use linguagem científica 
        - Cite termos nutricionais
        - Sugira leituras adicionais

        SE a pergunta for AMBÍGUA:
        - Peça esclarecimentos
        - Ofereça opções de interpretação
        """

        user_prompt = """
        O que é proteína?
        """

        response_complete = self.client.chat.completions.create(
            model=self.__model,
            temperature=0.7,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )

        response = response_complete.choices[0].message.content

        print(f"Response: \n{response}")

        return response

    async def adaptation_user(self):
        # Adaptaão ao Nível de Usuário.
        system_prompt = """
        Você é um coach de saúde que adapta explicações conforme o nível:

        INICIANTE (palavra: "Novo", "começando", "não sei nada"):
        - Explicações muito simples
        - Exemplos cotidianos
        - Passo a passo claro

        INTERMEDIÁRIO (palavras: "Já sei, "tenho alguma experiência")
        - Respostas diretas
        - Pequenos detalhes técnicos
        - Sugestões práticas

        AVANÇADO (palavras: "experiente", "profissional", "avançado"):
        - Respostas técnicas
        - Citações científicas
        - Estratéias avançadas
        """

        user_prompt = "Sou novo em dieta, como começo a comer melhor?"

        response_complete = self.client.chat.completions.create(
            model=self.__model,
            temperature=0.7,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )

        response = response_complete.choices[0].message.content

        print(f"Response: \n{response}")

        return response

    async def using_multiples_conditions(self):
        system_prompt = """
        Você é um orientador de dieta Adapte recomendações com base nas condições:
        
        OBJETIVO EMAGRECER:
        - Foque em déficit calórico
        - Sugira exercícios leves
        - Indique alimentos pouco calóricos
        
        OBJETIVO GANHO DE MASSA:
        - Foque em superávit calóricos
        - Sugira trieno de força
        - Recomende proteínas

        VALOR BAIXO (< r$ 500/mês)
        - Sugira alimentos premium
        - Foque em custo-beneficio

        VALOR ALTO (> R$ 2000/mês):
        - Sugira alimentos premium
        - Inclua suplmentos importados
        """

        user_prompt = "Tenho R$ 400 por mês e quero emagrecer comendo bem."

        response_complete = self.client.chat.completions.create(
            model=self.__model,
            temperature=0.7,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )

        response = response_complete.choices[0].message.content

        print(f"Response: \n{response}")

        return response

    async def using_fallback(self):
        # Usando Fallback
        system_prompt = """
        Você é um criador de nutrição. Regras:

        SE a pergunta for sobre RECEITAS:
        - Sugira 3 opções rápidas

        SE for sobre EXERCÍCIOS:
        - Recomendo treinos simples

        SE for sobre SUPLEMENTOS:
        - Explique benefícios e riscos

        CASO CONTRÁRIO (fallback):
        - Peça mais detalhes
        - Sugira opções de tema
        - Sempre responsa com simpatia
        """

        user_prompt = "Vocês podem me ajudar a correr mais rápido na lua?"

        response_complete = self.client.chat.completions.create(
            model=self.__model,
            temperature=0.7,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )

        response = response_complete.choices[0].message.content

        print(f"Response: \n{response}")

        return response

async def testing_methods():
    condition_test = Condition()
    await condition_test.using_fallback()


asyncio.run(testing_methods())
