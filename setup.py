from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    # region core
    name="tsetmc-webservice",
    version="1.0.0",
    python_requires=">=3.5",
    install_requires=[
        "appdirs",
        "attrs",
        "cached-property",
        "certifi",
        "chardet",
        "defusedxml",
        "idna",
        "isodate",
        "lxml",
        "numpy",
        "pandas",
        "python-dateutil",
        "pytz",
        "requests",
        "requests-file",
        "requests-toolbelt",
        "six",
        "urllib3",
        "zeep",
    ],
    extras_require={
        "dev": [
            "appdirs",
            "attrs",
            "black",
            "bleach",
            "cached-property",
            "cerberus",
            "certifi",
            "cffi",
            "chardet",
            "click",
            "colorama",
            "cryptography",
            "distlib",
            "docutils",
            "idna",
            "jeepney",
            "keyring",
            "orderedmultidict",
            "packaging",
            "pathspec",
            "pep517",
            "pip-shims",
            "pipenv-setup",
            "pipfile",
            "pkginfo",
            "plette[validation]",
            "pycparser",
            "pygments",
            "pyparsing",
            "python-dateutil",
            "readme-renderer",
            "regex",
            "requests",
            "requests-toolbelt",
            "requirementslib",
            "rfc3986",
            "secretstorage",
            "six",
            "toml",
            "tomlkit",
            "tqdm",
            "twine",
            "typed-ast",
            "urllib3",
            "vistir",
            "webencodings",
            "wheel",
        ]
    },
    dependency_links=[],
    packages=find_packages(exclude=["scripts"]),
    # endregion
    # region data & scripts
    # endregion
    # region metadata
    description="api to communicate with tsetmc webservice (the paid one)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mahs4d/tsetmc-webservice/",
    author="Mahdi Sadeghi",
    author_email="mail2mahsad@gmail.com",
    classifiers=[  # https://pypi.org/classifiers/
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    keywords="sample setuptools development",
    project_urls={
        "Bug Reports": "https://github.com/mahs4d/tsetmc-webservice/issues",
        "Source": "https://github.com/mahs4d/tsetmc-webservice/",
    },
    # endregion
)
