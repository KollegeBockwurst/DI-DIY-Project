# Data Integration Project - DIY
# Who claps the most?

This repository serves as template for the students project accompanying the
"Data Integration" lecture at University of Marburg.

Students can
[fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) or copy
this repository to kick-start their project.

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

## Documentation
### API Dokumentations- und Informationssystem für Parlamentsmaterialien (DIP)
DIP provides an API to find protocols of parliament sessions. The sessions can be searched by date, election period and other meta data. 
Source: [https://dip.bundestag.de/%C3%BCber-dip/hilfe/api#content](https://dip.bundestag.de/%C3%BCber-dip/hilfe/api#content)

### Parliament member data
Deutscher Bundestag provides a huge dataset on all (former) members of Deutscher Bundestag, including a curriclum vita. The data is structured in .xml format and ordered alphabetically.
Source: [https://www.bundestag.de/resource/blob/472878/9851584d7baf44bb3ada0ebe745a35e1/MdB-Stammdaten-data.zip](https://www.bundestag.de/resource/blob/472878/9851584d7baf44bb3ada0ebe745a35e1/MdB-Stammdaten-data.zip)

