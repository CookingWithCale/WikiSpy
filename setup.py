import os.path
from setuptools import setup

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

# This call to setup() does all the work
setup(
    name="WikiSpy",
    version="0.0.1",
    description="A tool for monitoring Wikipedia for tampering, misinformation, political bias, and criminal activity.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/WikiSpy/WikiSpy",
    author="WikiSpy",
    author_email="info@WikiSpy.us",
    license="Kabuki Strong Source-available License",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    packages=["WikiSpy"],
    include_package_data=True,
    install_requires=[
        "feedparser", "html2text", "importlib_resources", "typing"
    ],
    entry_points={"console_scripts": ["wikispy=spy.__main__:main"]},
)
