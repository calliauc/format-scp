#!/usr/bin/env python3

import os
import argparse

import engine
import log


parser = argparse.ArgumentParser()
type_group = parser.add_mutually_exclusive_group()
type_group.add_argument(
    "-f", "--film", help="Récupère un film", action="store_true")
type_group.add_argument(
    "-s", "--serie", help="Récupère une série", action="store_true")

parser.add_argument(
     "-n", "--name", help="Le nom du fichier ou du répertoire à récupérer", type=str)
parser.add_argument(
    "-d", "--destination", help="Repertoire local de destination", type=str, default='.')
parser.add_argument(
    "-p", "--port", help="Port de la machine distante", type=str, default='22')

verbosity_group = parser.add_mutually_exclusive_group()
verbosity_group.add_argument(
    "-v", "--verbose", help="increase output verbosity", action="store_true")
verbosity_group.add_argument(
    "-vv", "--very-verbose", help="increase a lot output verbosity", action="store_true")


def main():
    args = parser.parse_args()
    logger = log.generate_logger(args)
    process = engine.Engine(args, logger)
    process.run()

main()

