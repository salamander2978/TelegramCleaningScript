import json
import time
import requests

BOT_TOKEN = 'Токен бота'

CHAT_ID = -12321312321 # ID чата 

with open('result.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    messages_data = data['messages']
    user_ids = list(set(msg['actor_id'].replace('user', '') for msg in messages_data 
                       if 'actor_id' in msg and 'action' in msg 
                       and (msg['action'] == 'invite_members' or msg['action'] == 'join_group_by_link')))

API_URL = f'https://api.telegram.org/bot{BOT_TOKEN}'

def ban_user(user_id):
    url = f"{API_URL}/banChatMember"
    params = {
        'chat_id': CHAT_ID,
        'user_id': user_id
    }
    response = requests.post(url, params=params)
    return response.json()

for user_id in user_ids:
    ban_user(user_id)
    time.sleep(0)  # задержка между банами
print("Готово") 