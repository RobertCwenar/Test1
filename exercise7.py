
liczby = [3, 5, 2, 8, 6, 1, 4, 7]

potegawanie = []
for liczba in liczby:
    potegawanie.append(liczba ** 2)


liczbyParzyste = []
for liczba in liczby:
    if liczba % 2 == 0:
        liczbyParzyste.append(liczba)


potegiDwojki = [element**2 for element in liczby]

liczbyParzyste2 = [element for # elemety wybierane z listy liczby
                   element in liczby # przechodzimy po elementach listy liczby
                   if element % 2 == 0] # warunek, który musi być spełniony, aby element znalazł się na liście