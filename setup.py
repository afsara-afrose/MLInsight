from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT='-e .'
def get_requirments(file_path:str)->List[str]:

    ''' 
    this function return the list of requirments

    '''
    requirments=[]
    with open(file_path)as file_object:
        requirments= file_object.readlines()
        install_requires=get_requirments('requirments.txt')
        requirments=[req.replace("\n"," ") for req in requirments]
        if HYPEN_E_DOT in requirments :
            requirments .remove(HYPEN_E_DOT)
            return requirments
setup(
        name='MLInsight',
        version='0.0.1',
        author='Afsara',
        author_email='afsaraorna@gmail.com',
        packages=find_packages(),
        install_requires=['pandas','numpy','seaborn'],
)
