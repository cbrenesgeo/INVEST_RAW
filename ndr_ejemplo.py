from natcap.invest import sdr
import os

# Ruta base de tu proyecto
workspace = '~/GIS_RS/NDR_/Input_data_SDR'

# Diccionario de argumentos para el modelo SDR (Sediment Delivery Ratio)
args = {
    'workspace_dir': workspace,
    'results_suffix': 'escenario_base',
    'dem_path': '/home/cbrenes/GIS_RS/NDR_/Input_data_SDR/DEM_gura.tif',
    'erosivity_path': '/home/cbrenes/GIS_RS/NDR_/Input_data_SDR/erosivity_gura.tif',
    'erodibility_path': '/home/cbrenes/GIS_RS/NDR_/Input_data_SDR/erodibility_gura.tif'.,
    'lulc_path': '/home/cbrenes/GIS_RS/NDR_/Input_data_SDR/land_use_gura.tif',
    'watersheds_path': '/home/cbrenes/GIS_RS/NDR_/Input_data_SDR/subwatersheds_gura.shp',
    'biophysical_table_path': '/home/cbrenes/GIS_RS/NDR_/Input_data_SDR/biophysical_table_Gura.csv',
    'threshold_flow_accumulation': 100,
    'k_param': 2.0,  # Parámetro SDR
    'ic_0_param': 0.5,  # Valor de referencia para índice de conectividad
    'sdr_max': 0.8,
    'drainage_path': '',  # Opcional, puede ser una red de drenaje vectorial
    'n_workers': -1  # Usa todos los núcleos disponibles
}

# Ejecutar el modelo SDR
sdr.execute(args)

#comando para extraer todos los nombre de los archivos y sus rutas
find ~/GIS_RS/NDR_/Input_data_SDR -type f -exec realpath {} \;


/home/cbrenes/GIS_RS/NDR_/Input_data_SDR/DEM_gura.tif.xml
/home/cbrenes/GIS_RS/NDR_/Input_data_SDR/DEM_gura.tif.aux.xml
/home/cbrenes/GIS_RS/NDR_/Input_data_SDR/erodibility_gura.tif.aux.xml
/home/cbrenes/GIS_RS/NDR_/Input_data_SDR/subwatersheds_gura.shp
/home/cbrenes/GIS_RS/NDR_/Input_data_SDR/land_use_gura.qlr
/home/cbrenes/GIS_RS/NDR_/Input_data_SDR/_README_InVEST_SDR_model_data.txt
/home/cbrenes/GIS_RS/NDR_/Input_data_SDR/subwatersheds_gura.sbx
/home/cbrenes/GIS_RS/NDR_/Input_data_SDR/erodibility_gura.tif.xml
/home/cbrenes/GIS_RS/NDR_/Input_data_SDR/watershed_gura.sbn
/home/cbrenes/GIS_RS/NDR_/Input_data_SDR/erosivity_gura.tif.aux.xml
/home/cbrenes/GIS_RS/NDR_/Input_data_SDR/DEM_gura.tif.vat.dbf
/home/cbrenes/GIS_RS/NDR_/Input_data_SDR/Untitled.ipynb
/home/cbrenes/GIS_RS/NDR_/Input_data_SDR/biophysical_table_Gura.csv
/home/cbrenes/GIS_RS/NDR_/Input_data_SDR/DEM_gura.tif
/home/cbrenes/GIS_RS/NDR_/Input_data_SDR/watershed_gura.dbf
/home/cbrenes/GIS_RS/NDR_/Input_data_SDR/watershed_gura.shp
/home/cbrenes/GIS_RS/NDR_/Input_data_SDR/land_use_gura.tif.vat.dbf
/home/cbrenes/GIS_RS/NDR_/Input_data_SDR/erosivity_gura.tif.xml

