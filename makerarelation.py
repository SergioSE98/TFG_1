import pyfits as pf
import numpy as np

data_ = pf.open('fits\exptime\EROs_withexptime.fits')[1].data
tag = 'EROs'
#maskfile = 'Y3Goldv2_lssred_April2018_MASK4096.fits'
maskfile = 'fits\exptime\des_area_healsparse_exptime.fits'
exptime = data_['EXPTIME']

print (min(exptime),max(exptime))

bins = np.linspace(10,2935,30)


hist_,bin_edges = np.histogram(exptime,bins=bins)
print (len(hist_))
print (len(bin_edges))

center_bins = []
for i in range(len(bin_edges)-1):
	center_bins.append((bin_edges[i]+bin_edges[i+1])/2.)

np.savetxt('bindata_%s' % tag,np.array([center_bins,hist_]).transpose())


mask_ = pf.open(maskfile)[1].data
masksignal = mask_['T']




area = 0.7376604303613771 #arcmin^2
print ('area ',area)

Mhist_, be = np.histogram(masksignal, bins=bins)
cc,ff,FF,EE = [],[],[],[]


meandens = np.sum(hist_)/(np.sum(Mhist_)*area)
dens = hist_/(Mhist_*area)
meameandens = np.mean(dens-meandens)
error = np.sqrt(np.power(Mhist_*meameandens,2)/(Mhist_*(Mhist_-1.)))

for M,D,C,S,E in zip(Mhist_,hist_,center_bins,masksignal,error):
	if M != 0.:
		#print M,D
		cc.append(C)
		ff.append(float(D)/(float(M)*S*area))
		FF.append(float(D)/(float(M)*area))
		EE.append(E)
print (EE)
import matplotlib.pyplot as plt
#plt.errorbar(np.array(cc),np.array(ff),yerr=EE,label='Frac',fmt='--o')
plt.errorbar(np.array(cc),np.array(FF),yerr=EE,label='Unity',fmt='--o')
plt.xlabel('EXPTIME')
plt.ylabel('Density [arcmin square]')
plt.legend()
plt.savefig('exptime_eros_density.png' .format(tag))
