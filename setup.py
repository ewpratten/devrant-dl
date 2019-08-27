import setuptools 

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='devrant_dl',
    version='1.0.0',
    packages=["devrant_dl"],
    description='Get a dump of your entire history on devRant',
    url='https://github.com/Ewpratten/devrant-dl',
    author='Evan Pratten',
    author_email='ewpratten@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
    ),
    entry_points={
        'console_scripts': [
            'devrant_dl = devrant_dl.__main__:main'
        ]
    })
