import requests
import csv
import json

url = 'https://cricbuzz-cricket.p.rapidapi.com/stats/v1/rankings/batsmen'
headers = {
    'X-RapidAPI-Key': '62a1b6ffa5mshc112af599978152p12e9f8jsn45047491e356',
    'X-RapidAPI-Host': 'cricbuzz-cricket.p.rapidapi.com'
}
params = {
    'formatType': 'odi'
}
  
response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()

    # Check the actual keys and structure
    print(json.dumps(data, indent=4))  # <-- see structure here

    # Get ranking data from correct key
    rankings_data = data.get('rank', [])

    csv_filename = 'batsmen_rankings.csv'

    if rankings_data:
        field_names = ['rank', 'name', 'country']

        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            writer.writeheader()

            for entry in rankings_data:
                writer.writerow({
                    'rank': entry.get('rank', ''),
                    'name': entry.get('name', ''),
                    'country': entry.get('country', '')
                })

        print(f"Data fetched successfully and written to '{csv_filename}'")
    else:
        print("No ranking data available from the API.")

else:
    print("Failed to fetch data:", response.status_code)