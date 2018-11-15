### This plots various metrics for the first year atmospheric science practical

import numpy as np
import xarray as xar
import matplotlib.pyplot as plt
import os as os

# Read in the environment variable as the path
path = os.environ['GFDL_DATA']

# Open control data
dataset_control = xar.open_dataset(path + '/frierson1/run0023/atmos_monthly.nc')
dataset_exp = xar.open_dataset(path + '/frierson_rotate_slow/run0023/atmos_monthly.nc')

#dataset['land_mask'].mean('lon').plot()
plt.figure('Zonal Wind Control')
dataset_control['ucomp'].mean('lon')[0,:,:].plot.contourf(cmap = 'hot')

plt.figure('Zonal Wind Experiment')
dataset_exp['ucomp'].mean('lon')[0,:,:].plot.contourf(cmap = 'hot')

ucomp_diff = dataset_control['ucomp'].values - dataset_exp['ucomp'].values
lat =  dataset_control['lat'].values
pfull =  dataset_control['pfull'].values

plt.figure('Zonal Wind Difference')
plt.contourf(lat,pfull,np.mean(ucomp_diff,axis=3)[0,:,:],cmap='bwr')
plt.gca().invert_yaxis()
plt.colorbar()
plt.title('Zonal Wind Difference')
plt.ylabel('Pressure (hPa)')
plt.xlabel('Latitude')




# zonal temperature

plt.figure('Zonal Temperature Control')
dataset_control['temp'].mean('lon')[0,:,:].plot.contourf(cmap = 'hot')

plt.figure('Zonal Temperature Experiment')
dataset_exp['temp'].mean('lon')[0,:,:].plot.contourf(cmap = 'hot')

tcomp_diff = dataset_control['temp'].values - dataset_exp['temp'].values
lat =  dataset_control['lat'].values
pfull =  dataset_control['pfull'].values

plt.figure('Zonal T Difference')
plt.contourf(lat,pfull,np.mean(tcomp_diff,axis=3)[0,:,:],cmap='bwr')
plt.gca().invert_yaxis()
plt.colorbar()
plt.title('Zonal T Difference')
plt.ylabel('Pressure (hPa)')
plt.xlabel('Latitude')



# Meridional wind

plt.figure('Meridional Wind Control')
dataset_control['vcomp'].mean('lon')[0,:,:].plot.contourf(cmap = 'bwr')

plt.figure('Meridional Wind Experiment')
dataset_exp['vcomp'].mean('lon')[0,:,:].plot.contourf(cmap = 'bwr')

vcomp_diff = dataset_control['vcomp'].values - dataset_exp['vcomp'].values
lat =  dataset_control['lat'].values
pfull =  dataset_control['pfull'].values

plt.figure('Meridional Wind Difference')
plt.contourf(lat,pfull,np.mean(vcomp_diff,axis=3)[0,:,:],cmap='bwr')
plt.gca().invert_yaxis()
plt.colorbar()
plt.title('Meridional Wind Difference')
plt.ylabel('Pressure (hPa)')
plt.xlabel('Latitude')


plt.figure('Surface Temperature Control')
dataset_control['t_surf'][0,:,:].plot.contourf(cmap = 'hot')

plt.figure('Surface Temperature Experiment')
dataset_exp['t_surf'][0,:,:].plot.contourf(cmap = 'hot')

t_surf_diff = dataset_control['t_surf'].values - dataset_exp['t_surf'].values
lat =  dataset_control['lat'].values
lon =  dataset_control['lon'].values


plt.figure('Surface Temperature Difference')
plt.contourf(lon,lat,t_surf_diff[0,:,:],cmap='bwr')

plt.colorbar()
plt.title('Surface Temperature Difference')
#plt.ylabel('Pressure (hPa)')
#plt.xlabel('Latitude')

plt.show()

