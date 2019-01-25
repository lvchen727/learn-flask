# learn-flask
Learning flask through building projects


## What is Flask?

Flask is a web app framework written in Python. Web framework represents a collection of libraries and modules for developing webs without worrying about low-level details such as protocols, thread management etc.


## Set up
```
pip install virtualenv
cd proj-repo
virtualenv venv
. venv/bin/activate  #activate environment
pip install Flask. #install Flask for proj-repo env
```

## Projects

### 1. [blog-app](flask-tutorial/)

### 2. [microblog-heroku](https://github.com/lvchen727/microblog-heroku)


## References

- [flask tutorial](https://www.tutorialspoint.com/flask/index.htm)
- [flask website](http://flask.pocoo.org/docs/1.0/tutorial/layout/)


## Other good tutorials notes

-  [The Hitchhiker’s Guide to Python](https://docs.python-guide.org/)
-  [heroku vs aws](https://www.cleveroad.com/blog/heroku-vs-aws--which-cloud-based-solution-to-choose-)
-  [The Flask Mega](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world-legacy)
-  [sublime cheatsheet](http://docs.sublimetext.info/en/latest/reference/keyboard_shortcuts_osx.html)

## cheatsheet

shutdown virtualenv: ```deactivate```

To freeze current environment: ```pip freeze > requirements.txt```

install all packages ```pip install -r requirements.txt```

find heroku app name ``` heroku info -s | grep web_url | cut -d= -f2```

find jobs running python ```ps -fA | grep python```
