# Wstęp

MailBot służący do wysyłania automatycznie maili które są zapisane w pliku txt.

## Koordynator Projektu  

### Dund33

# Twórcy

| Część bota | nickname
| ---------- | -------
| Python | FilipJQ77
| Python | Byczax
| API | Dund33
| API | karolkicinski

# Potrzebne dane

* Plik txt z nazwami użytkowników oraz ich mailami
* Plik z wiadomością (odpowiednia konstrukcja)
* Plik json z loginem, hasłem do maila, hostem, portem oraz nazwą pliku txt

# Python Bot

## Wczytanie danych

* (1) :black_square_button: Wczytanie listy z mailami oraz nazwami użytkowników
* (2) :black_square_button: Wczytanie maila z którego będziemy wysyłać, login, hasło, serwer, port
* (3) :black_square_button: Wczytanie wiadomości którą chcemy wysłać
* (4) :black_square_button: Wysłanie wiadomości

## przetworzenie danych

* (1) :heavy_check_mark: Wygenerowanie listy *Krotek* < [(username1,email1,uuid1), (username2,email2,uuid2)] >
* (2) :heavy_check_mark: Wygenerowanie uuid do maili
* (3) :heavy_check_mark: Przekonwertowanie Krotek na słownik Python dict =  ('username' : 'nazwa_użytkownika', 'email': 'email''uuid':'uuid')  
* (4) :heavy_check_mark: Przekonwertowanie słownika do JSON
* (4) :heavy_check_mark: Przekonwertowanie klasy do JSON
* (5) :heavy_check_mark: Zapisanie tego do JSON

# instrukcja obsługi

### Uzupełnij plik mail_login.json
  
>Należy tam wpisać:

    maila
    hasło do maila
    adres serwera
    port ( domyślnie wszędzie powinien być 587 )
    Nazwę pliku z którego będą czytane maile do których należy wysłać wiadomość
    nazwę pliku w którym znajduje się nasza wiadomość

### Szablon pliku txt

>Plik powinien wyglądać następująco:

    użytkownik: <nazwa użytkownika>
    mail: <mail użytkownika>

Wszystko poza tym zostanie zignorowane.

### uruchamianie

* (1) Na początku należy uruchomić konwerter pliku .txt na .json
* (2) Następnie uruchamiamy bota aby rozesłał naszą wiadomość

#### Mam nadzieję że wszystko zostało wyjaśnione

Gdy są jakieś wątpliwości to pisać, komentować :smile:
