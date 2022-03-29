# New Jersey MVC Appointment Finder

MVC appointments are notoriously hard to find in NJ. This Python script (`njmvc.py`)lets you scrape the appointments and emails you when someone cancels his/her appointment.

You can specify the locations you want to have an appointment.

You can customize which type of appointment you want.

And then it emails you when the script is run. As soon as you get an email, you should click on the link on the email and make an appointment through NJ MVC's website.

So the best use of this would be setting up with cron job - where it'll be run regularly (I would prefer running every minute or so because the appointments fill up quickly).

Your cron job will look like this:

`*/1 * * * * /usr/local/bin/python3 /Users/your-username/njmvc.py`

To set up a cronjob on your Mac, you can use the instructions here:
https://towardsdatascience.com/how-to-schedule-python-scripts-with-cron-the-only-guide-youll-ever-need-deea2df63b4e
