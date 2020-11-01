"""Setup configuration."""
import setuptools

with open("README.md", "r") as fh:
    DESCRIPTION = fh.read()

setuptools.setup(
    name="pylaunches",
    version="0.0.0",
    author="Joakim Sorensen",
    author_email="hi@ludeeus.dev",
    description="",
    long_description=DESCRIPTION,
    install_requires=["aiohttp", "async_timeout<=3.0.1", "pytest-runner"],
    long_description_content_type="text/markdown",
    url="https://github.com/ludeeus/pylaunches",
    packages=setuptools.find_packages(exclude=["tests", "tests.*"]),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
