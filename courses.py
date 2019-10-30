from uwaterlooapi import UWaterlooAPI
from pprint import pprint

if __name__ == '__main__':
    uw = UWaterlooAPI(api_key="7d0e829ff82a1aa902f44d6609a1cbb2")
    courses = uw.courses()

    for course in courses:
        if course['subject'] == 'ECE':
            print(course['subject'] + ' ' + course['title'] + ' ' + course['catalog_number'])