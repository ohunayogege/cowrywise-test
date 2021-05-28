### How to install

`git clone https://github.com/ohunayogege/cowrywise-test.git`

`cd cowrywise`

Create a new environment
`python -m venv env`

Activate the environment
`source env/Source/activate` or `env\Source\activate` (Windows)
`source env/bin/activate` on Ubuntu/Linux

Install requirements
`pip install -r requirements.txt`

Run app
`python manage.py runserver`

Call the endpoint using GET request.
`http://localhost:8000/fetch_key/`

