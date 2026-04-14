import csv
import requests
from bs4 import BeautifulSoup

date = input("Enter date (month/day/year): ")

page = requests.get(f'https://www.yallakora.com/matches?date={date}')
soup = BeautifulSoup(page.content, 'lxml')

with open("matches.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Championship", "Team A", "Team B", "Time"])

    match_cards = soup.find_all("div", class_="matchCard")

    for card in match_cards:
        championship_name = card.find("h2").text.strip()
        print("\n🏆", championship_name)

        matches = card.find_all("div", class_="item")

        for match in matches:
            team_a = match.find("div", class_="teamA").text.strip()
            team_b = match.find("div", class_="teamB").text.strip()
            time = match.find("span", class_="time").text.strip()

            print(team_a, "vs", team_b, "|", time)

            writer.writerow([championship_name, team_a, team_b, time])
