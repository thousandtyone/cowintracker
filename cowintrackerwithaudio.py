
# Python script by ThousadntyOne for Monitoring Cowin Servers To Schedule Vaccine Appointments In India.
# Published Under GPL2. All Enhancements must be Published back to the repository to contribute to the community.
# Modify The Below Variables in the Script to Customize it.
# PollTime, District, Vaccine, Age, Dose, AudioFilePath, MinimumDoses.
# Each Variable has a comment to describe it's usage.

import requests
import datetime
import time
from playsound import playsound

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}

TodaysDate = datetime.datetime.today().strftime('%d-%m-%Y')

# Poll Interval In Seconds. Defines how frequently Cowin URL will be polled.
PollTime = 5

# Find out Your Destrict by Hitting F12 On Chrome in Cowin Site and Monitoring the Network Tab API Call.
# 294 is Bangalore BBMP. Find Your District And Replace Here. See Documentation on how to find out the District.
District = '294'

# Pick The Vaccine You Want To Use.
Vaccine = 'COVAXIN'

# Age - Options Are 18 and 45.
Age = 18

#  1 for First Slot, 2 for Second Slot
Dose = 1

# Replace this with Any MP3 File You Want To Play When Vaccine Is Found.
AudioFilePath = 'happy_clappy_by_john_bartmann.wav' 

# If Vaccine Does in a Slot are greater than the below number play music.
MinimumDoses = 0

# api-endpoints can be set depending on what you want to track. 
# URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByPin?pincode=560001&date=' + TodaysDate
URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id='+ District +'&date=' + TodaysDate
       
found = False
exception = True
n = 1
while n > 0:
    try:    
        found = False
        r = requests.get(url = URL, headers= headers)
        data = r.json()
        centers = data['centers']
        for center in centers:
            sessions = center['sessions']
            for session in sessions:
                if Dose == 1:
                    if session['min_age_limit'] == Age and session['available_capacity_dose1'] > MinimumDoses and session['vaccine'] == Vaccine:
                        print(str(datetime.datetime.now()) + ': session available for dose 1 in:' + center['name']  + ' pincode: ' + str(center['pincode']) + ' with ' + str(session['available_capacity_dose1']) + ' doses available on date:' + str(session['date']))
                        found = True
                if Dose == 2:
                    if session['min_age_limit'] == Age and session['available_capacity_dose2'] > MinimumDoses and session['vaccine'] == Vaccine:
                        print(str(datetime.datetime.now()) + ': session available for dose 2 in:' + center['name']  + ' pincode: ' + str(center['pincode']) + ' with ' + str(session['available_capacity_dose2']) + ' doses available on date:' + str(session['date']))
                        found = True
    except:
        exception = True
        print(str(datetime.datetime.now())+ ": something wrong wrong. may have skipped a session.")

    if found == True:
        print(str(datetime.datetime.now()) + ": One or More Appointments was found.")
        playsound(AudioFilePath)
        time.sleep(20)
    else:
        print(str(datetime.datetime.now()) + ": No appointment was found.")

    time.sleep(PollTime)