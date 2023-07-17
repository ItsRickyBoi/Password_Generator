import random
import logging
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Google Drive credentials

# Path to your Google Drive credentials file -> refer to this documentation https://developers.google.com/workspace/guides/create-project
credentials_file = 'your_credentials.json'

# ID of the folder in Google Drive where you want to upload the file ( don't forget to share the folder with the service account email)
# also don't forget to make the service account email has editor role
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


# User input for file name
file_name = input('Enter a name for the file: ')

chara = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$*&^%~'

total = input('How many passwords do you need? - ')
total = int(total)

length = input('The length of the password? - ')
length = int(length)

file_path = 'list.txt'  # Path to the output file

with open(file_path, 'w'):
    pass

for i in range(total):
    password = ''
    for x in range(length):
        password += random.choice(chara)
    logging.basicConfig(level=logging.DEBUG, filename=file_path, filemode="a+",
                        format="%(asctime)-15s %(levelname)-8s %(message)s")
    logging.info(password)

print("Success, now check the list folder for the password you generated")

# Upload file to Google Drive
upload_to_drive(file_path, file_name, folder_id)

input('Press ENTER to exit')
