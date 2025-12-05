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
    

test_outputs = StructuringOutput()
test_outputs.first_output()