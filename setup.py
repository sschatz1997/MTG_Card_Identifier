# setup.py
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MTG_Card_Identifier",  # Replace with your own username
    version="0.0.2",
    author="Sam Schatz",
    author_email="samsch1997@gmail.com",
    description="Find magic cards based on the Name on the card.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sschatz1997/MTG_Card_Identifier",
    packages=setuptools.find_packages(),
    #packages=['opencv_python', 'pandas', 'progress',	'pytesseract', 'Pillow','pytest', 'imagehash', 'art', 'colorama', 'requests', 'tabulate'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7.3',
)
