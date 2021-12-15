import os

DB_USERNAME = os.environ.get('DB_USERNAME', 'not_configured')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'not_configured')
DB_TNS_SERVICE_NAME = os.environ.get('DB_TNS_SERVICE_NAME', 'not_configured')
TNS_ADMIN = os.environ.get('TNS_ADMIN', 'not_configured')

URI_FORMAT = 'oracle+cx_oracle://{}:{}@{}'
DB_URI = URI_FORMAT.format(DB_USERNAME, DB_PASSWORD, DB_TNS_SERVICE_NAME)

print('TNS_ADMIN = {}'.format(TNS_ADMIN))
print('DB_TNS_SERVICE_NAME = {}'.format(DB_TNS_SERVICE_NAME))
print('DB_USERNAME = {}'.format(DB_USERNAME))
print('DB_PASSWORD = {}'.format(DB_PASSWORD))
print('DB_URI = {}'.format(DB_URI))
