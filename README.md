# 🔍 Let's find the hotsposts 🔴

First of all, we'll use a couple of tools in our analysis:

### Code Maat
Code Maat is a command line tool used to mine and analyze data from version-control systems. It works offline on your local machine.

Here you can find the github repo:
https://github.com/adamtornhill/code-maat

It's an executable jar (so you'll need Java to run it) that you can find in the codemaat directory.

You can run it by typing:

``` cmd
java -jar code-maat-0.8.5-standalone.jar
```

### Python
We'll use a couple of Pyhton scripts (that you can find in the script directory) to manipulate data and to start a lightweight http server for the visualization part.

You'll need Python installed on your machine. 
Both Python3 and Python2.

You can refer to the official website (https://www.python.org/) for installation instruction.
Take a look also at PyEnv (https://github.com/pyenv/pyenv) since you'll need to handle multiple versions of Python.

###  So here we are, let's start the investigation on our codebase 🔍

## 1 - Extract information with git log

Clone the repository you want to investigate if you haven't already done so.

Go inside the main directory of the repo and run this command:

``` cmd
git log --pretty=format:'[%h] %an %ad %s' --date=short --numstat > evolution_git.log
```
With this command we're extracting the git commit logs, formatting them and saving them to a file `evolution_git.log`.

If you want you can play with temporal windows here, for example 
``` cmd
git log --pretty=format:'[%h] %an %ad %s' --date=short --numstat  --before=2024-01-01 > evolution_git.log
```
will extract only the commits before 2024.

## 2 - Use Code Maat to get the revisions informations

Now that we have our `evolution_git.log` file we can use Code Maat to perform anlysis on it and extract informations about change frequiencies.

## 3 - Extract complexity using SonarQube

## 4 - Merging complexity and effort

## 5 - Creating the data for the visualization

## 6 - Visualize the hotspots in our codebase