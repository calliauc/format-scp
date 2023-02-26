import os

class Engine:
    def __init__(self, args, logger):
        self.logger = logger
        self.logger.debug(args)
        self.name = args.name
        self.command = 'scp -rP'
        self.port = args.port
        self.account = 'admin'
        self.ip = '192.168.0.63'
        self.path = '/share/CACHEDEV1_DATA/Data/'
        self.destination = args.destination
        if args.film == True :
            self.type = 'Films'
        elif args.serie == True :
            self.type = 'Series'
        else :
            logger.error('Il faut spécifier le type de contenu (--film ou --serie)')
            return 1
        




    def run(self):
        self.name = self.name.replace(' ', '\ ').replace('(', '\(').replace(')', '\)')

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
        commande += ' '
        print(commande) 

        os.system(commande)

