from uwaterlooapi import UWaterlooAPI
from pprint import pprint
import sys

uw = UWaterlooAPI(api_key="7d0e829ff82a1aa902f44d6609a1cbb2")
exam = uw.course_examschedule(sys.argv[1], sys.argv[2])
pprint(exam)