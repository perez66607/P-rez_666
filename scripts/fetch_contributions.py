import os
import json
from bs4 import BeautifulSoup
import requests

USERNAME = "perez66607"
URL = f"https://github.com/users/{USERNAME}/contributions"

def fetch_contributions():
    print(f"Obteniendo contribuciones para {USERNAME}...")
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(URL, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Error al conectar con GitHub: {response.status_code}")
    
    soup = BeautifulSoup(response.text, 'html.parser')
    days = soup.find_all('td', class_='ContributionCalendar-day')
    
    data = []
    for day in days:
        date = day.get('data-date')
        level = day.get('data-level')
        count_text = day.text.strip()
        
        count = 0
        if count_text:
            parts = count_text.split()
            if parts[0].isdigit():
                count = int(parts[0])
                
        data.append({
            "date": date,
            "level": int(level) if level else 0,
            "count": count
        })
        
    os.makedirs("data", exist_ok=True)
    with open("data/contributions.json", "w") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    fetch_contributions()
