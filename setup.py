from setuptools import setup

def readme():
    with open('README.md') as readme:
        return readme.read()

setup(name='opimage_things',
      version='0.0.1dev',
      description='Open PI Image hardware helper',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Image Processing :: Science',
      ],
      keywords='plant image processing raspberry pi',
      url='http://github.com/teammaclean/opimage_things',
      author='Team MacLean',
      author_email='dan.maclean@tsl.ac.uk',
      license='MIT',
      packages=['opimage_things'] ,
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      zip_safe=False)
