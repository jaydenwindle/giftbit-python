import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="giftbit",
    version="0.1",
    author="Jayden Windle",
    author_email="jaydenwindle@gmail.com",
    description="A Python SDK for GiftBit's API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jaydenwindle/giftbit-python",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
