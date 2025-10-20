#!/usr/bin/env python3

from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import os
import sys

sys.path.append("svgfig")
import defaults

# Optional extensions that can be skipped if they fail
extension_features = {
    "_curve": None
}


class my_build_ext(build_ext):
    def build_extension(self, extension):
        try:
            super().build_extension(extension)
        except Exception as e:
            for ext, feat in extension_features.items():
                if ext in extension.name and feat is None:
                    raise RuntimeError(f"Failed to compile {ext}") from e

            print("*" * 94)
            print(f"\nNote: couldn't compile \"{extension.name}\", so you will be unable to use this feature:")
            for ext, feat in extension_features.items():
                if ext in extension.name:
                    print(feat)
                    break
            print("\n" + "*" * 94)


#  Define the extension
curve_extension = Extension(
    "svgfig._curve",
    sources=[os.path.join("svgfig", "_curve.c")]
)

# Setup configuration
setup(
    name="SVGFig",
    version=defaults.version,
    description="SVGFig: Quantitative drawing in Python and SVG",
    author="Jim Pivarski",
    author_email="jpivarski@gmail.com",
    url="http://code.google.com/p/svgfig/",
    packages=["svgfig"],
    py_modules=[
        "svgfig.__init__",
        "svgfig.curve",
        "svgfig.defaults",
        "svgfig.glyphs",
        "svgfig.interactive",
        "svgfig.pathdata",
        "svgfig.plot",
        "svgfig.svg",
        "svgfig.trans"
    ],
    cmdclass={"build_ext": my_build_ext},
    ext_modules=[curve_extension],
)
