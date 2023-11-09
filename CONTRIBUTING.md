## Setup
To start contributing to this project, run the following in the project root folder:
```zsh
chmod +x ./mac-setup.sh
./mac-setup.sh
```

### 📌 Pre-commit

To ensure our standards, make sure to install pre-commit before starting to contribute.

```bash
pre-commit install
```

### 🧹 Linting

We use `ruff` to lint our code. You can run the linter by running the following command:

```bash
ruff pandasai examples
```

Make sure that the linter does not report any errors or warnings before submitting a pull request.

### Code Format with `black`

We use `black` to reformat the code by running the following command:

```bash
black pandasai 
```

### 🧪 Testing

We use `pytest` to test our code. You can run the tests by running the following command:

```bash
poetry run pytest
```

Make sure that all tests pass before submitting a pull request.
