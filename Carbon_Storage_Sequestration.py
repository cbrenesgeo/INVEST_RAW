# -*- coding: utf-8 -*-
"""
Ejecución del modelo Carbon Storage & Sequestration (CSS) de InVEST
-------------------------------------------------------------------
► Ajusta las rutas y valores según tu proyecto.
► Versiones InVEST ≥ 3.10 usan exactamente la misma interfaz “args”.
"""

from natcap.invest import carbon                           # punto de entrada del modelo
import os

# Carpeta donde el modelo escribirá salidas y temporales
workspace = '~/GIS_RS/CARBON/input_data_carbon'

# ------------------------------------------------------------------------------
# Diccionario de argumentos (TODOS los que reconoce el modelo)
# ------------------------------------------------------------------------------
args = {
    # -------------------------------------------------------------------------
    # Parámetros básicos (OBLIGATORIOS siempre)
    # -------------------------------------------------------------------------
    'workspace_dir': workspace,
    'results_suffix': 'escenario_base',        # se añade a cada archivo de salida
    'lulc_cur_path': os.path.join(workspace, 'lulc_2020.tif'),          # mapa actual
    'carbon_pools_path': os.path.join(workspace, 'carbon_pools.csv'),    # densidades C
    'lulc_cur_year': 2020,                     # año del LULC actual (para valoración)

    # -------------------------------------------------------------------------
    # Cálculo de secuestro entre presente y futuro (OPCIONAL)
    # -------------------------------------------------------------------------
    'calc_sequestration': True,                # ← pon en False si sólo quieres stocks
    'lulc_fut_path': os.path.join(workspace, 'lulc_2035.tif'),
    'lulc_fut_year': 2035,                     # año del escenario futuro

    # -------------------------------------------------------------------------
    # Análisis REDD (solo si tienes un tercer escenario “evitado”)
    # -------------------------------------------------------------------------
    'do_redd': False,                          # activa si modelas un escenario REDD
    'lulc_redd_path': '',                      # raster REDD (si do_redd = True)

    # -------------------------------------------------------------------------
    # Valorización económica del carbono (totalmente opcional)
    # -------------------------------------------------------------------------
    'do_valuation': True,                      # cambia a False si no necesitas $$
    'price_per_metric_ton_of_c': 42.0,         # USD t-1 C presente
    'discount_rate': 0.03,                    # tasa de descuento anual (3 %)
    'rate_change': 0.02,                      # % de incremento anual del precio

    # -------------------------------------------------------------------------
    # Configuración de cómputo
    # -------------------------------------------------------------------------
    'n_workers': -1                            # −1 = usar todos los núcleos disponibles
}

# ------------------------------------------------------------------------------
# Lanzar el modelo
# ------------------------------------------------------------------------------
carbon.execute(args)
