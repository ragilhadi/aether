class Setup:
    NAME = "aether"
    README = "README.md"
    REQUIREMENTS = "requirements.txt"
    VERSION = "src/aether/__init__.py"
    URL = "https://github.com/ragilhadi/aether"
    AUTHOR = "ragilhadi"
    AUTHOR_EMAIL = "ragilhprasetyo@gmail.com"
    LICENSE = "MIT"
    CLASSIFIERS = (
        [
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3.9",
            "Operating System :: OS Independent",
        ],
    )
    EXTRAS = {
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    }
    PYTHON_VERSION = ">=3.10"
    DESCRIPTION = "Aether is a deep learning tools for computer vision."
    ENTRY_POINTS = {"console_scripts": ["aether = aether.cli:cli_parser"]}
