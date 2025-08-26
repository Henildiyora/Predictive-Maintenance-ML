from setuptools import setup, find_packages

setup(
    name="predictive-maintenance-ml",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy",
        "pandas",
        "scipy",
        "scikit-learn",
        "matplotlib",
    ],
)
