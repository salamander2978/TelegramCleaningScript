import json
import time
import requests

BOT_TOKEN = 'Токен бота'

CHAT_ID = -12321312321 # ID чата 

with open('result.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    messages_data = data['messages']
    message_ids = [msg['id'] for msg in messages_data 
                  if 'id' in msg and 'action' in msg 
                  and (msg['action'] == 'invite_members' or msg['action'] == 'join_group_by_link')]

API_URL = f'https://api.telegram.org/bot{BOT_TOKEN}'

def delete_message(message_id):
    url = f"{API_URL}/deleteMessage"
    params = {
        'chat_id': CHAT_ID,
        'message_id': message_id
    }
    response = requests.post(url, params=params)
    return response.json()

count_deleted = 0
for msg_id in message_ids:
    try:
        delete_message(msg_id)
        count_deleted += 1
    except Exception as e:
        pass

print(f"Удалено сообщений: {count_deleted}") 