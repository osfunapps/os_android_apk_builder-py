from distutils.core import setup

setup(
    name='os_android_apk_builder',
    packages=['os_android_apk_builder'],
    version='1.01',  # Start with a small number and increase it with every change you make
    license='MIT',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='This module will create an apk programmatically (dynamically), without Android Studio.',  # Give a short description about your library
    author='Oz Shabat',  # Type in your name
    author_email='osfunapps@gmail.com',  # Type in your E-Mail
    url='https://github.com/osfunapps/os-android-apk-builder-py',  # Provide either the link to your github or to your website
    keywords=['python', 'osfunapps', 'apk', 'android', 'automation', 'release', 'assemble-release', 'create', 'pre-publish'],  # Keywords that define your package best
    install_requires=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package

        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',  # Again, pick a license

        'Programming Language :: Python :: 3',  # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)

