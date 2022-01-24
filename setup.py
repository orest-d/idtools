import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="idtools",
    version="0.1.0",
    author="Orest Dubay",
    author_email="orest3.dubay@gmail.com",
    description="LiQuer - Query in (URL) link",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/orest-d/idtools",
    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
