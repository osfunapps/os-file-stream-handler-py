from distutils.core import setup

setup(
    name='os_file_stream_handler',  # How you named your package folder (MyLib)
    packages=['os_file_stream_handler'],  # Choose the same as "name"
    version='1.04',  # Start with a small number and increase it with every change you make
    license='MIT',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='py file stream handling tools for os',  # Give a short description about your library
    author='Oz Shabat',  # Type in your name
    author_email='support@os-apps.com',  # Type in your E-Mail
    url='https://github.com/osfunapps/os-file-stream-handler-py',  # Provide either the link to your github or to your website
    keywords=['python', 'osfunapps', 'files', 'tools', 'utils', 'stream'],  # Keywords that define your package best
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
        'Programming Language :: Python :: 3.9',
    ],
)
