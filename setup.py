import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rename-dirs",  # Replace with your own username
    version="0.0.1",
    author="Rachit Gupta",
    author_email="guptarachit2004@gmail.com",
    description="A simple script to rename multiple directories.",
    url="https://github.com/rchtgpt/rename-dirs",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
