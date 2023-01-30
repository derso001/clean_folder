from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
    version='1',
    author='Boris Zdorovets',
    author_email='bor.zdorovets28@gmail.com',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']}
)