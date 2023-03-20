""" File name:   covid_curing_agents.py
    Author:      Ta Viet Thang  
    Date:        March 18,, 2023
    Description: This file contains agents which manage and curing covid19 disease. 
                 It is used in Exercise 4 of Assignment 0.
"""

import random
from covid_scenario import COVID19Scenario
from collections import deque

class COVID19CuringAgent:
    """ A simple covid eradication agent. """

    def __init__(self, locations, conn):
        """ This contructor does nothing except save the locations and conn.
            Feel free to overwrite it when you extend this class if you want
            to do some initial computation.

            (COVID19CuringAgent, [str], { str : set([str]) }) -> None
        """
        self.locations = locations
        self.conn = conn

    def choose_move(self, location, valid_moves, covid, threshold, growth, spread):
        """ Using given information, return a valid move from valid_moves.
            Returning an invalid move will cause the system to stop.

            Changing any of the mutable parameters will have no effect on the operation
            of the system.

            This agent will locally move to the highest covid patients population, if there is
            is no nearby covid, it will act randomly. 

            (COVID19CuringAgent, str, [str], [str], { str : float }, float, float, float) -> str
        """
        max_covid = None
        max_move = None
        for move in valid_moves:
            if max_covid is None or covid[move] > max_covid:
                max_covid = covid[move]
                max_move = move

        if not max_covid:
            return random.choice(valid_moves)

        return max_move


# Make a new agent here called SmartCOVID19CuringAgent, which extends COVID19CuringAgent and
# acts a bit more sensibly. Feel free to add other helper functions if needed.

class SmartCOVID19CuringAgent(COVID19CuringAgent):
    def __init__(self, locations, conn):
        """ This contructor does nothing except save the locations, conn and initialize solution.
            (SmartCOVID19CuringAgent, [str], { str : set([str]) }) -> None
        """
        self.locations = locations
        self.conn = conn
        self.solution = []

    
    def choose_move(self, location, valid_moves, covid, threshold, growth, spread):
        """My strategy is simple and straightforward: choose the nearest location that has covid
        and go there"""
        max_covid = None
        max_move = None
        for move in valid_moves:
            if max_covid is None or covid[move] > max_covid:
                max_covid = covid[move]
                max_move = move

        if not max_covid:
            covid_locations = []
            for key, value in covid.items():
                if value > 0:
                    covid_locations.append(key)
            nearest_covid = self.path_to_nearest_covid(location, covid_locations)[1]
            max_move = nearest_covid
        
        return max_move
    
    def path_to_nearest_covid(self, start, covid_locations):
        """a variant of BFS"""
        queue = deque()
        visited = set()
        path = {start: [start]}
        
        queue.append((start, 0))
        visited.add(start)
        
        while queue:
            node, distance = queue.popleft()
            if node in covid_locations:
                return path[node]
            for neighbor in self.conn[node]:
                if neighbor not in visited:
                    queue.append((neighbor, distance+1))
                    visited.add(neighbor)
                    path[neighbor] = path[node] + [neighbor]
        
        return []        


