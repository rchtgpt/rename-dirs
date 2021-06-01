import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rename-dirs",
    version="2.0.0",
    author="Rachit Gupta",
    author_email="guptarachit2004@gmail.com",
    description="A python script to rename multiple directories in a uniform format.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rchtgpt/rename-dirs",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={'console_scripts': [
        'rename-dirs=rename_dirs.__main__:main']},
)
