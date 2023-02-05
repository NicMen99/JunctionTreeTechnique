# JunctionTreeTechnique
Esame AI: In questo esercizio si implementa, in un linguaggio di programmazione a scelta, la tecnica del junction tree per l’inferenza probabilistica nelle reti Bayesiane.
Per semplicità, l’esercizio si limita alla costruzione del junction tree come descritto in classe e spiegato in dettaglio nel capitolo 4 di (Jensen 1997). Si verifichi quindi 
la correttezza dell’implementazione sull’esempio
riportato in Figura 4.18, e su altri due DAG (la cui versione orientata non sia un albero) scelti
a piacere, uno di dimensione piccola (10 variabili) e uno di dimensione media (30 variabili).
Si mostri l’albero costruito dall’algoritmo e per le reti più piccole lo si confronti con quello
costruito dal programma Hugin Lite.

## Moduli implementati

### _DirGraph.py_

In questo modulo sono raccolte le classi e le funzioni per generare grafi diretti. Viene utilizzato per modellare la 
rete bayesiana di partenza con le variabili rappresentate dalla classe *Node*.
In questo modulo è anche contenuto il metodo *moralize()*, usato poi nel metodo *get_moral_graph()* per ottenere un 
grafo non diretto e moralizzato su cui procedere con l'elaborazione.

### _Graph.py_

In questo modulo sono raccolte le classi e le funzioni per generare e manipolare grafi non diretti. Viene utilizzato per
modellare il grafo su cui eseguire le operazioni di traingolazione e su cui vengono trovate le cricche massimali ai fini
di creare un Junction Graph.
Di nuovo, la classe *Node* è utilizzata per rappresentare le variabili che fungono da nodi del grafo. In questo modulo
sono contenuti due diversi metodi per triangolare il grafo, *elimination_game()* e *make_chordal()*, che operano in 
maniera differente ma con lo stesso risultato di ottenere un grafo triangolato, oltre a un metodo (*Bron_Kerbosch_no_pivot()*)
che implementa l'omonimo algoritmo usato per trovare le cricche massimali, necessarie per costruire il Junction Graph.
Il metodo *gey_junction_graph()*, infine, viene invocato per restituire un Junction Graph a partire da un grafo triangolato
su cui sono già state individuate le cricche.

### _JunctionGraph.py_

In questo modulo sono raccolte le classi e le funzioni per generare e lavorare su Junction Graphs. Viene utilizzato per
modellare il Junction Graph e il relativo Junction Tree della rete bayesiana di partenza. 
La classe *Node* viene utilizzata per rappresentare i cluster di variabili che caratterizzano il Junction Graph, può 
essere di due tipi diversi "Supernode" o "Separator", il primo viene utilizzato per rappresentare le varie cricche del
grafo precedentemente triangolato il secondo per rappresentare i separatori (che consistono nelle intersezioni tra nodi 
adiacenti).
Il metodo principale implementato in questo modulo è l'algoritmo di Kruskal (*kruskal()*), qui rielaborato per ottenere 
uno spanning tree con peso massimo piuttosto che con peso minimo, che viene chiamato in *get_maximal_weight_spanning_tree()*
per ottenere il Junction Tree finale.

## Main

Nel main, oltre ad essere presente la definizione di alcune funzioni per la visualizzazione grafica dei vari grafi 
(implementate con il supporto della libreria GraphViz), si può modificare lo script per la generazione di un Junction Tree.
Si parte creando un grafo diretto e aggiungendo ad esso i nodi e gli archi della rete bayesiana prescelta con i metodi
*add_node()* e *add_edge()*, successivamente si invoca il metodo per la moralizzazione *get_moral_graph()* e al grafo 
appena ottenuto il meotodo per la triangolazione scelto, *make_chordal()* o alternativamente *elimination_game()*.
Una volta triangolato il grafo, si applica l'algoritmo di Bron-Kerbosch per trovare le cricche massimali (*Bron_Kerbosch_no_pivot()*)
e il metodo *get_junction_graph()* per ottenere il relativo Junction Graph; giunti a questo punto si invoca il metodo
*get_maximal_weight_spanning_tree()* che fornisce il Junction Tree della rete bayesiana di partenza. Durante l'esecuzione
vengono prodotti vari file PDF per poter visualizzare i vari stadi del processo di trasformazione, grazie alle funzioni
considerate all'inizio di questo paragrafo.