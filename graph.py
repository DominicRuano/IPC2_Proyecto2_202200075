import graphviz

class Graph():
    def __init__(self, fondo = "white", fuente = "black", forma = "circle"):
        self.dot = graphviz.Digraph('structs', filename='Reporte.png', node_attr={'shape': forma, 'style': 'filled', 'fillcolor': fondo, 'fontcolor': fuente, 'fontname': 'Helvetica'})

    def addEncabezado(self, dato1, contador):
        self.dot.node(str(contador), str(dato1))

    def add1Nodo(self, dato1, contador1, contador2):
        self.dot.node(str(contador2),str(dato1))
        self.dot.edge(str(contador1), str(contador2))

    def add2Nodos(self, dato1,dato2, contador):
        self.dot.node(str(contador),str(dato1))
        self.dot.node(str(contador + 1),str(dato2))
        self.dot.edge(str(contador), str(contador + 1))

    def graficar(self):
        self.dot.render(outfile="Sistemas.png")