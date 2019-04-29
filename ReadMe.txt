1. Starting the Server

Windows - python 3
-> enter into flaskenv virtualenv (virtualenv.bat) or create your own with requirements.txt
-> type "flask run" into cmd window

if everything fails at this point then the project can be remade by 
-> deleting the app/app.db file
-> deleting the migration file found in migrations/versions
	enter virtualenv at top of file structure
-> flask db migrate -m "create"  (should recreate the database and migration file)
-> flask db upgrade		 (update the database structure)
-> python app/update_database.py (repopulate the database)


Test the API with 
-> cd app
-> python _TEST.py 


Overview

This is an application built in Flask-Sqlalchemy, using the Flask-Migrate wrapper to integrate the alembic database versioning structure

app.models -> 		database models:
				Products - 	product id, 
						price 
						vat_band

				VatRates - 	vat_band
						vat_rate
					  (I thought it would be best to leave these tables split so additional bands can be added easily and 
					  rates can be adjusted on the fly)

				ExchangeRates -	country_code
						exchange_rate
						last_updated
					(This table is prepopulated with a list of the usable country codes taken from the exchange rate API
					this allows the country_code to be cheched as it enters the database,
					This table also acts as a Cache as it is timestamped every update, and any rates younger than a time
					limit do not need to be recalled from the API

				ApiKeys -   	name
					   	api_key
						url
					(literally just a place to store API keys if the project requires more than one.  In a real project the keys would
					be encrypted as they were stored in the database)


app.routes -> 		API stored here, checks for json data and returns output if currency not specified, 
	      		otherwise sends request with currency code to app.exchange_rate
app.exchange_rate ->	If currency code matches ones stored in the db, then get_exchange_rate() chacks if there is an exchange rate 
			stored for that code in the db and if it is less than a day old. If so then it is returned, otherwise a new 
			exchange rate is generated using the exchange_rate_api() and it is stored in the database and the timestamp
			updated automatically
app.update_database ->  used to populate the database with data pulled from the json files within json_data


2. If I had more time, I would clean up the API code to make fewer database calls and make it more resilient/reactionary to junk inputs,
   It would probably also make sense to add a form to the frontend of the framework where testing could be done from a browser

3. The toughest part was probably setting up the environment so all the separate parts worked together, it was a bit of a hassle getting alembic to work properly.
   Im most proud of the fact that I got it to run fairly well despite not using flask-sqlalchemy before.

4. The test seems fine, maybe would be more rewarding to do connect the backend to some frontend, a graph or form or something to make it visually more interesing


