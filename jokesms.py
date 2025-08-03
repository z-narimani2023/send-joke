import requests
from kavenegar import *

r = requests.get('https://icanhazdadjoke.com/slack', headers={"Accept": "application/json"})
data = r.json()

fallback_text = data['attachments'][0]['fallback']

api = KavenegarAPI('#your_API_KEY')

params = { 'sender' : '2000660110', 'receptor': '#Receptor', 'message' :'جوک امروز: %s' %fallback_text }

response = api.sms_send(params)