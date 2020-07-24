# Github Actions

## pre-commit hooks

### What is a Pre-Commit Hook?

Pre-commit hooks are a simple way to check your code for any issues before committing your code to Github. It could be something as simple as removing extra spaces from the end of a file to verifying that the code you want to commit is valid Python or does not contain any secrets or access tokens. Pre-Commit Hooks can be written in a number of languages including Python, Ruby, and Rust but we're going to focus on Python for this demo. 

###  Setup

##### With `pip`

`pip install pre-commit`
or 
`pip3 install pre-commit`


##### With `conda`

`conda install -c conda-forge pre-commit`


### Pre-Written Hooks

One of the most useful aspects is the ability to easily use pre-written hooks in your own repo. 


##### Adding Pre-Commit Hooks to your Repo

To add, you create a file called `.pre-commit-config.yaml` and save it in the root of your repo.    

Example: 

repos:
-   repo: https://github.com/path-to-repo-with-hook # url to repo containing hook.       
    rev: v2.3.0       
    hooks: # list of hooks to use.  
    -   id: hook-i-want.  
        description: Looks at file size, max set to 250kb.    
        args: [--maxkb=250].  


### Examples of Useful Pre-Commit Hooks

Examples and notes in `.pre-commit-config.yaml`

### Custom Pre-Commit-Hooks

### Using Hooks

Add the `.pre-commit-config.yaml` to the root of your directory.      
Create a `requirements.txt` file and add `pre-commit`.       
run `pre-commit install` from the root of your repo on the command line to add the hooks to your `.git/`.     

### More Resources

[More Information on Hooks](https://githooks.com/)

[More Pre-Built Pre-Commit Hooks](https://github.com/pre-commit/pre-commit-hooks)


