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
    

test_best_pratics = BestPraticsOfPrompts()
test_best_pratics.first_prompt()