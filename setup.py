from setuptools import find_packages,setup
from typing import List
e_dot='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function return a list
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requiremnts=file_obj.readlines()
        [req.replace("/n","") for req in requirements]
        if e_dot in requirements:
            requirements.remove(e_dot)
    return requirements


setup(
name='MLPROJECTS',
version='0.01',
author='prakash',
author_email='.gmail.com',
packages=find_packages(),
insatll_requires=get_requirements('requirements.txt')



)