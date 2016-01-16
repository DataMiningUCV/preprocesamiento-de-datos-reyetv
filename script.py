# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 03:50:49 2016

@author: rey
"""

import os
import pandas as pd
import numpy as np
import re

#Cambio de directorio de trabajo al que tenga el script
os.chdir(os.getcwd())

#Leo el archivo de data.csv y lo almaceno en un DataFrame 
df = pd.read_csv('data.csv', header=0)

#Cambio el nombre de las columnas del DataFrame  para tener mayor control sobre las columnas e índices
#y arreglar nombres con caracteres de más
df.columns = ["ID", "PeríodoAcadémicoARenovar", "CédulaDeIdentidad", "FechaDeNacimiento", "Edad", "EstadoCivil", "Sexo", "Escuela", "AñoIngresoUCV", "ModalidadDeIngresoUCV", "SemestreActual", "CambióDeDirección", "MotivoCambioDeDirección", "NúmeroMateriasInscritasEnPeríodoAnterior", "NúmeroMateriasAprobadasEnPeríodoAnterior", "NúmeroMateriasRetiradasEnPeríodoAnterior", "NúmeroMateriasReprobadasEnPeríodoAnterior", "PromedioPonderadoAprobado", "Eficiencia", "MotivoEnCasoDeReprobarUnaOMásMaterias", "NúmeroMateriasInscritasEnPeríodoActual", "EstáRealizandoTesisOTrabajoDeGradoOPasantíasDeGrado", "VecesQueHaRealizadoTesisTrabajoDeGradoOPasantíasDeGrado", "DirecciónDeVivienda", "LugarDeResidenciaDuranteEstudios", "RelaciónConPersonasConLasQueViveDuranteEstudios", "TipoDeViviendaDeResidenciaDuranteEstudios", "MontoMensualDeViviendaAlquiladaOResidenciaEstudiantil", "DirecciónHabitaciónOResidenciaEstudiantil", "ContrajoMatrimonio", "HaSolicitadoOtroBeneficioALaUniversidadUOtraInstitución", "IndiqueAñoDeSolicitudYMotivo", "RealizaActividadRemunerada", "IndiqueTipoDeActividadYFrecuencia", "MontoMensualBeca", "AporteMensualQueObtieneDeRepresentanteEconómico", "AporteMensualQueObtieneDeFamiliaresOAmigos", "IngresoMensualQueRecibePorActividadesADestajoOPorHoras", "IngresoMensualTotal", "GastosAlimentación", "GastosTransportePublico", "GastosMédicos", "GastosOdontológicos", "GastosPersonales", "GastosResidenciaOHabitaciónAlquilada", "GastosMaterialesDeEstudio", "GastosDeRecreación", "OtrosGastos", "TotalEgresos", "ResponsableEconómico", "CargaFamiliar", "IngresoMensualResponsableEconómico", "OtrosIngresos", "TotalDeIngresos", "GastosViviendaResponsableEconómico", "GastosAlimentaciónResponsableEconómico", "GastosTransporteResponsableEconómico", "GastosMédicosResponsableEconómico", "GastosOdontológicosResponsableEconómico", "GastosEducativosResponsableEconómico", "GastosServiciosPúblicosResponsableEconómico", "GastosCondominioResponsableEconómico", "OtrosGastosResponsableEconómico", "TotalEgresosResponsableEconómico", "PuntuaciónDelServicioOfrecido", "SugerenciasYRecomendaciones"]

 
 #Ya con el DataFrame listo, podemos empezar a realizar cambios por columnas según sea el caso
 
 #                                         Columna ID
 #Eliminamos la columna ID ya que tiene información relevante para el negocio y la cédula de identidad
 #es mejor para identificar algún registro
 
del df["ID"]
 
 #                                  Columna CédulaDeIdentidad
 #Cambiamos de lugar las columnas CedulaDeIdentidad y PeríodoAcadémicoARenovar para que la columna
 #identificadora esté de primera en la tabla, no convertimos a enteros sus valores porque pandas ya
 #hace eso al momento de leer la data
cols = df.columns.tolist()
cols[0],cols[1] = cols[1],cols[0]
df = df[cols]
 
 #                              Columna PeríodoAcadémicoARenovar
 #Separaremos esta columna en dos columnas, una para el año del período y otro para el semestre (1 ó 2)
 
 #Código aquí :D
 
 #                                  Columna FechaDeNacimiento
 #Separamos la columna en tres columnas, día, mes y año respectivamente con valores numéricos solamente
 
df["FechaDeNacimiento"][12] = "1/05/1989" 
df["FechaDeNacimiento"][19] = "22/04/1985"
df["FechaDeNacimiento"][151] = "21/04/1994"
 
df["DíaDeNacimiento"] = [re.split('[/ -]',item)[0] for item in df["FechaDeNacimiento"]]
df["MesDeNacimiento"] = [re.split('[/ -]',item)[1] for item in df["FechaDeNacimiento"]]
df["AñoDeNacimiento"] = [re.split('[/ -]',item)[2] for item in df["FechaDeNacimiento"]]
 
for a in df["AñoDeNacimiento"]:
    if len(a) == 2:
        df.loc[df["AñoDeNacimiento"] == a, "AñoDeNacimiento"] = "19" + a
         
df["DíaDeNacimiento"] = df["DíaDeNacimiento"].astype(int)
df["MesDeNacimiento"] = df["MesDeNacimiento"].astype(int)
df["AñoDeNacimiento"] = df["AñoDeNacimiento"].astype(int)
 
del df["FechaDeNacimiento"]
 
 #                                          Columna Edad
 
 #Convertimos todos los valores a enteros y limpiamos los strings en los registros
for x in df["Edad"]:
    if(len(x)) > 2:
        df.loc[df.Edad == x, "Edad"] = x[:2]
        
df["Edad"] = df["Edad"].astype(int)
 
 #                                      Columna EstadoCivil
 #Realizamos un mapeo entre los valores string de la columna para usar valores enteros
 
ecmap = {"Soltero (a)": 0, "Casado (a)": 1, "Viudo (a)": 2, "Unido (a)": 3}
 
df["EstadoCivil"] = df["EstadoCivil"].map(ecmap).astype(int)
 
 #                                          Columna Sexo
 #Se hace un mapeo similar al anterior por el mismo motivo
smap = {"Masculino": 0, "Femenino": 1}
 
df["Sexo"] = df["Sexo"].map(smap).astype(int)
 
 #                                        Columna Escuela
 #El mismo mapeo
emap = {"Enfermería": 0, "Bioanálisis": 1}
 
df["Escuela"] = df["Escuela"].map(emap).astype(int)
 
 #                                      Columna AñoIngresoUCV
 #Esta columna ya está bien y el paquete pandas infirió el tipo de dato entero por nosotros
 
 #                                  Columna ModalidadDeIngresoUCV
 #Misma correspondencia y parseo de datos
mdimap = {"Convenios Interinstitucionales (nacionales e internacionales)": 0,
           "Prueba Interna y/o propedéutico": 1,
           "Convenios Internos (Deportistas, artistas, hijos empleados docente y obreros, Samuel Robinson)": 2,
           "Asignado OPSU": 4 }

df["ModalidadDeIngresoUCV"] = df["ModalidadDeIngresoUCV"].map(mdimap).astype(int)
 
 #                                      Columna SemestreActual
 #Extraemos los números de los strings en los registros usando expresiones regulares y asignamos esos números a los valores
 
for x in df["SemestreActual"]:
    nums = re.findall("[\d]+", x)
    df.loc[df.SemestreActual == x, "SemestreActual"] = nums
 
df["SemestreActual"] = df["SemestreActual"].astype(int)
 
 #                                  Columna CambióDeDirección
 #Realizamos el mismo mapeo con los valores correspondientes
 
ynmap = {"No": 0, "Si": 1}
 
df["CambióDeDirección"] = df["CambióDeDirección"].map(ynmap).astype(int)
 
 
 #              Columna VecesQueHaRealizadoTesisTrabajoDeGradoOPasantíasDeGrado
 #Eliminación de la columna 
del df["VecesQueHaRealizadoTesisTrabajoDeGradoOPasantíasDeGrado"]
 
 #              Columna MontoMensualDeViviendaAlquiladaOResidenciaEstudiantil
 #Eliminación de la columna 
del df["MontoMensualDeViviendaAlquiladaOResidenciaEstudiantil"] 

 #                          Columna ContrajoMatrimonio 
 #Eliminación de la columna 
del df["ContrajoMatrimonio"]
 
 
 #Columnas finales en el orden que tendrán
cols2 = ["CédulaDeIdentidad", "PeríodoAcadémicoARenovar", "DíaDeNacimiento", "MesDeNacimiento", 
 "AñoDeNacimiento", "Edad", "EstadoCivil", "Sexo", "Escuela", "AñoIngresoUCV", "ModalidadDeIngresoUCV", 
 "SemestreActual", "CambióDeDirección", "MotivoCambioDeDirección", "NúmeroMateriasInscritasEnPeríodoAnterior", 
 "NúmeroMateriasAprobadasEnPeríodoAnterior", "NúmeroMateriasRetiradasEnPeríodoAnterior", 
 "NúmeroMateriasReprobadasEnPeríodoAnterior", "PromedioPonderadoAprobado", "Eficiencia", "MotivoEnCasoDeReprobarUnaOMásMaterias", 
"NúmeroMateriasInscritasEnPeríodoActual", "EstáRealizandoTesisOTrabajoDeGradoOPasantíasDeGrado", 
 "DirecciónDeVivienda", "LugarDeResidenciaDuranteEstudios", "RelaciónConPersonasConLasQueViveDuranteEstudios", 
"TipoDeViviendaDeResidenciaDuranteEstudios", "DirecciónHabitaciónOResidenciaEstudiantil", 
 "HaSolicitadoOtroBeneficioALaUniversidadUOtraInstitución", "IndiqueAñoDeSolicitudYMotivo", 
 "RealizaActividadRemunerada", "IndiqueTipoDeActividadYFrecuencia", "MontoMensualBeca", 
 "AporteMensualQueObtieneDeRepresentanteEconómico", "AporteMensualQueObtieneDeFamiliaresOAmigos", 
 "IngresoMensualQueRecibePorActividadesADestajoOPorHoras", "IngresoMensualTotal", "GastosAlimentación",
 "GastosTransportePublico", "GastosMédicos", "GastosOdontológicos", "GastosPersonales", 
 "GastosResidenciaOHabitaciónAlquilada", "GastosMaterialesDeEstudio", "GastosDeRecreación", 
 "OtrosGastos", "TotalEgresos", "ResponsableEconómico", "CargaFamiliar", "IngresoMensualResponsableEconómico", 
 "OtrosIngresos", "TotalDeIngresos", "GastosViviendaResponsableEconómico", "GastosAlimentaciónResponsableEconómico", 
 "GastosTransporteResponsableEconómico", "GastosMédicosResponsableEconómico", "GastosOdontológicosResponsableEconómico", 
 "GastosEducativosResponsableEconómico", "GastosServiciosPúblicosResponsableEconómico", 
 "GastosCondominioResponsableEconómico", "OtrosGastosResponsableEconómico", "TotalEgresosResponsableEconómico", 
 "PuntuaciónDelServicioOfrecido", "SugerenciasYRecomendaciones"]
 
 #Con la lista defino las columas y se las asigno al DataFrame
df = df[cols2]
 #Ordeno por cédula de identidad de manera ascendente 
df = df.sort_values(by = "CédulaDeIdentidad", ascending = True)
 
 #Uso pandas para pasar el DataFrame a un archivo .csv
df.to_csv("minable.csv")
 