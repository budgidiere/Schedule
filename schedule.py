#schudgule
print("Starting Now")
print("LOADING APIS")
import time
wgweek = open("wgweekfile.txt","r")
wg = wgweek.read()
wgweek.close()
print(wg)
changewg = False

clock = (time.ctime())
hour = clock[11:13]
minute = clock[14:16]
currenttime = 60*int(hour) + int(minute)
day = clock[0:3]
print (currenttime)
print (clock)
whatclass = ("none")
while True:
    if wg == ("0"):
        if day == ("Mon"):
            if currenttime < 480 and currenttime > 420:
                whatclass = ("Building Open")
            elif currenttime < 508.8 and currenttime > 480:
                whatclass = ("4th Period")
            elif currenttime < 540 and currenttime > 508.9:
                whatclass = ("Advisory")
            elif currenttime < 569.4 and currenttime > 540:
                whatclass = ("5th Period")
            elif currenttime < 611.4 and currenttime > 569.5:
                whatclass = ("Activites")
            elif currenttime < 666 and currenttime > 611.5:
                whatclass = ("6th Period")
            elif currenttime < 684 and currenttime > 666.1:
                whatclass = ("Lunch")
            elif currenttime < 738.6 and currenttime > 684.1:
                whatclass = ("7th Peorid")
            elif currenttime < 793.2 and currenttime > 738.7:
                whatclass = ("1st Peorid")
            elif currenttime < 794.6 and currenttime > 793.3:
                whatclass = ("Afternoon Break")
            elif currenttime < 856.2 and currenttime > 794.7:
                whatclass = ("2nd Peorid")
            elif currenttime < 912 and currenttime > 856.3:
                whatclass = ("3rd Peorid")
        if day == ("Tue"):
            if currenttime < 480 and currenttime > 420:
                whatclass = ("Building Open")
            elif currenttime < 547.1 and currenttime > 480.1:
                whatclass = ("1st Period")
            elif currenttime < 553.2 and currenttime > 547.2:
                whatclass = ("Advisory")
            elif currenttime < 565.2 and currenttime > 553.3:
                whatclass = ("Activities")
            elif currenttime < 634.2 and currenttime > 565.3:
                whatclass = ("2nd Period")
            elif currenttime < 676.1 and currenttime > 634.2:
                whatclass = ("Lunch")
            elif currenttime < 745.2 and currenttime > 676.2:
                whatclass = ("3rd Period")
            elif currenttime < 814.2 and currenttime > 745.3:
                whatclass = ("4th Period")
            elif currenttime < 843.0 and currenttime > 814.3:
                whatclass = ("Afternoon Break")
            elif currenttime < 912.0 and currenttime > 843.1:
                whatclass = ("5th Period")
        if day == ("Wed"):
            if currenttime < 540 and currenttime > 420:
                whatclass = ("Building Open")
            elif currenttime < 605.4 and currenttime > 540.1:
                whatclass = ("6th Period")
            elif currenttime < 611.4 and currenttime > 605.5:
                whatclass = ("Advisory")
            elif currenttime < 667.1 and currenttime > 611.5:
                whatclass = ("X Period")
            elif currenttime < 682.1 and currenttime > 667.2:
                whatclass = ("Lunch")
            elif currenttime < 749.4 and currenttime > 682.2:
                whatclass = ("7th Period")
            elif currenttime < 840.6 and currenttime > 749.5:
                whatclass = ("1st Period")
            elif currenttime < 845.4 and currenttime > 840.7:
                whatclass = ("Afternoon Break")
            elif currenttime < 912.0 and currenttime > 845.5:
                whatclass = ("2nd Period")
        if day == ("Thu"):
            if currenttime < 480 and currenttime > 420:
                whatclass = ("Bulding Open")
            elif currenttime < 547.1 and currenttime > 480.1:
                whatclass = ("3rd Period")
            elif currenttime < 553.2 and currenttime > 547.2:
                whatclass = ("Advisory")
            elif currenttime < 565.2 and currenttime > 553.3:
                whatclass = ("Activities")
            elif currenttime < 634.2 and currenttime > 565.3:
                whatclass = ("4th Period")
            elif currenttime < 676.1 and currenttime > 634.2:
                whatclass = ("Lunch")
            elif currenttime < 745.2 and currenttime > 676.2:
                whatclass = ("5th Period")
            elif currenttime < 814.2 and currenttime > 745.3:
                whatclass = ("6th Period")
            elif currenttime < 843.0 and currenttime > 814.3:
                whatclass = ("Afternoon Break")
            elif currenttime < 912.0 and currenttime > 843.1:
                whatclass = ("7th Period")
        if day == ("Fri"):
            if currenttime < 480 and currenttime > 420:
                whatclass = ("Building Open")
            elif currenttime < 508.8 and currenttime > 480:
                whatclass = ("5th Period")
            elif currenttime < 540 and currenttime > 508.9:
                whatclass = ("Advisory")
            elif currenttime < 569.4 and currenttime > 540:
                whatclass = ("6th Period")
            elif currenttime < 611.4 and currenttime > 569.5:
                whatclass = ("Activites")
            elif currenttime < 666 and currenttime > 611.5:
                whatclass = ("7th Period")
            elif currenttime < 684 and currenttime > 666.1:
                whatclass = ("Lunch")
            elif currenttime < 738.6 and currenttime > 684.1:
                whatclass = ("1st Peorid")
            elif currenttime < 793.2 and currenttime > 738.7:
                whatclass = ("2nd Peorid")
            elif currenttime < 794.6 and currenttime > 793.3:
                whatclass = ("Afternoon Break")
            elif currenttime < 856.2 and currenttime > 794.7:
                whatclass = ("3rd Peorid")
            elif currenttime < 912 and currenttime > 856.3:
                whatclass = ("4th Peorid")
            elif currenttime < 912.1:
                changewg = True
                changewgvalue = ("1")
    if wg == ("1"):
        if day == ("Mon"):
            if currenttime < 480 and currenttime > 420:
                whatclass = ("Building Open")
            elif currenttime < 508.8 and currenttime > 480:
                whatclass = ("4th Period")
            elif currenttime < 540 and currenttime > 508.9:
                whatclass = ("Advisory")
            elif currenttime < 569.4 and currenttime > 540:
                whatclass = ("5th Period")
            elif currenttime < 611.4 and currenttime > 569.5:
                whatclass = ("Activites")
            elif currenttime < 666 and currenttime > 611.5:
                whatclass = ("6th Period")
            elif currenttime < 684 and currenttime > 666.1:
                whatclass = ("Lunch")
            elif currenttime < 738.6 and currenttime > 684.1:
                whatclass = ("7th Peorid")
            elif currenttime < 793.2 and currenttime > 738.7:
                whatclass = ("1st Peorid")
            elif currenttime < 794.6 and currenttime > 793.3:
                whatclass = ("Afternoon Break")
            elif currenttime < 856.2 and currenttime > 794.7:
                whatclass = ("2nd Peorid")
            elif currenttime < 912 and currenttime > 856.3:
                whatclass = ("3rd Peorid")
        if day == ("Tue"):
            if currenttime < 480 and currenttime > 420:
                whatclass = ("Building Open")
            elif currenttime < 547.1 and currenttime > 480.1:
                whatclass = ("5th Period")
            elif currenttime < 553.2 and currenttime > 547.2:
                whatclass = ("Advisory")
            elif currenttime < 565.2 and currenttime > 553.3:
                whatclass = ("Activities")
            elif currenttime < 634.2 and currenttime > 565.3:
                whatclass = ("6th Period")
            elif currenttime < 676.1 and currenttime > 634.2:
                whatclass = ("Lunch")
            elif currenttime < 745.2 and currenttime > 676.2:
                whatclass = ("7th Period")
            elif currenttime < 814.2 and currenttime > 745.3:
                whatclass = ("1st Period")
            elif currenttime < 843.0 and currenttime > 814.3:
                whatclass = ("Afternoon Break")
            elif currenttime < 912.0 and currenttime > 843.1:
                whatclass = ("2nd Period")
        if day == ("Wed"):
            if currenttime < 540 and currenttime > 420:
                whatclass = ("Building Open")
            elif currenttime < 605.4 and currenttime > 540.1:
                whatclass = ("3rd Period")
            elif currenttime < 611.4 and currenttime > 605.5:
                whatclass = ("Advisory")
            elif currenttime < 667.1 and currenttime > 611.5:
                whatclass = ("X Period")
            elif currenttime < 682.1 and currenttime > 667.2:
                whatclass = ("Lunch")
            elif currenttime < 749.4 and currenttime > 682.2:
                whatclass = ("4th Period")
            elif currenttime < 840.6 and currenttime > 749.5:
                whatclass = ("5th Period")
            elif currenttime < 845.4 and currenttime > 840.7:
                whatclass = ("Afternoon Break")
            elif currenttime < 912.0 and currenttime > 845.5:
                whatclass = ("6th Period")
        if day == ("Thu"):
            if currenttime < 480 and currenttime > 420:
                whatclass = ("Bulding Open")
            elif currenttime < 547.1 and currenttime > 480.1:
                whatclass = ("7th Period")
            elif currenttime < 553.2 and currenttime > 547.2:
                whatclass = ("Advisory")
            elif currenttime < 565.2 and currenttime > 553.3:
                whatclass = ("Activities")
            elif currenttime < 634.2 and currenttime > 565.3:
                whatclass = ("1st Period")
            elif currenttime < 676.1 and currenttime > 634.2:
                whatclass = ("Lunch")
            elif currenttime < 745.2 and currenttime > 676.2:
                whatclass = ("2nd Period")
            elif currenttime < 814.2 and currenttime > 745.3:
                whatclass = ("3rd Period")
            elif currenttime < 843.0 and currenttime > 814.3:
                whatclass = ("Afternoon Break")
            elif currenttime < 912.0 and currenttime > 843.1:
                whatclass = ("4th Period")
        if day == ("Fri"):
            if currenttime < 480 and currenttime > 420:
                whatclass = ("Building Open")
            elif currenttime < 508.8 and currenttime > 480:
                whatclass = ("2nd Period")
            elif currenttime < 540 and currenttime > 508.9:
                whatclass = ("Advisory")
            elif currenttime < 569.4 and currenttime > 540:
                whatclass = ("3rd Period")
            elif currenttime < 611.4 and currenttime > 569.5:
                whatclass = ("Activites")
            elif currenttime < 666 and currenttime > 611.5:
                whatclass = ("4th Period")
            elif currenttime < 684 and currenttime > 666.1:
                whatclass = ("Lunch")
            elif currenttime < 738.6 and currenttime > 684.1:
                whatclass = ("5th Peorid")
            elif currenttime < 793.2 and currenttime > 738.7:
                whatclass = ("6th Peorid")
            elif currenttime < 794.6 and currenttime > 793.3:
                whatclass = ("Afternoon Break")
            elif currenttime < 856.2 and currenttime > 794.7:
                whatclass = ("7th Peorid")
            elif currenttime < 912 and currenttime > 856.3:
                whatclass = ("1st Peorid")
            elif currenttime < 912.1:
                changewg = True
                changewgvalue = ("0")


    print(whatclass)
    time.sleep(60)
    if changewg == True:
        wgweek_write = open("wgweekfile.txt","w")
        new_days.write(changewgvalue)
        wgweek_write.close()
        changewg = False
