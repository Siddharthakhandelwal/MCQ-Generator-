from setuptools import find_packages,setup

setup(
    name='mcqgenrator',
    version='1.0.5',
    author='Keshav Agrawal',
    author_email='tekionix.askkeshav@gmail.com',
    install_requires=["google-generativeai","langchain","streamlit","python-dotenv","PyPDF2","langchain-google-genai"],
    packages=find_packages()
)