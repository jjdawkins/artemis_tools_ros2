from setuptools import setup

package_name = 'artemis_tools_ros2'

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
    maintainer='arty',
    maintainer_email='dawkins@usna.edu',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['pose_listener = artemis_tools_ros2.pose_listener:main',
                   'pose_listener_qualisys = artemis_tools_ros2.pose_listener_qualisys:main',
                   'rosbag_service = artemis_tools_ros2.rosbag_service:main',
                   'rigid_bodies_repub = artemis_tools_ros2.rigid_bodies_republisher:main' 
        ],
    },
)
