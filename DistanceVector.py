#Patrick Sbrighi 0001071460
import random

#Classe che implementa i nodi della rete
class Nodo:

    #Metodo di inizializzazione a cui passo il nome del nodo
    def __init__(self, nome):
        self.nome = nome
        self.tabella = {nome: (0, nome)}  #Di default la distanza da se stessi è 0 e il next hop è se stessi
        self.vicini = {}  #Elenco dei vicini con le relative distanze

    #Aggiunta dei diretti vicini, passo il nome del vicino e la distanza da esso
    def aggiungiVicini(self, vicino, distanza):
        self.vicini[vicino.nome] = distanza
        self.tabella[vicino.nome] = (distanza, vicino.nome)

    #Aggiornamento della tabella di routing del nodo
    def aggiornaTabella(self):
        aggiornata = False
        for nome, distanza in self.vicini.items():
            vicini = nodi[nome]
            for destinazione, (vicinoDest, nextHop) in vicini.tabella.items():
                if destinazione == self.nome:
                    continue

                new_distance = distanza + vicinoDest
                if destinazione not in self.tabella or new_distance < self.tabella[destinazione][0]:
                    self.tabella[destinazione] = (new_distance, nome)
                    aggiornata = True
        return aggiornata

    #Stampo la tabella attuale del nodo
    def stampaTabella(self):
        print(f"Tabella di {self.nome}:")
        print("Destinazione\tDistanza\tNext Hop")
        for destinazione, (distanza, next_hop) in sorted(self.tabella.items()):
            print(f"{destinazione}\t\t{distanza}\t\t{next_hop}")
        print()


#Metodo per simulare il funzionamento del protocollo
def simulazione():
    i = 0
    while True:
        print(f"------------------------------------- Iterazione numero {i+1} -------------------------------------")
        for nodo in nodi.values():
            nodo.stampaTabella()

        aggiornamenti = [nodo.aggiornaTabella() for nodo in nodi.values()]
        if not any(aggiornamenti):
            break
        i += 1

#Definizione dei nodi
nodi = {
    'NodoA': Nodo('NodoA'),
    'NodoB': Nodo('NodoB'),
    'NodoC': Nodo('NodoC'),
    'NodoD': Nodo('NodoD'),
    'NodoE': Nodo('NodoE'),
    'NodoF': Nodo('NodoF'),
    'NodoG': Nodo('NodoG')
}

#Aggiungo dei vicini ad ogni nodo con le relative distanze
nodi['NodoA'].aggiungiVicini(nodi['NodoB'], random.randint(1,10))
nodi['NodoA'].aggiungiVicini(nodi['NodoC'], random.randint(1,10))
nodi['NodoA'].aggiungiVicini(nodi['NodoE'], random.randint(1,10))
nodi['NodoB'].aggiungiVicini(nodi['NodoA'], random.randint(1,10))
nodi['NodoB'].aggiungiVicini(nodi['NodoC'], random.randint(1,10))
nodi['NodoB'].aggiungiVicini(nodi['NodoD'], random.randint(1,10))
nodi['NodoB'].aggiungiVicini(nodi['NodoE'], random.randint(1,10))
nodi['NodoC'].aggiungiVicini(nodi['NodoA'], random.randint(1,10))
nodi['NodoC'].aggiungiVicini(nodi['NodoB'], random.randint(1,10))
nodi['NodoC'].aggiungiVicini(nodi['NodoD'], random.randint(1,10))
nodi['NodoC'].aggiungiVicini(nodi['NodoF'], random.randint(1,10))
nodi['NodoC'].aggiungiVicini(nodi['NodoE'], random.randint(1,10))
nodi['NodoD'].aggiungiVicini(nodi['NodoB'], random.randint(1,10))
nodi['NodoD'].aggiungiVicini(nodi['NodoC'], random.randint(1,10))
nodi['NodoD'].aggiungiVicini(nodi['NodoG'], random.randint(1,10))
nodi['NodoE'].aggiungiVicini(nodi['NodoC'], random.randint(1,10))
nodi['NodoE'].aggiungiVicini(nodi['NodoA'], random.randint(1,10))
nodi['NodoE'].aggiungiVicini(nodi['NodoD'], random.randint(1,10))
nodi['NodoF'].aggiungiVicini(nodi['NodoA'], random.randint(1,10))
nodi['NodoF'].aggiungiVicini(nodi['NodoD'], random.randint(1,10))
nodi['NodoF'].aggiungiVicini(nodi['NodoC'], random.randint(1,10))
nodi['NodoG'].aggiungiVicini(nodi['NodoD'], random.randint(1,10))
nodi['NodoG'].aggiungiVicini(nodi['NodoE'], random.randint(1,10))
nodi['NodoG'].aggiungiVicini(nodi['NodoA'], random.randint(1,10))

#Faccio partire la simulazione
simulazione()

#Stampo le tabelle che ho ottuneto alla fine
print("------------------------------------- Stampa Finale -------------------------------------")
for nodo in nodi.values():
    nodo.stampaTabella()
