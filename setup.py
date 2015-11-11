try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import re
import os

def pandas_rs_version():
    version_regex  = re.compile(r'__version__ = "([^\"]*)"')
    return version_regex.match(
        open('pandas_rs/version.py').read()
    ).group(1)

def read_file(filename):
    filepath = os.path.join(
        os.path.dirname(
            os.path.dirname(__file__)
        ),
        filename
    )
    if os.path.exists(filepath):
        return open(filepath).read()
    else:
        return ''

setup(
    name = "pandas-rs",
    packages = ["pandas_rs"],
    install_requires = ["pandas", "psycopg2"],
    version = pandas_rs_version(),
    description = "pandas extension for AWS RedShift (Not Officail library)",
    author = "Tatsuro Yasukawa",
    author_email = "mark@diveintomark.org",
    url = "https://github.com/SamuraiT/pandas-rs",
    download_url = "",
    keywords = ["pandas", "RedShift", "sql"],
    classifiers = [
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    long_description = read_file('README.md')
)