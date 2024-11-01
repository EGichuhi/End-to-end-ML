from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    #function will return list of requirements
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        #in requirements.txt it will read with \n included after every word,
        # we need to remove that. 
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements

setup(
    name='mlproject1',
    version='0.0.1',
    author='Eunice G',
    author_email='ewgichuh@uwaterloo.ca',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
