from setuptools import (
    find_packages,
    setup
)

INSTALL_REQUIRES = (
    'bottle',
    'spotibar'
)

setup(
    name='home-rfid',
    version='0.0.1',
    python_requires='>=3.6',
    description='A simple home automation RFID controller.',
    author='Conor Flynn',
    url='https://github.com/conor-f/home-rfid',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=INSTALL_REQUIRES,
    entry_points={
        'console_scripts': [
            'backend = home_rfid.bin.backend:main',
            'rfid_reader = home_rfid.bin.rfid_reader:main'
        ]
    }
)
