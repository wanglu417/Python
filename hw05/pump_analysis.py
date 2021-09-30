# Magic numbers used in this program
MINUTES_PER_HOUR = 60
GALLONS_PER_MINUTE = 2
WATTS_PER_MINUTE = 1000
HOURS_PER_DAY = 24
KWMINUTE_PER_HOUR = 60000
MIN_MINUTES_PER_ROW = 120
GALLONS1 = 5
GALLONS2 = 100
# Get input of file name from the user
file_name = input("Please enter the file name: ")


def exists(file_name):
    # exists() takes a filename and returns true
    # if the file exists, false if it doesn't
    try:
        f = open(file_name, 'r')
        f.close()
        return True
    except IOError:
        print("Unable to open", file_name)


def getlines():
    # Count lines(minutes) of the file and convert it to hours and days
    count_minutes = len(open(file_name, 'r').readlines())
    count_hours = round(count_minutes/MINUTES_PER_HOUR, 1)
    count_days = round(count_hours/HOURS_PER_DAY, 3)
    print("Data covers a total of", count_hours, "hours")
    print("(That's", count_days, "days)")


def getconsumption():
    # Read the comma-separated integer data from
    # the text file and return the data in a list
    # List initially empty
    result = []
    with open(file_name, 'r') as f:
        for line in f:
            # Remove any trailing spaces, comma, and newline
            result += [int(x.strip()) for x in line.rstrip(" ,\n").split(",")]
    total_minutes = round(sum(result)/WATTS_PER_MINUTE)
    total_gallons = GALLONS_PER_MINUTE * total_minutes
    kWh = sum(result)/KWMINUTE_PER_HOUR
    gallons_per_day = round(float(total_gallons * HOURS_PER_DAY), 1)
    print("Pump was running for", total_minutes,
          "minutes,", "producing", total_gallons, "gallons")
    print("That's", gallons_per_day, "gallons per day")
    print("Pump required a total of", sum(result), "watt minutes of power")
    print("That's", round(kWh, 3), "kWh")


def time_needed():
    result = []
    # Read the comma-separated integer data from the
    # text file and return the data in a list
    with open(file_name, 'r') as f:
        for line in f:
            result += [int(x.strip()) for x in line.rstrip(" ,\n").split(",")]
    # get minutes needs and translate them into watts needed
    minutes_needed = round(GALLONS1 / GALLONS_PER_MINUTE, 1)
    watts_needed = WATTS_PER_MINUTE * minutes_needed
    minutes_needed2 = round(GALLONS2 / GALLONS_PER_MINUTE, 1)
    watts_needed2 = WATTS_PER_MINUTE * minutes_needed2
    sum = 0
    for i in range(0, len(result)):
        # find i if sum of result[i] >= expected watts
        sum += result[i]
        if sum >= watts_needed:
            minutes = i+1
            print("It took", minutes, "minutes of data to reach 5 gallons.")
            break
    # if sum of result[i] >= expected watts drawn
    flag = False
    for i in range(0, len(result)):
        sum += result[i]
        if sum >= watts_needed2:
            flag = True
            print(i+1)
            break
    # if sum of results[i] < expected watts, print "-1"
    if not flag:
        minutes2 = -1
        print("It took", minutes2,
              "minutes of data to reach 100 gallons")


def softener_recharge():
    print("Information on water softener recharges: ")
    # List initially empty
    result2 = []
    with open('pump_data.txt', 'r') as f:
        for line in f:
            result2 += [int(x.strip()) for x in line.rstrip(" ,\n").split(",")]
        t = []
        sum = 0
        for i in range(0, len(result2)):
            # count i if result[i] > 500
            if result2[i] > WATTS_PER_MINUTE/2:
                sum += 1
            else:
                # result[i] == 0 or ==-1 or < 500
                if sum >= MIN_MINUTES_PER_ROW:
                    t.append([i-sum+1, sum])
                sum = 0
    for i in range(0, len(t)):
        print(t[i][1], "minute run started at", t[i][0])


# wrap functions in main
def main():
    if exists(file_name):
        getlines()
        getconsumption()
        time_needed()
        softener_recharge()


main()
