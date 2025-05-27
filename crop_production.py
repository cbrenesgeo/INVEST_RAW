# -*- coding: utf-8 -*-
"""
InVEST | Crop Production  –– dos enfoques
========================================
El paquete InVEST incluye **dos modelos** de producción agrícola:

1. **Crop Production Percentile**  → usa percentiles de rendimiento
   empíricos (históricos) por zona climática (bins).
2. **Crop Production Regression**  → ajusta una regresión lineal múltiple con
   variables climáticas y de manejo; permite escenarios (fertilizante, riego).

A continuación encontrarás **plantillas completas para ambos**.  
Sustituye rutas, tablas y parámetros según tu proyecto.  
Necesitas InVEST ≥ 3.14  (`pip install natcap.invest`).

---------------------------------------------------------------------------
PARTE A · Percentile
---------------------------------------------------------------------------
"""

# ---------------------------------------------------------------------------
# 1.  Imports
# ---------------------------------------------------------------------------
from natcap.invest import crop_production_percentile as cpp
import os

# ---------------------------------------------------------------------------
# 2.  Carpeta de trabajo
# ---------------------------------------------------------------------------
workspace_perc = '~/GIS_RS/CROP/percentile_ws'

# ---------------------------------------------------------------------------
# 3.  Diccionario de argumentos (TODOS los admitidos por la API)
# ---------------------------------------------------------------------------
args_perc = {
    # ——————————————————  OBLIGATORIOS  ——————————————————
    'workspace_dir': workspace_perc,
    'results_suffix': 'pct_base',                   # se añade a cada output

    # Raster de uso/cobertura agrícola (códigos enteros; p. ej. 1=Maíz, 2=Arroz…)
    'landcover_raster_path': os.path.join(workspace_perc, 'lulc_cultivos_2020.tif'),

    # Tabla CSV que mapea código LULC → ‘crop_name’
    #   columnas mínimas: lucode, crop_name
    'landcover_to_crop_table_path': os.path.join(
        workspace_perc, 'lucode_to_crop.csv'),

    # Raster de **bins climáticos** (enteros 1–5) provisto por IFPRI
    'climate_bin_raster_path': os.path.join(
        workspace_perc, 'climate_bins_IFPRI.tif'),

    # Ruta al directorio ‘model_data’ que viene con InVEST (contiene
    # archivos .nutrient_table.csv y .yield_table.csv)
    # – Si dejas '', InVEST intentará localizarlo automáticamente.
    'model_data_path': '',

    # ——————————————————  OPCIONALES  ——————————————————
    # Polígonos de agregación (p. ej. distritos o fincas) para resumen
    'aggregate_polygon_path': '',

    # Paralelización
    'n_workers': -1,           # −1 = todos los núcleos
}

# ---------------------------------------------------------------------------
# 4.  Ejecutar el modelo
# ---------------------------------------------------------------------------
cpp.execute(args_perc)

"""
SALIDAS clave
─────────────
<workspace>/output/
  • yield_map_<crop>_<suffix>.tif  …… t ha⁻¹ por píxel para cada cultivo
  • nutrient_maps_*.tif           …… kcal, proteína, etc. por píxel
  • pixel_yield_table_<suffix>.csv…… resumen por cultivo
  • agg_yield_table_<suffix>.csv  …… resumido por polígono (si se usó)
  • report_<suffix>.html          …… informe interactivo
"""


# ===========================================================================
# PARTE B · Regression
# ===========================================================================
"""
Este enfoque **regresión** requiere variables climáticas y de manejo; útil
para analizar escenarios de insumos (fertilizante, irrigación).
"""

from natcap.invest import crop_production_regression as cpr

workspace_reg = '~/GIS_RS/CROP/regression_ws'

args_reg = {
    # ————————————————  OBLIGATORIOS  ————————————————
    'workspace_dir': workspace_reg,
    'results_suffix': 'reg_base',

    # Mismos dos insumos que el modelo Percentile
    'landcover_raster_path': os.path.join(workspace_reg, 'lulc_cultivos_2020.tif'),
    'landcover_to_crop_table_path': os.path.join(
        workspace_reg, 'lucode_to_crop.csv'),

    # Variables predictoras (rasters, una banda por variable)
    'climate_variables_table_path': os.path.join(
        workspace_reg, 'predictor_rasters.csv'),
    #   predictor_rasters.csv — columnas mínimas:
    #       varname, path
    #       (ej. ppt_mean, ~/CROP/regression_ws/ppt_mean.tif)

    # Tabla de **coeficientes de regresión** ya calibrada
    'regression_table_path': os.path.join(
        workspace_reg, 'regression_coefficients.csv'),
    #   columnas: crop_name, intercept, beta_ppt_mean, beta_temp_mean, …

    # ————————————————  OPCIONALES  ————————————————
    # Escenario de manejo (fertilizante/riego) — define 0/1 por píxel
    'management_scenario_path': '',  # raster con valores 0 (no) / 1 (sí)

    # Polígonos para agregar resultados
    'aggregate_polygon_path': '',

    'n_workers': -1,
}

cpr.execute(args_reg)

"""
SALIDAS clave (Regresión)
———————————
  • yield_reg_<crop>_<sufijo>.tif …… t ha⁻¹ estimados bajo el set de predictores
  • scenario_yield_<crop>.tif      …… (si se usó manejo) diferencia escenario
  • agg_reg_results_<sufijo>.csv   …… resúmenes por polígono
  • report_<sufijo>.html           …… informe interactivo
"""

# =============================================================================
#                GUIA RÁPIDA DE INSUMOS PRINCIPALES
# =============================================================================
"""
1. landcover_raster_path
   Raster categórico con clases agrícolas.  Solo se procesan los códigos
   listados en lucode_to_crop.csv; todo lo demás se ignora (NODATA).

2. lucode_to_crop.csv
   Mapear `lucode`  →  `crop_name`
   El `crop_name` debe coincidir EXACTAMENTE con los nombres admitidos en
   los archivos de datos del modelo (maize, rice, wheat, soybean, etc.).

3. climate_bin_raster_path  (Percentile)
   El raster de bins climáticos globales (1-5) se distribuye con InVEST en
   <invest_data>/climate_bins/<archivos.tif>.  Recórtalo a tu AOI si es muy
   grande para acelerar el cálculo.

4. model_data_path  (Percentile)
   Directorio «model_data/» de InVEST:  
      ├── crop_yield_nutrient_table.csv  
      └── ...  
   Si mantienes la instalación estándar, deja la cadena vacía para que
   InVEST lo localice solo; si copiaste los archivos, indica la ruta.

5. climate_variables_table_path  (Regresión)
   Tabla con **rutas absolutas** a rasters predictivos (ppt, temp, etc.).
   Cada raster debe tener la misma resolución, proyección y extensión que
   el LULC.

6. regression_coefficients.csv
   Coefs β calibrados por cultivo.  Puedes usar los de la guía oficial o
   recalibrar con datos locales (FAOSTAT, MAG/INEC, etc.).

7. management_scenario_path (Regresión, opcional)
   Raster binario (0/1) para simular la adopción de insumo extra
   (fertilizante, riego).  Si se omite, el modelo solo predice la situación
   base.

8. aggregate_polygon_path
   Shapefile o GeoPackage con polígonos (pueden ser microcuencas, cantones,
   fincas).  Los resultados se agregan y se exporta un CSV.

Tips
────
• Para **escenarios múltiples** (cambio de cultivo, clima o manejo) duplica
  el script, cambia `results_suffix` y los insumos pertinentes y vuelve a
  ejecutar.  
• Revisa siempre el reporte HTML: muestra mapas, tablas resumen y alerta
  sobre clases o variables faltantes.

Con esto tienes un flujo homogéneo con los otros módulos (SDR, UFRM, CSS,
AWY, SWY) para integrar el componente **productividad agrícola** en tu
análisis ecosistémico.
