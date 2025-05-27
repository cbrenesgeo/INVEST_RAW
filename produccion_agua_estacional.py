# -*- coding: utf-8 -*-
"""
InVEST | Seasonal Water Yield (SWY)
===================================
Plantilla exhaustiva para ejecutar el modelo **Seasonal Water Yield** (versión ≥ 3.15).  
► Incluye **TODOS** los argumentos que el API expone; los opcionales aparecen
  con valores de ejemplo o como cadenas vacías ('') para que los rellenes.  
► Sustituye las rutas, los parámetros alfa/β/γ y cualquier tabla según tu caso.

Instalación rápida:
    pip install natcap.invest
"""

# --------------------------------------------------------------------------- #
# 1) Imports
# --------------------------------------------------------------------------- #
from natcap.invest import seasonal_water_yield as swy      # ← nombre del módulo
import os

# --------------------------------------------------------------------------- #
# 2) Carpeta de trabajo (salidas + temporales)
# --------------------------------------------------------------------------- #
workspace = '~/GIS_RS/SWY/workspace'

# --------------------------------------------------------------------------- #
# 3) Diccionario de argumentos
# --------------------------------------------------------------------------- #
args = {
    # ----------------------------------------------------------------------- #
    # A. PARÁMETROS OBLIGATORIOS
    # ----------------------------------------------------------------------- #
    'workspace_dir'      : workspace,
    'results_suffix'     : 'escenario_base',

    # ► Datos base
    'dem_path'           : os.path.join(workspace, 'dem.tif'),          # DEM (m)
    'lulc_path'          : os.path.join(workspace, 'lulc_2020.tif'),    # uso/cobertura

    # ► Directorios con 12 capas mensuales (1.tif … 12.tif o precip_01.tif …)
    'precip_dir'         : os.path.join(workspace, 'precip_mm'),        # mm mes⁻¹
    'eto_dir'            : os.path.join(workspace, 'eto_mm'),           # mm mes⁻¹

    # ► Tabla biofísica (CSV)
    #    Columnas mínimas: lucode, root_depth, kc, LULC_veg, LULC_soil
    'biophysical_table_path': os.path.join(workspace, 'biophysical_table.csv'),

    # ► Parámetros alfa, beta, gamma (escala cuenca)
    #   α_m  … partición de lluvia en quick-flow (0–6≈)
    #   β_i  … coef. de infiltración (0–1)
    #   γ    … factor de recarga profunda (0–1)
    'alpha_m'            : 1.5,
    'beta_i'             : 1.0,
    'gamma'              : 1.0,

    # ----------------------------------------------------------------------- #
    # B. OPCIONALES  (déjalos '' si no los usarás)
    # ----------------------------------------------------------------------- #

    # ► Profundidad a capa restrictiva (D_RRL)  y  PAWC → raster o constantes
    'depth_to_root_rest_layer_path': os.path.join(workspace, 'dtrrl_m.tif'),
    # Si no tienes raster, deja la ruta vacía y define:
    # 'depth_to_root_rest_layer'   : 2.0,   # m

    'pawc_path'          : os.path.join(workspace, 'pawc_fraction.tif'),
    # O como constante:
    # 'pawc'             : 0.15,  # fracción (0–1)

    # ► Tabla de eventos de lluvia (opcional si tu α_m es calibrado)
    'rain_events_table_path': '',  # CSV con columnas: month, rain_events

    # ► Raster de fracción de área impermeable (permite evaluar urbanización)
    'monthly_alpha_path' : '',     # 12-band raster con α por mes (avanza la v3.16)

    # ► Malla para análisis celular (hex/square) — igual lógica que en VoRT
    'grid_aoi'           : False,
    'grid_type'          : 'hexagon',   # 'square' | 'hexagon'  (si grid_aoi=True)
    'cell_size'          : 5000,        # m

    # ► Procesamiento paralelo
    'n_workers'          : -1           # −1 = todos los núcleos
}

# --------------------------------------------------------------------------- #
# 4) Ejecutar el modelo
# --------------------------------------------------------------------------- #
swy.execute(args)

# =========================================================================== #
#               ───  GUÍA RÁPIDA DE CADA ARGUMENTO  ───
# =========================================================================== #
"""
DEM (dem_path) ................. Elevación en metros; define cuencas y flujo.
LULC (lulc_path) ............... Raster entero (códigos); una sola banda.

precip_dir, eto_dir ............ Carpetas que contienen **exactamente 12** tif:
                                  1.tif … 12.tif  (o cualquier nombre, pero orden
                                  alfabético = orden mensual).  Unidades mm.

biophysical_table.csv .......... Claves mínimas
                                  lucode | root_depth (mm) | kc
                                  Puedes añadir quick_flow_accum, etc.  No
                                  borres columnas obligatorias aunque estén 0.

alpha_m, beta_i, gamma ......... Parámetros de partición de flujo (ver manual):
                                  α_m: valor ≈1–2 vegetación densa, >3 suelo sellado.
                                  β_i: fracción infiltrable; 1 = todo infiltra.
                                  γ  : porcentaje de recarga que se convierte en
                                      caudal base.

depth_to_root_rest_layer_path
pawc_path ...................... Si usas constantes, deja la ruta vacía ('') y
                                 define los valores bajo las mismas claves sin
                                 ‘_path’ (ver ejemplos comentados).

rain_events_table_path ......... Si disponible: CSV (month, rain_events) donde
                                 `rain_events` es nº de tormentas/mes (≥1).

grid_aoi / grid_type / cell_size
                               .. Discretiza el AOI en teselas para resultados
                                  homogéneos por celda (p.ej. hotspots  urban).

n_workers ....................... −1 → todos los cores; 1 = secuencial.

"""

# =========================================================================== #
#                ───  PRINCIPALES SALIDAS EN <workspace>/output  ───
# =========================================================================== #
"""
quickflow_<sufijo>.tif ........... mm a-¹ de escorrentía rápida por pixel
local_recharge_<sufijo>.tif ...... mm a-¹ que recarga acuífero superficial
baseflow_<sufijo>.tif ............ mm a-¹ (cálculo aproximado de caudal base)
seasonal_summary_<sufijo>.csv .... Tabla: sumas/medias por cuenca o tesela
report_<sufijo>.html ............. Informe interactivo con mapas y gráficos
"""
