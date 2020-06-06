from win10toast import ToastNotifier
import time

Notify = ToastNotifier()

# 1 = on, 0 = off
E = 1
SR = 1
SRDone = 0
#Gives a notification to stretch
def SRNotify():
    global SRnow, before
    if SR == 1:
        Notify.show_toast("Hrthon", SRmessage, duration=15, icon_path=None)
        before = time.time()
        SRnow = before + SRamount
    else:
        print("SR Off")
    check()

#Gives a notification to rest your eyes
def ENotify():
    global before, Enow
    if E == 1:
        Notify.show_toast("Hrthon", Emessage, duration=15, icon_path=None)
        before = time.time()
        Enow = before + Eamount
    else:
        print("Eye off")
    check()

#Determines what type of notification is sent
def who():
    global Enow,SRnow, before
    if SRnow == Enow:
        Allmessage = "A Healthy Reminder to stretch and rest your eyes!"
        Notify.show_toast("Hrthon", Allmessage, duration=15, icon_path=None)
        before = time.time()
        Enow = before + Eamount
        SRnow = before + SRamount
        check()
    #If before is greater than this, then that
    elif before > SRnow:
        SRNotify()
    elif before > Enow:
        ENotify()
    else:
        print("Error")

#Checks if the time = reminder's time over and over again
def check():
    global before, SRhour, SRminutes, SRmessage, Enow, Ehour, Eminutes, Emessage
    while before < SRnow and before < Enow:
        before = time.time()
    print("Checking which reminder to use")
    who()

def SRagain():
    global SRhour, SRminutes, SRDone
    try:
        print("If you would not like to be reminded to stretch, set hour and minutes to 0!\n")
        SRhour = float(input("In how many hours would you like to be reminded?:"))
        SRminutes = float(input("In how many minutes would you like to be reminded?:"))
        SRDone = 1
    except:
        print("This program only accepts numbers. Please try again!")
        SRagain()


# Checks if the time = reminder's time, then again

print("")

def Eagain():
    global Ehour, Eminutes
    try:
        print("If you would not like to be reminded to rest your eyes, set hour and minutes to 0!\n")
        Ehour = float(input("In how many hours would you like to be reminded?:"))
        Eminutes = float(input("In how many minutes would you like to be reminded?:"))
    except:
        print("This program only accepts numbers. Please try again!")
        Eagain()

SRhour = "Blank" #Otherwise it would say SRhour is not defined
if SRDone == 0:
    SRagain()
else:
    Eagain()
Eagain()
SRhoursec = SRhour * 3600  # Converts hours to seconds
SRminsec = SRminutes * 60  # Converts minutes to seconds

SRamount = SRhoursec + SRminsec

before = time.time()
SRnow = before + SRamount
Ehoursec = Ehour * 3600  # Converts hours to seconds
Eminsec = Eminutes * 60  # Converts minutes to seconds

Eamount = Ehoursec + Eminsec

before = time.time()
Enow = before + Eamount

if SRhour > 0 and SRminutes == 0:
    if SRhour == 1:
        SRmessage = "It's been " + str(SRhour) + " hour! A Healthy Reminder to take a short stretch!"
    else:
        SRmessage = "It's been " + str(SRhour) + " hours! A Healthy Reminder to take a short stretch!"
elif SRhour == 0 and SRminutes > 0:
    if SRminutes == 1:
        SRmessage = "It's been " + str(SRminutes) + " minute! A Healthy Reminder to take a short stretch!"
    else:
        SRmessage = "It's been " + str(SRminutes) + " minutes! A Healthy Reminder to take a short stretch!"
elif SRhour > 0 and SRminutes > 0:
    if SRhour == 1 and SRminutes == 1:
        SRmessage = "It's been " + str(SRhour) + " hour and " + str(
            SRminutes) + " minute! A Healthy Reminder to take a short stretch!"
    elif SRhour == 1 and SRminutes > 1:
        SRmessage = "It's been " + str(SRhour) + " hour and " + str(
            SRminutes) + " minutes! A Healthy Reminder to take a short stretch!"
    elif SRhour > 1 and SRminutes == 1:
        SRmessage = "It's been " + str(SRhour) + " hours and " + str(
            SRminutes) + " minute! A Healthy Reminder to take a short stretch!"
    elif SRhour > 1 and SRminutes > 1:
        SRmessage = "It's been " + str(SRhour) + " hours and " + str(
            SRminutes) + " minutes! A Healthy Reminder to take a short stretch!"
else:
    SRmessage = ("Blank")
    print("Stretch Reminder Off")
    SR = 0

if Ehour > 0 and Eminutes == 0:
    if Ehour == 1:
        Emessage = "It's been " + str(Ehour) + " hour! A Healthy Reminder to rest your eyes for about 20 seconds!"
    else:
        Emessage = "It's been " + str(Ehour) + " hours! A Healthy Reminder to rest your eyes for about 20 seconds!"
elif Ehour == 0 and Eminutes > 0:
    if Eminutes == 1:
        Emessage = "It's been " + str(Eminutes) + " minute! A Healthy Reminder to rest your eyes for about 20 seconds!"
    else:
        Emessage = "It's been " + str(Eminutes) + " minutes! A Healthy Reminder to rest your eyes for about 20 seconds!"
elif Ehour > 0 and Eminutes > 0:
    if Ehour == 1 and Eminutes == 1:
        Emessage = "It's been " + str(Ehour) + " hour and " + str(Eminutes) + " minute! A Healthy Reminder to rest your eyes for about 20 seconds!"
    elif Ehour == 1 and Eminutes > 1:
        Emessage = "It's been " + str(Ehour) + " hour and " + str(Eminutes) + " minutes! A Healthy Reminder to rest your eyes for about 20 seconds!"
    elif Ehour > 1 and Eminutes == 1:
        Emessage = "It's been " + str(Ehour) + " hours and " + str(Eminutes) + " minute! A Healthy Reminder to rest your eyes for about 20 seconds!"
    elif Ehour > 1 and Eminutes > 1:
        Emessage = "It's been " + str(Ehour) + " hours and " + str(Eminutes) + " minutes! A Healthy Reminder to rest your eyes for about 20 seconds!"
else:
    Emessage = ("Blank")
    print("Eye Reminder Off")
    E = 0

check()