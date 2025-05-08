from setuptools import setup, find_packages

setup(
    name='agentplanner',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'openai',
        'boto3',
        'google-cloud-storage',
        'azure-identity',
        'azure-storage-blob',
        'simple-salesforce',
        'ibm-watson',
        'heroku3',
        'PyDrive',
        'transformers',
        'sentence-transformers'
    ],
    author='Raghavendra',
    description='A unified LLM, embedding, and cloud orchestration framework.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/narayanaraghavendra/agentplanner',  # Change to actual repo if needed
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
