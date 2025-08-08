from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="diffusion-mri-brain-network-analysis",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Automated pipeline for diffusion MRI brain network analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/skkuhg/diffusion-mri-brain-network-analysis",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0",
            "black>=22.0",
            "flake8>=5.0",
            "isort>=5.0",
        ],
        "docs": [
            "sphinx>=5.0",
            "sphinx-rtd-theme>=1.0",
        ],
    },
    keywords="neuroimaging, diffusion MRI, brain networks, machine learning, deep learning",
    project_urls={
        "Bug Reports": "https://github.com/skkuhg/diffusion-mri-brain-network-analysis/issues",
        "Source": "https://github.com/skkuhg/diffusion-mri-brain-network-analysis",
        "Documentation": "https://github.com/skkuhg/diffusion-mri-brain-network-analysis/wiki",
    },
)
