from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / 'README.md').read_text()

setup(
    name='pybibx',
    version='4.5.5',
    license='GNU',
    author='Valdecy Pereira',
    author_email='valdecy.pereira@gmail.com',
    url='https://github.com/Valdecy/pybibx',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # MODIFIED FOR THESIS
        # Mofidied to allow using with latest python version 3.13.5 
        #'bertopic',
        #'bert-extractive-summarizer',
        'chardet',
        'google-generativeai',
        # MODIFIED FOR THESIS
        # Mofidied to allow using with latest python version 3.13.5
        #'gensim',
        'llmx',
        'matplotlib',
        'networkx',
        'numba',
        'numpy',
        'pandas',
        'plotly',
        'scipy',
        'scikit-learn',
        # MODIFIED FOR THESIS
        # Mofidied to allow using with latest python version 3.13.5
        #'sentencepiece',
        'sentence-transformers',
        'torch', 
        'torchvision',
        'torchaudio',
        'transformers',
        'umap-learn',
        'openai',
        'wordcloud'
    ],
    zip_safe=True,
    description='A Bibliometric and Scientometric Library Powered with Artificial Intelligence Tools',
    long_description=long_description,
    long_description_content_type='text/markdown',
)
