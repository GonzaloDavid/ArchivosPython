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
	  
	# --------------------------------------------------------------------------------
	#Obtener datos de parametrizacion
	resultParam=main.Parametrizacion(['1001','6001']).param
	categoryListParam=resultParam[0]
	fieldsListParam=resultParam[1]
	subfieldListParam=resultParam[2]
	# --------------------------------------------------------------------------------
	#Variables
	orderandValueList = []
	subfields = []
	fieldSizeList=[]
	countLine=0
	positionCategoryFields=0
	positionCategorySubFields=0
	subcamposLabel={}
	subcamposValues={}
	# --------------------------------------------------------------------------------

	if(len(categoryListParam)>0):
		positionCategoryFields=categoryListParam[0][1]
		positionCategorySubFields=categoryListParam[0][2]

	# --------------------------------------------------------------------------------
	#Leer de archivo
	getListBuffer=getFieldsParam('EB.CONTRACT.BALANCES20200430Aux.txt')
	orderandValueList=getListBuffer[0]
	subfields=getListBuffer[1]
	fieldSizeList=getListBuffer[2]
	# --------------------------------------------------------------------------------
	#Escribir en el archivo
	
	countCategory=0
	for category in categoryListParam :
		#print "countCategory %s" %countCategory
		#print "category %s" %category[0]
		nameFile= 'LecturaArchivos'+category[3]+'.xlsx'
		libro = xlsxwriter.Workbook(nameFile)
		codecategoryCurrency=category[0]
		hoja = libro.add_worksheet(category[3])

		tamanio = len(orderandValueList);

		#Obtenemos el numero de campos o columnas en archivo
		numFields=np.amax(fieldSizeList)
		print "tamanio %s" %numFields

		col = 0
		row = 0

		#for fieldParam in fieldsListParam : 
		#Solo para los subItems


	
		for columnNumber in range(numFields) :
			#Buscar nombre de cabecera
			#print "columnNumber %s" %columnNumber
			keyandValueList=[]
			headerNameFilterbyCategory= filter(lambda field:  field[0]==category[0]  , fieldsListParam)
			
			headerNameFilter= filter(lambda field:  int(field[1])==columnNumber+1  , headerNameFilterbyCategory)
			nameColumn=''
			
			#Obtenemos el numero maximo de subcampos
			subfieldsFiltered=filter(lambda field: field.order==columnNumber, subfields)

			#subcamposLabel=set()
			
			if(len(headerNameFilter)>0):
				#print "headerNameFilter %s" %headerNameFilter				
				isMultiValue=headerNameFilter[0][3]
				if(isMultiValue=='N') :
					nameColumn=headerNameFilter[0][2]
				else : 
					#ES UN MULTI VALOR
					isLabel=headerNameFilter[0][4]
					#ES un valor
					if(isLabel=='N') :
						
						#Referencia a la etiqueta
						print "COLUMNA--++++++++++++++++-----------------------------------------------> %s" %columnNumber
						referenceValues=headerNameFilter[0][5]
						print "references--++++++++++++++++-----------------------------------------------> %s" %referenceValues
						if(referenceValues!=None and referenceValues!=''):

							print "referenceValues %s" %referenceValues
							referenceAux=int(referenceValues)-1
							columnLabel= filter(lambda field: str(field.order)==str(referenceAux) , subfields)
							#print "len columnLabel------> %s" %len(subfieldsFiltered)
							
							
							if(len(columnLabel)>0):

								for index,value in enumerate(subfieldsFiltered) :
									#print "Rownumber %s" %str(value.rowNumber)
									#print "numberrrrrrrr %s" %str(index)
									test=columnLabel[index]
									#print "test %s" %str(test.value)
									keyandValueList.append(File(columnNumber, value.value,0,0,test.value)) 


						else : 
							print "Es un valor sin referencia a label %s"



					

			#print "keyandValueList %s" %str(keyandValueList)
			#print "fieldsListParam %s" %str(headerNameFilter)
			#Filtramos los campos

			fieldsFiltered = filter(lambda field: field.order==columnNumber , orderandValueList)
			nameHeader= nameColumn
   			fieldsFiltered = [File(columnNumber, nameHeader,0,0,'')] + fieldsFiltered

   			
			subfieldSizeList=[]
			#for sizeSubfields in subfieldsFiltered :
			
			#	subfieldSizeList.append(sizeSubfields.sizeList)
		
			#	numSubfields= 0
			#if(len(subfieldSizeList)>0):
			#	numSubfields=np.amax(subfieldSizeList)
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
   			
   			
   			keyandValueListAux=keyandValueList
   			keyandValueListAux.append(File(4, 1222,0,0,'label de prueba')) 
   			keyandValueListAux.append(File(4, 1222,0,0,'label de prueba')) 
   			keyandValueListAux.append(File(4, 1222,0,0,'label de prueba')) 
   			keyandValueListAux.append(File(4, 1222,0,0,'label de prueba')) 
   			keyandValueListAux.append(File(4, 1222,0,0,'label de prueba')) 
   			keyandValueListAux.append(File(4, 1222,0,0,'label de prueba')) 
   			keyandValueListAux.append(File(4, 1222,0,0,'label de prueba')) 
   			keyandValueListAux.append(File(4, 1222,0,0,'label de prueba')) 
   			keyandValueListAux.append(File(4, 1222,0,0,'label de prueba')) 
   			keyandValueListAux.append(File(4, 1222,0,0,'label de prueba')) 
   			keyandValueListAux.append(File(4, 1222,0,0,'label de prueba')) 
   			keyandValueListAux.append(File(4, 1222,0,0,'label de prueba')) 

   			keyandValueListAux = [File(4, 'hola',0,0,'label')] + keyandValueListAux
   			
			#for i in keyandValueList :
   				#print "key %s" %i.key
   				#print "value %s" %i.value
   			listadeparametrosSubcampos = filter(lambda field: field[0]==category[0] and str(col)==field[1], subfieldListParam)

   			for listasubcamposFiltrada in listadeparametrosSubcampos : 
   				print "i???????????????????????????????????????????????????????????? %s" %len(keyandValueListAux)
   				print "tamaño de lista a imprimir %s" %len(listadeparametrosSubcampos)
   				subcamposKeyValueFinal = []
   				#filter(lambda field: str(field.key)==str(listasubcamposFiltrada[2]), keyandValueList)
   				
   				#subcamposKeyValueFinal
   				row=0
   				for orderandValueSub in keyandValueListAux:
   					print "GRAVO %s" %listadeparametrosSubcampos[0]
   					hoja.write(row, col-1, orderandValueSub.value)
   					row += 1


   			#print "listadeparametrosSubcampos %s" %listadeparametrosSubcampos
   			#listadeparametrosSubcampos=[]
   			#for t in subfieldListParam :
   				#print "-----------------------------------> %s" %str(t)
   			#	if(t[0]==category[0] and t[1]==str(col)) :
   			#		listadeparametrosSubcampos= t
   			#		print "testing %s" %str(listadeparametrosSubcampos)
   				
   			
   			

   			
   			row = 0

   			for idx,subfield in enumerate(subfieldsFiltered) : 
   				subfieldCount=0
   			
   				#print "rows ss %s" %idx
				#print "rows de filter %s" %subfield.value
   				if (subfieldCount==0) :
   					#row = 0
   					nameSubHeader= 'campo'+str(columnNumber)+'.'+str(col)
   					#hoja.write(row, col, nameSubHeader)	
   					#row += 1
   				#if(subfield.rowNumber != subfieldsFiltered[idx-1].rowNumber) :
	   				#print "rows ss %s" %idx
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


def getFieldsParam(ruta) :
	#Variables
	orderandValueList=[]
	subfields=[]
	fieldSizeList=[]
	f = open(ruta, 'r')
	countLine=0
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
	return (orderandValueList,subfields,fieldSizeList)

metodo()