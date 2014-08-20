"""Super simple create table statement dumping. Hopefully gives you a
useful create table statement and nothing else from postgres :).

"""
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.readlines()

setup(
    name='explain',
    description="Super simple create table statement dumping.",
    version='0.1.1',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    author='Anthony Grimes',
    author_email='i@raynes.me',
    url='https://github.com/Raynes/explain',
    license='MIT',
    install_requires=requirements,
    entry_points="""
    [console_scripts]
    explain=explain.__main__:explain
    """
)
