import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="arraymin",
    version="1.0.0",
    author="Milad Ghalejughi",
    author_email="miladghalejughi@email.com",
    description="array min operator python package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MLDSPARROW/arraymin",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
