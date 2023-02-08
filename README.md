# Wikipiedia-Fetcher-with-FastAPI-and-AWS-App-Runner

## Overview

This is a microservice that fetches Wikipedia entries. This allows you to:
1. Search for existing entries by providing partial keyword
2. Fetch description by entering full keyword

## Usage
- To run loacally:
    
    Type in `make install` in the terminal.This will install all the packages needed.
    
    To search for word "Benedict": `./cli-fire.py search_wiki "Benedict"`
    
    To get description of "Benedict Cumberbatch": `./cli-fire.py wiki "Benedict Cumberbatch"`
    
    
- To run on the server:
    
    Type in `make all` in the terminal.
    
    This will install all the packages needed and run it on port 8080.
    
    Open it in a web brower and you can see a simple message:
    `{"message":"Hi, this is a wikipedia API. Call /search or /fetch"}`
    ### Search
    
    Here is an example for searching for entries:
    ```
    https://sherry-ma-didactic-sniffle-5r4jpr95799fxpj-8080.preview.app.github.dev/search/benedict
    ```
    
    And the output will be:
    ```
    {"Entries":["Benedict","Pope Benedict XVI","Benedict Cumberbatch","Dirk Benedict","Benedict Wong","Pope Benedict","Benedict Arnold","Eggs     Benedict","Paul Benedict","Benedict of Nursia"]}
    ```
    
    ### Fetch
    Here is an example for fetching descriptions:
    ```
    https://sherry-ma-didactic-sniffle-5r4jpr95799fxpj-8080.preview.app.github.dev/fetch/Benedict%20Cumberbatch
    ```
    And the output will be:
    ```
  {"Result":"Benedict Timothy Carlton Cumberbatch  (born 19 July 1976) is an English actor."}
    ```
    - To run the microservice on AWS APP Runner, go to
    
    https://v6xr4krcmd.us-east-1.awsapprunner.com 




## Reference

https://fastapi.tiangolo.com/

