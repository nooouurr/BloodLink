BLOODLINK
Application Django de gestion de dons de sang.

INSTALLATION

1. Cloner le projet
   git clone https://github.com/nooouurr/BloodLink.git
   cd BloodLink

2. Creer et activer l'environnement virtuel
   python -m venv venv
   venv\Scripts\activate        (Linux/Mac : source venv/bin/activate)

3. Installer les dependances
   pip install -r requirements.txt

4. Creer la base de donnees
   python manage.py migrate

5. Lancer le serveur
   python manage.py runserver

Ouvrir http://127.0.0.1:8000/