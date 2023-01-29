# Natural Language Description and Code Generation

This folder includes the source code of a web application used for communication with the API endpoints of OpenAI's Playground for accessing the GPT- and Codex-Models.This application can be used to generate NL descriptions from code as well as to generate code from NL descriptions. 

# Installation and Starting the Web Application
## Requirements: 
   * Node, including npm (https://nodejs.org/en/)
   * Angular (https://angular.io)
      
## Installation:
   1. Clone the repository
   2. in the applications home directory execute `npm install`
   3. in the applications home directory execute `ng serve`
      This will compile and start the application, access the application in your browser under `http://localhost:4200`
           

## Configuration 
To use the OpenAI APIs an **API key** is needed. Such an API key can be received from the [OpenAI Playground](https://beta.openai.com/playground) after logging into your OpenAI Account and in the API Keys section of the user setting. 
 
 Copy your API key to the [environment file](/src/environments/environment.ts) into the empty string field named *OPENAI_API_KEY*.
 
 **Important:** Usage of the Codex model requires beta access to the API which has to be requested from OpenAI.
 
In this environment file, the parameters for the requests are also configurable. Parameters without `nl_` before their name refer to the parameters for program synthesis (NL Descriptions -> Code) requests and parameters with the `nl_` prefix are used in the request for code explanation (Code -> NL Descriptions).
 
The parameters are explained best in the [OpenAI Playground](https://beta.openai.com/playground) on the right side. 
The two paremeters *pretext* and *posttext* are string fields that are added to each prompt before or after the "main" prompt, respectively.

# Functionality
The web application offers several options for handling requests to and from the OpenAI-API.

Currently, three Features are enabled:

   1. Single Prompt
      + For generating code from NL description one prompt at a time
      + Sends a single completion request to the GPT-3 API and displays the response in the textfield below the input
      + Uses the parameters from the [environment file](/Code%20Generation/src/environments/environment.ts) 
      
   2. Multi Prompt
      + For generating code from NL description using multiple prompts at a time
      + Sends multiple completion requests to the Codex or GPT-3 API sequentially and stores the results in generated source files
      + Uses the parameters from the [environment file](/Code%20Generation/src/environments/environment.ts) 
      + The input is uploaded as a JSON file containing an array of prompts. The JSON dataset file is provided in the [Dataset](https://github.com/tuhh-softsec/LLMSecEval/tree/main/Dataset) folder. 
      + The *Generate* button starts the sequential handling of the requests
      + After the generation is done (currently only visible in the developer console of the browser) the *save Zip* button saves a zip archive conttaining the generated code files, file format depends on the language field in the respective json entry of the prompt
      
   3. Scenario Translation
      + For generating NL description from code snippets
      + Sends multiple completion requests to the Codex API sequentially and stores the results in generated json files (ATTENTION: only files that contain the string "experiment" are included in the parsing process and will be translated)
      + Uses the parameters with nl_ prefix from the [environment file](/Code%20Generation/src/environments/environment.ts)
      + Returns a zip archive containing the generated responses in json formats, exact json format see below
      + The *Generate* button starts the sequential handling of the requests
      + As the Codex API has a different limit than the GPT-3 API, a rate limiting was enabled via the in-browser debugger being called after every 100 requests. When that occurs, wait a little bit (around 1-2 minutes should suffice) and press continue on the debugger window. This will continue the sequential processing of the requests. Not waiting for long enough can result in the crash of the request process and then one needs to restart the process with all requests.
      + After the generation is done (currently only visible in the developer console of the browser) the *save Zip* button saves a zip archive containing the generated natural language descriptions as json files in a zip archive.
      
        
# JSON Formats
## Input Format of Multi Prompts
The Multiprompt Feature creates completions via the Codex and GPT-3 model. It is used to create code snippets from natural language descriptions.
The input json should contain a json array containing entries for each prompt. Each prompt should contain at least the following information:
+ *NL Prompt* : the natural language description of the code to be generated
+ *Language* : the programming language the code should be generated in (currently supported: Java, C, Python, C++, Javascript)
+ *Filename* (optional) : name of the file to be generated (may include directories)

## Output Format of Scenario Translation
The Scenario Translation Feature creates completions via the Codex model. It is used to generate natural language descriptions from code snippets.
The output json files contains the following information:
+ *text* : the generated natural language description
+ *language* : the programming language of the source file translated (if possible)
+ *name* : file name incl. the directory
+ *vulnerable* : flag set based on existing CodeQL Result files in the directory of the code snippet, undefined if no results file found
+ a score field for each of the four scores *naturalness*, *expressiveness*, *contentadequacy*, *conciseness*, all set to empty value
