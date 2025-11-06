# Anime Recommender System
## Description
ARS is a flask application that uses a kNN recommendation algorithm to generate recommendations based on a chosen series. It uses the MyAnimeList API to display series details such as anime titles, posters, etc. 
The dataset was extracted from Kaggle ("https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database/code") and as such may not be up to date - It is recommended that you only search for series made before 2018.

## Setup Instructions

Create and activate a python virtual environment and run the following to install the required dependencies:

```bash
pip install -r requirements.txt
```

Once done, run the flask application via:

```bash
py app.py
```
and open localhost in the browser to access the system. From there you can search any series to get its details, scroll down, and click on the next series.

## Skills Learned and Implemented
- Learned to serve an ML model via a REST API
- Learned to work with very large datasets with limited system resources
- Learned to train kNN models for multivariate outputs
- Additional JavaScript Skills (i.e API requests, database calls for search bars, etc)

## Future Changes
- Adding an expanded dataset
- Updating the project CSS
- Creating a age-filtered seperate model.
