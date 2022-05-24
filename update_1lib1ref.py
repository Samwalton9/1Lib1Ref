import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import requests

__dir__ = os.path.dirname(__file__)

spreadsheet_key = ''
worksheet_name = 'May 2019 Edits'
dates = ['2019-05-15', '2019-06-05']


def gspread_login():
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        os.path.join(__dir__, 'client_secret.json'), scope)
    g_client = gspread.authorize(creds)
    if creds.access_token_expired:
        g_client.login()

    return g_client


def download_hashtags(start_date, end_date):
    hashtags = ['1lib1ref', '1bib1ref']

    hashtag_url = 'https://hashtags.wmcloud.org/csv/?query={hashtags}&startdate={start_date}&enddate={end_date}'
    download_csv = requests.get(hashtag_url.format(
        hashtags=','.join(hashtags),
        start_date=start_date,
        end_date=end_date
    ))
    open(os.path.join(__dir__, 'hashtags.csv'), 'wb').write(download_csv.content)

g_client = gspread_login()

g_sheet = g_client.open_by_key(spreadsheet_key)
worksheet = g_sheet.worksheet(worksheet_name)

download_hashtags(dates[0], dates[1])

row_count = worksheet.row_count

data_range = worksheet.range('B2:G{row}'.format(row=row_count))

with open(os.path.join(__dir__, 'hashtags.csv'), 'r', encoding='utf-8') as data_csv:
    csv_reader = csv.reader(data_csv)
    next(csv_reader)
    cell_counter = 0
    for line in csv_reader:
        for data in line:
            data_range[cell_counter].value = data
            cell_counter += 1

worksheet.update_cells(data_range)
