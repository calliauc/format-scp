# format-scp
Petit script python parce que ça me saoule de mettre des antislash à la main
C'est pensé pour récupérer des films et series sur mon nas, donc faudra adapter pour un usage plus général.

## Explication et cofiguration

Configurer des variables d'environnement pour la cible scp
export NAS_LOGIN="account"
export NAS_IP="192.168.0.50"
export NAS_PATH="/media/data"
export NAS_PORT="22"

Lancer le script avec le paramètre -f ou -s pour recup un film ou une serie (propre à mon nas, faudra éditer dans le code)
Et enfin -n "nom" pour le nom du fichier ou répertoire à récupérer
Le script ajoute automatiquement .mkv dans certains cas, encore une fois c'est propre à mon usage
Le principal intérêt reste le fomatage du nom, l'ajout des antislash.

## Exemple d'utilisation

Pour le film "Truc le film (2023).mkv"

Ecrire la commande `python3 main.py -f -n "Truc le film (2023)`

Lancera la commande `scp -rP 22 account@192.168.0.50:/media/data/Films/"Truc\ le\ film\ \(2023\).mkv" .`
