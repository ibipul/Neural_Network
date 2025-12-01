import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gradengine",
    version="0.1.0",
    author="Bipul Islam",
    author_email="islam.bipul@gmail.com",
    description="A tiny scalar-valued autograd engine for computational graphs for backpropagation, and other abstractions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ibipul/gradengine",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
    install_requires=[
        'numpy>=1.20',  # Required for core functionality
        'requests',     # Another core dependency
        'graphviz'      # Required for visualization utility
    ],
    extras_require={
        'dev': ['pytest', 'pytest-cov'],
    },
)

# Set these inside the venv
# export PIP_INDEX_URL=https://pypi.org/simple/
# export PIP_EXTRA_INDEX_URL=""