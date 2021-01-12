from setuptools import find_packages, setup

from djangocms_4_migration import __version__


setup(
    name='djangocms-4-migration',
    version=__version__,
    author="Andrew Aikman (Aiky30)",
    description="A django CMS 3 to 4 migration package",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    zip_safe=False,
)
