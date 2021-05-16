
# <center>CI Framework</center> #

## Creating the template file ##

Created the GitHub Actions template inside the project root directory **“.github/workflows”**, and after that I created a YAML file inside that directory with the workflow template.

GitHub will run the workflow on every commits and pull requests on the branch main/master.

    on:
    push:
        branches: 
        - master
        - main
    pull_request:
        branches: 
        - master
        - main

## Install dependencies ##

Installing all the dependencies including the ones in **"requirements.txt"** 
and **algorithms** package to run the tests and see coverage

    - name: Install dependencies
        run: |
            cd docs
            python -m pip install --upgrade pip
            python -m pip install flake8 pytest
            pip install algorithms
            if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

## Running tests and coverage ##

Running all the unittest and pytests. See the coverage report and save it as an html files in */htmlcov* directory.

    - name: Run Unit Tests and generate coverage report
        run: |
            python3 -m unittest discover tests
            coverage run -m pytest
            coverage report
            coverage html
    - name: Archive code coverage html report
        uses: actions/upload-artifact@v2
        with:
            name: code-coverage-report
            path: htmlcov

## Incident with github actions ##

There's currently an issue with github actions, which makes all the workflows queued. **Date: 5/16/21**

You can see the related picture with name *github_action_issue.png*