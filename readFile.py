# coding: utf-8
#import Parametrizacion
import xlsxwriter
import threading
import numpy as np
import main

class File:
    order = 0
    value = ''
    sizeList =0
    rowNumber = 0
    key =''

    def __init__(self, n, s,size,rowNumber,key):
        self.order = n
        self.value = s
        self.sizeList=size
        self.rowNumber=rowNumber
        self.key=key

     
    def print_order(self):
        print self.order
         
    def print_value(self):
        print self.value

def metodo():
	  
	#ListadecategoriaIngresasPorUsuario
	#Invocar al metodo que va contruir andrea
	#parametros de entrada(ListadecategoriaIngresadasporelusuario)
	#parametrosdesalida 3 arreglos : Matriz de categorias, Matriz de campos por categorias, matriz de subcampos por categoria
	#metodo()
	#parametrizacion = Parametrizacion()
	#print "parametrizacion %s" %parametrizacion
	#arrayListCategoriasCliente=['1001','6001']
	resultParam=main.Parametrizacion(['1001','6001']).param

	#print "resultParam %s" %str(resultParam)

	categoryListParam=resultParam[0]
	fieldsListParam=resultParam[1]
	subfieldListParam=resultParam[2]
	
	orderandValueList = []
	subfields = []
	fieldSizeList=[]
	countLine=0
	positionCategoryFields=0
	positionCategorySubFields=0
	subcamposLabel={}
	subcamposValues={}

	if(len(categoryListParam)>0):
		positionCategoryFields=categoryListParam[0][1]
		positionCategorySubFields=categoryListParam[0][2]

	#print "positionCategoryFields %s" %positionCategoryFields

	f = open('EB.CONTRACT.BALANCES20200430Aux.txt', 'r')
	for line in f:
		if line!=None:
			
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
							#Llenamos los subcampos

							subfields.append(File(index, subcampos,sizeSubfields,countLine+1,'')) 
							
							#print "Subcampos %s" %subcampos
					else :

						orderandValueList.append(File(index, campos,0,0,''))
						
					index= index+1
		countLine= countLine+1
	
	#Escribir en el archivo
	libro = xlsxwriter.Workbook('LecturaArchivos.xlsx')
	#Construye una pestaña por cada categoria
	#Maximo va a leer hasta 5 pestañas
	countCategory=0
	for category in categoryListParam :
		#print "countCategory %s" %countCategory
		#print "category %s" %category[0]
		codecategoryCurrency=category[0]
		hoja = libro.add_worksheet(category[3])
		if(countCategory==0) :
			print "category 0%s"
			#hoja = libro.add_worksheet(category[3])
			#d=LeerArchivo()
			#print "suma %s" %d

		if(countCategory==1) :
			print "category 1---------------------------------------------------%s" 

		if(countCategory==2) :
			print "category 2%s" 

		if(countCategory==3) :
			print "category 2%s" 

		tamanio = len(orderandValueList);

		#Obtenemos el numero de campos o columnas en archivo
		numFields=np.amax(fieldSizeList)
		print "tamanio %s" %numFields

		col = 0
		row = 0

		#for fieldParam in fieldsListParam : 
	
		for columnNumber in range(numFields) :
			#Buscar nombre de cabecera
			#print "columnNumber %s" %columnNumber
			headerNameFilterbyCategory= filter(lambda field:  field[0]==category[0]  , fieldsListParam)
			headerNameFilter= filter(lambda field:  int(field[1])==columnNumber+1  , headerNameFilterbyCategory)
			nameColumn=''
			
			#Obtenemos el numero maximo de subcampos
			subfieldsFiltered=filter(lambda field: field.order==columnNumber, subfields)

			subcamposLabel=set()
			keyandValueList=[]
			if(len(headerNameFilter)>0):
				print "headerNameFilter %s" %headerNameFilter
				isMultiValue=headerNameFilter[0][3]
				if(isMultiValue=='N') :
					nameColumn=headerNameFilter[0][2]
				else : 
					#ES UN MULTI VALOR
					isLabel=headerNameFilter[0][4]
					if(isLabel=='S') :
						#Es un etiqueta
						#print "es etiqueta"
						
						for label in subfieldsFiltered :
							print "label %s" %str(label.value)
							subcamposLabel.add(label)
					else :
						print "es valor"
						#Es un valor

					


			#print "nameColumn %s" %nameColumn
			
			#print "fieldsListParam %s" %str(headerNameFilter)
			#Filtramos los campos

			fieldsFiltered = filter(lambda field: field.order==columnNumber , orderandValueList)
			nameHeader= nameColumn
   			fieldsFiltered = [File(columnNumber, nameHeader,0,0,'')] + fieldsFiltered

   			
			subfieldSizeList=[]
			for sizeSubfields in subfieldsFiltered :
			
				subfieldSizeList.append(sizeSubfields.sizeList)
		
				numSubfields= 0
			if(len(subfieldSizeList)>0):
				numSubfields=np.amax(subfieldSizeList)
			#-------------------------------LLENA CAMPOS---------------------
			#Recorremos los campos por posicion
			row = 0
			for orderandValue1 in fieldsFiltered:
				#Poner cabeceras
	   			if (columnNumber==positionCategoryFields) :
					codeCategoryTokenizado = orderandValue1.value.strip().split('.')
					
					for code in codeCategoryTokenizado :
					
						if(len(codeCategoryTokenizado)>positionCategorySubFields):
						
							codeCategory=codeCategoryTokenizado[positionCategorySubFields]
							#print "codeCategory %s" %codeCategory
						else :
						#Alerta no tiene categoria
							print("NO TIENE CATEGORIA %s" %code)

				hoja.write(row, col, orderandValue1.value)
   				row += 1
   			
   			#--------------------------------------------------------------------
   			col += 1
   			row = 0

   			for idx,subfield in enumerate(subfieldsFiltered) : 
   				subfieldCount=0
   			
   				#print "rows ss %s" %idx
				#print "rows de filter %s" %subfield.value
   				if (subfieldCount==0) :
   					#row = 0
   					#nameSubHeader= 'campo'+str(columnNumber)+'.'+str(col)
   					#hoja.write(row, col, nameSubHeader)	
   					#row += 1
   				if(subfield.rowNumber != subfieldsFiltered[idx-1].rowNumber) :
	   				print "rows ss %s" %idx
   					#row += 1

	   			#hoja.write(row, col, subfield.value)
   				#col += 1
   			
   				subfieldCount +=1

   		row += 1
   			
   		countCategory +=1;
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


def getFieldsParam() :
				
	return 2

metodo()