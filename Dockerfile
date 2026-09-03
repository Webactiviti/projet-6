FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1 \
    PORT=3000

WORKDIR /app

# Installation des dépendances système
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# Installation de uv
RUN pip install --no-cache-dir uv

# Copie du projet
COPY . /app

# Installation des dépendances Python (s'adapte à pyproject.toml ou requirements.txt)
RUN uv pip install --system -e . || uv pip install --system -r requirements.txt || true

EXPOSE 3000

# Commande de démarrage BentoML
CMD ["uv", "run" ,"bentoml", "serve", ".", "--port", "3000"]
