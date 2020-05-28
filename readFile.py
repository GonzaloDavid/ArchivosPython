# coding: utf-8
import xlsxwriter
import threading
import numpy as np
class File:
    order = 0
    value = ''
    sizeList =0

    def __init__(self, n, s,size):
        self.order = n
        self.value = s
        self.sizeList=size
     
    def print_order(self):
        print self.order
         
    def print_value(self):
        print self.value

def metodo():
	  
	#ListadecategoriaIngresasPorUsuario
	#Invocar al metodo que va contruir andrea
	#parametros de entrada(ListadecategoriaIngresadasporelusuario)
	#parametrosdesalida 3 arreglos : Matriz de categorias, Matriz de campos por categorias, matriz de subcampos por categoria

	f = open('EB.CONTRACT.BALANCES20200430Aux.txt', 'r')
	orderandValueList = []
	subfields = []
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
					
					existeSubcampos = campos.find("]")
					if(existeSubcampos != -1) :
						stringTokenizadosubcampos=campos.strip().split(']')
						sizeSubfields=len(stringTokenizadosubcampos)
						for subcampos in stringTokenizadosubcampos :
							subfields.append(File(index, subcampos,sizeSubfields)) 
							#print "Subcampos %s" %subcampos
					else :
						orderandValueList.append(File(index, campos,0))
						#print "stringTokenizadoCampos %s" %campos
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
		#Filtramos los campos
		fieldsFiltered = filter(lambda field: field.order==x , orderandValueList)
		nameHeader= 'campo'+str(x)
   		fieldsFiltered = [File(x, nameHeader,0)] + fieldsFiltered

   		#Obtenemos el numero maximo de subcampos
		
		subfieldsFiltered=filter(lambda field: field.order==x , subfields)
		subfieldSizeList=[]
		for sizeSubfields in subfieldsFiltered :
			subfieldSizeList.append(sizeSubfields.sizeList)
		
		numSubfields= 0
		if(len(subfieldSizeList)>0):
				numSubfields=np.amax(subfieldSizeList)
		
		print "sizeSubfields %s" %numSubfields
		#Recorremos los campos por posicion
		row = 0
		for orderandValue1 in fieldsFiltered:
			#Poner cabeceras
   			if (x==16) :
				codeCategoryTokenizado= orderandValue1.value.strip().split('.')
				
				for code in codeCategoryTokenizado :
					
					if(len(codeCategoryTokenizado)>4):
						
						codeCategory=codeCategoryTokenizado[4]
						#print "codeCategory %s" %codeCategory
					else :
					#Alerta no tiene categoria
						print("NO TIENE CATEGORIA %s" %code)

			hoja.write(row, col, orderandValue1.value)
   			row += 1
   		row = 0
   		print "-------------------------------------> %s" 
   		
   		
   		for subfield in subfieldsFiltered : 
   			subfieldCount=0
   			print "subfield CAMPOS %s" %subfield.value
   			print "col %s" %col
   			print "row %s" %row
   			if (subfieldCount==0) :
   				row = 0
   				nameSubHeader= 'campo'+str(x)+'.'+str(col)
   				#hoja.write(row, col, nameSubHeader)	
   				#row += 1
   			#hoja.write(row, col, subfield.value)
   			#col += 1
   			
   			subfieldCount +=1

   		col += 1
   		
   	#Cerramos el libro
   	libro.close()
   	
   	#print "resultado de la suma %s" %dd
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
