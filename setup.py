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

'''
1. python3 -m venv .venv (create a venv)
2. add export PIP_INDEX_URL=https://pypi.org/simple/ to the end of .venv/bin/activate
3. add export PIP_EXTRA_INDEX_URL="" to the end of .venv/bin/activate
4. activate venv: source .venv/bin/activate
5. pip install setuptools pip
6. pip install -e . #for main set of packages
6. pip install -e '.[dev]' for dev packages on Zsh, just [dev] on Bash
7. deactivate
'''


# Set these inside the venv
# 
# export PIP_EXTRA_INDEX_URL=""