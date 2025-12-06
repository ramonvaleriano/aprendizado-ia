from groq import Groq

from settings import groq_apy_key, model_start

class StructuringOutput:

    def __init__(self):
        self.__model = model_start
        self.__api_key = groq_apy_key
        self.client = Groq(api_key=groq_apy_key)

    def first_output(self):
        # Saída em formato de tabela.
        system_prompt = """
        Você é um historiador especialista em civilizações antigas.
        Sempre responda no formato de tabela:

        | Civilização | Período | Contribuição Marcante | Região |
        | ----------- | ------- | --------------------- | ------ |
        """

        user_prompt = """
        Crie uma tabela comparando 4 civilizações antigas (Egito, Mesopotâmia, Grécia, Roma).
        """

        response_output_one = self.client.chat.completions.create(
            model=self.__model,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
            temperature=0.5
        )

        response = response_output_one.choices[0].message.content

        print("Response:")
        print(response)

        return response
    
    def second_output(self):
        # Saída em uma lista simples.
        system_prompt = "Você é um critico de cinema que apresenta informações em listas claras."
        user_prompt = "Liste 5 filmes premiados no Oscar que marcaram a história do cinema."

        response_list_simple = self.client.chat.completions.create(
            model=self.__model,
            temperature=0.6,
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

        response = response_list_simple.choices[0].message.content

        print(f"Response: {response}")

        return response
    
    def thrird_output(self):
        # Lista númerada.
        system_prompt = """
        Você cria listas númeradas no formato:
        1. [Título]: [Descrição curta]
        """
        user_prompt = "Liste 4 estrategias de treinameto usda por atletas olimpicos."

        response_list_numeric = self.client.chat.completions.create(
            model=self.__model,
            temperature=0.7,
            max_completion_tokens=200,
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

        response = response_list_numeric.choices[0].message.content

        print("Response: ")
        print(response)

        return response
    
    def fourth_output(self):
        # Lista Hierarquica
        system_prompt = """
        Você organiza informações em listas hierarquicas no formato:
        * Categoria Principal
            - Subcategoria 1
            - Subcategoria 2
        """

        user_prompt_hierarquia = "Organize áreas da ciência em categorais: Física, Biologia, Química"

        response_hierarquia = self.client.chat.completions.create(
            model=self.__model,
            temperature=0.6,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt_hierarquia
                }
            ]
        )

        response = response_hierarquia.choices[0].message.content

        print("Response: ")
        print(response)

        return response

    def fifth_output(self):
        # Parágrafos Estruturados
        system_prompt = """
        Você escreve textos estruturados no formato:

        INTRODUÇÃO: [1-2 frases de contexto]
        DESENVOLVIMENTO: [Explica datalhadas]
        CONCLUSÃO: [Síntese Final]
        """

        user_prompt = "Explique a importância da moda como expressão cultural"

        response_output = self.client.chat.completions.create(
            model=self.__model,
            temperature=0.7,
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

        response = response_output.choices[0].message.content

        print("Response: ")
        print(response)

        return response

    def sixth_output(self):
        # Formato Customizado.

        system_prompt = """
        Você cria cards informativos sobre missões espaciais no formato:

        🚀 MISSÃO: [Nome]
        📅 ANO: [Ano]
        🌌 OBJETIVO: [Resumo em 1 frase]
        🔭 RESULTADO: [Principais descobertas]
        """
        user_prompt = "Crie um card sobre a missão Voyager 1."

        response_output = self.client.chat.completions.create(
            model=self.__model,
            temperature=0.6,
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

        response = response_output.choices[0].message.content

        print("Response: ")
        print(response)

        return response

    

test_outputs = StructuringOutput()
test_outputs.sixth_output()