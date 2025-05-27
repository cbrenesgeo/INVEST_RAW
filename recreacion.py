# -*- coding: utf-8 -*-
"""
InVEST | Visitation: Recreation & Tourism (VoRT)
===============================================
► Script‐plantilla que ejecuta el modelo vía su **cliente Python**  
  (`natcap.invest.recreation.recmodel_client`).  
► Incluye **TODOS** los argumentos reconocidos por la API (versión ≥ 3.15).  
► Modifica las rutas, años, servidor y opciones según tu proyecto.

Requisitos previos
------------------
* InVEST instalado como paquete Python (`pip install natcap.invest`).
* Conexión a internet: el cliente llama a un servidor remoto que descarga y
  procesa las fotografías georreferenciadas de Flickr/Twitter.
"""

from natcap.invest.recreation import recmodel_client
import os

# Carpeta donde se guardarán salidas («output») e intermedios («intermediate»)
workspace = '~/GIS_RS/VoRT/workspace'

# ---------------------------------------------------------------------------
# 1) Argumentos **obligatorios**
# ---------------------------------------------------------------------------
args = {
    'workspace_dir': workspace,
    'aoi_path': os.path.join(workspace, 'aoi_recreacion.shp'),  # polígono/s AOI
    'hostname': 'services.naturalcapitalproject.org',  # servidor oficial NatCap
    'port': 56789,                                     # puerto (default=56789)
    'start_year': '2015',   # año inicial (inclusive) para filtrar fotos
    'end_year':   '2024',   # año final (inclusive)
}

# ---------------------------------------------------------------------------
# 2) Opciones de **grillado** del AOI (útil para hotspots de alta resolución)
# ---------------------------------------------------------------------------
args.update({
    'grid_aoi': False,        # True → genera una cuadrícula o teselado hexagonal
    'grid_type': 'hexagon',   # 'square' o 'hexagon' (requerido si grid_aoi=True)
    'cell_size': 5000,        # tamaño de celda en m (requerido si grid_aoi=True)
})

# ---------------------------------------------------------------------------
# 3) Opciones de **regresión** (para estimar visitas con predictores)
# ---------------------------------------------------------------------------
args.update({
    'compute_regression': False,  # True → necesita tabla de predictores
    'predictor_table_path': os.path.join(workspace, 'predictors.csv'),
    #  Tabla CSV con columnas:
    #    id,path,type   (id ≤ 10 car.; ver documentación para tipos)
    'scenario_predictor_table_path': os.path.join(
        workspace, 'predictors_escenario.csv'),        # opcional: escenario futuro
})

# ---------------------------------------------------------------------------
# 4) Miscelánea
# ---------------------------------------------------------------------------
args.update({
    'results_suffix': 'escenario_base',  # se anexa a todos los outputs
    'n_workers': -1,                     # –1 → todos los núcleos disponibles
})

# ---------------------------------------------------------------------------
# Lanzar el modelo
# ---------------------------------------------------------------------------
recmodel_client.execute(args)
# ---------------------------------------------------------------------------


# ===========================================================================
# Notas prácticas y explicación de cada parámetro
# ===========================================================================

#  • workspace_dir ........ Carpeta raíz de trabajo (rutas absolutas o «~/…»).
#  • aoi_path ............. Vector poligonal (proyectado en metros) que define
#                           la zona de análisis; puede contener varios polígonos.
#  • hostname, port ....... Dirección del servidor que aloja la base global de
#                           fotos + motor de regresión.  Usar el oficial de
#                           NatCap o tu propio servidor si lo has desplegado.
#  • start_year, end_year . Ventana temporal (YYYY).  La densidad de “Photo
#                           User Days” (PUD) se filtra dentro de este rango.
#  • grid_aoi ............. Si True, el vector del AOI se discretiza en una
#                           malla para obtener valores uniformes por celda
#                           (ideal para mapas de “hotspots”).
#  • grid_type ............ 'square' o 'hexagon'.  Requerido cuando grid_aoi=True.
#  • cell_size ............ Lado (cuadrado) o ancho (hexágono) en metros.
#  • compute_regression ... Activa el modo de regresión lineal que vincula
#                           PUD con variables explicativas.  Necesita:
#                               ▸ predictor_table_path  (obligatorio)
#                               ▸ scenario_predictor_table_path (opcional)
#  • predictor_table_path .. CSV con columnas:
#       id .......... ≤10 caracteres, único
#       path ........ ruta absoluta/relativa a raster o vector
#       type ........ ver listado de la documentación (‘raster_mean’, ‘point_count’,
#                     ‘polygon_percent_coverage’, etc.).
#  • scenario_predictor_table_path
#      Tabla idéntica a la de predictores, pero con datasets alterados para
#      representar un escenario futuro (cambios de uso del suelo, etc.).
#  • results_suffix ...... Texto para diferenciar escenarios (“_escenarioX”).
#  • n_workers ........... Procesamiento paralelo (–1 = todos los cores).
#
# ---------------------------------------------------------------------------
# Principales SALIDAS (en <workspace>/output)
# ---------------------------------------------------------------------------
#  • pud_results_<sufijo>.shp ... Visitas modeladas (Photo User Days) por polígono
#     ▸ PUD_YR_AVG ............. Promedio anual  PUD
#     ▸ VISITATION ............. Estimación de visitas (si hay regresión)
#  • monthly_table_<sufijo>.csv . PUD mensual por polígono o celda
#  • regression_coefficients.csv  Coeficientes β de la regresión (si procede)
#  • scenario_results_<sufijo>.shp  Impacto de los cambios descritos en
#                                   scenario_predictor_table (solo si se usa)
#
# Consulta la guía oficial para detalles finos de formato y post-procesamiento.:contentReference[oaicite:0]{index=0}
::contentReference[oaicite:1]{index=1}
