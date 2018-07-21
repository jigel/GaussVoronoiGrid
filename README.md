# Gauss Voronoi Grid

Dependencies: numpy, scipy, basemap (1.1.0), h5py, pandas, pyproj, pillow. Run below to install after cloning the repository:

```
conda install numpy scipy basemap h5py pandas pyproj pillow
```
If basemap 1.1.0 is not installed automatically, run:

```
conda install --channel "conda-forge" basemap
```

This code can be used to create Gaussian Grids with various input arguments, such as the minimum and maximum grid point distance, the size of the area of interest, the steepness of the decrease of gridpoint density, and the center of the dense area. Additionally, the voronoi cell surface areas for the grids can be calculated. If wanted, all gridpoints and voronoi cell areas on land can be removed. All this is then saved in .h5 files in the folder /GaussVoronoiGrid/grids.

At the moment, all this is done in the Jupyter Notebook 'GaussVoronoiGrid.ipynb'. The option of running it without Jupyter Notebooks will soon be added. 

For the Voronoi cell surface areas the code from the following sources was implemented:
https://github.com/tylerjereddy/spherical-SA-docker-demo/blob/master/docker_build/demonstration.py
https://github.com/MITHaystack/scikit-discovery/blob/master/skdiscovery/visualization/spherical_voronoi.py#L40

## Gaussian Grid Example

Below is an example of a Gaussian Grid. 

![Gaussian Grid](docs/GaussianGrid_Example_1.png)

As mentioned, all gridpoints on land can be removed.

![Gaussian Grid](docs/GaussianGrid_Example_3.png)

## Voronoi Cells

The Voronoi cells can also be plotted, although this is not recommended as it increase the computation time by a lot. 

![Gaussian Grid](docs/GaussianGrid_Example_2.png)

