# Projet-4 Utilisez les bases de Python pour l'analyse de marché

## Prérequis
- Python 3
- Git.

## Récupérer le projet :
```sh
git clone https://github.com/lmdevpy/ocr-project-four.git
```

## Création de l'environnement virtuel

```sh
python -m venv env
```

## Activation de l'environnement virtuel

Une fois l'environnement virtuel créé, vous pouvez l'activer.
Sur Windows, lancez :
```sh
env\Scripts\activate.bat
```
Sur Unix et MacOS, lancez :
```sh
source env/bin/activate
```

## Il faudra ensuite installer les dépendences necessaires au script:
```sh
pip install -r requirements.txt
```

## lancer l'application à la racine du projet:
```sh
python -m chess
```


## Générer un rapport avec FLAKE8:
```sh
flake8 chess --format=html --htmldir=flake8_rapport  --max-line-length=119 
```