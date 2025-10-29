from groq import Groq

from settings import GROQ_API

client = Groq(api_key=GROQ_API)


class RolesGroq:
    """
    Roles: São os papeis que o agente tem.

    O Agente pode ser dividios em Roles e Contents, os Contents são o conteudo propriamente dito.

    User: Mensagem do Usuário
    Assistant: Resposta do Modelo
    System: Intruções de comportamento para o modelo.

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
            model="openai/gpt-oss-120b",
        )

        return chat_completion


roles_groq = RolesGroq()
chat_completion = roles_groq.chat_simple

print(f"Resposta completo do modelo: {chat_completion}")
print("\n")
print(f"Resposta do Agente: {chat_completion.choices[0].message.content}")
