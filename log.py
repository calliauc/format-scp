import logging

def generate_logger(args):
    logger = logging.getLogger('Journal_exemple')
    logger.setLevel(logging.DEBUG)

    fl = logging.FileHandler('recup.log')
    fl.setLevel(logging.DEBUG)
    fileFormatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fl.setFormatter(fileFormatter)
    logger.addHandler(fl)

    cl = logging.StreamHandler()
    if args.verbose == True:
        cl.setLevel(logging.INFO)
    elif args.very_verbose == True:
        cl.setLevel(logging.DEBUG)
    else:
        cl.setLevel(logging.WARNING)
    consoleFormatter = logging.Formatter('%(levelname)s - %(message)s')
    cl.setFormatter(consoleFormatter)
    logger.addHandler(cl)

    return logger