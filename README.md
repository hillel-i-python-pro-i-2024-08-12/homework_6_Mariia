# homework_6_Mariia
This project generates a list of humans, each with a name and group association, and organizes this data into a readable format. The output displays the names and number of members in each group. The project uses the Faker library to generate random human names and group names, with logic to assign members to random groups and print the organized results.
## Installation
If Poetry is not installed:
For PowerShell (Windows):
```
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```
For Linux:
```
curl -sSL https://install.python-poetry.org | python3 -
```
After cloning the repository, initialize the virtual environment with:
```
poetry shell
```
Then, install project dependencies with:
```
poetry install
```

## Running with poetry
To run the project using Poetry, use:
```
poetry run python main.py
```
## Running with docker
To run the project using Docker, use:
```
make d-homework-i-run
```
To purge all data related to the services, use:
```
make d-homework-i-purge
```

## Linting
To set up the hooks for linting, run:

```
pre-commit install
```
To manually run pre-commit hooks, use:
```
pre-commit run --all-files
```
