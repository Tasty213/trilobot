from setuptools import find_packages, setup

package_name = 'trilobot_core'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    package_data={'': ['py.typed']},
    install_requires=['setuptools', 'trilobot'],
    zip_safe=True,
    maintainer='George Sykes',
    maintainer_email='gsykes537@gmail.com',
    description='TODO: Package description',
    license='MIT',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'driver_node = trilobot_core.driver_node:main'
        ],
    },
)
