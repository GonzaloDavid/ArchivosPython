
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
				#print "headerNameFilter %s" %headerNameFilter
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
							#print "label %s" %str(label.value)
							subcamposLabel.add(label)
					else :
						#Es un valor
						for value in subfieldsFiltered :
							print "value %s" %str(label.value)
							keyandValueList.append(File(columnNumber, label.value,0,0,'')) 
						
			print "keyandValueList %s" %str(keyandValueList)


			#ListadecategoriaIngresasPorUsuario
	#Invocar al metodo que va contruir andrea
	#parametros de entrada(ListadecategoriaIngresadasporelusuario)
	#parametrosdesalida 3 arreglos : Matriz de categorias, Matriz de campos por categorias, matriz de subcampos por categoria
	#metodo()
	#parametrizacion = Parametrizacion()
	#print "parametrizacion %s" %parametrizacion
	#arrayListCategoriasCliente=['1001','6001']
	#Llamar a a parametrizacion


	   	#print "resultado de la suma %s" %dd
   		#Pintamos la fila de totales
   		#hoja.write(row, 0, 'Total:')
	 	#hoja.write(row, 1, '=SUM(B1:B7)')
#NUM_HILOS = 3
#for num_hilo in range(NUM_HILOS):
#   hilo = threading.Thread(name='hilo%s' %num_hilo, 
#                          target=metodo)    
# hilo.start()



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