from settings import GROQ_API
from groq import Groq


class ParamsGroq:
    """
    temperature: controla a aleatoridade das respostas. Valores entre 0.0 a 1.0 são aceitos.
    max_comletion_tokens: define o número máixmo de tokens que podem ser gerados pelo modelo. Esse parâmetro substitui o max_tokens em desuso.
    top_p: controla a diversidade vi "nucleos sampling" - em torno de 0.5 significa cosiderar apenas os tokens que somam 50% da probabilidade.
    """

    def __init__(self):
        self.client = Groq(api_key=GROQ_API)
        self.model = "openai/gpt-oss-120b"
        self.temperature = 0.0
        self.prompt = "Escreva uma frase poetica sobre o anoitecer"
        self.system_prompt = "Você é um poeta minimalista que descreve a natureza de forma simples e direta"
        self.top_p = 0.1

    @property
    def first_code_params_low(self):
        response_low = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": self.prompt},
            ],
            model=self.model,
            temperature=self.temperature,
        )

        return response_low

    @property
    def second_code_params_medium(self):
        self.temperature = 0.7
        response_medium = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": self.prompt},
            ],
            model=self.model,
            temperature=self.temperature,
        )

        return response_medium

    @property
    def second_code_params_medium_nive_two(self):
        self.temperature = 0.7
        self.system_prompt = (
            "Você é um poeta classico que mistura metáforas e imagens da natureza"
        )
        response_medium = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": self.prompt},
            ],
            model=self.model,
            temperature=self.temperature,
        )

        return response_medium

    @property
    def thrird_code_params_high(self):
        self.temperature = 1.5
        self.system_prompt = (
            "Você é um poeta surrealista que usa imagens improváveis e linguagem ousada"
        )
        reponse_high = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": self.prompt},
            ],
            model=self.model,
            temperature=self.temperature,
        )

        return reponse_high

    @property
    def fouth_code_params_top_p_focused(self):
        self.prompt = "Complete a frase: 'A inteligência artificial no futuro será...'"
        self.system_prompt = (
            "Você é um futurista que faz previsoes sérias e objetivas sobre tecnologia"
        )
        self.temperature = 1.0

        response = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": self.system_prompt
                },
                {
                    "role": "system",
                    "content": self.prompt
                }
            ],
            model=self.model,
            temperature=self.temperature,
            top_p=self.top_p
        )

        return response
    
    @property
    def fifth_code_params_top_p_balance(self):
        self.prompt = "Complete a frase: 'A inteligência artificial no futuro será...'"
        self.system_prompt = (
            "Você é um futurista que faz previsoes sérias e objetivas sobre tecnologia"
        )
        self.temperature = 1.0
        self.top_p = 0.7

        reponse_balance = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": self.system_prompt
                },
                {
                    "role": "user",
                    "content": self.prompt
                }
            ],
            model=self.model,
            temperature=self.temperature,
            top_p=self.top_p
        )

        return reponse_balance
    
    @property
    def sixth_code_params_top_p_diverse(self):
        self.prompt = "Complete a frase: 'A inteligência artificial no futuro será...'"
        self.system_prompt = (
            "Você é um futurista que faz previsoes sérias e objetivas sobre tecnologia"
        )
        self.temperature = 1.0
        self.top_p = 0.9

        response_diverse = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": self.system_prompt
                },
                {
                    "role": "user",
                    "content": self.prompt
                }
            ],
            model=self.model,
            temperature=self.temperature,
            top_p=self.top_p
        )
        
        return response_diverse


params_groq = ParamsGroq()
message = params_groq.sixth_code_params_top_p_diverse

print(f"\nResponse: {message.choices[0].message.content}\n")
