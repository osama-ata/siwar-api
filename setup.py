from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="siwar-api",
    version="0.1.0",
    author="Osama Ata",
    author_email="me@osamata.com",  # Replace with your email if different
    description="Python wrapper for the Siwar Arabic Lexicon API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/osama-ata/siwar-api",
    project_urls={
        "Bug Tracker": "https://github.com/osama-ata/siwar-api/issues",
        "Documentation": "https://github.com/osama-ata/siwar-api#readme",
        "Source Code": "https://github.com/osama-ata/siwar-api",
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Linguistic",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: Arabic",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.25.0",
    ],
    extras_require={
        'dev': [
            'pytest>=6.0',
            'pytest-cov>=2.0',
            'flake8>=3.9',
            'mypy>=0.910',
            'black>=21.0',
            'isort>=5.0',
            'sphinx>=4.0',
            'sphinx-rtd-theme>=0.5',
        ],
    },
)
