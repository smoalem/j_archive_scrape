import bs4 as bs
import urllib.request
import numpy as np
import pandas as pd
import time
import re


if __name__ == "__main__":
    start = time.perf_counter()
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
