from setuptools import setup

package_name = 'autonomous_robot'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    install_requires=['setuptools'],
    entry_points={
    'console_scripts': [
        'navigation_node = autonomous_robot.my_node:main',
        ],
    },
)