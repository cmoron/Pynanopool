from setuptools import setup

setup(
    name='pynanopool',
    version='1.0',
    scripts=['pynanopool'],
    author='Cyril Moron',
    author_email='cyril.moron@gmail.com',
    description='cli tool to monitor nanopool status',
    url='https://github.com/cmoron/pynanopool',
    install_requires=['wheel', 'requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
