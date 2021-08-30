from setuptools import setup

setup(
    name="my-lib",
    description="Repro lib",  # Required
    install_requires=[],
    dependency_links=[],
    extras_require={
        "test": [
            "pytest",
        ],
    },
)
