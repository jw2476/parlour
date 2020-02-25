import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='parlour',
    version='0.0.2',
    author="Jack Whitehorn",
    author_email="jackwh.whitehorn@gmail.com",
    description="A python-based system-independent community-driven setup tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jw2476/parlour",
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Unix Shell',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: Unix',
    ],
    python_requires='>=3.6',

    py_modules=['parlour'],
    install_requires=[
        'typer', 'click-completion'
    ],
    entry_points='''
        [console_scripts]
        parlour=parlour.main:cli
    '''
)