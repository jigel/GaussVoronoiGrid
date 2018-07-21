import cartopy.io.shapereader as shpreader
import shapely.geometry as sgeom
from shapely.ops import unary_union
from shapely.prepared import prep

land_shp_fname = shpreader.natural_earth(resolution='50m', category='physical', name='land')
land_geom = unary_union(list(shpreader.Reader(land_shp_fname).geometries()))
land = prep(land_geom)

def is_land(x, y):
    """
    Copied from: https://stackoverflow.com/questions/47894513/checking-if-a-geocoordinate-point-is-land-or-ocean-with-cartopy
    Input: longitude, latitude
    Returns:  True if point is on land
    """

    return land.contains(sgeom.Point(x, y))