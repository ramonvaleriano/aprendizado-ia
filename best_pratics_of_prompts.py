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

    def fith_prompt(self):
        # Sem limite de formato de saída.
        prompt_sem_limite = "Quais são frutas tropicais famosas"

        response_sem_limite = self.client.chat.completions.create(
            model=self.__model,
            temperature=0.7,
            max_completion_tokens=400,
            messages=[
                {
                    "role": "system",
                    "content": "Você é um nutricionista que fala sobre alimentos."
                },
                {
                    "role": "user",
                    "content": prompt_sem_limite
                }
            ]
        )

        response = response_sem_limite.choices[0].message.content

        print(f"Reponse: {response}")

        return response
    
    def sixth_prompt(self):
        # Limitando o formato
        prompt_limite_format = """Liste exatamente 4 frutas tropicais
        Use o formato:
        - [Nome]: [1 Beneficio em um frase]
        """
        response_limite_format = self.client.chat.completions.create(
            model=self.__model,
            temperature=0.7,
            max_completion_tokens=400,
            messages=[
                {
                    "role": "system",
                    "content": "Você é um nutricionista e deve seguir o formato solicitado."
                },
                {
                    "role": "user",
                    "content": prompt_limite_format
                }
            ]
        )

        reponse = response_limite_format.choices[0].message.content

        print(f"Response: {reponse}")

        return reponse
    
    def seventh_prompt(self):
        # Sem delimitadores
        prompt_sem_delimitadores = """
        Analise o desempenho de uma startup:
        Receita 2022: R$2M, Receita 2023: R$3.5M, Receita 2024: R$ 5M.
        Faça observações e dê sugestões
        """

        response_prompt_sem_delimitadores = self.client.chat.completions.create(
            model=self.__model,
            temperature=0.7,
            max_completion_tokens=400,
            messages=[
                {
                    "role": "system",
                    "content": "Você é um consutor de negócios."
                },
                {
                    "role": "user",
                    "content": prompt_sem_delimitadores
                }
            ]
        )

        response = response_prompt_sem_delimitadores.choices[0].message.content

        print(f"Response: {response}")

        return response
    
    def eigth_prompt(self):
        # Com delimitedores
        prompt_com_delimitadore = """
        Analise os seguintes dados de receita anual:

        --- DADOS ---
        2022: R$ 2M
        2023: R$ 3.5M
        2024: R$ 5m
        --- FIM DE DADOS ---

        TAREFA: Identifique o ritmo de crescimento e sugira 2 estrategias de expansão.
        """

        response_com_delimitador = self.client.chat.completions.create(
            model=self.__model,
            temperature=0.7,
            messages=[
                {
                    "role": "system",
                    "content": "Você é um um consultor de negócios e deve considerar apenas os dados entre os delimitadores."
                },
                {
                    "role": "user",
                    "content": prompt_com_delimitadore
                }
            ]
        )

        response = response_com_delimitador.choices[0].message.content

        print(f"Response: {response}")

        return response
    
    def end_prompt(self):
        # Prompt com todas as estrategias
        system_prompt = """
        Você é um estrategista de marketing criativo.
        Sempre siga o formato solicitado e use linguagem clara e objetiva.
        """

        user_prompt = """
        TAREFA: Criar um mini plano e marketing para lançamento de uma aplicativo fitnes.

        --- INFORMAÇÕES ---
        Público: Jovens de 18-30 anos
        Orçamento: R$ 50.000
        Objetivo: 10.000 downloads no primeiro mês
        --- FIM ---

        FORMATO DA RESPOSTA:
        1. POSICIONAMETO (2 frases)
        2. CANAIS DE MARKETING (3 itens númerados)
        3. AÇÃO CRIATIVA PRINCIPAL (1 frase)
        """

        response_complete = self.client.chat.completions.create(
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
            ],
            max_completion_tokens=800
        )

        response = response_complete.choices[0].message.content

        print(f"Response: {response}")

        return response

test_best_pratics = BestPraticsOfPrompts()
test_best_pratics.end_prompt()