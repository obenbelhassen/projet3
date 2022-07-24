# projet3


j'ai  choisi la base de donée "top250" disponible sur le site kaggle: https://www.kaggle.com/datasets. Les donnees sont sous forme de table ce qui justifie le choix de sql pour ces donnees. En fait c'est une base de donnees relationnelle et les donnees sont structures.

Description des choix faits au long du projet

Script pour peupler la bdd : 

df = pd.read_csv('top250-00-19.csv')

df.to_sql('top250', conn, if_exists='append', index = False)

utilisation de la methode pandas.DataFrame.to_sql pour stocker les donnees de la dataframe dans une base de donnees


Les routes de l'api :  J'ai utilise des templates html : une pour l'affichage des tableaux et une pour la route d'ajout de joueur 

/first5 : retourne les informations des 5 premiers joueurs dans la base de donnees 

/most_expensive : retourne les informations du joueur avec le transfert le plus cher

/add_player : rajouter les informations d'un joueur a la base de donnees

/list : lister la totalite de la base de donnees 

Dockerfile: creation des images a partir des fichiers dockerfile

docker image build . -t my_api:latest

cd /database

docker image build . -t my_database:latest

Docker compose :

creation de network :

docker network create --gateway 172.16.0.1 --subnet 172.16.0.0/24 app_subnet

et on fixe l'adresse ip de l'api dans le docker-compose ipv4_address: 172.16.0.10

utilisation de volumes pour passer la sortie du script utilise pour peupler la base de donnees (my_data.db) vers le container de l'api

Cote database :

  volumes:
            - ./database:/app

cote api :

  volumes:
            - .:/app
            
ajout de depends on sur le container de l'api afin que la base donnees soit deja peuplee et accessible par l'api
