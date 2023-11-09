
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
    echo "Miniconda not found. Installing Miniconda..."
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -O ~/miniconda.sh
    bash ~/miniconda.sh -b -p $HOME/miniconda
    rm ~/miniconda.sh
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