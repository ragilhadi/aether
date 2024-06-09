from pathlib import Path
from utils import FileManagement
from constant import Setup
from setuptools import find_packages, setup

FILE = Path(__file__).resolve()
PARENT = FILE.parent
fm = FileManagement(PARENT)


README = fm.get_readme()
REQUIREMENTS = fm.get_requirements()
VERSION = fm.get_version()

setup(
    name=Setup.NAME,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    version=VERSION,
    description=Setup.DESCRIPTION,
    long_description=README,
    long_description_content_type="text/markdown",
    python_requires=Setup.PYTHON_VERSION,
    install_requires=REQUIREMENTS,
    url=Setup.URL,
    author=Setup.AUTHOR,
    author_email=Setup.AUTHOR_EMAIL,
    license=Setup.LICENSE,
    classifiers=Setup.CLASSIFIERS,
    extras_require=Setup.EXTRAS,
    entry_points=Setup.ENTRY_POINTS,
)
