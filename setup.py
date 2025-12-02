from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements



# setup() is the main function used to define your Python package metadata and dependencies
setup(
    # Name of the package
    name='Student Performance Analysis',
    author='Samuel K C',
    author_email='samuelsam2k27@gmail.com',
    
    # Automatically find all packages (folders containing __init__.py)
    # In my project, 'src' folder contains __init__.py, so it will be included as a package
    packages=find_packages(),
    
    # External dependencies required for this package
    install_requires=get_requirements('requirements.txt')
)

"""
Explanation of key points:

1. setuptools:
   - A Python library used to **package and distribute** Python projects.

2. setup():
   - The main function that defines your package metadata, packages, and dependencies.

3. find_packages():
   - Automatically detects Python packages in your project folder.
   - A package is any folder containing an __init__.py file.
   - In this project, 'src/__init__.py' ensures 'src' is treated as a package.

4. install_requires:
   - Specifies external libraries required for your package.
   - When someone installs your package, these dependencies are installed automatically.

5. Purpose:
   - Once this setup.py is configured, you can build and install your package locally or distribute it.
   - After installation, you can import your package from anywhere using:
        import src  # or from src import <module>
"""
