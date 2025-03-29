from setuptools import setup, find_packages

setup(
    name="llamaduck",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click>=8.1.8",
        "requests>=2.25.1",
        "beautifulsoup4>=4.9.3",
        "rich>=13.0.0",
        "duckduckgo-search>=6.1.0",
    ],
    extras_require={
        "dev": [
            "uv>=0.1.0",
            "tox>=4.0.0",
        ],
        "test": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "mypy>=1.0.0",
            "ruff>=0.4.0",
            "types-requests>=2.31.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "llamaduck=llamaduck.cli:cli",
        ],
    },
    python_requires=">=3.8",
)
