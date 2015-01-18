[![Build Status](https://travis-ci.org/mnewsome/penny-for-your-thoughts.svg?branch=master)](https://travis-ci.org/mnewsome/penny-for-your-thoughts)

## Penny for Your Thoughts

A web application/fundraiser for help support Alzheimer's Diesease research and awareness.

###Prepare

You will need the following installed:
  -[pip](https://pypi.python.org/pypi/pip)
  -[virtualenv](https://virtualenv.pypa.io/en/latest/)
  -[autoenv](https://github.com/kennethreitz/autoenv)

  I also highly recommend [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/) for automatically activating your Virtualenv. However, this is not needed.

###Install

1. Clone the repo
  `git clone git@github.com:mnewsome/penny-for-your-thoughts.git`

2. cd into the project

3. Create a .env file
    You can use the [.env.example](https://github.com/mnewsome/penny-for-your-thoughts/blob/master/.env.example) file to get started. **Make sure to remove the .example extension so that your .env file is not committed.**

4. Install dependencies
  `pip insall -r requirements.txt`
