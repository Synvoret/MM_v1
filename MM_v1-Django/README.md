
If You want start develop server Django:
(venv) PS C:\Users\lukasz.szabat\Desktop\Pulpity\Pulpit_05_12_2024\KursPython\_free_apps\MM_v1\MM_v1-Django\app> .\start.bat





EXAMPLE structure for big Django Project:
myproject/
├── myproject/                  # Główny katalog projektu
│   ├── __init__.py
│   ├── settings/              # Ustawienia projektu
│   │   ├── __init__.py
│   │   ├── base.py            # Wspólne ustawienia
│   │   ├── development.py     # Ustawienia deweloperskie
│   │   ├── production.py      # Ustawienia produkcyjne
│   │   └── testing.py         # Ustawienia testowe
│   ├── urls.py                # Główne URL-e projektu
│   ├── wsgi.py                # WSGI config
│   └── asgi.py                # ASGI config
├── apps/                      # Katalog na aplikacje Django
│   ├── __init__.py
│   ├── core/                  # Aplikacja core (np. wspólne funkcjonalności)
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── admin.py
│   │   ├── urls.py
│   │   └── tests/
│   │       ├── __init__.py
│   │       └── test_models.py
│   ├── users/                 # Aplikacja użytkowników
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── admin.py
│   │   ├── urls.py
│   │   └── tests/
│   │       ├── __init__.py
│   │       └── test_views.py
│   └── api/                   # Aplikacja API
│       ├── __init__.py
│       ├── views.py
│       ├── serializers.py
│       ├── urls.py
│       └── tests/
│           ├── __init__.py
│           └── test_serializers.py
├── static/                    # Pliki statyczne
│   ├── css/
│   ├── js/
│   └── images/
├── templates/                 # Szablony HTML
│   ├── base.html
│   ├── core/
│   └── users/
├── manage.py                  # Skrypt zarządzający Django
├── requirements/              # Pliki zależności
│   ├── base.txt
│   ├── development.txt
│   └── production.txt
├── .env                       # Zmienne środowiskowe
├── .gitignore                 # Plik .gitignore
├── README.md                  # Dokumentacja projektu
└── docker-compose.yml         # Konfiguracja Docker Compose
