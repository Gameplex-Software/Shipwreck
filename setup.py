import setuptools

with open('README_pypi.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='ShipWreck',
    author='Gameplex Software',
    author_email='info@gameplexsoftware.com',
    description='A library for logging and handling Python errors and suggesting fixes',
    keywords='ShipWreck, pypi, package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/gameplex-software/ShipWreck',
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    extras_require={
        'dev': ['check-manifest'],
    },
)