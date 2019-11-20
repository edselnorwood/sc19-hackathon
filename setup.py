import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="teamchord",
    version="0.0.1",
    author="Team CHORD",
    author_email="ishan.paranjape@utexas.edu",
    description="Client for the CCQ meta-scheduler in CloudyCluster",
    long_description=long_description,
    long_description_content_type="text/plain",
    url="https://github.com/edselnorwood/sc19-hackaton",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU LGPLv2.1",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
