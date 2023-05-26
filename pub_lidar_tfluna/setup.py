from setuptools import setup

package_name = 'pub_lidar_tfluna'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ubuntu',
    maintainer_email='brayanelgamesa@hotamail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = pub_lidar_tfluna.publisher_function:main',
            'listener = pub_lidar_tfluna.subscriber_function:main',
            'direc_subscriber = pub_lidar_tfluna.direct_subscriber:main',
            'direc_subscriber_arduino = pub_lidar_tfluna.direct_subscriber_arduino:main',
            'direc_publisher_lidar = pub_lidar_tfluna.direct_publisher_lidar:main'
        ],
    },
)

