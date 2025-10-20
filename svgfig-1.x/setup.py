#!/usr/bin/env python

from setuptools import setup

setup(
    name="SVGFig",
    version="1.1.3",
    description="SVGFig: Quantitative drawing in Python and SVG",
    author="Jim Pivarski",
    author_email="jpivarski@gmail.com",
    url="http://code.google.com/p/svgfig/",
    py_modules=["svgfig"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
)
