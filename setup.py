from setuptools import setup, find_packages

setup(
    name="height_estimator",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "opencv-python",
        "numpy"
    ],
    author="Sajid Islam",
    description="A package to estimate height from images or videos using OpenCV.",
    url="https://github.com/sajid-00/height_measure",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
