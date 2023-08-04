

import requests
from bs4 import BeautifulSoup

# URL to the webpage
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.html"

# Download the webpage using requests library
html_data = requests.get(url)

# Check if the request was successful (status code 200 means success)
if html_data.status_code == 200:
    print("Webpage successfully downloaded!")
else:
    print(f"Failed to download the webpage. Status code: {html_data.status_code}")
    exit()

# Parse the html data using BeautifulSoup
soup = BeautifulSoup(html_data.text, "html5lib")

# Now you can use 'soup' to extract specific data from the webpage
# For example, if the revenue data is present in a table, you can find the table and extract the data from there.
# Without knowing the structure of the webpage, I can't provide the exact code to extract Tesla revenue data.
# Please provide more details about the structure of the webpage or the location of the revenue data, and I'll help you further.
