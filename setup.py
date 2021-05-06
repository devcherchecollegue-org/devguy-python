from setuptools import find_packages, setup

setup(
    name="devguy",
    version="0.0.1",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=["discord"],
    extras_require={
        "dev": ["flake8", "coverage", "mypy", "black", "pytest", "elmock", "pydantic"],
    },
)
