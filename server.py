from oauth2client.service_account import ServiceAccountCredentials
import gspread
from gsheets import Sheets




scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
s =sheets.g
sheet = client.open("demo").sheet1

sheet.to_csv('Spam.csv', encoding='utf-8', dialect='excel')

print (sheet.get_all_values())




