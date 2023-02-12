import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import seaborn as sns 
import numpy as np

df = pd.read_csv("C:\\Users\\Rebecca\\Downloads\\pedscrashes.txt")

#Seperate data into columns
time = df.loc[:,"Time of Day"]
day = df.loc[:,"Day of Week"]
month = df.loc[:,"Crash Month"]
lighting = df.loc[:,"Lighting Conditions"]
age = df.loc[:,"Person Age"]
gender = df.loc[:,"Person Gender"]
injuries = df.loc[:,"Worst Injury in Crash"]
weather = df.loc[:,"Weather Conditions (2016+)"]
hitandrun = df.loc[:, "Crash: Hit-and-Run"]

#Pie charts comparing percentages of hit and runs during the daylight vs dark-lighted
def hitandrun_lighting():
    dark_lighted = []
    daylight = []
    other = []
    #seperating by lighting, not the fastest way
    for (x, y) in zip(lighting, hitandrun):
        if x == 'Dark lighted':
            dark_lighted.append(y)
        elif x == 'Daylight':
            daylight.append(y)
        else:
            other.append(y)

    a = Counter(dark_lighted)
    b = Counter(daylight)
    #drawing first pie chart, dark-lighted
    plt.figure(0)
    colors = ['cyan', 'red']
    plt.pie(a.values(), labels = a.keys(), colors = colors, autopct='%1.1f%%',
            shadow=True)
    plt.title("Dark lighted Hit and Runs")
    #drawing second pie chart, daylight
    plt.figure(1)
    plt.pie(b.values(), labels = b.keys(), colors = colors, autopct='%1.1f%%',
            shadow=True)
    plt.title("Daylight Hit and Runs")
    plt.show()

#Number of injuries by month
def injuries_month():
    month_count = Counter(month)
    plt.plot(month_count.keys(), month_count.values(), color = 'red', marker = 'o')
    plt.grid(True)
    plt.xticks(rotation=30)
    plt.title('Month vs Number of Crashes')
    plt.show()

#Severity of injury vs weather conditions
#stacked bar chart
#could possibly be done clearer with counter but was too diffiuclt to work with
def injury_severity_weather():
    injury_types = ['Suspected serious injury (A)', 'Suspected minor injury (B)', 'Possible injury (C)']
    serious_injury = []
    minor_injury = []
    possible_injury = []
    for (x, y) in zip(injuries, weather):
        if x == 'Suspected serious injury (A)':
            serious_injury.append(y)
        elif x == 'Suspected minor injury (B)':
            minor_injury.append(y)
        else:
            possible_injury.append(y)

    serious_injury_count = [0, 0, 0]
    for x in serious_injury:
        if x == "Clear":
            serious_injury_count[0] += 1
        elif x == "Cloudy":
            serious_injury_count[1] += 1
        elif x == "Rain":
            serious_injury_count[2] += 1
        
    minor_injury_count = [0, 0, 0]
    for x in minor_injury:
        if x == "Clear":
            minor_injury_count[0] += 1
        elif x == "Cloudy":
            minor_injury_count[1] += 1
        elif x == "Rain":
            minor_injury_count[2] += 1

    possible_injury_count = [0, 0, 0]
    for x in possible_injury:
        if x == "Clear":
            possible_injury_count[0] += 1
        elif x == "Cloudy":
            possible_injury_count[1] += 1
        elif x == "Rain":
            possible_injury_count[2] += 1


    weather_types = ["Clear", "Cloudy", "Rain"]

    plt.bar(weather_types, serious_injury_count, color = '#C43d34')
    plt.bar(weather_types, minor_injury_count, bottom = serious_injury_count, color = '#E4D020')
    plt.bar(weather_types, possible_injury_count, bottom = minor_injury_count, color = '#20E4C0')
    plt.legend(["Serious Injury", "Minor Injury", "Possible Injury"])
    plt.title("Severity of Injuries vs Weather Conditions")
    plt.xlabel("Weather")
    plt.ylabel("Number of Injuries")
    plt.show()



#Pie chart of age 
def age_injuries():
    age_counts = [0, 0, 0, 0, 0, 0, 0, 0]
    age_labels = ['16-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80-89']
    for x in age:
        try:
            x = int(x)
        except ValueError:
            x = 0  #default
        if x > 10 and x < 20:
            age_counts[0] += 1
        elif x < 30:
            age_counts[1] += 1
        elif x < 40:
            age_counts[2] += 1
        elif x < 50:
            age_counts[3] += 1
        elif x < 60:
            age_counts[4] += 1
        elif x < 70:
            age_counts[5] += 1
        elif x < 80:
            age_counts[6] += 1
        elif x < 90:
            age_counts[7] += 1

    plt.title("Percentage of Crashes Belonging to Each Age Group")
    myexplode=[0, 0.1, 0, 0, 0, 0, 0, 0]
    plt.pie(age_counts, explode=myexplode, labels=age_labels, autopct='%1.0f%%')
    plt.show()



#Drawing number of accidents vs time of day
def time_accidents():
    a = Counter(time).keys() #labels
    b = Counter(time).values() #counts of elements
    barcolor = [{p<190: 'green', 190<=p<=300: 'orange', p>300: 'red'}[True] for p in b]
    plt.bar(a, b, color=barcolor)
    plt.title("Number of Accidents vs Time of Day")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

time_accidents()
age_injuries()
injury_severity_weather()
injuries_month()
hitandrun_lighting()