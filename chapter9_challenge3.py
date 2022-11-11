import csv

movies = [["TopGun", "RiskyBusiness", "MinorityReport"],
          ["Titanic", "TheRevenant", "Inception"],
          ["TrainingDay", "ManonFire", "Flight"]]

with open("movie.csv", "w", newline="") as f:
    w = csv.writer(f, delimiter=",")
    for movie in movies:
        w.writerow(movie)
