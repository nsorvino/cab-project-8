#! /usr/bin/python3

"""
This is an example Flask | Python | Psycopg2 | PostgreSQL
application that connects to the 7dbs database from Chapter 2 of
_Seven Databases in Seven Weeks Second Edition_
by Luc Perkins with Eric Redmond and Jim R. Wilson.
The CSC 315 Virtual Machine is assumed.

John DeGood
degoodj@tcnj.edu
The College of New Jersey
Spring 2020

----

One-Time Installation

You must perform this one-time installation in the CSC 315 VM:

# install python pip and psycopg2 packages
sudo pacman -Syu
sudo pacman -S python-pip python-psycopg2

# install flask
pip install flask

----

Usage

To run the Flask application, simply execute:

export FLASK_APP=app.py 
flask run
# then browse to http://127.0.0.1:5000/

----

References

Flask documentation:  
https://flask.palletsprojects.com/  

Psycopg documentation:
https://www.psycopg.org/

This example code is derived from:
https://www.postgresqltutorial.com/postgresql-python/
https://scoutapm.com/blog/python-flask-tutorial-getting-started-with-flask
https://www.geeksforgeeks.org/python-using-for-loop-in-flask/
"""

import psycopg2
from config import config
from flask import Flask, render_template, request

# Connect to the PostgreSQL database server
def connect(query):
    conn = None
    try:
        # read connection parameters
        params = config()
 
        # connect to the PostgreSQL server
        print('Connecting to the %s database...' % (params['database']))
        conn = psycopg2.connect(**params)
        print('Connected.')
      
        # create a cursor
        cur = conn.cursor()
        
        # execute a query using fetchall()
        cur.execute(query)
        rows = cur.fetchall()

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
    # return the query result from fetchall()
    return rows
 
# app.py
app = Flask(__name__)

# serve form web page
@app.route("/")
def form():
    counties = connect("SELECT DISTINCT cname FROM county ORDER BY cname")
    return render_template('my-form.html', counties = counties)





# handle average gas price query and serve result web page
@app.route('/avg-gas-price', methods=['POST'])
def avg_gas_price():
    county = request.form['county']
    rows = connect("SELECT average_gas_price FROM Gas_Prices_View WHERE cName = '{0}';".format(county))
    heads = ['Average Gas Price']
    return render_template('my-result.html', rows=rows, heads=heads)

# handle percentage of workers who use public transportation query and serve result web page
@app.route('/workers-public-transport', methods=['POST'])
def workers_public_transport():
    county = request.form['county']
    rows = connect("SELECT pct_public_transport FROM Transportation_View WHERE cName = '{0}';".format(county))
    heads = ['Percentages of Public Transport']
    return render_template('my-result.html', rows=rows, heads=heads)

# handle percentage of population in poverty query and serve result web page
@app.route('/population-in-poverty', methods=['POST'])
def population_in_poverty():
    county = request.form['county']
    rows = connect("SELECT pct_population_in_poverty FROM Poverty_View WHERE cName = '{0}';".format(county))
    heads = ['Percent of Population in Poverty']
    return render_template('my-result.html', rows=rows, heads=heads)

# handle total number of housing units query and serve result web page
@app.route('/total-housing-units', methods=['POST'])
def total_housing_units():
    county = request.form['county']
    rows = connect("SELECT total_housing_units FROM Housing_Density_View WHERE cName = '{0}';".format(county))
    heads = ['Housing Units']
    return render_template('my-result.html', rows=rows, heads=heads)

# handle EV charging station density query and serve result web page
@app.route('/ev-station-density', methods=['POST'])
def ev_station_density():
    county = request.form['county']
    rows = connect("SELECT charging_station_density FROM EV_Station_Density_View WHERE cName = '{0}';".format(county))
    heads = ['Charging Station Density']
    return render_template('my-result.html', rows=rows, heads=heads)

#handle population density POST and serve result web page
@app.route('/population-density', methods=['POST'])
def population_density():
    rows = connect("SELECT population_density FROM Population_Density_View WHERE cName = '" + request.form['county'] + "';")
    heads = ['Population Density']
    return render_template('my-result.html', rows=rows, heads=heads)

#handle percentage of workers who walk or bike to work POST and serve result web page
@app.route('/bike-walk-to-work', methods=['POST'])
def bike_walk_to_work():
    rows = connect("SELECT pct_bicycle, pct_walk FROM Commuting_View WHERE cName = '" + request.form['county'] + "';")
    heads = ['Percent of Bicycle Riders', 'Percent of Walkers']
    return render_template('my-result.html', rows=rows, heads=heads)

#handle median household income POST and serve result web page
@app.route('/median-household-income', methods=['POST'])
def median_household_income():
    rows = connect("SELECT median_household_income FROM Income_View WHERE cName = '" + request.form['county'] + "';")
    heads = ['Median Household Income']
    return render_template('my-result.html', rows=rows, heads=heads)

#handle EV charging stations POST and serve result web page
@app.route('/ev-charging-stations', methods=['POST'])
def ev_charging_stations():
    rows = connect("SELECT num_of_stations FROM EV_Station_Availability_View WHERE cName = '" + request.form['county'] + "';")
    heads = ['Number of Charging Stations']
    return render_template('my-result.html', rows=rows, heads=heads)

#handle public transportation and total housing units POST and serve result web page
@app.route('/public-transportation-housing', methods=['POST'])
def public_transportation_housing():
    rows = connect("SELECT pct_public_transport, total_housing_units FROM Transportation_Housing_View WHERE cName = '" + request.form['county'] + "';")
    heads = ['pct_public_transport', 'total_housing_units']
    return render_template('my-result.html', rows=rows, heads=heads)


# handle venue POST and serve result web page
@app.route('/venue-handler', methods=['POST'])
def venue_handler():
    rows = connect('SELECT venue_id, title FROM events WHERE venue_id = ' + request.form['venue_id'] + ';')
    heads = ['venue_id', 'title']
    return render_template('my-result.html', rows=rows, heads=heads)

# handle query POST and serve result web page
@app.route('/query-handler', methods=['POST'])
def query_handler():
    rows = connect(request.form['query'])
    return render_template('my-result.html', rows=rows)

if __name__ == '__main__':
    app.run(debug = True)
