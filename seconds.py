time = float(input("Enter the amount of time in seconds: "))
minutes = time % 60
hour = time // 3600
second= int(time %60)
print(hour,"hour" ,minutes, "minutes",second,"seconds" )
