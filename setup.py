try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

def pandas_rs_version():
    import re
    version_regex  = re.compile(r'__version__ = "([^\"]*)"')
    return version_regex.match(
        open('pandas_rs/version.py').read()
    ).group(1)

def readme():
    return open("README.md").read()

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
    long_description = readme()
)