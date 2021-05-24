from setuptools import setup, find_packages

def readRequirements():
    with open('requirements.txt') as req:
        content = req.read()
        requirements = content.split('\n')
    return requirements

setup(
    name="miniurl",
    version="0.2",
    packages=find_packages(),
    includePackageData=True,
    install_requires=readRequirements(),
    entry_points='''
        [console_scripts]
        miniurl=miniurl.cli:cli
    '''
)