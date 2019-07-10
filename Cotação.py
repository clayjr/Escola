import requests
import json

requisicao = requests.get(
    '/api/v1/locale/city/:id?token=ff6ce694a3f8ad1ab4717e5483c63a1e')
clima = json.loads(requisicao.text)

print('', id)
