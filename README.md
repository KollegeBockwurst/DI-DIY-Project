# Data Integration Project - DIY
# Who claps the most?

## Structure

This data integration project has four components: preparation, data
integration, data cleaning, and showcase.

- `0_datasets`: Contains the datasets used for our analysis.
- `1_preparation`: Code to extract and load the datasets into a common space. Contains code to fetch data from the API.
- `2_integration`: Experiments to integrate your datasets and a program that
  implements your final integration pipeline.
- `3_cleaning`: Experiments to clean your integrated dataset and a program that
  implements your final data cleaning pipeline.
- `3_showcase`: Code to implement your showcase. You can already run it against
  the results of your data integration pipeline, and, finally, against your
integrated and cleaned data.

## Used Data
### API Dokumentations- und Informationssystem für Parlamentsmaterialien (DIP)
DIP provides an API to find protocols of parliament sessions. The sessions can be searched by date, election period and other meta data. 
Source: [https://dip.bundestag.de/%C3%BCber-dip/hilfe/api#content](https://dip.bundestag.de/%C3%BCber-dip/hilfe/api#content)
Some of the available data is structured in .xml files, at least all sessions from 19th election period.

### Parliament member data
Deutscher Bundestag provides a huge dataset on all (former) members of Deutscher Bundestag, including a curriclum vita. The data is structured in .xml format and ordered alphabetically.
Source: [https://www.bundestag.de/resource/blob/472878/9851584d7baf44bb3ada0ebe745a35e1/MdB-Stammdaten-data.zip](https://www.bundestag.de/resource/blob/472878/9851584d7baf44bb3ada0ebe745a35e1/MdB-Stammdaten-data.zip)

## Importing data from Bundestag API
/1_preparation/import.ipynb contains a function named 'bundestag_search(resourcetype, wahlperiode)', wich ask the bundestag API for a list of all fitting file ids.
'plenarprotokoll' is the resource type we are looking for, election_period is 19 in the proof of concept.

The ids can be hand over to the function 'bundestag_xml', wich will then download the session protocol as .xml file (if available and not already downloaded). The function will save the files in '0_datasets/bundestag'

Pay attention to eventual rate limits of the API, these are not documented by DIP.

## Data integration
/2_integration/integration.ipynb contains functions to read and interprete the xml files downloaded in step 1. The second cell of the Jupyter notebook will use these functions 
for all session files in /0_datasets/bundestag and concats the results. The result (=integrated data) is saved to multiple .csv files. The relational data represents the ER-model you can find in "2_integration/who claps the most.pdf"

Please notice that the used intergration algorithms still need a lot improvement, gathered data is not trustworthy.

The algorithms count different events during the parliament sessions. This is an overview of different events and their indices:
0: Beifall (claps)
1: Zwischenruf
2: Lachen
3: Zuruf
4: Widerspruch'
5: Heiterkeit

Parties are also represented by an index:
0: CDU/CSU
1: SPD
2: BÜNDNIS 90/DIE GRÜNEN
3: FDP
4: AfD
5: DIE LINKE

## Showcases
/3_showcase/showcase.py provides different functions with take the integrated data and primarily count the number of events that happend, filtered by different showcases.
It also executes these functions for some scenarios by reading the files from the previous step and writing the result to '3_showcase/df_result.csv'. This file basically
contains a list of all deputies of the 19th election period and the total number of events happend with their participation along different other properties.  
Examples: see '/3_showcase/Who clpas the most_showcase.pdf'

## Disclaimer
this documentation is incomplete and still needs some updates
Please notice that the provided algorithms still need a lot improvement, gathered data is not trustworthy.