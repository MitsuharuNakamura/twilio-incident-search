###########################################################################
# 過去のインシデントを検索して、特定のキーワードを含むインシデントをみつける
###########################################################################
import requests
from bs4 import BeautifulSoup
import json

# 検索キーワード
search_word = 'Japan'
# 対象とするIncidentsのページ数
max_pages = 5 # 4ページまで
# Twilio IncidentsのページURLのベース
base_url = "https://status.twilio.com/history"

# ページ番号を指定して繰り返し処理
for page in range(1, max_pages): 
    url = f"{base_url}?page={page}"

    # Send a GET request to fetch the HTML content
    try:
        response = requests.get(url)
        response.raise_for_status()  # ステータスコードが200以外の場合は例外を発生
    except requests.RequestException as e:
        print(f"Failed to fetch the webpage: {e}")
        continue

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all elements with the 'data-react-props' attribute
    elements_with_props = soup.find_all(attrs={'data-react-props': True})

    # Extract and parse JSON data
    for element in elements_with_props:
        data = element.get('data-react-props')
        if not data:
            continue

        try:
            # Convert the JSON-like string into a dictionary
            parsed_data = json.loads(data)
        except json.JSONDecodeError as e:
            print(f"Failed to parse JSON: {e}")
            continue

        # Check if 'months' exists in the parsed data
        for month in parsed_data.get('months', []):
            # Check if 'incidents' exists in the current month
            for incident in month.get('incidents', []):
                name = incident.get('name', 'N/A')  # Get 'name', default to 'N/A'
                message = incident.get('message', 'N/A')  # Get 'message', default to 'N/A'
                timestamp = incident.get('timestamp', 'N/A')  # Get 'timestamp', default to 'N/A'

                # Filter: Check if the keyword is in 'name' or 'message'
                if search_word.lower() in name.lower() or search_word.lower() in message.lower():
                    print(f"Timestamp: {timestamp}")
                    print(f"Name: {name}")
                    print(f"Message: {message}")
                    print("-" * 80)
