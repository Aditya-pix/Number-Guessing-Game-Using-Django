🎯 Number Guessing Game (Django)

A simple Number Guessing Game built with Django.
The game chooses a random number between 1 and 100, and you have 10 chances to guess it!


!

🚀 Features

-> Random number generation between 1–100
-> 10 chances to guess
-> Hints if your guess is too high or too low
-> Restart option after finishing
-> Django-powered web version

🛠️ Installation & Setup

1. Clone the Repository
>>git clone https://github.com/YOUR-USERNAME/django-number-guessing-game.git
>>cd django-number-guessing-game

2. Create Virtual Environment
>>python -m venv guessingame
>>source guessingame/bin/activate   # On macOS/Linux
>>guessingame\Scripts\activate      # On Windows

3. Run Database Migrations
>>python manage.py migrate


4. Run Development Server
>>python manage.py runserver

Now open 👉 http://127.0.0.1:8000 in your browser.


📂 Project Structure
django-number-guessing-game/
│── guessingame/          # Virtual environment (ignored in git)
│── game/                 # Django app (game logic, views, templates)
│   ├── templates/
│   │   └── index.html    # Game UI
│   └── views.py          # Game logic
│── project/              # Django project settings
│── manage.py
│── requirements.txt
│── .gitignore
│── README.md
