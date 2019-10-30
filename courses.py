from uwaterlooapi import UWaterlooAPI
from pprint import pprint
import xlsxwriter

if __name__ == '__main__':
    wb = xlsxwriter.Workbook('test.xlsx')
    sheet = wb.add_worksheet()

    uw = UWaterlooAPI(api_key="7d0e829ff82a1aa902f44d6609a1cbb2")
    courses = uw.courses()
    count = 1

    for course in courses:
        sheet.write('A%d' % count, course['subject'])
        sheet.write('B%d' % count, course['catalog_number'])
        sheet.write('C%d' % count, course['title'])
        count += 1

    wb.close()