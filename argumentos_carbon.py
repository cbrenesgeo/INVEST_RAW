##Help on function execute in module natcap.invest.carbon:

execute(args)
    Carbon.
    
    ##Calculate the amount of carbon stocks given a landscape, or the difference
    ##due to some change, and calculate economic valuation on those scenarios.
    
    The model can operate on a single scenario or a combined baseline and
    alternate scenario.
    
    Args:
        args['workspace_dir'] (string): a path to the directory that will
            write output and other temporary files during calculation.
        args['results_suffix'] (string): appended to any output file name.
        args['lulc_bas_path'] (string): a path to a raster representing the
            baseline carbon stocks.
        args['calc_sequestration'] (bool): if true, sequestration should
            be calculated and 'lulc_alt_path' should be defined.
        args['lulc_alt_path'] (string): a path to a raster representing alternate
            landcover scenario.  Optional, but if present and well defined
            will trigger a sequestration calculation.
        args['carbon_pools_path'] (string): path to CSV or that indexes carbon
            storage density to lulc codes. (required if 'do_uncertainty' is
            false)
        args['lulc_bas_year'] (int/string): an integer representing the year
            of `args['lulc_bas_path']` used if `args['do_valuation']`
            is True.
        args['lulc_alt_year'](int/string): an integer representing the year
            of `args['lulc_alt_path']` used in valuation if it exists.
            Required if  `args['do_valuation']` is True and
            `args['lulc_alt_path']` is present and well defined.
        args['do_valuation'] (bool): if true then run the valuation model on
            available outputs. Calculate NPV for an alternate scenario and
            report in final HTML document.
        args['price_per_metric_ton_of_c'] (float): Is the present value of
            carbon per metric ton. Used if `args['do_valuation']` is present
            and True.
        args['discount_rate'] (float): Discount rate used if NPV calculations
            are required.  Used if `args['do_valuation']` is  present and
            True.
        args['rate_change'] (float): Annual rate of change in price of carbon
            as a percentage.  Used if `args['do_valuation']` is  present and
            True.
        args['n_workers'] (int): (optional) The number of worker processes to
            use for processing this model.  If omitted, computation will take
            place in the current process.
    
    Returns:
        None.

