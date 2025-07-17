Help on function execute in module natcap.invest.annual_water_yield:

execute(args)
    Annual Water Yield: Reservoir Hydropower Production.
    
    Executes the hydropower/annual water yield model
    
    Args:
        args['workspace_dir'] (string): a path to the directory that will write
            output and other temporary files during calculation. (required)
    
        args['lulc_path'] (string): a path to a land use/land cover raster
            whose LULC indexes correspond to indexes in the biophysical table
            input. Used for determining soil retention and other biophysical
            properties of the landscape. (required)
    
        args['depth_to_root_rest_layer_path'] (string): a path to an input
            raster describing the depth of "good" soil before reaching this
            restrictive layer (required)
    
        args['precipitation_path'] (string): a path to an input raster
            describing the average annual precipitation value for each cell
            (mm) (required)
    
        args['pawc_path'] (string): a path to an input raster describing the
            plant available water content value for each cell. Plant Available
            Water Content fraction (PAWC) is the fraction of water that can be
            stored in the soil profile that is available for plants' use.
            PAWC is a fraction from 0 to 1 (required)
    
        args['eto_path'] (string): a path to an input raster describing the
            annual average evapotranspiration value for each cell. Potential
            evapotranspiration is the potential loss of water from soil by
            both evaporation from the soil and transpiration by healthy
            Alfalfa (or grass) if sufficient water is available (mm)
            (required)
    
        args['watersheds_path'] (string): a path to an input shapefile of the
            watersheds of interest as polygons. (required)
    
        args['sub_watersheds_path'] (string): a path to an input shapefile of
            the subwatersheds of interest that are contained in the
            ``args['watersheds_path']`` shape provided as input. (optional)
    
        args['biophysical_table_path'] (string): a path to an input CSV table
            of land use/land cover classes, containing data on biophysical
            coefficients such as root_depth (mm) and Kc, which are required.
            A column with header LULC_veg is also required which should
            have values of 1 or 0, 1 indicating a land cover type of
            vegetation, a 0 indicating non vegetation or wetland, water.
            NOTE: these data are attributes of each LULC class rather than
            attributes of individual cells in the raster map (required)
    
        args['seasonality_constant'] (float): floating point value between
            1 and 30 corresponding to the seasonal distribution of
            precipitation (required)
    
        args['results_suffix'] (string): a string that will be concatenated
            onto the end of file names (optional)
    
        args['demand_table_path'] (string): (optional) if a non-empty string,
            a path to an input CSV
            table of LULC classes, showing consumptive water use for each
            landuse / land-cover type (cubic meters per year) to calculate
            water scarcity.  Required if ``valuation_table_path`` is provided.
    
        args['valuation_table_path'] (string): (optional) if a non-empty
            string, a path to an input CSV table of
            hydropower stations with the following fields to calculate
            valuation: 'ws_id', 'time_span', 'discount', 'efficiency',
            'fraction', 'cost', 'height', 'kw_price'
    
        args['n_workers'] (int): (optional) The number of worker processes to
            use for processing this model.  If omitted, computation will take
            place in the current process.
    
    Returns:
        None

