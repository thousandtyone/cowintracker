# CoWin Tracker
Recently the Indian Government launched the Co-Win website to schedule vaccinations across India. 

The site is at: https://www.cowin.gov.in/

However scheduling an appointment is the site as of today is difficult since all hospitals are opening slots on random timings and on ad-hoc basis. The script helps continuously poll and monitor the co-win site to see when slots are opening and plays music file of your choice to notify whenever your desired slots are opened up.

## Installation

Install Regular Python 3 or above.

Install require libraries using PIP: requests, datetime, time and playsound.

Once the needed libraries are installed, open the script and tweak the variables:

```
# Poll Interval In Seconds. Defines how frequently Cowin URL will be polled.
PollTime = 5

# Find out Your Destrict by Hitting F12 On Chrome in Cowin Site and Monitoring the Network Tab API Call.
# 294 is Bangalore BBMP. Find Your District And Replace Here. See Documentation on how to find out the District.
District = '294'

# Pick The Vaccine You Want To Use.
Vaccine = 'COVAXIN'

# Age - Options Are 18 and 45.
Age = 18

#  1 for First Dose, 2 for Second Dose
Dose = 1

# Replace this with Any MP3 File You Want To Play When Vaccine Is Found.
AudioFilePath = 'happy_clappy_by_john_bartmann.wav' 

# If Vaccine Does in a Slot are greater than the below number play music. Useful because sometimes hospital 
# just open 1 or 2 doses for their internal employees. In such cases keeping a number higher than 2 will ensure 
# you are aiming for a valid slot that has been opened for public. If you want to aim for situations
# even when a single dose is opened, leave the below number as 0.
MinimumDoses = 0

```

Once done, simply run the script using py command and let it run. It will keep polling co-win site on the pre-configured time interval (default is 5 seconds) and will play a music (royalty free wave fie included but you can change this as per your choice) whenever it finds a vaccine slot meeting your requirements. 

We know there are many Telegram bots available but this is just in case you want more control over what you are running and want to run is locally so that you get instant notification.
