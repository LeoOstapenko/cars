# from openai import OpenAI
# # client = OpenAI()

# def get_car_ai_bio(model, brand, year): # A ordem aqui não importa aparentemente.
    
#     client = OpenAI()

#     prompt = '''
#     Desejo uma descrição de venda específica para o veículo {} {} {} em no máximo 250 caracteres.
#     '''

#     prompt = prompt.format(brand, model, year) # Aqui substituo a chaves do prompt acima. Atenção para a ordem dos parâmetros.

#     response = client.responses.create(
#         model="gpt-4.1",
#         prompt=prompt,
#         max_tokens=1000
#     )

#     return response['choices'][0]['text']


