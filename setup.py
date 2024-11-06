from setuptools import setup, find_namespace_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="siwar-api",
    version="0.1.0",
    author="Osama Ata",
    author_email="me@osamata.com",
    description="Python wrapper for the Siwar Arabic Lexicon API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/osama-ata/siwar-api",
    project_urls={
        "Bug Tracker": "https://github.com/osama-ata/siwar-api/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_namespace_packages(where="src", include=["siwar", "siwar.*"]),
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.25.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=3.0.0",
            "mypy>=0.910",
            "flake8>=3.9.0",
            "black>=22.0.0",
            "isort>=5.9.0",
            "responses>=0.23.0",
        ],
    },
)
