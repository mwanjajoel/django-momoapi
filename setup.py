import pathlib
from setuptools import setup

# the directory containing this file
HERE = pathlib.Path(__file__).parent

# The Readme file
README = (HERE / "README.md").read_text()

# This does all the work once called
setup(
    name="django-momoapi",
    version="1.0.0",
    description="This is a Django package for the MTN MoMo API.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/mwanjajoel/django-momoapi",
    author="mwanjajoel",
    author_email="joelsilverworks@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ]

)
