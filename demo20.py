music_artist = ["Jackson Micheal", "Lady Gaga", "Micheal Jackson", "Taylor Swift", "Justin Bieber", 
                "Backstreet boys", "Enrique", "Marley Bob", "Mars Bruno"]

names_longer_than_10 = [art for art in music_artist if len(art)>10]
print(names_longer_than_10)

name_with_j_or_m = [art for art in music_artist if art.startswith("J") or art.startswith("M")]
print(name_with_j_or_m)

name_with_space = [art.replace(" ", "-") for art in music_artist if " " in art]
print(name_with_space)

name_with_upper = [a if a.startswith("J") or a.startswith("M") else a.upper() for a in music_artist]
print(name_with_upper)

fav_names = ["Special "+art for art in music_artist]
print(fav_names)