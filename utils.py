import re
from constant import Setup


class FileManagement:
    def __init__(self, parent) -> None:
        self.parent = parent

    def get_version(self) -> str:
        """
        Get the version from the __init__.py file.

        return:
            str: The version number.
        """
        file_path = self.parent / Setup.VERSION

        with file_path.open(encoding="utf-8") as f:
            file_content = f.read()

        version_match = re.search(
            r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', file_content, re.MULTILINE
        )

        if version_match:
            return version_match.group(1)
        else:
            raise ValueError("Version information not found in the file.")

    def get_requirements(self) -> list:
        """
        Get the requirements from the requirements.txt file.

        return:
            list: The list of requirements.
        """
        file_path = self.parent / Setup.REQUIREMENTS

        with file_path.open(encoding="utf-8") as f:
            return f.read().splitlines()

    def get_readme(self) -> str:
        """
        Get the README content from the README.md file.

        return:
            str: The README content.
        """
        file_path = self.parent / Setup.README

        with file_path.open(encoding="utf-8") as f:
            return f.read()
