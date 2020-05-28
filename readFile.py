# coding: utf-8
import xlsxwriter
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
	f = open('Muestra_EB.CONTRACT.BALANCE', 'r')
	orderandValueList = []
	for line in f:
		if line!=None:
			print("******************************************+ line")
			stringTokenizadoCampos=line.strip().split('|')
			sizeList=len(stringTokenizadoCampos)
			if(sizeList > 0) :
				index =0


				for campos in stringTokenizadoCampos : 
					orderandValueList.append(File(index, campos))
					existeSubcampos = campos.find("]")
					if(existeSubcampos != -1) :
						stringTokenizadosubcampos=campos.strip().split(']')
						for subcampos in stringTokenizadosubcampos : 
							print "Subcampos %s" %subcampos
					#print "stringTokenizadoCampos %s" %stringTokenizadoCampos
					#print "valor %s" %campos
					#print "index %s" %index
					index= index+1
	
	#for orderandValue in orderandValueList :
		#print "order %s" %orderandValue.order
		#print "orderandValue %s" %orderandValue.value
	row = 0
	col = 0
	#Escribir en el archivo
	libro = xlsxwriter.Workbook('Presupuesto1.xlsx')
	#for category in categoryList
	hoja = libro.add_worksheet('Categoria1')

	for orderandValue1 in (orderandValueList):
		hoja.write(row, col,     orderandValue1.order)
   		hoja.write(row, col + 1, orderandValue1.value)
   		row += 1
   		print "value %s" %orderandValue1.value
   	
   	#Pintamos la fila de totales
   	hoja.write(row, 0, 'Total:')
   	hoja.write(row, 1, '=SUM(B1:B7)')

	#Cerramos el libro
	libro.close() 
		

metodo()
