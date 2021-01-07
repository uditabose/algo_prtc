import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="algo-prtc",
    version="1.0.0",
    author="Papa Bose",
    author_email="papabose@gmail.com",
    description="Algorithm practice",
    long_description="Very long Algorithm practice",
    long_description_content_type="text/markdown",
    url="git@github.com:uditabose/algo_prtc.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
