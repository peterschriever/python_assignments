print("Welcome to the Average Daily Temperature Program.")
print("This program requires you to have the file: station_VL.txt"\
 +" in the same folder")
stationFilePresent = input("Do you have this file? [y/n]:")
if stationFilePresent != "y":
    raise ValueError("Required file: station_VL.txt not present. Quitting.")

stationFile = open("station_VL.txt", 'r')

lstFormattedLines = []
stationFile.readline() # skip the first line
for line in stationFile:
    lstFormattedLines.append(line.strip('\n').split("\t"))
    # list format: [day, hour, temp*10] all items are integer

currentDay = '1'
sumOfHourlyTemps = 0
averageDailyTemps = []
for formattedLine in lstFormattedLines:
    sumOfHourlyTemps += int(formattedLine[2])
    if currentDay != formattedLine[0]:
        averageDailyTemps.append( (currentDay,
            round((sumOfHourlyTemps / 24) * 0.1, 1)) )
        sumOfHourlyTemps = 0
        currentDay = formattedLine[0]

print("\n")
print("Average Daily Temperatures: ")
for temps in averageDailyTemps:
    print("Day: ", temps[0], " Average Temperature: ", temps[1])

# I feel pretty bad for using 3 different loops and this probably sub-optimal
# code, but I cba to update it tbh. Just so you know, I know its pretty bad.
