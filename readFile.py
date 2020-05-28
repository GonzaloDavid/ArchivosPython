# coding: utf-8
import xlsxwriter
import threading
import numpy as np
class File:
    order = 0
    value = ''

    def __init__(self, n, s):
        self.order = n
        self.value = s
     
    def print_order(self):
        print self.order
         
    def print_value(self):
        print self.value

def metodo():
	  
	#ListadecategoriaIngresasPorUsuario
	#Invocar al metodo que va contruir andrea
	#parametros de entrada(ListadecategoriaIngresadasporelusuario)
	#parametrosdesalida 3 arreglos : Matriz de categorias, Matriz de campos por categorias, matriz de subcampos por categoria

	f = open('EB.CONTRACT.BALANCES20200430Aux.text', 'r')
	orderandValueList = []
	fieldSizeList=[]

	for line in f:
		if line!=None:
			#print("******************************************+ line")
			stringTokenizadoCampos=line.strip().split('|')
			sizeList=len(stringTokenizadoCampos)
			if(sizeList > 0) :
				index =0
				#Tamaño del arreglo de campos
				fieldSizeNumber=len(stringTokenizadoCampos)
				fieldSizeList.append(fieldSizeNumber)
				
				for campos in stringTokenizadoCampos : 
					orderandValueList.append(File(index, campos))
					existeSubcampos = campos.find("]")
					if(existeSubcampos != -1) :
						stringTokenizadosubcampos=campos.strip().split(']')
						for subcampos in stringTokenizadosubcampos : 
							varoo=0
							#print "Subcampos %s" %subcampos
					#print "stringTokenizadoCampos %s" %stringTokenizadoCampos
					index= index+1
	
	#Escribir en el archivo
	libro = xlsxwriter.Workbook('Presupuesto1.xlsx')
	#for category in categoryList
	hoja = libro.add_worksheet('Categoria1')
	tamanio = len(orderandValueList);
	
	#Obtenemos el numero de campos o columnas en archivo
	numFields=np.amax(fieldSizeList)
	print "tamanio %s" %numFields
	col = 1
	row = 0
	for x in range(numFields) :
		
		fieldsFiltered = filter(lambda field: field.order==x , orderandValueList)
		
		#Recorremos los campos por posicion
		row = 0
		for orderandValue1 in fieldsFiltered:
   			hoja.write(row, col, orderandValue1.value)
   			row += 1
   		col += 1
   	#Cerramos el libro
   	libro.close()
   	dd=suma()
   		#Pintamos la fila de totales
   		#hoja.write(row, 0, 'Total:')
	 	#hoja.write(row, 1, '=SUM(B1:B7)')
#NUM_HILOS = 3
#for num_hilo in range(NUM_HILOS):
 #   hilo = threading.Thread(name='hilo%s' %num_hilo, 
  #                          target=metodo)    
   # hilo.start()

metodo()
def suma() :
	return 2
