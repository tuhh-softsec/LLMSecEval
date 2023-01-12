


## Usage of DB Creation Scripts
The scripts to creating the codeql databases work the same for the different languages to be generated.
The available languages are C (create_db_c.sh), Python(create_db_python.sh) and Java(create_db_java.sh). For the diff
Create CodeQL-dbs by invoking the shell scripts with two command line parameters.
The first parameter is the path to the source root of the files under analysis, relative to "../Data/Synth/".
The second parameter is the name the created db should be given. It will be created in the folder the script is executed in.
### Example
sh create_db_python.sh Codex/py/1 pythontest


## Usage of DB Analysis Scripts
The script for analysis of codeQL databases can be used for any previously created database, independently of language.
The script requires three command line parameters:
The first parameter is the name of the query set to be executed.
The second parameter is the path to the database, relative to "~/Repositories/master-thesis/Analysis/".
The third parameter is the output path for the results.

The results will be printed in csv format.

#### Example 

sh analyse_db.sh ../../codeql/python/ql/src/codeql-suites/python-security-extended.qls pythontest Results/pythontest.csv
