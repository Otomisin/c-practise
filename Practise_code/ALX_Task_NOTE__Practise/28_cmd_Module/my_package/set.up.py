from setuptools import setup  # Import the setup function from setuptools

setup(
    name='my_package',  # The name of the package
    version='1.0.0',  # The version number of the package
    description='A simple Python package',  # A short description of the package
    author='Your Name',  # The name of the package's author
    author_email='your.email@example.com',  # The email address of the package's author
    packages=['my_package'],  # A list of the packages to include in the distribution
    install_requires=[],  # A list of any dependencies required by the package
    classifiers=[  # A list of classifiers used to categorize the package on PyPI
        'Development Status :: 3 - Alpha',  # The current development status of the package
        'Intended Audience :: Developers',  # The intended audience of the package
        'License :: OSI Approved :: MIT License',  # The type of license under which the package is released
        'Programming Language :: Python :: 3',  # The version(s) of Python the package is compatible with
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)

