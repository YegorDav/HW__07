from setuptools import setup, find_namespace_packages


def setup(name='clean_folder',
        version='1.0.0',
        description='Sorted folders',
        author='Yegor_Davydenko',
        license='MIT',
        packages=find_namespace_packages(),
        entry_points={'console_scripts':['clean = clean_folder.clean:get_category,normalize']})



