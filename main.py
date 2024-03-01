from selenium import webdriver
import time
from datetime import date, datetime
from selenium.webdriver.common.keys import Keys
import matplotlib.pyplot as plt
import os

"""
    This program gets the Premier League table as arrays, then it creates a bar graph, saves that graph to desktop in a
    folder named PL_Tables (if it doesn't exists it creates one)
    Author: Okkes Donbaloglu 
"""

# After importing python libraries create the driver as chrome driver
driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.maximize_window()

# Go to google
driver.get("https://www.google.com")

# Find the search bar and write pl and hit enter to search
# In here if you want to search for some other leagues you can edit below string "pl"

driver.find_element(by="xpath", value='//*[@id="APjFqb"]').send_keys("pl")
driver.find_element(by="xpath", value='//*[@id="APjFqb"]').send_keys(Keys.ENTER)
time.sleep(3)

# Try to get the week of the leagues or get the current day and edit it, we will show it on the title of the graph
# and use it to create the file
try:
    week = driver.find_element(by="xpath", value='//*[@id="sports-app"]/div/div[1]/div/div/div[2]/span').text
    print(week)
    filename = week[4:6]

except:
    week = datetime.today().strftime("%B %d, %Y") # Month Day Year format
    filename = week[:11]

# Click to the table button
driver.find_element(by="xpath", value='//*[@id="sports-app"]/div/div[2]/div/div/div/ol/li[3]').click()
time.sleep(3)

# Get the names and points and add them to arrays
template = '//*[@id="liveresults-sports-immersive__league-fullpage"]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody'
i = 0
team_number = 20
teams = []
points = []

while i < team_number:

    # Get the name
    name = driver.find_element(by="xpath", value=template + '/tr[' + str(i+2) + ']/td[3]/div/div/span').text
    teams.append(name)

    # point elementi
    point = driver.find_element(by="xpath", value=template + '/tr[' + str(i+2) + ']/td[11]/div').text
    points.append(point)

    i += 1

print(teams)
print(points)

# Close the browser we don't need it anymore
driver.quit()

# It needs to be integer instead of string in order to show it in graph
points = [int(point) for point in points]

fig, ax1 = plt.subplots(figsize=(11, 7))

# Create a bar graph and style it
bars = ax1.bar(teams, points, color=['blue', 'blue', 'blue', 'blue', 'orange'] + ['gray'] * (len(teams) - 8) + ["red"] * 3)
plt.xlabel("Teams", fontsize=16, labelpad=12)
plt.ylabel("Points", fontsize=16, labelpad=12)
plt.title("Premier Leauge (" + str(week[4:]) + ")", fontsize=14, pad=14, fontweight="bold")
plt.xticks(rotation=90, ha='right')
plt.subplots_adjust(bottom=0.3)

# Write the points of the first three teams
for bar, point in zip(bars[:3], points[:3]):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(point), ha='center', va='bottom')

# Create the filepath which we'll create pdf later
file_path = os.path.expanduser('~') + r"\Desktop\PL_Tables\PL_Table_{}.pdf".format(filename)

# Check if there is an old pdf, and if there is remove it because we'll create a new one
if os.path.exists(file_path):
    os.remove(file_path)
    print("Mevcut dosya silindi.")

# Check if there is a folder named PL_Tables, if there is not create one because we'll put pdf in it
if not os.path.exists(os.path.expanduser('~') + r"/Desktop/PL_Tables"):
    os.makedirs(os.path.expanduser('~') + r"/Desktop/PL_Tables")
    print("klasör olustu")

# Create the pdf file with the given file_path
plt.savefig(file_path, format='pdf')

# And open the graph after saving it
plt.show()
