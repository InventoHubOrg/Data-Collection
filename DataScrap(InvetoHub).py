# %%
# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

# %%


# %%
import gspread
from google.oauth2.service_account import Credentials

# Path to your service account JSON file
SERVICE_ACCOUNT_FILE = "/kaggle/input/supportingfile/service_account.json"

# Define the scope for the API
SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

# Authenticate with the service account
credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Access the Google Sheet
client = gspread.authorize(credentials)
spreadsheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1P6pq8tYcCWcmcFwar-crm-M7vwEzWgOE-s5I_uppMm8/edit?usp=sharing")
sheet = spreadsheet.sheet1

# Get the title and paragraphs (or content from cells)
rows = sheet.get_all_records()  # Fetch all rows as a list of dictionaries
print(rows)


# %%
#export GOOGLE_APPLICATION_CREDENTIALS="/kaggle/input/supportingfile/service_account.json"


# %%
import os
from google.auth import default

credentials, project = default()

# %%
# Extract the data from list[] of dictionaries{} in table format
import pandas as pd

# Example list of dictionaries
data = rows 

# Convert to DataFrame
df = pd.DataFrame(data)

# Remove trailing '>' from the Link column
df['Link'] = df['Link'].str.rstrip('>')

# Display the updated DataFrame
print(df.to_string(index=False))

df.to_csv('saved_files(1)', index=False)

print("File saved Successfully")


# %%


# %% [markdown]
# ## Extracting Data(Scraping Data)

# %%
import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://cxotoday.com/press-release/velocity-travel-secures-funding-from-new-york-based-investor-raj-shah-at-10m-pre-money-to-transform-business-travel/"

# Send a GET request to the webpage
response = requests.get(url)

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the article's title
title = soup.find('h1').get_text()

# Extract the publication date (if available)
date = soup.find('time')
if date:
    publication_date = date.get_text()
else:
    publication_date = "Date not found"

# Try extracting the content from the article body (adjust selector as needed)
content = soup.find('div', {'class': 'post-content'})  # Adjust if the class is different
if content:
    text = content.get_text()
else:
    text = "Content not found"

# Output the extracted details
print(f"Title: {title}")
print(f"Publication Date: {publication_date}")
print(f"Content: {text[:500]}...")  # Show a snippet of the content


# %%
import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://cxotoday.com/press-release/velocity-travel-secures-funding-from-new-york-based-investor-raj-shah-at-10m-pre-money-to-transform-business-travel/"

# Send a GET request to the webpage
response = requests.get(url)

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the article's title
title = soup.find('h1').get_text()

# Extract the publication date (if available)
date = soup.find('time')  # The <time> tag is often used for publication dates
publication_date = date.get_text() if date else "Date not found"

# Extract the main content using find_all to handle multiple <p> tags
content = soup.find_all('p')  # All <p> tags
article_text = " ".join([para.get_text() for para in content])

# Output the extracted details
print(f"Title: {title}")
print(f"Publication Date: {publication_date}")
print(f"Content: {article_text}")  # Show a snippet of the content


# %%


# %%
import pandas as pd

# Adjust display options to show full content in DataFrame
pd.set_option('display.max_colwidth', None)

df1 = pd.read_csv('/kaggle/working/saved_files(1)')

df1.head()

# %%
df1.shape

# %%
df1.info()

# %%


# %%



