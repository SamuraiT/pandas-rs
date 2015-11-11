try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name = "pandas-rs",
    packages = ["pandas_rs"],
    install_requires = ["pandas", "psycopg2"],
    version = "0.1.0",
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
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ]
)