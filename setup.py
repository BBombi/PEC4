from setuptools import setup, find_packages
from pathlib import Path

setup(
    name="embassaments",
    version="1.0",
    author="Borja Bombí",
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/borjabombi/analisis_embalses',
    license="MIT",
    packages=find_packages(),
    install_requires=Path("requirements.txt").read_text().splitlines(),
    install_requires=[
        "pandas==2.2.3",
        "matplotlib==3.10.0",
        "scipy==1.15.1"
    ],
    extras_require={
        "dev": [
            "pytest==8.4.0"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "embalses=embassaments.main:main"
        ]
    }
)
