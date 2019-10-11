import setuptools

setuptools.setup(
    name="githubcommit",
    version='0.1.0',
    url="https://github.com/Thajudheen/custom_plugin",
    author="Thaj",
    description="Jupyter extension for a plugin",
    packages=setuptools.find_packages(),
    install_requires=[
        'psutil',
        'notebook',
        'gitpython'
    ],
    package_data={'githubcommit': ['static/*']},
)
