from setuptools import find_packages, setup

from djangocms_4_migration import __version__


setup(
    name='djangocms-4-migration',
    version=__version__,
    description=open('README.md').read(),
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
