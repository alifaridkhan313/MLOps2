from setuptools import find_packages
from setuptools import setup
from typing import List

PROJECT_NAME = "MLOps using Modular Coding"
VERSION = "0.0.1"
DESCRIPTION = "This repo is for understanding modular coding in MLOps"
AUTHOR_NAME = "Ali Farid Khan"
AUTHOR_EMAIL = "alifaridkhan313@gmail.com"


REQUIREMENT_FILE_NAME = 'requirements.txt'
HYPHEN_E_DOT = "-e ."

###open --> read --> return 


def get_requirements_list() -> List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]

        if HYPHEN_E_DOT in requirement_list: 
            requirement_list.remove(HYPHEN_E_DOT)

        return requirement_list


setup(
    
    name = PROJECT_NAME, 
    version = VERSION, 
    description = DESCRIPTION, 
    author = AUTHOR_NAME, 
    author_email = AUTHOR_EMAIL, 
    packages = find_packages(), 
    install_requirements = get_requirements_list()

)