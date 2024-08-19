# Awesome Text Only News
# https://github.com/localjo/awesome-text-only-news?tab=readme-ov-file

import requests
from bs4 import BeautifulSoup

# Step 1: Fetch the webpage
url = "https://lite.cnn.com/"
response = requests.get(url)

print(response.status_code)
