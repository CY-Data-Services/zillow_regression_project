# Zillow Regression Project

### Author: Corey Solitaire, Ryvyn Young

## Description: 
- Build, fit, and train a regression model to predict single unit property tax assessment value

## Instructions for Replication
Files are located in Git Repo [here](https://github.com/CY-Data-Services/zillow_regression_project)
User will need env.py file with access to Codeup database 

## Domain Research:

**What is a single unit property?**     
By James Chen Updated Sep 11, 2020 What Is a Housing Unit?

The term housing unit refers to a single unit within a larger structure that can be used by an individual or household to eat, sleep, and live. The unit can be in any type of residence such as a house, apartment, mobile home, or may also be a single unit in a group of rooms. Essentially, a housing unit is deemed to be a separate living quarter where the occupants live and eat separately from other residents of the structure or building. They also have direct access from the building's exterior or through a common hallway.
- https://www.investopedia.com/terms/h/housingunits.asp

**What is 'fips'?**
This code is use to identify US counties by assigning a number to each county. To look up the county corresponding to the fips number in the dataset add the leading 0 and ignore the decimal. A chart of fips codes can be found [here](https://www.nrcs.usda.gov/wps/portal/nrcs/detail/national/home/?cid=nrcs143_013697)
- https://en.wikipedia.org/wiki/FIPS_county_code


## Key Findings

1. **Top 5 drivers of property tax assessment value (RMSE)**
- bathroomcnt
- calculatedfinishedsquarefeet
- bedroomcnt
- garage
- zip_cc

2. **Top Model = Polynomial Features**
- With 5 Features (above) and (degree = 2)
- Avg. RMSE of $447039.41
- 31% Improvement over baseline

3. **Additional Reporting**
- What state and county are these properties in?
All properties are located in California, USA   
06037 = Los Angles county   
06059 = Orange county   
06111 = Ventura county   

- Tax Rate for each property
Summary of Overall Tax Rate Information
Min rate = .014%
Max rate = 8.9%
mean rate = 1.3%
median rate = 1.2%

- Distribution of tax rates for each county
![](https://github.com/CY-Data-Services/zillow_regression_project/blob/main/Zillow%20Regression%20Project/visuals/generated_graphics/tax_by_county.png)


- How much does the tax rate vary by county?
![](https://github.com/CY-Data-Services/zillow_regression_project/blob/main/Zillow%20Regression%20Project/visuals/generated_graphics/Screen%20Shot%202020-10-07%20at%208.51.30%20PM.png)

- What tax rate do the bulk of the properties sit around?
  - 1st quartile tax rate percentage: 1.16%
  - 3rd quartile tax rate percentage: 1.35%



###### Next Steps    
Investigate impact of further reducing outliers with regards to calculated tax rate   
Investigate impact of feature engineering using combine features    
  - Example: combine bedrooms and bathrooms into single feature column 


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
| **Feature**                  | **Definition**                                         |
| ---                          | ---                                                    |
| bathroomcnt                  | # of bathrooms in home                                 |
| bedroomcnt                   | # of bedrooms in home                                  |
| calculatedfinishedsquarefeet | calculated square footage                              |
| garage                       | 1 : Yes, 0 : No                                        |
| fips                         | Code to identify US counties                           |
| fireplace                    | 1 : Yes, 0 : No                                        |
| hottub_spa                   | 1 : Yes, 0 : No                                        |
| latitude                     | Angular distance north or south of the earth's equator |
| longitude                    | Geographic coordinate, east–west position on the Earth |
| lotsizesquarefeet            | lot size in square feet                                |
| poolcnt                      | 1 : Yes, 0 : No                                        |
| roomcnt                      | # of rooms in home                                     |
| taxamount 	                 | Amount paid in taxes in dollars                        |
| year                         | year of construction                                   |
| zip                          | zip code                                               |
| useid                        | property land use code                                 |
| year_cc                      | year of construction (.cat)                            |
| zip_cc                       | zip code (.cat)                                        |
| useid_cc                     | property land use code                                 |
 
  ---                            ---                                                    
| **Target**                   | **Definition**                                         |
| ---                          | ---                                                    |
| taxvaluedollarcnt            | Tax value in dollars                                   |
***
## Planning Stage
Project Description: 
- This project looks to predict home price between the month of May and June 2017 using a variety of home features
  found on the zillow 

GOALS:
- Need a way to predict the values of single unit properties between the months of May and June 2017.

MVP Questions to answer:
- What are the drivers of single unit property values (Model Features)
- How do you know that these drivers have signficiance (Significance Tests)

Audience: 
- Zillow Data Science Team 

Setting: 
- Professional

Brainstorm: 

## Acquire Stage
DELIVERABLES: 
- Acquire a df of single unit property values between May and June 2017
- Define single unit property

## Preparation Stage
DELIVERABLES:
- Clean dataset that is split and scaled in to train, validate, and test

## Exploration and Pre-Processing Stage
DELIVERABLES: 
- Distribution of Tax Rates per County 
- Data Visualization
- Statistical Test
  - Chi Squared Test for Independence 

## Modeling Stage
DELIVERABLES: 
- Regression model built on property data between May and June 2017

## Delivery Stage
DELIVERABLES: 
- [Presentation](https://docs.google.com/presentation/d/1O1oWwpjngXqnWylhtI1CFIcE8Nl13MardtJ5TaAJ7oo/edit?usp=sharing)
- [Main_Notebook]()
- [Additional_Information]()
