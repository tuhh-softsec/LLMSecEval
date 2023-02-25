We can use Codeql to evaluate the generated code snippets for security vulnerabilities. This folder contained CodeQL queries that can detect 18 out of the top 25 CWEs of 2021 in code.

### Requirements

To run this, CodeQL CLI needs to be installed on your system. The instructions to installation can be found [here](https://codeql.github.com/docs/codeql-cli/getting-started-with-the-codeql-cli/)

## Workflow of CodeQL
CodeQL treats code like data. Software vulnerabilities are found in code by executing queries (one specific software vulnerability = one specific query)
on a database representation of the code. To do so, first this database representation of the code files under scope of analysis have to be created. Then queries or query sets can be run against the database. The results of the queries will be printed to a result file.

## Usage of DB Creation Scripts
The scripts to create the codeql databases work the same for the different languages to be generated.
The available languages are C (create_db_c.sh), Python(create_db_python.sh) and Java(create_db_java.sh).
Create CodeQL-dbs by invoking the shell scripts with two command line parameters.
The first parameter is the path to the source root of the files under analysis.
The second parameter is the name the created db should be given. It will be created in the folder the script is executed in.
### Example

`sh create_db_python.sh ~/Codebase python_example_db`


## Usage of DB Analysis Scripts
The script for analysis of codeQL databases can be used for any previously created database, independently of language.
The script requires three command line parameters:
The first parameter is the name of the query set to be executed.
The second parameter is the path to the database.
The third parameter is the output path for the results.

The results will be printed in csv format.

#### Example 

`sh analyse_db.sh Queries/py/top25/python-top25.qls python_example_db ~/Results/python_results_sec_extended.csv`
