## Overview
This project is built to copy the data from source to the target database. The purpose was to build a flexible data copying pipeline, where existing or newly added procedures could be easily modified and integrated.

Thus, this project utilizes decorators for data characteristics evaluation step.
The evaluation characteristics can be easily added to `quality_checks` folder and get registered with `@procedure` decorator.
The procedure modules can be easily hidden by adding ```'_'``` or ```'.'``` in front of the module name if it is desired to skip a certain data quality check.

For instance, if it is desired to not check for NA values in the tables, one can rename the module to ```'_check_na.py'``` in ```quality_checks``` folder.

Additional data characteristic checks can be added or transformations to the data can be applied upon request.

Folder overview:
```angular2html
db - Contains modules to connect, read and write to the databases

quality_checks - Data characteristics evaluation modules

reports - Configured data copying and characteristics reports in .log format.

tests - Unit tests for connection and quality_checks modules
```
The credentials for accessing SOURCE and TARGET databases are stored in ```db/creds.yaml```

## Prerequisites
![Python 3.9](https://img.shields.io/badge/Python-3.9-blue)

This project uses Python 3.9.
## Installation
There are two ways you can run this project locally. Either by creating a new conda environment and installing the requirements, or by building a docker image.
### Conda
1. Create and activate a new conda environment
```angular2html
conda create --name [name] python=3.9
conda activate [name]
```
2. Install the requirements
```angular2html
pip install -r requirements.txt
```
3. Run the script `(--test=[True/False])` where True is for running the unittests
```angular2html
python3 run.py --test False
```
### Docker
1. Build the image from Dockerfile
```angular2html
docker build -t [name] --no-cache .
```
2. Run the application `(--test=[True/False])` where True is for running the unittests
```angular2html
docker run --rm [name] --test=False
```

## Future improvements
- [ ] Replace logging with loguru for better log readability
- [ ] Utilize pytest for unit testing and disregard the call from the main script.
- [ ] Use os.environ() instead of basic --args calls.
