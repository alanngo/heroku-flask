# Deploy Flask App to Heroku

## Deployment
https://ramen-flask-app.herokuapp.com/

### Prerequisites

##### General 
```bash
$ curl https://cli-assets.heroku.com/install.sh | sh
$ pip3 install gunicorn
```

##### MongoDB
```bash
$ pip3 install pymongo
$ pip3 install pymongo[srv]
$ pip3 install dnspython
```

### Deployment

Set up library requirements
```bash
$ pip3 freeze >> requirements.txt
```

Set up procfile, replace $1 w/ the name of your main flask app
```bash
$ echo "web: gunicorn app:$1" >> Procfile
```

#### Use git to push the app to heroku

Initialization
```bash
$ git init
$ git add .
$ git commit -m "init commit"
$ heroku login # it will open a browser window, enter email and password
$ heroku create
$ git push heroku master
```

Continuous
```bash
$ git pull heroku master
$ git add <FILES>
$ git commit -m "<MESSAGE>"
$ git push heroku master
```
