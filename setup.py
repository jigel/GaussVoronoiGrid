from setuptools import setup, find_packages

setup(
    name = 'Gauss-Voronoi Grid',
    version = '0.0.0a0',
    description = 'Package to create a Gaussian Grid and compute the Voronoi cell surface areas',
    #long_description =
    # url = 
    author = 'J.Igel, L.Ermert, A.Fichtner',
    author_email  = 'jigel@student.ethz.ch',
    license = 'MIT',
    # license
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Topic :: Seismology',
        'Programming Language :: Python :: 3',
    ],
    keywords = 'Gauss Voronoi Grid',
    packages = find_packages(),
    #package_data = ,
    install_requires = [
        "numpy",
        "scipy",
        "cartopy",
        "pandas",
        "h5py",],
)

