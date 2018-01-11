from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='pygreppy',
      version='1.0.0',
      description='Tool for searching in python source code',
      python_requires='>=3',
      long_description=readme(),
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: General',
      ],
      url='https://github.com/skvoter/pygreppy',
      author='Kirill Korovin',
      author_email='skvoter46@gmail.com',
      license='BSD',
      packages=['pygreppy'],
      install_requires=[
          'pygments',
          'flake8',
      ],
      entry_points={
          'console_scripts': ['pygreppy=pygreppy.core:main'],
      },
      include_package_data=True,
      zip_safe=False)
