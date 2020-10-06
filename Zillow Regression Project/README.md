# Zillow Regression Project

### Author: Corey Solitaire, Ryvyn Young

## Description: 
Zillow Regression Project

## Project Organization

Generated with [ryans_codeup_data_science_mvp](https://github.com/RyanMcCall/ryans_codeup_data_science_mvp)

Modified from [datasciencemvp](https://github.com/cliffclive/datasciencemvp/)

```
├── README.md               <- The top-level README for developers using this project.
│
├── data                    <- All of the data for the project
│   ├── modeling            <- The prepared, processed and split datasets for modeling.
│   ├── prepared            <- The prepared datasets for exploration
│   └── raw                 <- The original, immutable data
│
├── main.py                 <- The main python script that calls all src scripts
│
├── mvp.ipynb               <- The main notebook for the project
│
├── src                     <- The source code for use in this project
│   ├── __init__.py         <- Makes src a Python module
│   ├── acquire.py          <- The script to download or generate data and store it in
│   │                          data/raw/
│   ├── explore.py          <- The script for creating any visuals that need to be stored
│   │                          in visuals/generated_graphics/
│   ├── model.py            <- The script for preprocessing, modeling, and interpreting
│   └── prepare.py          <- The script for preparing the raw data and storing it in
│                              data/prepared/
│
└── visuals                 <- All project visuals
    ├── external_visuals    <- Visuals brought from outside the project
    ├── generated_graphics  <- Visuals generated from the project
    └── presentation        <- A copy of your presentation
```

## Data Dictionary
  ---                            ---
| **Feature**                  | **Definition**            |
| ---                          | ---                       |
| bathroomcnt                  | # of bathrooms in home    |
| bedroomcnt                   | # of bedrooms in home     |
| calculatedfinishedsquarefeet | calculated square footage |
| fireplace                    | 1 : Yes, 0 : No           |
| garage                       | 1 : Yes, 0 : No           |
| hottub_spa                   | 1 : Yes, 0 : No           |
| lotsizesquarefeet            | lot size in square feet   |
| poolcnt                      | 1 : Yes, 0 : No           |
| roomcnt                      | # of rooms in home        |
| year                         | year of construction      |
| zip                          | zip code                  |
| useid                        | property land use code    |

  ---                            ---
| **Target**                   | **Definition**            |
| ---                          | ---                       |
| taxvaluedollarcnt            | Tax value in Dollars      |