import xlrd


class Parametrizacion:

	def __init__(self,arrayListCategories):
		self.param=self.cargarParametrizacion(arrayListCategories)

	def cargarParametrizacion(self, arrayListCategorias):
	#	arrayListCategorias=['1001','6001']
		arrayCategorias=[]
		arrayCampos=[]
		arraySubCampos=[]
		#Abrimos el fichero excel
		documento = xlrd.open_workbook("parametrizaion.xlsx")
			#Podemos guardar cada una de las hojas por separado
		categorias = documento.sheet_by_index(0)
		campos = documento.sheet_by_index(1)
		subcampos = documento.sheet_by_index(2)

		#Numero de Filas
		filas_categorias = categorias.nrows
		col_categorias = categorias.ncols

		filas_campos = campos.nrows
		col_campos = campos.ncols

		filas_subCampos = subcampos.nrows
		col_subCampos=subcampos.ncols

		#### Matriz de Categorias
		i=-1
		for x in xrange(filas_categorias):
			y=x+1
			if y < filas_categorias:
				if categorias.cell_value(y,0) in arrayListCategorias: 
					i=i+1;
					arrayCategorias.append([])
					for j in xrange(col_categorias):
						arrayCategorias[i].append(categorias.cell_value(y,j))
					
						

		#print (arrayCategorias[0][2])
		
		print("*******************************************")
		##### Matriz de Campos
		i=-1
		for x in xrange(filas_campos):
			y=x+1
			if y < filas_campos:
				
				if campos.cell_value(y,0) in arrayListCategorias: 
					i=i+1;
					arrayCampos.append([])
					for j in xrange(col_campos):
						arrayCampos[i].append(campos.cell_value(y,j))
					
		#print (arrayCategorias[0][2])
		
		

		##### Matriz de SubCampos
		i=-1
		for x in xrange(filas_subCampos):
			y=x+1
			if y < filas_subCampos:
				
				if subcampos.cell_value(y,0) in arrayListCategorias: 
					i=i+1;
					arraySubCampos.append([])
					for j in xrange(col_subCampos):
						arraySubCampos[i].append(subcampos.cell_value(y,j))

		print("*******************************************Categorias")
		print (arrayCategorias)
		return (arrayCategorias,arrayCampos,arraySubCampos)
		
