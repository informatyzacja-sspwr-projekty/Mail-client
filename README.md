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

* (1) :black_square_button: Wczytanie listy z mailami oraz nazwą użytkownika
* (2) :black_square_button: Wczytanie maila z którego będziemy wysyłać, login, hasło, serwer
* (3) :black_square_button: Wczytanie wiadomości którą chcemy wysłać

## przetworzenie danych

* (1) :speech_balloon: Wygenerowanie listy *Krotek* < [(username1,email1,uuid1), (username2,email2,uuid2)] >
* (2) :speech_balloon: Wygenerowanie uuid do maili
* (3) :black_square_button: Przekonwertowanie Krotek na słownik Python dict =  ('username' : 'nazwa_użytkownika', 'email': 'email''uuid':'uuid')  
* (4) :black_square_button: Przekonwertowanie słownika do JSON
* (4) :black_square_button: Przekonwertowanie klasy do JSON
* (5) :black_square_button: Zapisanie tego do JSON
