# Coding Assignment – RickAndMorty Integration

#### Task description:
In file with name - Integrations_HA.pdf


#### Setup:

##### Please, create virtualenv and activate it and run:
    1. pip install -r requirements.txt
	2. uvicorn sample:app --reload

#### REST API:
##### Implement a REST API with the following capabilities:
1. GET /fetch-data/ - get all content in and save it in three separate JSON files
2. GET /episode-names/{start_year}/{end_year} - return the list of episode released between some years

#### OpenAPI/Swagger Specification:
Provide a detailed specification of the API in OpenAPI/Swagger format - http://0.0.0.0:8000/docs
