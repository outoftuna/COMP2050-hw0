""" File name:   covid_scenario.py
    Author:      Ta Viet Thang
    Date:        March 18, 2023
    Description: This file represents a scenario simulating the spread of 
                 covid19. It should be implemented for Part 1 of 
                 Exercise 4 of Assignment 0.

                 See the lab notes for a description of its contents.
"""
from typing import List


class COVID19Scenario:
    def __init__(self):
        self.threshold = float(0)
        self.growth = float(0)
        self.spread = float(0)

        self.location = ''
        self.locations = []
        self.covid = dict()
        self.conn = dict()

    def read_scenario_file(self, path_to_scenario_file: str) -> bool:
        try: 
            with open(path_to_scenario_file) as file:
                for line in file:
                    if line.startswith('threshold'):
                        self.threshold = line.split()[1]
                    elif line.startswith('growth'):
                        self.growth = line.split()[1]
                    elif line.startswith('spread'):
                        self.spread = line.split()[1]
                    elif line.startswith('start'):
                        self.location = line.split()[1]
                    elif line.startswith('covid'):
                        self.covid[line.split()[1]] = float(line.split()[2])
                    elif line.startswith('location'):
                        self.locations.append(line.split()[1])
                    elif line.startswith('conn'):
                        loc1 = line.split()[1]
                        loc2 = line.split()[2]
                        if loc1 not in self.conn:
                            self.conn[loc1] = {loc2}
                        else: 
                            self.conn[loc1].add(loc2)
                        if loc2 not in self.conn:
                            self.conn[loc2] = {loc1}
                        else: 
                            self.conn[loc2].add(loc1)
                for loc in self.locations:
                    if loc not in self.covid.keys():
                        self.covid[loc] = float(0)
        except IOError:
            return False
        else: 
            return True
            

    def valid_moves(self) -> List[str]:
        moves = list(self.conn[self.location])
        moves.append(self.location)
        return moves

    def move(self, loc):
        if loc in self.conn[self.location]:
            self.location = loc
            self.covid[loc] = float(0)
        else: 
            raise ValueError

    def spread_covid(self):
        more_covid = self.covid.copy()
        for loc in self.loactions.keys():
            if self.location != loc:
                d = self.covid[loc]
                d *= 1 + self.growth
                for neighbour in self.conn[loc]:
                    if self.covid[neighbour] >= self.threshold:
                        d += self.covid[neighbour] * self.spread
                more_covid[loc] = d
            else: 
                more_covid[loc] = float(0)
        self.covid = more_covid





    def current_covid(self):
        """ Get the current total hawkseed in the scenario """
        return sum(self.covid.values())

    def check_free_location(self, loc):
        """ 
        Check if `loc` is a free location.
        A location is a free location when its neighbors don't have any hawkseed
        """
        conn = self.conn[loc]
        check = 0
        for location in conn:
            if self.covid[location] < 0.001:
                check += 1
        return check == len(conn)