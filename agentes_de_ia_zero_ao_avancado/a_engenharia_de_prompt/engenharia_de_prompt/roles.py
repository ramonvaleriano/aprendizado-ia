from groq import Groq
from settings import GROQ_API, MODEL_START


class Roles:
    """
    Compreendendo as Roles
        Roles: São os papeis

        User: Mensagem do usuário
        Assistant: Resposta do Modelo
        System: Instruções de comportamento para o modelo

        Em um agente de IA você terá um role e um content, o role são o papeis que
        deve-se ser dados a instruções de um agente. O content e de fato o conteúdo
        gerado ou enviado ao/do agente.
    """

    def __init__(self):
        self.__model = MODEL_START
        self.__api_key = GROQ_API
        self.client = Groq(api_key=self.__api_key)

    async def role_first(self):
        response_complete = self.client.chat.completions.create(
            model=self.__model,
            messages=[
                {
                    "role": "user",
                    "content": "Me explique de forma resumida o que são as LLMs.",
                }
            ]
        )

        response = response_complete.choices[0].message.content

        print("Mensagem de Retorno: ")
        print(response)

        return response
    

async def run_main():
    role_groq = Roles()
    await role_groq.role_first()
