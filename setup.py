from setuptools import find_packages, setup


setup(name='dcos-shakedown',
      version='1.4.9',
      description=u"DC/OS testing harness and library",
      long_description=u"A tool and library to abstract common DC/OS-related tasks.",
      classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Topic :: Software Development :: User Interfaces',

        'License :: OSI Approved :: Apache Software License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
      ],
      keywords='',
      author=u"Mesosphere QE",
      author_email='qe-team@mesosphere.com',
      url='https://github.com/dcos/shakedown',
      license='Apache 2',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'click',
          'dcoscli',
          'paramiko',
          'pytest',
          'pytest-timeout',
          'retrying',
          'scp'
      ],
      dependency_links=[
          "git+https://github.com/dcos/dcos-cli.git#egg=dcoscli"
      ],
      python_requires='>=3.5',
      entry_points="""
      [console_scripts]
      shakedown=shakedown.cli.main:cli
      dcos-shakedown=shakedown.cli.main:cli
      """
      )
