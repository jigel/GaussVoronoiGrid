import numpy as np
import pandas as pd
from GaussVoronoiGrid.borrowed_functions.voronoi_polygons import getVoronoiCollection
from GaussVoronoiGrid.borrowed_functions.voronoi_surface_area import calculate_surface_area_of_a_spherical_Voronoi_polygon
from GaussVoronoiGrid.borrowed_functions.voronoi_polygons import xyzToSpherical
import warnings
warnings.filterwarnings("ignore")


def get_voronoi_surface_area(grd, voronoi_plot = False):
    """
    Computes the spherical voronoi cells and calculates their surface areas.
    Input: grid with longitude and latitude 
    Output: grid (since the order might change) and voronoi surface areas corresponding to each point
    
    Functions from:
        https://github.com/tylerjereddy/spherical-SA-docker-demo/blob/master/docker_build/demonstration.py
        https://github.com/MITHaystack/scikit-discovery/blob/master/skdiscovery/visualization/spherical_voronoi.py#L40
    """
    # convert grid into panda dataframe
    gridpd = {'lat': grd[1], 'lon': grd[0]}
    grid_data = pd.DataFrame(data=gridpd)
    
    # Calculate the vertices for the voronoi cells
    if voronoi_plot:
        collection,voronoi,patch_index = getVoronoiCollection(data=grid_data,lat_name='lat',lon_name='lon',voronoi_plot = voronoi_plot, full_sphere=True)
    
        from matplotlib import colors
        import scipy
        import matplotlib.pyplot as plt
        #from mpl_toolkits.mplot3d import proj3d
        from mpl_toolkits.mplot3d.art3d import Poly3DCollection
        
        fig = plt.figure(figsize=(25,25))
        ax = fig.add_subplot(111, projection='3d')
        #ax.scatter(voronoi.vertices[:,0], voronoi.vertices[:,1], voronoi.vertices[:,2],s=5, color='b')
        ax.scatter(voronoi.points[:,0], voronoi.points[:,1], voronoi.points[:,2],s=5, color='k')
        for n in range(0, len(voronoi.regions)):
            region = voronoi.regions[n]
            #ax.scatter(points[n, 0], points[n, 1], points[n, 2], c='b')
            random_color = colors.rgb2hex(scipy.rand(3))
            polygon = Poly3DCollection([voronoi.vertices[region]], alpha=1.0)
            polygon.set_color(random_color)
            ax.add_collection3d(polygon)
        plt.show()
        
    else:
       voronoi = getVoronoiCollection(data=grid_data,lat_name='lat',lon_name='lon',voronoi_plot = voronoi_plot, full_sphere=True)

    # Calculate the surface area for each voronoi cell
    voronoi_lat = []
    voronoi_lon = []
    voronoi_area = []
    
    for i in range(0,np.size(voronoi.points,0)):
        P_cart = xyzToSpherical(x=voronoi.points[i,0],y=voronoi.points[i,1],z=voronoi.points[i,2])
        voronoi_lat.append(P_cart[0])
        voronoi_lon.append(P_cart[1])
        vert_points = voronoi.vertices[voronoi.regions[i]]
        area = calculate_surface_area_of_a_spherical_Voronoi_polygon(vert_points,1)
        voronoi_area.append(area)
        if i%1000 == 0:
            print('%g of %g voronoi cell surface areas calculated.' %(i,np.size(voronoi.points,0)),flush=True)
        
    # Reassign grd so that everything is in the right order
    grd = np.asarray([voronoi_lon,voronoi_lat])
    voronoi_area = np.asarray(voronoi_area)
    print('All voronoi cell surface areas calculated.')
    
    return grd, voronoi_area