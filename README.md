# Projet de Gestion

Ce projet est un système de gestion simple utilisant le design pattern Strategy pour la gestion des notifications. Il permet d'envoyer des notifications via différents canaux tels que l'e-mail et le SMS.

## Structure du projet
projet_gestion/
│
├── main.py
├── projet.py
├── notification.py
├── tests/
│ ├── init.py
│ └── test_projet.py
├── requirements.txt
└── README.md


## Installation

1. Clonez ce dépôt sur votre machine locale :

    ```bash
    git clone https://github.com/faLucas17/PMQPL.git
    cd PMQPL
    ```

2. Créez un environnement virtuel et activez-le :

    ```bash
    python -m venv venv
    source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\activate`
    ```

3. Installez les dépendances :

    ```bash
    pip install -r requirements.txt
    ```

## Utilisation

1. Modifiez le fichier `main.py` pour configurer et envoyer des notifications selon vos besoins.

2. Exécutez le script principal :

    ```bash
    python main.py
    ```

    
## Tests

1. Pour exécuter les tests, utilisez la commande suivante :

    ```bash
    python -m unittest discover tests
    ```

## Dépendances

Toutes les dépendances sont listées dans le fichier `requirements.txt`. Utilisez `pip` pour les installer :

```plaintext
radon==6.0.1
flake8==7.0.0

