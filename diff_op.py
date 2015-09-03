from pylab import *
from numpy import diff as diff
from numpy import gradient as gradient

from global_variables import *

def d_rho(F):
	Fp = zeros((F.__len__()))	
	# Fp[0] = -(Decimal(25.)*F[0]-Decimal(48.)*F[1]+Decimal(36.)*F[2]-Decimal(16.)*F[3]+Decimal(3.)*F[4])/Decimal(12.);
	# Fp[1] = -(Decimal(3.)*F[0]+Decimal(10.)*F[1]-Decimal(18.)*F[2]+Decimal(6.)*F[3]-F[4])/Decimal(12.);
	# Fp[-1]=	(Decimal(25.)*F[-1]-Decimal(48.)*F[-2]+Decimal(36.)*F[-3]-Decimal(16.)*F[-4]+Decimal(3.)*F[-5])/Decimal(12.)
	# Fp[-2] = (Decimal(3.)*F[-1]+Decimal(10.)*F[-2]-Decimal(18.)*F[-3]+Decimal(6.)*F[-4]-F[-5])/Decimal(12.)
	# Fp[2:-2] = Decimal(1./12)*F[0:-4]-Decimal(2./3)*F[1:-3]+Decimal(2./3)*F[3:-1]-Decimal(1./12)*F[4:]
	
	# Fp[2:-2] = 1./12*F[0:-4]-2./3*F[1:-3]+2./3*F[3:-1]-1./12*F[4:]
	# Fp[0] = -(25.*F[0]-48.*F[1]+36.*F[2]-16.*F[3]+3.*F[4])/12.
	# Fp[1] = -(3.*F[0]+10.*F[1]-18.*F[2]+6.*F[3]-F[4])/12.
	# Fp[-1]=	(25.*F[-1]-48.*F[-2]+36.*F[-3]-16.*F[-4]+3.*F[-5])/12.
	# Fp[-2] = (3.*F[-1]+10.*F[-2]-18.*F[-3]+6.*F[-4]-F[-5])/12.
	

	# Fp[0] = -49./20.*F[0]+6.*F[1]-15./2.*F[2]+20./3.*F[3]-15./4*F[4]+6./5.*F[5]-1./6.*F[6]
	# Fp[1] = -49./20.*F[1]+6.*F[2]-15./2.*F[3]+20./3.*F[4]-15./4*F[5]+6./5.*F[6]-1./6.*F[7]
	# Fp[1] = -(3.*F[0]+10.*F[1]-18.*F[2]+6.*F[3]-F[4])/12.
	# Fp[-1]=	-(-49./20.*F[-1]+6.*F[-2]-15./2.*F[-3]+20./3.*F[-4]-15./4*F[-5]+6./5.*F[-6]-1./6.*F[-7])
	# Fp[-2] = (3.*F[-1]+10.*F[-2]-18.*F[-3]+6.*F[-4]-F[-5])/12.
	# Fp[-2]=	-(-49./20.*F[-2]+6.*F[-3]-15./2.*F[-4]+20./3.*F[-5]-15./4*F[-6]+6./5.*F[-7]-1./6.*F[-8])
	

	# return Fp/drho
	return gradient(F)/drho
	
def d2_rho(F):
	# Fpp = zeros((F.__len__()))	
	# Fpp[0] = 35./12*F[0]-26./3*F[1]+19./2*F[2]-14./3*F[3]+11./12*F[4]
	# Fpp[1] = 11./12*F[0]-5./3*F[1]+F[2]/2.+F[3]/3.-F[4]/12.
	# Fpp[-1] = 11./12*F[-5]-14./3*F[-4] +19./2*F[-3] -26./3*F[-2]+ 35./12*F[-1]
	# Fpp[-2] = -F[-5]/12. + 1./3*F[-4]+F[-3]/2. -5./3*F[-2] + 11./12*F[-1]
	# Fpp[2:-2] = -F[0:-4]/12.+4./3*F[1:-3]-5./2*F[2:-2]+4./3*F[3:-1]-1./12*F[4:]
	# return Fpp/drho**2
	return gradient(gradient(F))/drho**2
	
# double discrete_deriv_2(double *f, double delta, int i_min, int i_max, int k)
# {
  # double D=DSQR(delta);
  # if (i_max-i_min < 4) nrerror("i_max-i_min<4 in function discrete_deriv_2");
  # if (k >= i_min+2 && k <= i_max-2)
    # return (-(f[k+2]+f[k-2])+16.*(f[k+1]+f[k-1])-30.*f[k])/(12.*D);
  # else if (k == i_max-1)
    # return (11.*f[k+1]-20.*f[k]+6.*f[k-1]+4.*f[k-2]-f[k-3])/(12.*D);
  # else if (k == i_max)
    # return (35.*f[k]-104.*f[k-1]+114.*f[k-2]-56.*f[k-3]+11.*f[k-4])/(12.*D);
  # else if (k == i_min)
    # return (35.*f[k]-104.*f[k+1]+114.*f[k+2]-56.*f[k+3]+11.*f[k+4])/(12.*D);
  # else if (k == i_min+1)
    # return (11.*f[k-1]-20.*f[k]+6.*f[k+1]+4.*f[k+2]-f[k+3])/(12.*D);
  # else nrerror("function discrete_deriv_2: k not in [i_min,i_max]");
# }
