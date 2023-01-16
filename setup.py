import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bert-tokens",
    version="0.0.1",
    author="StefenSal",
    author_email="4772896@gmail.com",
    description="A useful tool for bert tokenization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/StefenSal/Bert-Tokens-Tools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)