from setuptools import find_packages, setup

setup(
    name='scopus',
    packages=find_packages(include=['lib']),
    version='0.1.0',
    description='Scopus Library for make request to Scopus API, with query combinations.',
    author='Riccardo Amadio',
    license='MIT',
    install_requires=["chardet==3.0.4","cycler==0.10.0",
    "idna==2.10","kiwisolver==1.3.1","matplotlib==3.3.3","numpy==1.18.5",
    "pandas==1.1.4","pytz==2020.4","pillow==8.0.1","requests==2.25.0","urllib3==1.26.2"],
)