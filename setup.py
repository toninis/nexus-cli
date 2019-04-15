from setuptools import setup, find_packages


def get_requirements_from_file(requirements_file):
    with open(requirements_file) as f:
        requirements = []
        for line in f:
            line = line.strip()
            # ignore comments and editable packages
            if not line.startswith("#") or not line.startswith("-e"):
                requirements.append(line)

        return requirements


def get_long_description():
    with open("README.md") as f:
        return f.read()


setup(
    name="nexusCli",
    version="1.0.0",
    author="Encode Group",
    author_email="engineering-devops@encodegroup.com",
    license="Copyright 2019 Encode Group",
    description="Python application to manipulate nexus artifacts",
    long_description=get_long_description(),
    install_requires=get_requirements_from_file("requirements.txt"),
    packages=find_packages(),
    zip_safe=True,
    entry_points={
        "console_scripts": [
            "nexusCli = nexusCli.manage:main"
        ]
    }
)
