import os

class Engine:
    def __init__(self, args, logger):
        self.logger = logger
        self.logger.debug(args)
        self.name = args.name
        self.command = 'scp -rP'
        self.logger.debug("Recuperation des variables d'environnement")
        self.port = os.getenv('NAS_PORT') 
        self.account = os.getenv('NAS_LOGIN')
        self.ip = os.getenv('NAS_IP')
        self.path = os.getenv('NAS_PATH')
        self.destination = args.destination
        if args.film == True :
            self.type = 'Films'
        elif args.serie == True :
            self.type = 'Series'
        else :
            self.logger.error('Il faut spécifier le type de contenu (--film ou --serie)')
            return 1


    def run(self):
        ext = os.path.splitext(self.name)[1]
        if self.type == 'Films' and ext not in ['.avi', '.mp4']:
            self.logger.debug("Ajout automatique de l'extension .mkv")
            self.name += '.mkv'
        self.name = self.name.replace(' ', '\ ').replace('(', '\(').replace(')', '\)').replace(')', '\)').replace('\'', '\\\'')

        commande = self.command
        commande += ' '
        commande += self.port
        commande += ' '
        commande += self.account
        commande += '@'
        commande += self.ip
        commande += ':'
        commande += self.path
        commande += self.type
        commande += '/\"'
        commande += self.name
        commande += '\" '
        commande += self.destination
        
        self.logger.info(commande)

        os.system(commande)
