from setuptools import setup, find_packages


install_requires = []
with open('requirements.txt') as reqs:
    for line in reqs.readlines():
        req = line.strip()
        if not req or req.startswith('#'):
            continue
        install_requires.append(req)


setup(name='gladier-ptycho-portal',
      version='0.1.0',
      description='A portal for cataloging ptychography datasets',
      long_description=open('README.md').read(),
      author='',
      author_email='',
      url='https://github.com/globus-gladier/gladier-ptycho-portal',
      packages=find_packages(),
      dependency_links=[],
      include_package_data=True,
      keywords=['portal', 'globus', 'search', 'django'],
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: POSIX',
          'Programming Language :: Python',
      ],
      )
