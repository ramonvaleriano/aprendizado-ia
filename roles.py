from groq import Groq

from settings import groq_apy_key, model_start


class Roles:
    """
      A Roles são os papeis que nós podemos ter nos nossos prompts. Isso é muito importe pois em um
      agente nós temos as roles e o content, o content é basicamento o conteúdo proprimanente dito,
      a role é o papel daquele prompt e ele pode assumir. 

      User: Mensagem de usuário
      Assistent: Resposta do Modelo
      System: Instruções do comportamente para o modelo  
    
    """
    def __init__(self):
        self.__model_start = model_start
        self.__groq_apy_key = groq_apy_key
        self.client = Groq(api_key=self.__groq_apy_key) # Intaciando o cliente com a chave da API groq
        
    def first_chat_completion(self):
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "Me explique de forma reduzida o que são LLMs"
                }
            ],
            model=self.__model_start
        )

        response = chat_completion.choices[0].message.content

        print(f"Resposta completa: {chat_completion}")
        print("\n\n")
        print(f"Resposta: {response}")

        return response


test_roles = Roles()
test_roles.first_chat_completion()