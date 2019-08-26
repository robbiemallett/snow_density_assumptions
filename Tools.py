import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset
from mpl_toolkits.basemap import Basemap
import pickle
import netCDF4

def getOSISAF(month, year, variable):       #This function returns a month's variable from the netcdf
    if variable == 'snow':
        data = Dataset('snowdata.nc',"r")
        return(data)
    else:
        folder = 'Monthly_means/'

        data=Dataset(folder+year+month+'monmean.nc',"r")

        var=np.array(data[variable])
        return(var)
    
def getEASE(month, year, variable):       #This function returns a month's variable from the netcdf
    
    if year == "2010" and month in ["01", "02", "03", "04"]:
        var = None
    else:
        data_dir ='/home/robbie/Dropbox/Landy_SIT/'
        
        path = data_dir+'ubristol_cryosat2_seaicethickness_nh25km_'+year+'_'+month+'_v1.nc'
            
        data=Dataset(path,"r")
        
        var=np.array(data.variables[variable])
    return(var)

def plot(month, year, variable, 
               extdata=False, 
               save=False,
               maxscale=0, 
               minscale=0, 
               show=True, 
               labelname="",
               stipple=False,
               savefile="",
               dpi=300, 
               scheme='RdBu_r',
               colorbar=False,
               grid = "EASE348"):

    plt.rcParams['figure.dpi'] = dpi
    
    if grid == "EASE":
        lon=getEASE("01", "2015", 'Longitude')
        lat=getEASE("01", "2015", 'Latitude')
    elif grid == "OSISAF":
        lon=getOSISAF("01", "2015", 'lon')
        lat=getOSISAF("01", "2015", 'lat')
    
    if extdata == True:
        var=variable
    else:
        var=getEASE(month, year, variable)

    #PLOTTER

    if var is None:
        print("Month " + month + " year " + year + " data can't be plotted")
    else:
        fig = plt.figure(figsize=(5, 4))
        m = Basemap(projection='npstere',boundinglat=55,lon_0=360,resolution='l')
        if stipple == True:
            data=Dataset('snowdata.nc',"r")
            myi_probability = np.array(data['MYI_prob'])
            m.contour(lon, lat, myi_probability[int(month)], 1, colors='k', linestyles='-',linewidths=0.5,latlon=True)

        m.drawcoastlines(linewidth=0.5)
        if maxscale == 0:
            m.pcolormesh(lon, lat, var, latlon=True,cmap=scheme)
        else:
            m.pcolormesh(lon, lat, var, latlon=True,cmap=scheme, vmax=maxscale, vmin=minscale)
        if colorbar == True:
            plt.colorbar(label=labelname)
            xannotationcoord = 0.09
        elif colorbar == False:
            xannotationcoord = 0.14
        plt.annotate("Year: "+year+"\nMonth: "+month, xycoords="figure fraction",
                     xy=(10, 10),xytext=(xannotationcoord, 0.09), fontsize=14)
        if save == True:
            plt.savefig(savefile,
                        dpi=dpi, bbox_inches="tight")
        if show == True:
            plt.show()
