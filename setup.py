from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    Returns a list of requirements / libraries
    :return: List of strings i.e. Library Names
    """
    requirements = []
    try:
        with open('requirements.txt', 'r') as file:
            # Read lines from the file
            lines = file.readlines()

            for line in lines:
                requirement = line.strip()
                #ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirements.append(requirement)
        return requirements
    except FileNotFoundError as e:
        print("Requirements.txt file not found!")
    return  requirements

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Vikramaditya Khupse",
    author_email="vikramadityakhupse@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements()
)