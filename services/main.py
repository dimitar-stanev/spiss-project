from bottle import *

@post('/main')
def thank_you():

    return "Thank you for trying to post something new to me ! I will keep that in mind :)"