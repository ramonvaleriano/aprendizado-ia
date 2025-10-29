from groq import Groq

from settings import GROQ_API

client = Groq(api_key=GROQ_API)

"""
Roles: São os papeis que o agente tem.

O Agente pode ser dividios em Roles e Contents, os Contents são o conteudo propriamente dito.

User: Mensagem do Usuário
Assistant: Resposta do Modelo
System: Intruções de comportamento para o modelo. 

"""

chat_completion = client.chat.completions.create(
    messages=[{"role": "user", "content": "Olá Mundo"}],
    model="openai/gpt-oss-120b"
)


print(f"Resposta completo do modelo: {chat_completion}")
print("\n")
print(f"Resposta do Agente: {chat_completion.choices[0].message.content}")