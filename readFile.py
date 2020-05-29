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

def Readprocess():
	  
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
	
	countCategory=0
	for category in categoryListParam :
		# --------------------------------------------------------------------------------
		nameFile= 'LecturaArchivos'+category[3]+'.xlsx'
		libro = xlsxwriter.Workbook(nameFile)
		codecategoryCurrency=category[0]
		hoja = libro.add_worksheet(category[3])
		tamanio = len(orderandValueList);

		# --------------------------------------------------------------------------------
		#Obtenemos el numero de campos o columnas en archivo
		numFields=np.amax(fieldSizeList)
		print "tamanio %s" %numFields

		col = 0
		row = 0
		# --------------------------------------------------------------------------------
		for columnNumber in range(numFields) :
			
			keyandValueList=[]
			nameColumn=''
			headerNameFilter=filterFieldParambyCategory(fieldsListParam,category,columnNumber)
			#Obtenemos el numero maximo de subcampos
			subfieldsFiltered=filter(lambda field: field.order==columnNumber, subfields)
			
			if(len(headerNameFilter)>0):
				#print "headerNameFilter %s" %headerNameFilter				
				isMultiValue=headerNameFilter[0][3]
				if(isMultiValue=='N') :
					nameColumn=headerNameFilter[0][2]
				else : 
					#Es una variable multivalor
					isLabel=headerNameFilter[0][4]
					#ES un valor
					if(isLabel=='N') :
						keyandValueList= buildKeyAndValue(columnNumber,headerNameFilter,subfields,subfieldsFiltered)

			# --------------------------------------------------------------------------------

			fieldsFiltered = filter(lambda field: field.order==columnNumber , orderandValueList)
			nameHeader= nameColumn
   			fieldsFiltered = [File(columnNumber, nameHeader,0,0,'')] + fieldsFiltered

			subfieldSizeList=[]
			# --------------------------------------------------------------------------------
			#Guardar en archivo los campos 
			row = 0
			for orderandValue1 in fieldsFiltered:
				codeCategory=getCategorybyLine(columnNumber,positionCategoryFields,orderandValue1,positionCategorySubFields)
				hoja.write(row, col, orderandValue1.value)
   				row += 1
   			col += 1
   			#--------------------------------------------------------------------
   			#Guaradar los Subcampos o compos Multivalor
   			keyandValueListAux=keyandValueList
			#for i in keyandValueList :
   				#print "key %s" %i.key
   				#print "value %s" %i.value
   			listadeparametrosSubcampos = filter(lambda field: field[0]==category[0] and str(col)==field[1], subfieldListParam)

   			for listasubcamposFiltrada in listadeparametrosSubcampos : 
   				print "i???????????????????????????????????????????????????????????? %s" %len(keyandValueListAux)
   				print "tamaño de lista a imprimir %s" %len(listadeparametrosSubcampos)
   				subcamposKeyValueFinal = filter(lambda field: str(field.key)==str(listasubcamposFiltrada[2]), keyandValueList)
   				row=0
   				for orderandValueSub in subcamposKeyValueFinal:
   					print "GRAVO %s" %listadeparametrosSubcampos[0]
   					hoja.write(row, col-1, orderandValueSub.value)
   					row += 1
   			#--------------------------------------------------------------------

   		row += 1
   		countCategory +=1;
   		libro.close()
   

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

def filterFieldParambyCategory(fieldsListParam,category ,columnNumber):
	headerNameFilterbyCategory= filter(lambda field:  field[0]==category[0]  , fieldsListParam)
	headerNameFilter= filter(lambda field:  int(field[1])==columnNumber+1  , headerNameFilterbyCategory)
	return  headerNameFilter

def buildKeyAndValue(columnNumber,headerNameFilter,subfields,subfieldsFiltered):
	#Construir clave y valor
	keyandValueList=[]
	print "COLUMNA--++++++++++++++++-----------------------------------------------> %s" %columnNumber
	referenceValues=headerNameFilter[0][5]
	print "references--++++++++++++++++-----------------------------------------------> %s" %referenceValues
	if(referenceValues!=None and referenceValues!=''):
		print "referenceValues %s" %referenceValues
		referenceAux=int(referenceValues)-1
		columnLabel= filter(lambda field: str(field.order)==str(referenceAux) , subfields)							
		if(len(columnLabel)>0):
			for index,value in enumerate(subfieldsFiltered) :
				label=columnLabel[index]
				keyandValueList.append(File(columnNumber, value.value,0,0,label.value)) 

	else : 
		print "Es un valor sin referencia a label %s"
	return  headerNameFilter

def getCategorybyLine(columnNumber,positionCategoryFields,orderandValue1,positionCategorySubFields):
	#Poner cabeceras
	codeCategory=''
	if (columnNumber==positionCategoryFields) :
		codeCategoryTokenizado = orderandValue1.value.strip().split('.')
		for code in codeCategoryTokenizado :
			if(len(codeCategoryTokenizado)>positionCategorySubFields):
				codeCategory=codeCategoryTokenizado[positionCategorySubFields]
			else :
				print("NO TIENE CATEGORIA %s" %code)
	return  codeCategory



Readprocess()