## Data Data Data

![obligatory morpheus](https://c1.staticflickr.com/6/5218/5497866713_8d32e6098a_z.jpg)

The one stop shop to helping us make better decisions about our members

### Heroku deployment
- Add remote url
   - https://git.heroku.com/botfrey.git
- Deploy to heroku
   - `deploy`
   
### Run Server
- `flask run`

### Run Script
- `python app.py`

### Dependencies
- Python3 
   - Recommended to use virtualenv to handle environment
- [Direnv](https://direnv.net/)
    - copy `.envrc_SAMPLE` => `.envrv` and enter values to variables
    - run `direnv allow` to load env variables
- `pip install -r requirements.txt`