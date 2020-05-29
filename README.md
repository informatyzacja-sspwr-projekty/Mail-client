# Wstęp

MailBot służący do wysyłania automatycznie maili które są zapisane w pliku csv.

## Główno dowodzący : Dund33

# Twórcy

| Część bota | nickname
| ---------- | -------
| Python | Byczax
| Python | FilipJQ77
| API | Dund33
| API | karolkicinski

# Potrzebne dane

* Plik csv z nazwą użytkownika oraz mailem
* Plik z wiadomością
* Plik z loginem oraz hasłem do maila

# Python Bot

## Wczytanie danych

* (1) Wczytanie listy z mailami oraz nazwą użytkownika
* (2) Wczytanie maila z którego będziemy wysyłać, login, hasło, serwer
* (3) Wczytanie wiadomości którą chcemy wysłać

## przetworzenie danych

* (1) Wygenerowanie listy *Krotek* < [(username1,email1,uuid1), (username2,email2,uuid2)] >
* (2) Wygenerowanie uuid do maili
* (3) Przekonwertowanie Krotek na słownik Python dict =  ('username' : 'nazwa_użytkownika', 'email': 'email''uuid':'uuid')  
* (4) Przekonwertowanie słownika do JSON
* (4) Przekonwertowanie klasy do JSON
* (5) Zapisanie tego do JSON
