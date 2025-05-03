from setuptools import setup, find_packages

from python_coreml_stable_diffusion._version import __version__

with open('README.md') as f:
    readme = f.read()

setup(
    name='python_coreml_stable_diffusion',
    version=__version__,
    url='https://github.com/apple/ml-stable-diffusion',
    description="Run Stable Diffusion on Apple Silicon with Core ML (Python and Swift)",
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Apple Inc.',
    install_requires=[
        "coremltools>=8.0",
        "diffusers[torch]==0.30.2",
        "torch==2.5.0",
        "transformers==4.51.3",
        "huggingface-hub==0.30.2",
        "scipy",
        "numpy",
        "pytest",
        "scikit-learn==1.5.1",
        "invisible-watermark",
        "safetensors",
        "matplotlib",
        "diffusionkit==0.4.0",
    ],
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
