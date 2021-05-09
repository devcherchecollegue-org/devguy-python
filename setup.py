from setuptools import find_packages, setup

setup(
    name="devguy",
    version="0.0.1",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "discord",
        "pydantic",
        "sqlalchemy",
    ],
    extras_require={
        "dev": [
            "black",
            "bandit",
            "coverage",
            "elmock",
            "flake8",
            "mypy",
            "pytest",
        ],
    },
)
