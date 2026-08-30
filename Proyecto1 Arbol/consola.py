class Prioridad:
    def __init__(self):
        self.prioridad=-1
        self.operador= False

      #/////////////////////////////////////////////////////////// acabar
    '''  @property
        def gett
       '''
    def _prioridad(self,caracter: chr):
        if(caracter=='*' or caracter=='/'):
            self.prioridad=1
            self.operador=True

        if(caracter=='+'or caracter=='-'):
            self.prioridad=2
            self.operador= True

        if(caracter>='0'and caracter<='9'):
            self.prioridad=3
            self.operador=False
      


class Nodo:
    def __init__(self,dato: int):
        self.dato= dato
        self.izquierda= None
        self.derecha= None



class ArbolBinario:

    def __init__(self,dato):
        self.raiz=Nodo(dato)

    def insertar(self,valor):
        self.raiz=self._insertar_recursivo(self.raiz,valor)

    def _insertar_recursivo(self,nodo,valor):
        if not nodo:
            return nodo(valor)
        if valor<nodo.dato:
            nodo.izquierda= self._insertar_recursivo(nodo.izquierda,valor)
        else:
            if valor>nodo.dato:
                nodo.derecha=self._insertar_recursivo(nodo.derecha,valor)

    
            
def EsValido(cadena):
    b = True
    n = len(cadena)
    i = 0

    while i < n and b == True:
        if(cadena[i] == '*' or cadena[i] == '+' or cadena[i] == '/'
           or cadena[i] == '+' or cadena[i] == '-' or cadena[i] >= '0'
           and cadena[i] <= '9'):
            b = True
        else:
            b = False
        i = i + 1
    return b


operacion = input("Introduzca la operacion: ")

if(not EsValido(operacion)):
    print("Introduzca las operaciones sin espacios ni caracteres raros!")