from bs4 import BeautifulSoup
import requests
 
videogames_page = requests.get("https://en.wikipedia.org/wiki/List_of_best-selling_video_games")
vgame_soup = BeautifulSoup(videogames_page.content, "html.parser")
games_table = vgame_soup.find("table")
games_th = games_table.find_all("th")
categoryHeaders = []

for th in games_th:
    categoryHeaders.append(th.get_text().strip())
header_string = ",".join(categoryHeaders)

table_rows = games_table.find_all("tr")
games_rows = [header_string]

for row in table_rows:
    row_list = []
    print(row)
    for cell in row.find_all("td"):
        cell_text = cell.get_text().strip()
        row_list.append(cell_text)
    row_string = ",".join(row_list)
    games_rows.append(row_string)
    
print(games_rows)