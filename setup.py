import setuptools

def requirements(filename):
    with open(filename) as f:
        return f.readlines()


setuptools.setup(
    name = 'proxie',
    version = '0.0.1',
    author = 'AJ Friend',
    author_email = 'ajfriend@gmail.com',
    description = 'Solving proximal iteration problems',
    long_description = 'later',

    install_requires = requirements('requirements.txt'),
    include_package_data = True,
    package_dir = {'': 'src'},
    packages = setuptools.find_packages(where='src'),
    python_requires = '>=3.7',
    zip_safe = False,
)
