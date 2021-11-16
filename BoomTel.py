# Telegram Bommber

import requests

url = 'https://api.telegram.org/bot'

def SendMessage(id, text):
    method = url + token + '/SendMessage'

    while True:
        r = requests.post(method, data={
            "chat_id": id,
            "text": text
            })

        

        print('status: ' + str(r) + ' | Message sent!')


def main():
    SendMessage('989673924', 'Я сделал короче))')

main()
