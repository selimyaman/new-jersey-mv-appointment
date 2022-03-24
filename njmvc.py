# NEW JERSEY APPOINTMENT REMINDER - IT EMAILS ME IF THERE'S AN APPOINTMENT AVAILABLE BEFORE PRE-SET DATE
#!/usr/bin/env python
import requests
import json
from dateutil import parser
import datetime
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def rip_js_var(blob, varname):
    ss = 'var ' + varname +' ='
    for ln in blob.splitlines():
        if ln.lstrip().startswith(ss):
            return ln.split(ss)[1].rstrip(';')


# Remove No Appointments from output (False for debugging)
rmempty = True

# Only consider a certain list of locations (False for statewide)
#onlylook = [186, 195]
onlylook = False

# Which URL to use.  This is for Initial Permit
# You can configure it for your spesific needs 
theurl = 'https://telegov.njportal.com/njmvc/AppointmentWizard/19'

r = requests.get(theurl)
times = json.loads(rip_js_var(r.text, 'timeData'))

# Enhance times with location names
locs  = json.loads(rip_js_var(r.text, 'locationData'))
loc_table = {}
for l in locs:
    loc_table[l['Id']] = l['Name']
for t in times:
    t['LN'] = loc_table[t['LocationId']]

# Remove no Appointments from output
if rmempty:
    times = [x for x in times if not x['FirstOpenSlot'].startswith('No Appointments')]

# Restrict to preferred locations (if set)
if onlylook:
    times = [x for x in times if x['LocationId'] in onlylook]

#EMAIL SETUP
from_address = "youremailaddress@gmail.com"
to_address = "youremailaddress@gmail.com"
username = 'youremailaddress@gmail.com'  
password = 'password'  
#IMPORTANT: IF you allowed less secure apps, you can use your own password. 
# Otherwise you'll need to set app-spesific password. See https://www.interviewqs.com/blog/py-email
def send_email(content):
 server = smtplib.SMTP('smtp.gmail.com', 587) 
 server.ehlo()
 server.starttls()
 server.login(username,password)  
 server.sendmail(from_address, to_address, content)  
 server.quit()

# NOW EMAIL ME IF WE FIND AN APPOINTMENT
for t in times:
    temp = t['FirstOpenSlot']
    tempnew = re.sub(r'.', '', temp, count = 48)
    tempnew2 = tempnew.lstrip(": ")
    res = parser.parse(tempnew2, fuzzy=True)
    deadline = parser.parse('04/22/22')
    condition = res < deadline
    if condition: send_email("22 NISAN ONCESINE BIR TANE YER VAR Go ahead telegov.njportal.com/njmvc/AppointmentWizard/19")