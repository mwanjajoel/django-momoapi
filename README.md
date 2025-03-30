
# Django MoMo API 
This is a django package for the MTN and Airtel APIs in Uganda. It can be added to your current django-based application so as to interact with the APIs in a much simpler way.

![Build Status](https://travis-ci.com/mwanjajoel/django-momoapi.svg?branch=develop) 



## Why we created the Django MoMo API Package
MTN Uganda released API documentation to their Mobile Money service and integrations for Python, NodeJS, PHP, Java etc have been created but at the time of writing, there is no django package and yet Django is a popular Python based web framework. 

## Installation
```
pip install django-momoapi 
```

## Usage
```
TBD
```
## Development Setup

Clone the repository by running the following command in your terminal:
```
git clone https://github.com/mwanjajoel/django-momoapi

```
Create a Python virtual environment 

```
virtualenv venv

```

Activate the virtual environment by running the following command in your terminal:
```
source venv/bin/activate

```
Install the dependencies by running the following command in your terminal:
```
pip install -r requirements.txt

```

Create .env file following the .env_example file

```
cp .env_example .env

```

Create a Postgres database and add its credentials to the .env file
    
```
DB_NAME=<db_name>
DB_USER=<db_user>
DB_PASSWORD=<db_password>
DB_HOST=<db_host>
DB_PORT=<db_port>
```

Run migrations
```
python manage.py migrate

```

- Run application
```
python manage.py runserver

```

## Run tests
```
pytest

```
## Code Formatting using Black
```
black momo
```

## How to submit an issue

Please follow our [Bug Report Guide](ISSUE_TEMPLATE/BUG_REPORT.md) on how to submit your issue. 

## How to request for a new feature 

Please follow our [Feature Request Guide](ISSUE_TEMPLATE/FEATURE_REQUEST.md) on how to submit a feature request

## Code of Conduct 
We follow a strict code of conduct and you can read it [Here](CODE_OF_CONDUCT.md)

## Credits

Django MoMo API package was designed and built by Mwanja Joel. Django MoMo API is licensed under the MIT license; for the full license please see the [LICENSE](LICENSE) file. 

Please see the [AUTHORS](AUTHORS) file for the full list of contributors. 

If you find Django MoMo API useful and want to reach out, find me on Twitter: [@mrjoelmwanja](https://twitter.com/mrjoelmwanja).




