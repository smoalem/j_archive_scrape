import bs4 as bs
import urllib.request
import numpy as np
import pandas as pd
import time
import re


def episode_scraper(episode_number):
    source = urllib.request.urlopen(
        "https://j-archive.com/showgame.php?game_id=" + str(6793)
    )
    soup = bs.BeautifulSoup(source, "html.parser")
    # print(soup)
    game_title = soup.find(id="game_title").text.strip()
    print(game_title)


episode_scraper(6793)
raise ValueError


if __name__ == "__main__":
    start = time.perf_counter()

    episode_numbers_list = list(range(1, 82913))
    # print(episode_numbers_list)
    # print(len(episode_numbers_list))
    # raise ValueError

    source = urllib.request.urlopen("https://j-archive.com/listseasons.php")
    soup = bs.BeautifulSoup(source, "html.parser")
    seasons_array = []
    table = soup.table
    table_rows = table.find_all("tr")
    # hlinks = []
    hlink_extract = time.perf_counter()
    for tr in table_rows:
        td = tr.find_all("td")
        row = [i.text.strip() for i in td]
        row = row[:-1]
        if len(row) == 3:
            seasons_array.append(row)
            print(row)

    print(seasons_array)
    seasons_columns = ["season", "date_range", "total_games"]
    df = pd.DataFrame(seasons_array, columns=seasons_columns)
    print(df)
