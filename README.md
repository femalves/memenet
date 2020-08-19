<p align="center">

  <img alt="GitHub Language Count" src="https://img.shields.io/github/languages/count/femalves/memenet?style=flat-square" />
  <img alt="GitHub Top Language" src="https://img.shields.io/github/languages/top/femalves/memenet?style=flat-square" />
  <img alt="" src="https://img.shields.io/github/repo-size/femalves/memenet?style=flat-square" />
  <img alt="GitHub Last Commit" src="https://img.shields.io/github/last-commit/femalves/memenet?style=flat-square" />
  <img alt="License" src="https://img.shields.io/badge/license-MIT-blueviolet?style=flat-square">

</p>

___
<br>

![Memenet](https://user-images.githubusercontent.com/9547354/90655392-e27a1c00-e217-11ea-8683-93cb9ed96247.gif)
![Memenet](https://user-images.githubusercontent.com/9547354/90655401-e5750c80-e217-11ea-9286-27ad148f23ce.gif)
![Memenet](https://user-images.githubusercontent.com/9547354/90655410-e7d76680-e217-11ea-8282-2f4c038f8034.gif)
![Memenet](https://user-images.githubusercontent.com/9547354/90655417-e9a12a00-e217-11ea-9fb4-e032bfd7aa23.gif)

## :japanese_ogre: Demo Web

[Visit demo website](https://memesbyfernanda.herokuapp.com/)

## :computer: Tecnologies used

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Redis](https://www.redis.io/)


### :books: Other Libs

- [Django Crispy Forms](https://github.com/django-crispy-forms/django-crispy-forms)
- [JQuery](https://jquery.com/)
- [Pillow](https://pillow.readthedocs.io/en/stable/)
- [Markdown](https://pypi.org/project/django-markdown/)
- [Whitenoise](http://whitenoise.evans.io/en/stable/)

### :rocket: Deployed to [Heroku](http://www.heroku.com/)

### :nail_care: Styling

- [Font Awesome](https://fontawesome.com/)
- [Bootstrap](https://getbootstrap.com/)

### :gear: Functionalities
- Complete Auth (Register, Login, Logout, Recover password)
- Edit profile
- Upload image from other pages
- Social Network (Like/Unlike, Follow/Unfollow, Activities Feed) 
- Forms 
- Django admin page


### :running: How to run

```bash

# Clone this repository
$ git clone https://github.com/femalves/memenet

# From the terminal, go to folder
$ cd memenet

# Create and run virtual environment
$ virtualenv env
$ source env/bin/activate

# Install dependencies
$ pip install -r requirements.txt

# Run migrations
$ python manage.py makemigrations
$ python manage.py migrate

# Start local server
$ python manage.py runserver

# Go to http://localhost:8000

```
## :memo: License

[MIT](LICENSE)
