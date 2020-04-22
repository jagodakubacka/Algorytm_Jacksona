
s = []  # Moment rozpoczęcia
c = []  # Moment zakończeni
r = []  # Termin dostępności
p = []  # Czas wykonania

Pi = []  # Posegregowany zbiór zadań z rosnącym r
A = []  # Tablica poomocnicza do odczytu danych

# Wczytanie danych
f = open("JACK2.DAT", "r")
for i in f:
    A.append(i)  # Przypisanie danych z pliku
n = int(A[0])  # Liczba zadań
for x in range(len(A)):
    if x == 0:
        r.append(0) # tutaj stworzenie tych pierwszych zer, aby dobrze czytać plik
        p.append(0) #
    else:
        B = A[x].split()
        r.append(int(B[0]))  # Termin dostępności - pierwsza kolumna to termin dostępności
        p.append(int(B[1]))  # Czas wykonania - to jest druga kolumna

c.append(0)

X = []

# Stworzenie tablicy zawierającej numer zadania oraz jego termin dostępności
for x in range(n+1):
    a = (r[x], x)
    X.append(a) # to jest tablica, która zawiera termin dostępności zadania oraz numer zadania

# Sortowanie zadań względem r (tak by rosło)
X.sort() #sortowanie zadań względem r

# Stworzenie uporządkowanej tablicy Pi
for x in range(n+1):
    Pi.append(X[x][1]) #teraz jest tworzona tablica tych numerów zadań w zależności od r

# Poukładanie zadań w odpowiedzniej kolejności
for i in range(1, n+1):
    print(i)
    c.append(max(r[Pi[i]], c[i-1]) + p[Pi[i]])

print("Czas wykonania dla kolejności Pi:")
print(c[len(c)-1])

