# devrant-dl
💾 Get a dump of your entire history on devRant

People frequently come and go from [devRant](https://devrant.com), but must leave their data behind due to the platform's lack of a data export tool. `devrant_dl` is a community tool designed to fix that problem.

## Installation
To install `devrant_dl`, make sure both `python3` and `python3-pip` are installed on your machine, then run:
```sh
# Install
pip3 install devrant_dl

# View help
devrant_dl -h
```

## Usage
```
usage: devrant_dl [-h] [--rants-only] username output

Download all of your devRant account data

positional arguments:
  username              The (valid) username of your account
  output                An (empty) directory to dump your data into

optional arguments:
  -h, --help            show this help message and exit
  --rants-only          Only download rants
```