#!/usr/bin/python

import argparse


def Parser():
    the_parser = argparse.ArgumentParser()
    the_parser.add_argument(
        '--population', '-p', action="store", type=int,
        help="total size of the infectable population")
    the_parser.add_argument(
        '--infected', '-i', action="store", type=int,
        help="initial number of infected people")
    args = the_parser.parse_args()
    return args

class Individual:
    days = 0 # class-wide variable that propagates to class instances
    location_id = 0
    def __init__(self):
        self.living_days = 0
        self.infected_days = 0
        Individual.location_id += 1
        self.location = Individual.location_id
    


def agePopulation():
    Individual.days += 1
    return


def main(population, infected):
    population_list = [Individual() for i in range(population)]
    

if __name__ == "__main__":
    args = Parser()
    main(args.population, args.infected)
