from groq import Groq

from settings import GROQ_API

client = Groq(api_key=GROQ_API)


class RolesGroq:
    def __init__(self):
        self._model = "openai/gpt-oss-120b"
    """
    Roles: São os papeis que o agente tem.

    O Agente pode ser dividios em Roles e Contents, os Contents são o conteudo propriamente dito.

    User: Mensagem do Usuário
    Assistant: Resposta do Modelo, controla a resposta do modelo.
    System: Intruções de comportamento para o modelo, define um comportamente que o modelo terá.

    """

    @property
    def chat_simple(self):
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "Me explique de forma reduzida o qu são as LLMs",
                }
            ],
            model=self._model,
        )

        return chat_completion
    
    """
        Vamos usar o System para definir um comportamento para o modelo.
    """

    @property
    def chat_persona_simple(self):
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "Você é um especialista em IA que responde de forma clara e objetiva"
                },
                {
                    "role": "user",
                    "content": "Me explique de forma reduzida o que são as LLMs"
                }
            ],
            model=self._model

        )

        return chat_completion
    
    """
        Assistant: Controlar a resposta do modelo.
    """
    @property
    def chat_persona_complex(self):
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "Você é um expecialista em IA que responde de forma clara e objetiva"
                },
                {
                    "role": "user",
                    "content": "Expliquea importancia de LLMs com baixa latência"
                },
                {
                    "role": "assistant",
                    "content": "LLMs com baixa latência permitem respostas mais rápidas, o que melhora a experiência do usuário"
                },
                {
                    "role": "user",
                    "content": "Pode dar exemplos de aplicações?"
                }
            ],
            model=self._model
        )
        return chat_completion
    
    """
        System mais complexos, um pouco mais parecido do que veremos no mundo real.
    """

    @property
    def chat_persona_system_complex(self):
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Você é um especialista em Inteligência Artificial focado em explicar conceitos de forma clara, estruturada e prática."
                        "Sempre inicie suas respostas com um resumo em até 3 linhas,"
                        "depois detalhe com exemplos reais e aplicações no mundo dos negócios e tecnologia."
                        "Evite termos excessivamente técnicos sem explicação"
                        "e, quando necessário, use analogias simples."
                        "Se o usuário pedir código, forneça exemplos em Python bem comentados."
                    )
                },
                {
                    "role": "user",
                    "content": "Explique a importância de LLMs com baixa latência"
                }
            ],
            model=self._model
        )
        return chat_completion

roles_groq = RolesGroq()
chat_completion = roles_groq.chat_persona_system_complex

print(f"Resposta completo do modelo: {chat_completion}")
print("\n")
print(f"Resposta do Agente: {chat_completion.choices[0].message.content}")
