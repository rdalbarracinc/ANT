#Este programa se creó para identificar los conjuntos d datos que se dividen entre fmi, numero_predial y uit_operacion
https://colab.research.google.com/drive/1DfkCg5BFxjTsjJ-t7SuG4xaegtt7ncSt?usp=sharing

import pandas as pd

# CARGAAS DATOS
print("")
print("========================")
print("** PREDIAGNÓSTICO MTJ ++")
print("========================")
print("")

# Leer el archivo CSV especificando el tipo de datos como cadena para las columnas con tipos mixtos
df = pd.read_csv("C:/Users/rdalb/Documents/ANT/Mayo 2024/PRE_MTJ_JUR_17052024v3.csv", dtype=str)

# Mostrar las dos primeras filas del dataframe
print(df.head(2))

print(df.columns)


################
print("")
print("=================================================")
print("** INVENTARIO DE DATOS: INFORME PREDIAGNÓSTICO ++")
print("=================================================")
print("")
#######################


# Contar los valores 'q' según los filtros especificados por 'uit_operacion'
con_fmi_con_num_predial_uit = df[(df['fmi'].notna()) & (df['numero_predial'].notna())]['uit_operacion'].count()
con_fmi_sin_num_predial_uit = df[(df['fmi'].notna()) & (df['numero_predial'].isna())]['uit_operacion'].count()
sin_fmi_con_num_predial_uit = df[(df['fmi'].isna()) & (df['numero_predial'].notna())]['uit_operacion'].count()
sin_fmi_sin_num_predial_uit = df[(df['fmi'].isna()) & (df['numero_predial'].isna())]['uit_operacion'].count()

# Imprimir los resultados
# Imprimir los resultados
print("Con FMI y con número_predial:", con_fmi_con_num_predial_uit)
print("Con FMI y sin número_predial:", con_fmi_sin_num_predial_uit)
print("Sin FMI y con número_predial:", sin_fmi_con_num_predial_uit)
print("Sin FMI y sin número_predial:", sin_fmi_sin_num_predial_uit)

#
##########################################################3#####
print("")
print("===========================================")
print("** INVENTARIO DE DATOS: INFORME PREDIAGNÓSTICO SI O NO ++")
print("===========================================")
print("")
##################################################################3
# Contar los valores 'q' según los filtros especificados por 'uit_operacion'
con_fmi_con_num_predial_uit_con_nro_catastro = df[(df['si_fmi'].notna()) & (df['si_num_pred'].notna()) & (df['si_num_catastral'].notna())]['Q'].count()
con_fmi_sin_num_predial_uit_con_nro_catastro = df[(df['si_fmi'].notna()) & (df['si_num_pred'].isna()) & (df['si_num_catastral'].notna())]['Q'].count()
sin_fmi_con_num_predial_uit_con_nro_catastro = df[(df['si_fmi'].isna()) & (df['si_num_pred'].notna()) & (df['si_num_catastral'].notna())]['Q'].count()
sin_fmi_sin_num_predial_uit_con_nro_catastro = df[(df['si_fmi'].isna()) & (df['si_num_pred'].isna()) & (df['si_num_catastral'].notna())]['Q'].count()
# Contar los valores 'q' según los filtros especificados por 'uit_operacion'
con_fmi_con_num_predial_uit_sin_nro_catastro = df[(df['si_fmi'].notna()) & (df['si_num_pred'].notna()) & (df['si_num_catastral'].isna())]['Q'].count()
con_fmi_sin_num_predial_uit_sin_nro_catastro = df[(df['si_fmi'].notna()) & (df['si_num_pred'].isna()) & (df['si_num_catastral'].isna())]['Q'].count()
sin_fmi_con_num_predial_uit_sin_nro_catastro = df[(df['si_fmi'].isna()) & (df['si_num_pred'].notna()) & (df['si_num_catastral'].isna())]['Q'].count()
sin_fmi_sin_num_predial_uit_sin_nro_catastro = df[(df['si_fmi'].isna()) & (df['si_num_pred'].isna()) & (df['si_num_catastral'].isna())]['Q'].count()                                                      


# Imprimir los resultados
print("Caso 1: Con FMI y con número predial con nro catastro:", con_fmi_con_num_predial_uit_con_nro_catastro)
print("Caso 2: Con FMI y sin número predial con nro catastro:", con_fmi_sin_num_predial_uit_con_nro_catastro)
print("Caso 3: Sin FMI y con número predial con nro catastro:", sin_fmi_con_num_predial_uit_con_nro_catastro)
print("Caso 4: Sin FMI y sin número predial con nro catastro:", sin_fmi_sin_num_predial_uit_con_nro_catastro)
# Imprimir los resultados
print("Caso 5: Con FMI y con número predial sin nro catastro:", con_fmi_con_num_predial_uit_sin_nro_catastro)
print("Caso 6: Con FMI y sin número predial sin nro catastro:", con_fmi_sin_num_predial_uit_sin_nro_catastro)
print("Caso 7: Sin FMI y con número predial sin nro catastro:", sin_fmi_con_num_predial_uit_sin_nro_catastro)
print("Caso 8: Sin FMI y sin número predial sin nro catastro:", sin_fmi_sin_num_predial_uit_sin_nro_catastro)

##########################################################3#####
print("")
print("===========================================")
print("** CSV : DATOS POR FILTROS")
print("===========================================")
print("")
##################################################################

df_con_fmi_con_num_predial_uit_con_nro_catastro = df[(df['si_fmi'].notna()) & (df['si_num_pred'].notna()) & (df['si_num_catastral'].notna())]
#df_con_fmi_con_num_predial_uit_con_nro_catastro.to_csv("C:/Users/rdalb/Documents/ANT/Mayo 2024/df_con_fmi_con_num_predial_uit_con_nro_catastro.csv", index=False)  # Puedes especificar index=False si no deseas incluir el índice del DataFrame en el archivo CSV
df_con_fmi_sin_num_predial_uit_con_nro_catastro = df[(df['si_fmi'].notna()) & (df['si_num_pred'].isna()) & (df['si_num_catastral'].notna())]
df_sin_fmi_con_num_predial_uit_con_nro_catastro = df[(df['si_fmi'].isna()) & (df['si_num_pred'].notna()) & (df['si_num_catastral'].notna())]
df_sin_fmi_sin_num_predial_uit_con_nro_catastro = df[(df['si_fmi'].isna()) & (df['si_num_pred'].isna()) & (df['si_num_catastral'].notna())]
# Contar los valores 'q' según los filtros especificados por 'uit_operacion'
df_con_fmi_con_num_predial_uit_sin_nro_catastro = df[(df['si_fmi'].notna()) & (df['si_num_pred'].notna()) & (df['si_num_catastral'].isna())]
df_con_fmi_sin_num_predial_uit_sin_nro_catastro = df[(df['si_fmi'].notna()) & (df['si_num_pred'].isna()) & (df['si_num_catastral'].isna())]
df_sin_fmi_con_num_predial_uit_sin_nro_catastro = df[(df['si_fmi'].isna()) & (df['si_num_pred'].notna()) & (df['si_num_catastral'].isna())]
df_sin_fmi_sin_num_predial_uit_sin_nro_catastro = df[(df['si_fmi'].isna()) & (df['si_num_pred'].isna()) & (df['si_num_catastral'].isna())]

##########################################################3#####
print("")
print("===========================================")
print("** XLSX : DATOS POR FILTROS **")
print("===========================================")
print("")
##################################################################

# Crea un objeto ExcelWriter para el archivo Excel
with pd.ExcelWriter("C:/Users/rdalb/Documents/ANT/Mayo 2024/df_resultado.xlsx") as writer:
    # Guarda cada DataFrame en una pestaña diferente utilizando el método to_excel()
    df_con_fmi_con_num_predial_uit_con_nro_catastro.to_excel(writer, sheet_name='Caso1', index=False)
    df_con_fmi_sin_num_predial_uit_con_nro_catastro.to_excel(writer, sheet_name='Caso2', index=False)
    df_sin_fmi_con_num_predial_uit_con_nro_catastro.to_excel(writer, sheet_name='Caso3', index=False)
    df_sin_fmi_sin_num_predial_uit_con_nro_catastro.to_excel(writer, sheet_name='Caso4', index=False)
    
    df_con_fmi_con_num_predial_uit_sin_nro_catastro.to_excel(writer, sheet_name='Caso5', index=False)
    df_con_fmi_sin_num_predial_uit_sin_nro_catastro.to_excel(writer, sheet_name='Caso6', index=False)
    df_sin_fmi_con_num_predial_uit_sin_nro_catastro.to_excel(writer, sheet_name='Caso7', index=False)
    df_sin_fmi_sin_num_predial_uit_sin_nro_catastro.to_excel(writer, sheet_name='Caso8', index=False)


