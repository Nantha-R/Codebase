# Dealing with datetime implementation

import datetime

print(datetime.datetime.now()) # prints 2018-06-16 18:27:50.721191
print(datetime.datetime.now().replace(microsecond=0)) # prints 2018-06-16 18:27:50
print(datetime.datetime.utcnow()) # prints 2018-06-16 12:57:50.721191
'''
utcnow() tells you the date and time as it would be in Coordinated Universal Time, which is also called the Greenwich Mean Time time zone
basically like it would be if you were in London England.
now() gives the date and time as it would appear to someone in your current locale.

Use now() when displaying the time to the User.
Use utcnow() when storing time as it would solve the conflicts of different time zones of different users.
'''
