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
    
    async def summary_tourth(self):
        system_prompt = """
        Você uma anlsita de politicas publicas. Gere um resumo em bullet points claros e hierarquicos:
        - Destaques resultados (Métricas)
        - Liste problemas prioritários
        - Sugira 3 ações imediatas e 2 ações estrututais
        Mantenha frases curtas
        """

        user_prompt= """
        Relatório Piloto: Nova rota de ciclovia e corredores de ônibus rápidos implementada por 12 semanas.
        Resultados preliminares: aumento no uso de bicicleta em 22% nas rotas testadas; redução de tempo médio de deslocamento em ônibus local em 8%; aumento de reclamações de comerciantes sobre estacionamento; registro de 3 incidentes leves envolvendo ciclistas.
        Observações: infraestrutura temporária com sinalização provisória; campanhas educativas em 4 bairros; orçamento limitado para fiscalização.
        """

        response_complete = self.client.chat.completions.create(
            model = self.__model,
            temperature=0.25,
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

    async def summary_third(self):
        system_prompt = """
        Você é um consultor executivo. Construa um resumo executivo com:
        1) Sintese em 2-3 frases
        2) Principais métricas (visitantes, receita direta, parcerias)
        3) 3 Recomendações acionáveis para o próximo ano (prioricadas)
        Seja conciso e orientado para decisão
        """

        user_prompt = """
        Relatório: Festival "Olhar Curto" (3 dias).
        Métricas: 4.200 visitantes (inclui sessões pagas e gratuitas), receita direta: R$ 180.000 (ingressos + barra),
        patrocínios: R$ 70.000, custos operacionais: R$ 150.000.
        Impacto local: aumento de 18% no movimento de bares e cafés próximos durante o evento;
        envolvimento de 6 escolas técnicas; 25 curtas exibidos, 8 produções locais.
        Desafios: logística de exibição ao ar livre (chuva reprogramou 2 sessões), bilheteria online com alta taxa de desistência.
        """

        response_complete = self.client.chat.completions.create(
            model=self.__model,
            temperature=0.15,
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
    

async def run_main():
    summary = Summary()
    await summary.summary_third()

asyncio.run(run_main())