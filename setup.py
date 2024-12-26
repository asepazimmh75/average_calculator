
##### **`setup.py`**
from setuptools import setup, find_packages

setup(
    name="average_calculator",
    version="1.0.0",
    description="A simple tool to calculate the average of numbers",
    author="asepazimmh75",
    author_email="asepazizmiftahulhuda75@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "average_calculator=average_calculator:calculate_average",
        ],
    },
)
