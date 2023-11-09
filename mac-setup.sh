
#!/bin/bash

# Check if Git is installed
if ! command -v git &> /dev/null
then
    echo "Git not found. Installing Git..."
    brew install git
fi

# Check if Miniconda is installed
if ! command -v conda &> /dev/null
then
    brew install miniconda
fi

# Check if Miniconda is in PATH
if ! command -v conda &> /dev/null
then
    #zshrc case
    if [ -f ~/.zshrc ]
    then
        echo "Miniconda not found in PATH. Adding Miniconda to PATH..."
        echo "export PATH=$HOME/miniconda/bin:$PATH" >> ~/.zshrc
        source ~/.zshrc
    fi
    if [ -f ~/.bashrc ]
    then
        echo "Miniconda not found in PATH. Adding Miniconda to PATH..."
        echo "export PATH=$HOME/miniconda/bin:$PATH" >> ~/.bashrc
        source ~/.bashrc
    fi
fi

conda create -n ee114 python=3.10
conda activate ee114
pip install poetry
poetry install --no-root

pre-commit install