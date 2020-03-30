#  Kanban

Prosty Kanban zrobiony w Django.

## Instalacja
- Pobrać najnowszą wersję Pythona
- Na ścieżce C:\Users\twoja_nazwa_użytkownika\AppData\Local\Programs\Python\Python37\Scripts\ ,wykonać komendę:
    

```bash
py -m pip install Django
```
-  Jeśli polecenia 'py' lub 'python' nie działają należy dodać dwie ściężki do PATH w zmiennych środowiskowych użytkownika:
C:\Users\przem_41pf48b\AppData\Local\Programs\Python\Python37
C:\Users\przem_41pf48b\AppData\Local\Programs\Python\Python37\Scripts

## Obsługa
Komentarze w dużej mierze tłumaczą co się dzieje w poszczególnych segmentach, jednakże najważniejsze pliki w projekcie to:
- /tameplates/index.html
- /kanban/models.py
- /kanban/views.py
- /assets/script.js

By uruchomić serwer należy ustawić się w folderze w konsoli gdzie znajduje się plik 'manage.py' i  wykonać poszczególne komendy:

```bash
py manage.py migrate
py mnage.py makemigrations
```
Te dwie komendy eksportują Dane z 'models.py' do bazy danych.
Uruchomienie serwera:
```bash
    py manage.py runserver
```
By zobaczyć stronę należy wpisać adres: http://127.0.0.1:8000/kanban
By zobaczyć panel administracyjny należy wpisać adres: http://127.0.0.1:8000/admin
Dane do logowania:
 - Login: admin
 - Hasło: Q@wertyuiop



