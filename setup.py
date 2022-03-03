from setuptools import setup

setup(
    name='simple_flask_app',
    version='1.0',  # Also in config.py, setup.py, utils.py:save_daw_session_items
    description='Simple Flask App',
    author='Eric Dalrymmple',
    author_email='eric_dalrymple@apple.com',
    packages=['app'],
    include_package_data=True,  # needed for copying static files
    install_requires=open('requirements.txt').read().split(),
    classifiers=[
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing',
    ],
    license='MIT',
    python_requires='>=3.7',
    test_suite="tests.test_suite"
)
