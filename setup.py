from setuptools import setup

package_name = 'py_topic'

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
    maintainer='ashwina',
    maintainer_email='ashwina@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
        entry_points={
        'console_scripts': [ 'py_topic_publisher_spiral = py_topic.py_topic_publisher_spiral:main',
                             'py_topic_subscriber_spiral = py_topic.py_topic_subscriber_spiral:main',
        ],
    },
)