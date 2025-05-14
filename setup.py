from setuptools import setup, find_packages

setup(
    name="mdparsertp",
    version="1.0.0",
    description="Convertisseur Markdown vers site HTML stylisé",
    author="Anthony Mittica",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "mdparsertp = mdparsertp.cli:main"
        ]
    },
    python_requires='>=3.6',
)
