import json
import requests
from flask_babel import _
from app import app


def translate(text, source_language, dest_language):
    if 'JA_TRANSLATOR_KEY' not in app.config or not app.config['JA_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured')
    api_request = 'https://translate.yandex.net/api/v1.5/tr.json/translate?key={}&text={}&lang={}'
    r = requests.get(api_request.format(app.config['JA_TRANSLATOR_KEY'], text, source_language+'-'+dest_language))
    if r.status_code != 200:
        return _('Error: the translation service failed')
    return json.loads(r.content.decode('utf-8-sig'))['text'][0]


