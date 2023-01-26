# ChatGPT in a Panel App

## How to run?

1. Get your OpenAI API key from openai.com and add your keys to a .env file like so:
```
APIKEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

2. Set up a virtual environment using venv and activate it
```
$ pip install virtualenv
$ python -m venv .venv
$ source ./.venv/bin/activate
```

3. Install needed packages: 
```
$ pip install openai
$ pip install panel
$ pip install jupyterlab
```

4. Run Panel dashboard:\
```
$ panel serve panel_openai_text_completion.ipynb
```




