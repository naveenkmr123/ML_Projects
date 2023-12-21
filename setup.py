from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirement(file_path:str)->List[str]:
    '''
    This function will return the list of requirement
    '''
    #requirements=[]
    with open(file_path) as obj_file:
        requirements= [line.rstrip() for line in obj_file]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='naveenkmr123',
author_email='naveen.fbara22@gmail.com',
packages=find_packages(),
install_requires=get_requirement('requirements.txt')

)