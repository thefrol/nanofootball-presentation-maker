from setuptools import setup, find_packages
from pathlib import Path

with open('requirements.txt','r') as f:
    requirements=f.readlines()

this_directory=Path(__file__).parent
long_description=(this_directory / 'README.MD').read_text(encoding='utf8')


setup(
    name='nf_presentation',
    version='0.1.0',
    author='Dmitriy Frolenko',
    author_email='orangefrol@gmail.com',
    packages=find_packages(where='src'),
    package_dir={"": "src"},
    install_requires=requirements, # лол без этой строчки он ругался на README.MD
    url='https://github.com/thefrol/nanofootball-presentation',
    long_description=long_description,
    long_description_content_type='text/markdown; variant=GFM',
    license="MIT"
)