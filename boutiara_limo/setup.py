import os
from glob import glob
from setuptools import setup

package_name = 'boutiara_limo'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        
        (os.path.join('share', package_name, 'launch'),
         glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Boutiara',
    maintainer_email='abdelhak.boutiara@etu.uca.fr',
    description='Limo package',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'joy_to_twist = boutiara_limo.joy_to_twist:main',
            'safety_node = boutiara_limo.safety_node:main',

        ],
    },
)
