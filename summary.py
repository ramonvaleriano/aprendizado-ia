import asyncio
from groq import Groq

from settings import model_start, groq_apy_key


class Summary:
    def __init__(self):
        self.__model = model_start
        self.__key = groq_apy_key
        self.client = Groq(api_key=self.__key)

    async def Summary_first(self):
        system_prompt = """
        Você é um editor técnico especialiszado em jogos independentes.
        Crie um resumo objetivo com aproximadamente 1/3 do tamanho do texto original,
        preservando os pontos centrais e o tom informativo.
        """

        user_prompt = """
        A cena de jogos independentes segue em crescimento, com ferramentas como engines gratuitas,
        marketplaces digitais e financiamento coletivo tornando possível a criação por equipes pequenas.
        Desafios frequentes incluem descoberta (getting discovered) em lojas saturadas, financiamento
        sustentável após o lançamento e equilíbrio entre inovação e usabilidade. Muitos estúdios optam
        por construir comunidades durante o desenvolvimento (early access, betas) para reduzir riscos.
        Tendências recentes mostram ênfase em experiências narrativas curtas, jogos como serviço
        em modelo leve, e experimentos com integração de áudio procedural. O mercado também aponta
        maior valorização por jogos com estética única e mecânicas originais, embora isso nem sempre
        se traduza em vendas imediatas. Estratégias de monetização variam: premium, pay-what-you-want,
        DLCs pequenas, e microtransações bem posicionadas em jogos multiplayer. Em suma, o sucesso
        indie depende de produto de qualidade, comunidade engajada e escolhas estratégicas de lançamento.
        """

        response_complete = self.client.chat.completions.create(
            model=self.__model,
            temperature=0.2,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ]
        )

        response =  response_complete.choices[0].message.content

        print(f"Pergunta: {user_prompt}")
        print(f"Resposta: {response}")

        return response
    

async def run_main():
    summary = Summary()
    await summary.Summary_first()

asyncio.run(run_main())