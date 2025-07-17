Help on function execute in module natcap.invest.ndr.ndr:

execute(args)
    Nutrient Delivery Ratio.
    
    Args:
        args['workspace_dir'] (string):  path to current workspace
        args['dem_path'] (string): path to digital elevation map raster
        args['lulc_path'] (string): a path to landcover map raster
        args['runoff_proxy_path'] (string): a path to a runoff proxy raster
        args['watersheds_path'] (string): path to the watershed shapefile
        args['biophysical_table_path'] (string): path to csv table on disk
            containing nutrient retention values.
    
            For each nutrient type [t] in args['calc_[t]'] that is true, must
            contain the following headers:
    
            'load_[t]', 'eff_[t]', 'crit_len_[t]'
    
            If args['calc_n'] is True, must also contain the header
            'proportion_subsurface_n' field.
    
        args['calc_p'] (boolean): if True, phosphorus is modeled,
            additionally if True then biophysical table must have p fields in
            them
        args['calc_n'] (boolean): if True nitrogen will be modeled,
            additionally biophysical table must have n fields in them.
        args['results_suffix'] (string): (optional) a text field to append to
            all output files
        args['threshold_flow_accumulation']: a number representing the flow
            accumulation in terms of upslope pixels.
        args['k_param'] (number): The Borselli k parameter. This is a
            calibration parameter that determines the shape of the
            relationship between hydrologic connectivity.
        args['runoff_proxy_av'] (number): (optional) The average runoff proxy.
            Used to calculate the runoff proxy index. If not specified,
            it will be automatically calculated.
        args['subsurface_critical_length_n'] (number): The distance (traveled
            subsurface and downslope) after which it is assumed that soil
            retains nutrient at its maximum capacity, given in meters. If
            dissolved nutrients travel a distance smaller than Subsurface
            Critical Length, the retention efficiency will be lower than the
            Subsurface Maximum Retention Efficiency value defined. Setting this
            value to a distance smaller than the pixel size will result in the
            maximum retention efficiency being reached within one pixel only.
            Required if ``calc_n``.
        args['subsurface_eff_n'] (number): The maximum nutrient retention
            efficiency that can be reached through subsurface flow, a floating
            point value between 0 and 1. This field characterizes the retention
            due to biochemical degradation in soils.  Required if ``calc_n``.
        args['n_workers'] (int): if present, indicates how many worker
            processes should be used in parallel processing. -1 indicates
            single process mode, 0 is single process but non-blocking mode,
            and >= 1 is number of processes.
    
    Returns:
        None
