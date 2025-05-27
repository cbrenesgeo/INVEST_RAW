# -*- coding: utf-8 -*-
"""
InVEST  |  Annual Water Yield  (a.k.a.  Reservoir Hydropower Production – Water Yield)
======================================================================================
Plantilla completa (versión ≥ 3.14) con **TODOS** los parámetros que el API reconoce.  
—► Rellena o sustituye los valores según tus datos locales.  
—► El módulo calcula el rendimiento hídrico promedio-anual y, opcionalmente,
    el valor económico del recurso para generación hidroeléctrica.

Requiere:  `pip install natcap.invest`
"""

# ------------------------------------------------------------------------------
# 1.  Imports
# ------------------------------------------------------------------------------
# El sub-módulo ‘annual_water_yield’ está disponible desde InVEST 3.14;
# en versiones anteriores aparece como ‘hydropower.hydropower_water_yield’.
from natcap.invest import annual_water_yield as awy   # ← ajusta si usas < 3.14
import os

# ------------------------------------------------------------------------------
# 2.  Carpeta de trabajo (se creará si no existe)
# ------------------------------------------------------------------------------
workspace = '~/GIS_RS/AWY/workspace'

# ------------------------------------------------------------------------------
# 3.  Diccionario de argumentos
#    (todos los reconocidos por el modelo — obligatorios y opcionales)
# ------------------------------------------------------------------------------
args = {
    # -------------------------------------------------------------------------
    # A) OBLIGATORIOS
    # -------------------------------------------------------------------------
    'workspace_dir': workspace,
    'results_suffix': 'escenario_base',            # se añade a cada archivo de salida

    # Rasters de entrada (coincidentes en proyección, extensión y celda)
    'lulc_path'     : os.path.join(workspace, 'lulc_2020.tif'),     # uso/cobertura suelo
    'precip_path'   : os.path.join(workspace, 'precip_mean_mm.tif'),# precipitación anual (mm)
    'et0_path'      : os.path.join(workspace, 'eto_mean_mm.tif'),   # ET0 anual (mm)

    # Propiedades edáficas/hidrológicas
    'depth_to_root_rest_layer_path': os.path.join(
        workspace, 'dtrrl_m.tif'),                                   # profundidad (m)
    'pawc_path'     : os.path.join(workspace, 'pawc_fraction.tif'),  # PAWC (0–1)

    # Parámetro ‘Z’ de Budyko (controla la escorrentía relativa)
    'seasonality_constant': 10.0,          # típico 1 – 30 (mayor = más escorrentía)

    # Tabla biofísica (CSV ⇒ Kc, otros coef. por clase LULC)
    'biophysical_table_path': os.path.join(workspace, 'biophysical_table.csv'),

    # Shapefile de cuencas para resumen de resultados
    'watersheds_path': os.path.join(workspace, 'watersheds.shp'),

    # -------------------------------------------------------------------------
    # B) OPCIONALES  — utiliza si quieres valoración o datos constantes
    # -------------------------------------------------------------------------

    # 1.  Valoración económica (USD) para hidroelectricidad
    'demand_table_path'   : '',   # CSV con demanda anual de cada cuenca (m³ a-¹)
    'valuation_table_path': '',   # CSV con precio medio (USD / m³) y tasa descuento

    # 2.  Usar valores constantes en lugar de rasters
    #    (deja el *_path en '' y define la constante)
    # 'depth_to_root_rest_layer_path': '',
    # 'depth_to_root_rest_layer'    : 2.0,    # metros
    # 'pawc_path'                   : '',
    # 'pawc'                        : 0.15,   # fracción 0–1

    # 3.  Procesamiento paralelo
    'n_workers': -1                # −1 = todos los núcleos disponibles
}

# ------------------------------------------------------------------------------
# 4.  Ejecución del modelo
# ------------------------------------------------------------------------------
awy.execute(args)

# ==============================================================================
# Guía rápida de cada entrada
# ==============================================================================
"""
► lulc_path .................. Raster entero; cada valor es un código de clase.
► precip_path, et0_path ...... mm a-¹; pueden derivarse de WorldClim, CHIRPS, etc.
► dtrrl / depth_to_root_...... Profundidad a la capa restrictiva (m).
► pawc ....................... ‘Plant Available Water Content’ (vol/vol, 0–1).
► biophysical_table.csv ...... Columnas mínimas:
       lucode, root_depth, kc
   (puedes incluir más variables; las extras se ignoran).
► seasonality_constant ....... Parámetro Z del método Budyko-Zhang (sensibilidad
   a la estacionalidad y retención de agua en suelos).
► watersheds_path ............ Polígonos; los resúmenes se guardan en CSV/SHP.
► demand_table_path .......... [opcional]  id | demand_m3_y
► valuation_table_path ....... [opcional]  price_usd_m3 | discount_rate | years
"""

# ==============================================================================
# Principales SALIDAS (en <workspace>/output)
# ==============================================================================
"""
• wy_mm_<sufijo>.tif .............. Rendimiento hídrico promedio-anual (mm).
• wy_m3_<sufijo>.tif .............. Igual, convertido a m³ ∙ pixel-¹.
• wy_valuation_<sufijo>.tif ....... VAN del agua (USD)  ↦  solo si hay valoración.
• wy_summary_<sufijo>.csv  ........ Totales y medias por cuenca.
• report_<sufijo>.html  ........... Informe interactivo; incluye mapas y tablas.
"""
