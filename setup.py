from setuptools import setup, find_packages

setup(
    name="web_extractor",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "annotated-types==0.7.0",
        "beautifulsoup4==4.12.3",
        "cachetools==5.5.0",
        "certifi==2024.8.30",
        "charset-normalizer==3.4.0",
        "google-ai-generativelanguage==0.6.10",
        "google-api-core==2.23.0",
        "google-api-python-client==2.154.0",
        "google-auth==2.36.0",
        "google-auth-httplib2==0.2.0",
        "google-generativeai==0.8.3",
        "googleapis-common-protos==1.66.0",
        "grpcio==1.68.0",
        "grpcio-status==1.62.3",
        "httplib2==0.22.0",
        "idna==3.10",
        "proto-plus==1.25.0",
        "protobuf==4.25.5",
        "pyasn1==0.6.1",
        "pyasn1_modules==0.4.1",
        "pydantic==2.10.2",
        "pydantic_core==2.27.1",
        "pyparsing==3.2.0",
        "python-dotenv==1.0.1",
        "requests==2.32.3",
        "rsa==4.9",
        "soupsieve==2.6",
        "tqdm==4.67.1",
        "typing_extensions==4.12.2",
        "uritemplate==4.1.1",
        "urllib3==2.2.3",
    ],
    author="Abhinav C V",
    author_email="abhinavcv007@gmail.com",
    description="A library for extracting structured data from web pages using AI",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/abhinavcv007/web_extractor",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)