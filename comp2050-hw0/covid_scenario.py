""" File name:   covid_scenario.py
    Author: 
    Date:   
    Description: This file represents a scenario simulating the spread of 
                 covid19. It should be implemented for Part 1 of 
                 Exercise 4 of Assignment 0.

                 See the lab notes for a description of its contents.
"""
from typing import List


class COVID19Scenario:
    def __init__(self):
        """ YOUR CODE HERE. """

    def read_scenario_file(self, path_to_scenario_file: str) -> bool:
        """YOUR CODE HERE"""

    def valid_moves(self) -> List[str]:
        """ YOUR CODE HERE. """

    def move(self, loc):
        """ YOUR CODE HERE. """

    def spread_covid(self):
        """ YOUR CODE HERE. """

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