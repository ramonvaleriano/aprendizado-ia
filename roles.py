from groq import Groq

from settings import groq_apy_key, model_start


class Roles:
    """
    A Roles são os papeis que nós podemos ter nos nossos prompts. Isso é muito importe pois em um
    agente nós temos as roles e o content, o content é basicamento o conteúdo proprimanente dito,
    a role é o papel daquele prompt e ele pode assumir.

    User: Mensagem de usuário
    Assistent: Resposta do Modelo. Uma forma de controlar a resposta do modelo.
    System: Instruções do comportamente para o modelo. O system vai denotar o comportamento para um modelo.

    """

    def __init__(self):
        self.__model_start = model_start
        self.__groq_apy_key = groq_apy_key
        self.system_prompot = None
        self.client = Groq(
            api_key=self.__groq_apy_key
        )  # Intaciando o cliente com a chave da API groq

    @staticmethod
    def displaying_message(componet_of_message):
        print("\n\nMensagem Generalista: ")
        print(componet_of_message)
        print("\n")
        print(f"Mensagem response: {componet_of_message.choices[0].message.content}")

        return componet_of_message.choices[0].message.content

    def first_chat_completion(self):
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "Me explique de forma reduzida o que são LLMs",
                }
            ],
            model=self.__model_start,
        )

        response = chat_completion.choices[0].message.content

        print(f"Resposta completa: {chat_completion}")
        print("\n\n")
        print(f"Resposta: {response}")

        return response

    def second_chat_completion(self):
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "Você é um especialista em IA que responde de forma clara e objetiva.",
                },
                {
                    "role": "user",
                    "content": "Me explique de forma reduzida o que são LLMs.",
                },
            ],
            model=self.__model_start,
        )

        response = self.displaying_message(chat_completion)

        return response

    def thrith_chat_completion(self):
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "Você é um especialista em IA que responde de forma clara e objetiva.",
                },
                {
                    "role": "user",
                    "content": "Explique a importancia de LLMs com baixa latência.",
                },
                {
                    "role": "assistant",
                    "content": "LLMs com baixa latência permitem que respostas mais rápidas, o que melhora a experiência do usuário.",
                },
                {
                    "role": "user",
                    "content": "Pode dar exemplos de aplicações práticas?",
                },
            ],
            model=self.__model_start,
        )

        reponse = chat_completion.choices[0].message.content

        print(f"Response: {reponse}")

        return reponse

    def fouth_chat_completion(self):
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Você é um especialista em Inteligencia artificial focado em explicar conceitos"
                        "de forma clara, estruturada e prática. Sempre inicie suas respostas com um "
                        "resumo em até 3 linhas, depois detalhe com exemplos reais e aplicações no mundo "
                        "dos negócios e tecnologias. Evite termos excessivamente técnicos sem explicação "
                        "e, quando necessário, use analogias simples. "
                        "Se o ususário pedir código, forneça em python bem comentados."
                    ),
                },
                {
                    "role": "user",
                    "content": "Explique a importância de LLMs com baixa latência",
                },
            ],
            model=self.__model_start,
        )

        response = chat_completion.choices[0].message.content

        print(f"Response: {response}")

        return response


test_roles = Roles()
test_roles.fouth_chat_completion()
