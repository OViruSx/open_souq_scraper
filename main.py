import requests
import json
from bs4 import BeautifulSoup
import pandas as pd 
from datetime import datetime
import os 


def scrape_cars(base_url, total_pages):
    cars_data = []
    
    for page in range(1, total_pages + 1):
        # Append or modify the page query parameter
        url = f"{base_url}&page={page}&Car_Year_from=2020&Car_Year_to=2024&Brand_child=6977,6979,6981,7405,6983,6985,13073,7407,7409,8399,8403,13262"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        

        # Find the script tag containing the JSON object
        # This logic may need to be adjusted based on how the JSON is embedded
        scripts = soup.find_all('script')
        for script in scripts:
            if 'ItemList' in script.text:
                json_text = script.text
                # Further processing to isolate the JSON object
                # This is a placeholder: You’ll need to extract and clean the JSON string appropriately
                break
        
        # Load the JSON data
        try:
            data = json.loads(json_text)
            
            # Extract data for each car in the JSON object
            for item in data['itemListElement']:
                name = item['name']
                url = item['url']
                price = item['offers']['price']
                image_url = item['image']
                
                cars_data.append({ 
                    "Name": name,
                    "Price": price,
                    "URL": url,
                    "Image URL": image_url
                })
        except Exception as e:
            print(f"Error processing page {page}: {e}")
            continue

    return cars_data
# Example usage
base_url = "https://om.opensooq.com/en/cars/cars-for-sale/bmw/bmw-m3?search=true"
total_pages = 5
cars_details = scrape_cars(base_url, total_pages)
# for car in cars_details:
#     print(car)
df = pd.DataFrame(cars_details)
df['Date'] = datetime.today().strftime('%Y-%m-%d-%H:%M')
print(df)
file_exists = os.path.exists('Cars.csv')

# Write the DataFrame to CSV, appending if it exists, including headers if it doesn't
df.to_csv('Cars.csv', mode='a', header=not file_exists, index=False, encoding='utf-8-sig')