# Utiliser une image de base Python 3
FROM python:3.11.9

# Définir le répertoire de travail dans le conteneur Docker
WORKDIR /app

# Copier les fichiers de dépendances dans le répertoire de travail
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste des fichiers dans le répertoire de travail
COPY . .

# Exposer le port pour l'application
ENV PORT=5000
EXPOSE $PORT

# Utiliser Gunicorn comme serveur WSGI
CMD gunicorn -b 0.0.0.0:$PORT api:app

# Définir le volume pour le répertoire des données
VOLUME [ "/app/datas" ]