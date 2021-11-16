# Telegram Bommber

import requests
import argparse
import time
from datetime import datetime

url = 'https://api.telegram.org/bot'


def CreateAndGetArg():

    global args

    parser = argparse.ArgumentParser()

    parser.add_argument('-t', '--token', required=True, type=str, help='Bot token', )
    parser.add_argument('-i', '--UserID', required=True, type=str, help='User ID in telegram')
    parser.add_argument('-m', '--massage', required=True, type=str, help='The text of the sent message')
    parser.add_argument('-q', '--quantity', default=-1, type=int, help='Number of messages sent')
    parser.add_argument('-d', '--date', default='Now', type=str, help='Date and time of script launch (year-month-day hours:minutes)')


    args = parser.parse_args()

def SendMessage(token, id, text):
    method = 'https://api.telegram.org/bot' + token + '/SendMessage'

    index = args.quantity

    try:
        while index != 0:
            r = requests.post(method, data={
                "chat_id": id,
                "text": text
                })

            if r.status_code != 200:
                print('Message not sent')
            
            print('status: ' + str(r))

            index -= 1

    except KeyboardInterrupt:
        print('\nSubmission completed.')
        print('Submitted: ' + str((index+1)*-1))


    print('\nCompleted')


def main():
    CreateAndGetArg()
    if args.date == 'Now':
        SendMessage(args.token, args.UserID, args.massage)
    else:
        while True:
            print('We are waiting for the right moment ...')
            date_now = datetime.now()
            date_now = str(date_now.year)+'-'+str(date_now.month)+'-'+str(date_now.day)+' '+str(date_now.hour)+':'+str(date_now.minute)

            if date_now == args.date:
                SendMessage(args.token, args.UserID, args.massage)

            else:
                time.sleep(1)

main()
