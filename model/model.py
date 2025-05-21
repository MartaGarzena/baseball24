import itertools

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._allTeams = []

    def getYears(self):
        return DAO.getAllYears()

    def getTeamsOfYear(self, year):
        self._allTeams = DAO.getTeamsFromYear(year)
        return self._allTeams

    def buildGraph(self):
        self._grafo.clear()
        if len(self._allTeams) == 0:
            print("No teams yet")
            return
        self._grafo.add_nodes_from(self._allTeams)

        #serve un arco tra qualsiasi nodo
        myEdges = list(itertools.combinations(self._allTeams, 2))
        #lista di tuple con nodo partenza e di arrivo
        self._grafo.add_edges_from(myEdges)


    def printGraph(self):
        print(f"Grafo creato con {len(self._grafo.nodes)} nodi e {len(self._grafo.edges)} archi")
