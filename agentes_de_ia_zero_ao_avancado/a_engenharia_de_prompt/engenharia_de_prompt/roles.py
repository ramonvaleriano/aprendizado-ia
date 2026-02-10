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
            ],
        )

        response = response_complete.choices[0].message.content

        print("Mensagem de Retorno: ")
        print(response)

        return response

    async def role_second(self):
        system_prompt = (
            "Você é um especialista em IA que responde de forma clara e objetiva"
        )
        user_prompt = "Explique a importância de LLMS com baixa latência."
        assistant = "LLMs com baixa latência permitem respostas mais rápidas, o que melhora a experiência do usuário."
        response_complete = self.client.chat.completions.create(
            model=self.__model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
                {"role": "assistant", "content": assistant},
                {
                    "role": "user",
                    "content": "Pode dar exemplos de aplicações práticas?",
                },
            ],
        )

        response = response_complete.choices[0].message.content

        print("Mensagem de Retorno: ")
        print(response)

        return response


async def run_main():
    role_groq = Roles()
    await role_groq.role_second()
