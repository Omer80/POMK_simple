import numpy
def laplacian(var, dh2):
    """ (1D array, dx^2) -> laplacian(1D array)
    periodic_laplacian_1D_4th_order
    Implementing the 4th order 1D laplacian with periodic condition
    """
    lap = numpy.zeros_like(var)
    lap[1:]    = (4.0/3.0)*var[:-1]
    lap[0]     = (4.0/3.0)*var[1]
    lap[:-1]  += (4.0/3.0)*var[1:]
    lap[-1]   += (4.0/3.0)*var[0]
    lap       += (-5.0/2.0)*var
    
    lap[2:]   += (-1.0/12.0)*var[:-2]
    lap[:2]   += (-1.0/12.0)*var[-2:]
    lap[:-2]  += (-1.0/12.0)*var[2:]
    lap[-2:]  += (-1.0/12.0)*var[:2]
    
    return lap / dh2
