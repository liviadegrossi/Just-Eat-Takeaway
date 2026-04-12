<img width="8838" height="1488" alt="Logo of the Just Eat Takeaway.com company" src="https://github.com/user-attachments/assets/bdede2cd-a14f-4d04-9033-f3101dc7a2df" />

<!-- ADD BADGES HERE -->

# Code Assessment Instructions

The application should send a postcode to the JET API and return the restaurant data in an interface. The data must be filtered to return only the restaurant name, cuisines, rating (as a number), and address. The data can be displayed however you choose, such as a web interface or a console application. Regardless of the interface, the data should be limited to the first 10 restaurants returned, since the company is more interested in how the data is displayed than in a long list. It is worth noting that the API only works for UK postcodes and does not work for postcodes from any other country.

# Requirements

Considering the previous instructions, the following requirements were derived:

1. The system must accept a postcode as input from the user.
2. The system must validate the provided postcode (the postcode must be in a valid UK format).
3. The system must request the JET API for the list of restaurants based on the provided postcode.
4. The system must extract only the restaurant name, cuisines, rating (as a numeric value), and address from the list of restaurants.
5. The system must return the first 10 restaurants from the API response.
6. The system must display the filtered restaurant data to the user.


### Assumptions
**Assumption:** the system must display only 10 restaurant data at a time. Nevertheless, if the user decides, he/she could explore another 10 restaurant data. 

**Assumption:** a resturant does not include the cuisines: "Deals", "Collect stamps", "Alcohol", "Beauty", "Electronics", "Local Legends", "Pharmacy", "All Night Alcohol", "Groceries", "£8 off", "Your favourites", "Meal deal", "Cheeky Tuesday", "Shops"

### Improvements
**Improvement 1:** The system must include pagination and provide only 10 restaurant data at a time.

**Improvement 2:** To avoid too many requests, the API response must be cached. For each postcode, the API response is cached for 5 minutes.

<figure >
  <img width="1280" height="640" alt="main-interface" src="https://github.com/user-attachments/assets/256ff01c-b7a6-4543-865c-fbee13156065" />
  <figcaption style="text-align: center;"><b>Figure 1:</b> The main interface of the application.</figcaption>
</figure>
<p><br></p>
<p> </p>
<figure>
  <img width="1280" height="640" alt="list-restaurants" src="https://github.com/user-attachments/assets/edb63ce0-70c0-4e1d-a99d-022a851fa92b" />
  <figcaption style="text-align: center;"><b>Figure 2:</b> The list of restaurants, displaying the restaurant name, cuisines, rating, and address.</figcaption>
</figure>
<p><br></p>

# Installation and Setup Guide

To install and run the application, please follow the instructions detailed below.

## Prerequisites
1. Python 3.13
2. pip (Python package manager)

To verify the Python version:
```
python --version
```
## Download the repository
To run the application, you will need to download this repository to your local computer. 
1. In a browser, open this repository: https://github.com/liviadegrossi/Just-Eat-Takeaway
2. On the top right corner, click on the button ```<> Code```
<img width="439" height="83" alt="download-instructions-1" src="https://github.com/user-attachments/assets/b74cb7f1-5a47-4aff-a17b-84d2fc138859" />


3. At the bottom, click on ```Download ZIP```
<img width="438" height="303" alt="download-instructions-2" src="https://github.com/user-attachments/assets/ac2dcfd5-2049-455d-bc6d-dc6df1cdbcc0" />

4. Unzip the folder into a directory of your preference.

## Create a virtual environment (recommended)

The application has several dependencies that must be installed to run the application. It is recommended to create a virtual environment to isolate the application's dependencies from your computer's global Python setup. This way, you guarantee there will be no conflict. 

1. To create a virtual environment, open a command prompt and navigate to the directory where you unzipped the application.
   
``` cd <project-folder> ```

2. In the project directory, create the virtual environment by running

``` python -m venv venv ```

3. To activate the virtual environment, run the command

``` source venv/bin/activate ``` (on macOS/Linux)

``` venv\Scripts\activate  ``` (on Windows)

You should see a ``` (venv) ``` in the terminal.

## Install the dependencies

The application's dependencies are listed in the ``` requirements.txt ``` file. To install all required packages:

``` pip install -r requirements.txt  ```

## Apply migrations

Apply the Django migrations by running:

``` python manage.py migrate ```

## Run the development server

To start the Django development server, run

``` python manage.py runserver ```

By default, the application will be available at:

``` http://127.0.0.1:8000/ ```

You can copy and paste it to a browser of your preference.

# Technologies
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![Django](https://img.shields.io/badge/django-092E20?logo=django&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) 

# Developers

<img loading="lazy" width="160" height="160" alt="livia degrossi" src="https://github.com/user-attachments/assets/96f580f1-fac6-47ed-acd5-d28ab0af0947" />

[Lívia Degrossi](https://github.com/liviadegrossi) 








