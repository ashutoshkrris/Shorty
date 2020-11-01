![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
![GitHub stars](https://img.shields.io/github/stars/ashutoshkrris/Shorty?style=social)
![GitHub forks](https://img.shields.io/github/forks/ashutoshkrris/Shorty?style=social)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/ashutoshkrris/Shorty.svg)](https://GitHub.com/ashutoshkrris/Shorty/pull/)
![Hacktoberfest2020](https://img.shields.io/github/hacktoberfest/2020/badges/shields?label=hacktoberfest%202020)


# Shorty - URL Shortener :memo:

Shorty is a URL shortening service built using Django. This service includes user authentication as well as shortening service. The app also keeps tracks of URLs that you have already shortened and it can show you how many times that site has been visited using that link. In addition to shortening URLs, it will also auto-generate QR codes for the shortened links.

## Website Link :bookmark_tabs:

You can visit the site [here](http://.srty.me/) or http://srty.me

## Open Source :two_women_holding_hands::two_men_holding_hands:

This is a completely open sourced project. You can contribute to it if you want to add some feature or improve some feature. Feel free to create a pull request.

Please refer to the [instructions](https://github.com/ashutoshkrris/Shorty/blob/master/contributors/README.md) to get yourself added in the [Contributors](https://ashutoshkrris.github.io/Shorty/) page.

See you there!!

## Features :hearts:

- Custom/Random Short Link Generator(for everyone)
- Auto-generate QR Code(only for logged in users)
- User Authentication
  - Sign Up
  - Login
  - Change Password
  - Logout
- Keep track of all shortened URLs(only for logged in users)



## Working Demo :computer:

* **Homepage(before login)**

<img src="https://github.com/ashutoshkrris/Shorty/blob/master/demo/homepage.png" alt="Homepage" width=1000 height=500/>

* **Signup Page**

<img src="https://github.com/ashutoshkrris/Shorty/blob/master/demo/signup.png" alt="Signup Page" width=1000 height=500/>

* **Login Page**

<img src="https://github.com/ashutoshkrris/Shorty/blob/master/demo/login.png" alt="Login Page" width=1000 height=500/>

* **Homepage(after login)**

<img src="https://github.com/ashutoshkrris/Shorty/blob/master/demo/after_login.png" alt="Dashboard" width=1000 height=500/>

* **Dashboard/Shortener**

<img src="https://github.com/ashutoshkrris/Shorty/blob/master/demo/dashboard.png" alt="Dashboard" width=1000 height=500/>

* **Change Password**

<img src="https://github.com/ashutoshkrris/Shorty/blob/master/demo/password.png" alt="Dashboard" width=1000 height=500/>



## Getting Started

* [Fork this repository](https://github.com/ashutoshkrris/Shorty/fork) and clone the forked repository

* Change the working directory to the folder where you downloaded the files

* Install all the dependencies using the pip command :

  `pip install -r requirements.txt`

* After successful installation of all packages, run the follwing Django commands :
  
  `py manage.py migrate`

  `py manage.py runserver`

* Visit `127.0.0.1:8000` in your browser and enjoy the app.

Built using Django 3.1 and Python 3.8.5 by Ashutosh Krishna

Please don't forget to ⭐ the repository if you liked it.
