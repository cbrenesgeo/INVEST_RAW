# -*- coding: utf-8 -*-
"""
Ejecución del modelo Urban Flood Risk Mitigation (UFRM) de InVEST
----------------------------------------------------------------
Ajusta las rutas y parámetros según tus insumos.
"""

from natcap.invest import urban_flood_risk_mitigation as ufrm
import os

# Carpeta de trabajo donde se guardarán salidas y temporales
workspace = '~/GIS_RS/UFRM_/input_data_ufrm'

# Construimos un diccionario con **todas** las opciones del modelo
args = {
    # OBLIGATORIOS -----------------------------------------------------------
    'workspace_dir': workspace,
    'results_suffix': 'escenario_base',      # se añade a cada archivo de salida
    'aoi_watersheds_path': os.path.join(workspace, 'subwatersheds_ufrm.shp'),
    'rainfall_depth': 50.0,                  # profundidad de lluvia de diseño (mm)
    'lulc_path': os.path.join(workspace, 'land_use_ufrm.tif'),
    'soils_hydrological_group_raster_path': os.path.join(
        workspace, 'soil_groups_ufrm.tif'),
    'curve_number_table_path': os.path.join(
        workspace, 'curve_number_table.csv'),

    # OPCIONALES -------------------------------------------------------------
    # Vector de infraestructura expuesta (puede omitirse con '' o None)
    'built_infrastructure_vector_path': os.path.join(
        workspace, 'infraestructura_urbana.shp'),

    # Tabla de daños potenciales por tipo de infraestructura (en la misma
    # clave de 'Type' que el vector anterior). Moneda / m².
    'infrastructure_damage_loss_table_path': os.path.join(
        workspace, 'damage_loss_table.csv'),

    # Número de procesos paralelos (-1 = usar todos los núcleos disponibles)
    'n_workers': -1,
}

# Ejecutar el modelo ---------------------------------------------------------
ufrm.execute(args)
