import urllib
import urllib2
import cookielib
import re
import time
import webbrowser
# from random import randrange
import random

random.seed()

# Base UBC URL
BASE_UBCURL = 'https://courses.students.ubc.ca/cs/main'

# Base Template for the URL to change the term to check
BASE_TERMURL = 'https://courses.students.ubc.ca/cs/main?sessyr=2016&sesscd=S'
# Base Template for the URL to check courses
BASE_COURSEURL = 'https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas'

# COURSESTOCHECK is a static 2D array that is a listof Course
# Course is a 3 string array, [X,Y,Z] where X is the Course Name, Y is the Number Code
# and Z is the ability to register in restricted seats
# where 0 = false, 1 = true
COURSESTOCHECK = [['CPSC', '121', '1'], ['CPSC', '312', '0']]

# switchTerms consumes two strings, year and term
# year is the year to check
# term is the term to check, which is ONEOF:
# - 'S'
# - 'W'
# switchTerms constructs a new URL and then switches to that term
def switchTerms(year, term):
    TERMURL = BASE_UBCURL + '?sessyr=' + year + '&sesscd=' + term
    # ~!!!~ <<TODO: Switch to term>>

# createCourseURL consumes a Course and returns a string
# course is an array of two strings
# constructs a new URL based on the course given and returns it
def createCourseURL(course):
    COURSEURL = BASE_UBCURL + '?pname=subjarea&tname=subjareas&req=3&dept=' + course[0] + '&course=' + course[1]
    # ~!!!~ <<TODO: Check this>>
    return COURSEURL

# wait causes the script to pause for a pseudo-random amount of time
def wait(delay):
    randDelay = BASE_DELAY + int(random.randint(1,10))
    time.sleep(randDelay)


# 'https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=3&dept=CPSC&course=312'
# https://courses.students.ubc.ca/cs/main?sessyr=2016&sesscd=S
# https://courses.students.ubc.ca/cs/main?sessyr=2016&sesscd=W
# https://courses.students.ubc.ca/cs/main?campuscd=UBCO
# https://courses.students.ubc.ca/cs/main?campuscd=UBC