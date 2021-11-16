# Telegram Bommber

import requests

#token = '2138879226:AAEyuMiFRYw8_e_NeJug231AgBAox0YQZBg'
token = '977978002'
url = 'https://api.telegram.org/id'

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