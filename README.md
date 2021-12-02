# MailBot

MailBot służy do wysyłania automatycznie maili o określonej treści do odbiorców, którzy są zapisani w pliku txt.

## Konfiguracja

### Struktura pliku konfiguracyjnego

> `config/config.json` (szablon: `config/config.json.example`)

```json
[
  {
    "mail": "informatyzacja@samorzad.pwr.edu.pl",
    "password": "",
    "host": "student.pwr.edu.pl",
    "port": 587,
    "mails_txt_file": "mails.txt",
    "mails_json_file": "mails.json",
    "subject": "Informatyzacja mailbot test",
    "mail_template": "mail_template.txt",
    "confirm_link": "https://ewidencjamaili.samorzad.pwr.edu.pl/confirm?uuid="
  }
]
```

- `mail` - adres e-mail nadawcy,
- `password` - hasło nadawcy,
- `host` - adres serwera mailowego,
- `port` - port SMTP serwera,
- `mails_txt_file` - nazwa pliku `.txt` w katalogu `data` zawierająca listę maili wraz z użytkownikami, którzy mają być końcowymi odbiorcami wiadomości (struktura pliku poniżej),
- `mails_json_file` - nazwa pliku `.json` (w katalogu `data`), do której ma być zapisana struktura danych zawierająca nazwy użytkowników, adresy e-mail oraz ich UUID,
- `subject` - temat wiadomości
- `mail_template` - nazwa pliku `.txt`, w którym jest szablon wiadomości przesyłanej do użytkowników (struktura pliku poniżej),
- `confirm_link` - link do strony służącej do potwierdzania użytkowników z przygotowanym już wcześniej polem w adresie do przyjęcia żądania `HTTP GET`

### Szablon pliku pod `mails_txt_file`

Pojedynczy rekord danych powinien wyglądać następująco:

    użytkownik: <nazwa użytkownika>
    mail: <mail użytkownika>

Rekordów może być dowolna ilość, wszystko poza tym schematem zostanie zignorowane.

### Szablon pliku pod `mail_template`

Treść pliku może być dowolna, istnieją ponadto dwa literały podmiany indywidualizujące treść maila:

- `{user}` jest zamieniane w treści maila na nazwę danego użytkownika z pliku
- `{confirm_link}` jest zamienane na podany link wraz z dodanym UUID danego użytkownika

## Kroki konfiguracji

1. Przekopiuj plik `config/config.json.example` jako `config/config.json`.
2. Wprowadź swoją konfigurację do utworzonego wyżej pliku.
3. Postąp tak samo w przypadku pliku zapisanego pod `mail_template`.
4. Utwórz katalog `data`, po czym umieść w nim plik zapisany pod `mails_txt_file`.

## Uruchamianie

Wystarczy wpisać polecenie:

    python index.py

Należy być jednak ostrożnym, gdyż przy każdym uruchomieniu generowane jest nowe UUID każdego użytkownika, rozsyłane także zaczynają być maile.

## Po uruchomieniu

Koniecznie zapisz w bezpiecznym miejscu pliki

- `data/mails.json` - struktura danych zawierająca niezbędne UUID
- `logs/sent.log` - lista adresów, na które udało się wysłać mail
- `logs/notsent.log` - lista adresów, na które nie udało się wysłać maila

## Twórcy

#### Koordynator Projektu - Dund33

|        | Nickname      |
| ------ | ------------- |
| Python | FilipJQ77     |
| Python | Byczax        |
| Python | Omikorin      |
| API    | Dund33        |
| API    | karolkicinski |
