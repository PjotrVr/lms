import os
import json


with open('config.json') as config_file:
    config = json.load(config_file)

config['DB_PATH'] = os.environ.get('LMS_DB_PATH')
config['SMTP_SERVER'] = os.environ.get('LMS_SMTP_SERVER')
config['SMTP_PORT'] = os.environ.get('LMS_SMTP_PORT')
config['EMAIL'] = os.environ.get('LMS_EMAIL')
config['EMAIL_PASSWORD'] = os.environ.get('LMS_EMAIL_PASSWORD')
config['PEPPER'] = os.environ.get('LMS_PEPPER')
