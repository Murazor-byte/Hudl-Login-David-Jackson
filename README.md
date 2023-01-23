# Hudl Login Verification
Technical Project for Hudl's QA Engineer I - 2023 May Graduates - David Jackson

Authors: David Jackson

## Introduction
This project is designed to create an automation testing suite verifiying Hudl's login page. This project was created as a test for the next round in the interview process for Hudls QA Engineering for May 2023 Graduates.

## Technologies
* Selenium Framework
* Python 3.9.12
* Chrome Webdriver

## Setup
To run this project, install it locally on your device

The webdriver used to run the suites is the 'ChromeDriver'.
If you do not have this already installed on your machine you can find it [here](https://chromedriver.chromium.org/downloads)

* For Installation, select the correct release based on the version of Chrome installed on your machine and store it at a location of your choosing
  

For testing purposes, an active account is required to accuracetly run the testing suite. So a valid username and password are needed to pass the tests. Your login information and the PATH to your chrome webdriver will need to be inputted to run. To do this change the fields within the 'constants.py' file based on your requirements:
* 'CHROME_WEBDRIVER_PATH' - to the absolute path of your chrome webdriver
* 'USERNAME' - to your account username
* 'PASSWORD' - to your account password

To run the tests, simply run the main.py file by typing

`python main.py`

(Depending on what version of python you have installed.)

## Features
There are twelve test cases within the suite, testing for various edge cases for Hudl's login verification.

The structure of the project allows for seamless integration of additional test cases - if needed - through the helper classes of 'element.py' and 'page.py' for reusability.
