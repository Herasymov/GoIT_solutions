from setuptools import setup

setup(
    name='useful',
    description='Very useful code',
    url='https://github.com/Herasymov/GoIT_solutions.git/lesson8/useful',
    author='Herasymov',
    author_email='slava.herasymov@gmail.com',
    license='MIT',
    packages=['useful'],
    install_requires=['markdown'],
    entry_points={'console_scripts': ['helloworld = useful.some_code:hello_world']}
)

#_install_setup_requires