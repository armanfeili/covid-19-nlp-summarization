# Generating and Summarizing worldwide Covid-19 reports using Abstractive and Extractive NLP
This project provides the facility of generating a quick and meaningful summary to make it possible for all readers to get notified about their country's Covid-19 condition just by taking a glance at a single paragraph.

The scientific paper for this code is available at the following link:
https://www.linkedin.com/in/arman-feili-89b622132/details/featured/1635517655517/single-media-viewer/?profileId=ACoAACB73HcBYrHj3VrRAoEZHyPHciZet35eNrg

## Step-1
Download all necessary CSV files from the links below and put the files in the sources folder.

Download [owid-covid-data.csv] from:
https://github.com/owid/covid-19-data/blob/master/public/data/owid-covid-data.csv

Download the following files:
[by-sex.csv]
[by-age.csv]
[demographics.csv]
[health.csv]
[index.csv]
[oxford-government-response.csv]
[hospitalizations.csv]

From:
https://health.google.com/covid-19/open-data/raw-data

Place all CSV files in the 'sources' directory.

## Step-2
Download and install the following python dependencies:
pandas,
spacy,
transformers,
happytransformer,
collections,
pytorch,
tensorflow

## Step-3
Run the 'covid-19-report-generator.ipynb' file in the jupyter editor and execute every cell one by one.


