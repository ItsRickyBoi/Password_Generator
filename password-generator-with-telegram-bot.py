import random
import logging
import requests
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Google Drive credentials
# Path to your Google Drive credentials file
credentials_file = 'your_credentials.json'
# ID of the folder in Google Drive where you want to upload the file
folder_id = 'your_folder_id'

# Function to upload file to Google Drive


def upload_to_drive(file_path, file_name, folder_id):
    credentials = service_account.Credentials.from_service_account_file(
        credentials_file)
    drive_service = build('drive', 'v3', credentials=credentials)

    file_metadata = {
        'name': file_name,
        'parents': [folder_id]
    }
    media = MediaFileUpload(file_path, resumable=True)
    file = drive_service.files().create(
        body=file_metadata, media_body=media, fields='id').execute()
    print('File uploaded successfully. File ID: {}'.format(file.get('id')))
    

def telegram_bot_sendText(bot_message):
    #your bot token
    bot_token = 'your_bot_token'
    #Open a new tab with your browser, enter 
    # https://api.telegram.org/bot<yourtoken>/getUpdates , replace <yourtoken> after /start with your bot token
    chat_id = 'your_chat_id'
    
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + bot_message
    
    response = requests.get(send_text)

    return response.json()
    
   
# Main program

def main():
    # User input for file name
    file_name = input('Enter a name for the file: ')
    username = input('Enter username / email of this account: ')
    chara = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$*&^%~'
    total = input('How many passwords do you need? - ')
    total = int(total)
    length = input('The length of the password? - ')
    length = int(length)

    file_path = (file_name + '.txt')  # Path to the output file

    with open(file_path, 'w'):
        pass

    for i in range(total):
        password = ''
        for x in range(length):
            password += random.choice(chara)
        logging.basicConfig(level=logging.DEBUG, filename=file_path, filemode="a+",
                            format="%(asctime)-15s %(levelname)-8s %(message)s")
        logging.info(username)
        logging.info(password)


    # Upload file to Google Drive
    upload_to_drive(file_path, file_name, folder_id) 
    print("Success, now check the list folder for the password you generated and don't forget to save it")
    
    #sending to Telegram bot
    message_bot = 'New Credentials' + '\n' + 'File Name: ' + file_name + '\n' + 'Username: ' + username + '\n' + 'Password: ' + password
    send_to_telegram = telegram_bot_sendText(message_bot)
    print("Success sending to Telegram bot")
    
    
    input('Press ENTER to exit')


if __name__ == '__main__':
    main()