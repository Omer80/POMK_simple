from derivatives import laplacian

def dbdt(b,w,p,m,d,dx2):
	""" db/dt of Modified Klausmeier """
	return w*b**2 - m*b + laplacian(b,dx2)
	
def dwdt(b,w,p,m,d,dx2):
	""" dw/dt of Modified Klausmeier """
	return p - w - w*b**2 + d*laplacian(b,dx2)
