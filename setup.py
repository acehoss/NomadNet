import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nomadnet",
    version="0.0.1",
    author="Mark Qvist",
    author_email="mark@unsigned.io",
    description="Communicate freely",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/markqvist/nomadnet",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points= {
        'console_scripts': ['nomadnet=nomadnet:main']
    },
    install_requires=['rns', 'lxmf'],
    python_requires='>=3.5',
)