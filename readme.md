
# Telegram Chat Moderation Scripts

This set of scripts helps automate the moderation of a Telegram chat by removing invitation messages and banning users who invite others.

## What the scripts do

### ban.py
- Reads a JSON file with chat history
- Finds all users who invited others or joined via a link
- Bans these users through the bot

### delete.py
- Reads the same JSON file
- Finds all messages about invitations and joining via links
- Deletes these messages through the bot

## Important
- The bot must be an administrator of the chat
- The bot must have permission to delete messages and ban users
- The scripts only work with messages available in the JSON file
- When exporting chat history, MAKE SURE to select the correct dates, otherwise, all messages might be lost
- This only works if there are messages like "X is now in the group (3:02)" or "X joined the group via invite link"
- Do not manually delete join messages without using the script (otherwise, not all users will be banned)

## How to use

1. Place the `result.json` file (exported chat history, select json and the date range for banning) in the same folder as the scripts
2. In both scripts, replace:
   - `Bot Token` with your bot token (or get it from @BotFather)
   - `-12321312321` with your chat ID
3. Run the scripts:
   ```bash
   python ban.py
   python delete.py



# Скрипты для модерации Telegram чата

Этот набор скриптов помогает автоматизировать модерацию Telegram чата, удаляя сообщения о приглашениях и баняя пользователей, которые приглашают других.

## Что делают скрипты

### ban.py
- Читает JSON файл с историей чата
- Находит всех пользователей, которые приглашали других или присоединялись по ссылке
- Банит этих пользователей через бота

### delete.py
- Читает тот же JSON файл
- Находит все сообщения о приглашениях и присоединениях по ссылке
- Удаляет эти сообщения через бота

## Важно
- Бот должен быть администратором чата
- У бота должны быть права на удаление сообщений и бан пользователей
- Скрипты работают только с сообщениями, которые есть в JSON файле
- При экспорте истории чата ОБЯЗАТЕЛЬНО ВЫБРАТЬ ДАТЫ иначе могут отлететь все
- Работает ТОЛЬКО в случае того если есть сообщения типа "X теперь в группе (3:02)" или "X вступил(а) в группу по ссылке-приглашению"
- Не удалять сообщения о входе без использования скрипта(иначе не все забанятся)

## Как использовать

1. Положите файл `result.json` (экспорт истории чата, в экспорте выбрать json и дату в промежуток которой нужен бан) в ту же папку, где лежат скрипты
2. В обоих скриптах замените:
   - `Токен бота` на токен вашего бота(или получите у @BotFather)
   - `-12321312321` на ID вашего чата
3. Запустите скрипты:
   ```bash
   python ban.py
   python delete.py
   ```


Сделано для людей которых внезапно зарейдили и у них не было бота для антиспама
