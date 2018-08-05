import json
import requests
from flask_babel import _
from flask import current_app
import os

def translate(text, source_language, dest_language):
    # if 'JA_TRANSLATOR_KEY' not in current_app.config or not current_app.config['JA_TRANSLATOR_KEY']:
    #     return _('Error: the translation service is not configured')
    if os.environ.get('JA_TRANSLATOR_KEY') is None:
        return _('Error: the translation service is not configured')
    api_request = 'https://translate.yandex.net/api/v1.5/tr.json/translate?key={}&text={}&lang={}'
    #r = requests.get(api_request.format(current_app.config['JA_TRANSLATOR_KEY'], text, source_language+'-'+dest_language))
    r = requests.get(api_request.format(os.environ.get('JA_TRANSLATOR_KEY'), text, source_language+'-'+dest_language))
    if r.status_code != 200:
        return _('Error: the translation service failed')
    return json.loads(r.content.decode('utf-8-sig'))['text'][0]


