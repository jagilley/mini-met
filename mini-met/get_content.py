import requests
import os

"""curl -X POST \
  https://chrome.browserless.io/content?token=MY_API_TOKEN \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -d '
{
  "url": "https://example.com/"
}'
"""

def get_content(site_url):
    response = requests.post(
        "https://chrome.browserless.io/scrape",
        params={
            "token": os.getenv("BROWSERLESS_API_KEY"),
        },
        json={
            "url": site_url,
            "elements": [
                {
                    "selector": "body",
                }
            ],
        },
    )
    return response.json()["data"][0]["results"][0]["text"]