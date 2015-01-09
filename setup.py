from setuptools import setup, find_packages

setup(name='timeme',
      version='0.1',
      description='Library for timing your program in a separate thread.',
      author='Filip Sufitchi',
      author_email='fsufitchi@gmail.com',
      packages=find_packages('src'),
      package_dir={'':'src'},
      install_requires=[''],
      entry_points = {
        }
     )
