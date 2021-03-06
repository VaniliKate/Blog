####  FLASK BLOG

This site allows writers to write blogs and readers to read, engage and react to the blogs. Also shows a quote every time the site is loaded.

#### By **Vanili Kate**

## Description

This site allows writers to pour themselves out and write blogs and readers to read, engage and react to the blogs. Also shows an inspirational quote every time the site is loaded.

## Setup/Installation Requirements

### Requirements
* Postgresql

### Setup
* Clone the repo `git clone https://github.com/VaniliKate/Blog.git`
* Move into the directory `cd Blog`
* Create a virtual environment `python -m venv virtual`
* Open `start.sh` file and replace what's inside the <> with your email address, password and a `SQLALCHEMY_DATABASE_URI` from psql db created.\
See more on how to construct `SQLALCHEMY_DATABASE_URI` here -> https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/#connection-uri-format
* Run `python manage.py db init` to initialize a psql db.
* Run `python manage.py db migrate` to make the psql database migrations.
* Run `python manage.py db upgrade` to upgrade the psql db version to the latest with the migrated changes.
* To run the application `./start.sh`
## Technologies Used

* HTML
* CSS
* Bootstrap
* Flask
* Postgresql

### MIT License

Copyright (c) 2022 Blog

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
Copyright (c) {2022} **Vanili Kate**
