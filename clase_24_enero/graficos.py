import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv("urbania_data.csv")
df.head(3)


# df.info()


# df.describe()


# df["'Terma'"].unique()


# df#.columns



# df.columns = df.columns.str.replace("'", "")
# df.columns




# df_cut_obj = df[['Cuarto de servicio', 'Deposito', 'Terraza', 'Kitchenette',
#        'Sala de estar', 'Sotano', 'Patio', 'anx81tico', 'Comedor diario',
#        'Comedor', 'Banio de servicio', 'Jardanxadn Interno', 'Walking Closet',
#        'Escritorio', 'Cocina', 'Banio independiente', 'Lavanderanxada',
#        'Balcon', 'Sala', 'Closet', 'Banio de visitas', 'Agua',
#        'Guardiananxada', 'Internet', 'Luz', 'Cable', 'Servicio de Limpieza',
#        'Conexion a gas', 'Sistema de seguridad', 'Telefono', 'Areadeportiva',
#        'Piscina', 'Solarium', 'Sala de internet', 'Sala de cine', 'Jardanxadn',
#        'Parque interno', 'Guarderanxada', 'anx81reas verdes', 'Club House',
#        'Hall de ingreso', 'Areade BBQ', 'Gimnasio', 'Areade sauna',
#        'Juegos para ninios', 'Ingreso independiente', 'Colegios cercanos',
#        'Cerca al mar', 'Centros comerciales cercanos', 'Parques cercanos',
#        'Acceso personas discapacidad', 'Frente al mar', 'Desagaue', 'Jacuzzi',
#        'Chimenea', 'Intercomunicador', 'Cerco Electrico', 'Parrilla',
#        'Aire acondicionado', 'Amoblado', 'Sauna', 'Calefaccion', 'Equipado',
#        'Terma', 'Portero electrico', 'Cocina con reposteros']]#.info()
# df_cut_obj




# df[df['Cuarto de servicio']=='NoEspecifica']




# columnas_obj =['Cuarto de servicio', 'Deposito', 'Terraza', 'Kitchenette',
#        'Sala de estar', 'Sotano', 'Patio', 'anx81tico', 'Comedor diario',
#        'Comedor', 'Banio de servicio', 'Jardanxadn Interno', 'Walking Closet',
#        'Escritorio', 'Cocina', 'Banio independiente', 'Lavanderanxada',
#        'Balcon', 'Sala', 'Closet', 'Banio de visitas', 'Agua',
#        'Guardiananxada', 'Internet', 'Luz', 'Cable', 'Servicio de Limpieza',
#        'Conexion a gas', 'Sistema de seguridad', 'Telefono', 'Areadeportiva',
#        'Piscina', 'Solarium', 'Sala de internet', 'Sala de cine', 'Jardanxadn',
#        'Parque interno', 'Guarderanxada', 'anx81reas verdes', 'Club House',
#        'Hall de ingreso', 'Areade BBQ', 'Gimnasio', 'Areade sauna',
#        'Juegos para ninios', 'Ingreso independiente', 'Colegios cercanos',
#        'Cerca al mar', 'Centros comerciales cercanos', 'Parques cercanos',
#        'Acceso personas discapacidad', 'Frente al mar', 'Desagaue', 'Jacuzzi',
#        'Chimenea', 'Intercomunicador', 'Cerco Electrico', 'Parrilla',
#        'Aire acondicionado', 'Amoblado', 'Sauna', 'Calefaccion', 'Equipado',
#        'Terma', 'Portero electrico', 'Cocina con reposteros']

# conteo_NoEsp_l = []
# Columna_l = []
# for column in columnas_obj:
    
#     conteo = df[column].value_counts()
#     conteo_NoEsp = conteo["NoEspecifica"]
#     #print(f"\nConteo de valores en {column}:\n{conteo}")
#     conteo_NoEsp_l.append(conteo_NoEsp)
#     Columna_l.append(column)





# Columna_l




# conteo_temp = df['Cuarto de servicio'].value_counts()
# conteo_temp["NoEspecifica"]




# plt.bar(Columna_l, conteo_NoEsp_l)
# plt.xticks(rotation=90)
# plt.show()






# columnas_relevantes = pd.DataFrame(conteo_NoEsp_l,Columna_l).sort_values(by=0,ascending=True).reset_index()
# columnas_relevantes = columnas_relevantes.rename(columns={"index": "columnas", 0: "conteo_no_reg"})
# columnas_relevantes





# columnas_relevantes.iloc[20]







# columnas_relevantes = columnas_relevantes[columnas_relevantes["conteo_no_reg"]<=223]
# columnas_relevantes






# columnas_relevantes_l = list(columnas_relevantes["columnas"])
# columnas_relevantes_l






# df_cutted = df[['Unnamed: 0', 'Antiguedad', 'Anunciante', 'Balneario',
#        'NroBanios', 'Nro_pisos', 'Cocheras', 'Descripcion', 'Direccion',
#        'Dormitorios', 'Estado de Inmueble', 'Fecha_pub', 'Luminosidad',
#        'Mascotas', 'Precio', 'Tipo', 'TipoCochera', 'Ubicacion',
#        'Uso_comercial', 'Uso_profesional', 'latitud', 'longitud',
#        'Area_constr', 'Area_total', 'Area_constr_m2', 'Area_total_m2', 'match', 'Cuarto de servicio',
#  'Banio de visitas',
#  'Closet', 'Sala', 'Balcon', 'Banio independiente', 'Cocina', 'Escritorio', 'Walking Closet',
#  'Jardanxadn Interno', 'Lavanderanxada', 'Comedor', 'Comedor diario', 'anx81tico', 'Patio', 'Sotano',
#  'Sala de estar', 'Kitchenette', 'Terraza', 'Deposito', 'Banio de servicio'  ]]
# df_cutted.head(3)






# plt.hist(df_cutted["Terraza"])
# plt.legend()





# df_cutted.columns#[df_cutted["Terraza"]]#==223]








# valor_filtrado = 'NoEspecifica'
# df_clean = df_cutted.drop(df_cutted[df_cutted["Terraza"]==valor_filtrado].index,  inplace=False)
# df_clean = df_clean.drop(df_clean[df_clean["Area_total_m2"]==valor_filtrado].index,  inplace=False)
# df_clean = df_clean.reset_index().drop(['index','Unnamed: 0'], axis=1)
# df_clean







# df_clean[columnas_relevantes_l]










# #df_cutted[columnas_relevantes_l]
# df_clean[columnas_relevantes_l] = df_clean[columnas_relevantes_l].apply(pd.to_numeric)
# df_clean







# df_clean.info()



# #Solo datos categoricos



# df_clean_cat = df_clean.select_dtypes(include='object')
# df_clean_cat.info()



# # Solo datos numericos


# df_clean_num = df_clean.select_dtypes(include=np.number)
# df_clean_num.info()



# df_clean_num.columns


# df_clean.groupby("Antiguedad")['Antiguedad'].size() 




# # Ejemplo de agrupación por 'Anunciante' y cálculo del promedio del precio
# grouped_by_anunciante = df.groupby('Anunciante')['Precio'].mean()
# pd.DataFrame(grouped_by_anunciante)





# # Ejemplo de agrupación por 'Tipo' y conteo de registros
# grouped_by_tipo = df.groupby('Tipo').size()
# df_grouped_by_tipo=pd.DataFrame(grouped_by_tipo).rename(columns={ 0: "conteo_tipos"}).reset_index()
# df_grouped_by_tipo= df_grouped_by_tipo.sort_values(by='conteo_tipos', ascending=False)
# df_grouped_by_tipo




# plt.bar(df_grouped_by_tipo["Tipo"], df_grouped_by_tipo["conteo_tipos"])
# plt.xticks(rotation=60)
# plt.show()





# # Ejemplo de agrupación por 'Ubicacion' y cálculo de estadísticas descriptivas
# grouped_by_ubicacion = df.groupby('Ubicacion')['Dormitorios'].describe()
# print(grouped_by_ubicacion)






# # Puedes aplicar múltiples funciones de agregación al mismo tiempo
# grouped_multiple = df_clean.groupby('Anunciante').agg({
#     'Precio': ['mean', 'min','max'],
#     'Dormitorios': 'max'
# })
# grouped_multiple





# df_clean.columns





# df_clean[["Area_total_m2"]] = df_clean[["Area_total_m2"]].apply(pd.to_numeric)
# df_clean[["Area_total_m2"]].info()







# df_clean[["Area_total_m2"]] = df_clean[["Area_total_m2"]].apply(pd.to_numeric)
# df_clean[["Area_total_m2"]].info()


# df_grafico1 = df_clean[["Tipo","Precio","Area_total_m2","Antiguedad"]]#.info()
# df_grafico1.sort_values(by='Precio', ascending=False)











# df_grafico1.describe()





# df_grafico1.describe()







# mean_value = df_grafico1["Precio"].mean()
# std_dev = df_grafico1["Precio"].std()

# mean_value2 = df_grafico1["Area_total_m2"].mean()
# std_dev2 = df_grafico1["Area_total_m2"].std()

# lower_thresholds= mean_value - (2*std_dev)
# upper_thresholds= mean_value + (2*std_dev)

# lower_thresholds2= mean_value2 - (2*std_dev2)
# upper_thresholds2= mean_value2 + (2*std_dev2)





# df_grafico1_wo= df_grafico1[(df_grafico1["Precio"]>= lower_thresholds) & (df_grafico1["Precio"] <=upper_thresholds)] 
# df_grafico1_wo= df_grafico1_wo[(df_grafico1_wo["Area_total_m2"]>= lower_thresholds2) &
#                                (df_grafico1_wo["Area_total_m2"] <=upper_thresholds2)] 




# num_outliers = len(df_grafico1) - len(df_grafico1_wo)
# num_outliers





# df_grafico1_wo.iloc[3198]


# import seaborn as sns

# sns.pairplot(df_grafico1_wo,hue='Tipo')




# x_axis = df_clean_num['Antiguedad']
# y_axis = df_clean_num['Precio']
# sns.scatterplot(x=x_axis, y=y_axis, hue=df_clean_num.Antiguedad,s=100)
# plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
import random

# Imprime las columnas antes de realizar cambios
print(df.columns.tolist())

# Selecciona una muestra aleatoria de hasta 1000 datos
max_samples = 1000
random_samples = random.sample(range(len(df)), min(len(df), max_samples))

# Crea el gráfico de dispersión categórico con la muestra aleatoria y colorea por cantidad de pisos
ax = sns.swarmplot(data=df.iloc[random_samples], x='Antiguedad', y='Precio', hue='Tipo', palette='viridis', size=3)

# Establece el límite superior del eje y en 8,000,000
plt.ylim(0, 5000000)

# Ajusta las etiquetas de los ejes según sea necesario
ax.set(xlabel="Antigüedad", ylabel="Precio")

# Muestra el gráfico
plt.show()

# Imprime las columnas después de realizar cambios
#print(df.columns.tolist())
