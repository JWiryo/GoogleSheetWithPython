import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

pp = pprint.PrettyPrinter()

scope =['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('SheetsDatabase-d61611f5391b.json', scopes=scope)
client = gspread.authorize(credentials)

sheet = client.open('Rakuten').sheet1

all_records = sheet.get_all_records()
pp.pprint(all_records)

# single_row = sheet.range(2)
# pp.pprint(single_row)

# sheet.update_cell(2,2,'Java')
# single_row = sheet.row_values(2)
# pp.pprint(single_row)

# new_row = ["Here","is","a","new","row"]
# index = 2
# sheet.insert_row(new_row, index)

# sheet.delete_row(2)

print(sheet.row_count)


