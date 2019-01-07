from setuptools import find_packages, setup

setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),  # tells python what package directories to include, will find them automatically
    include_package_data=True, # include other files like templates and static directories. Python needs MANIFEST.in to tell where the data is
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)