# Pair
#### a simple dhash duplicate image checker

## Installation

Recommended is to use `python3.10` or higher, this project is made using `python3.12` and the preferred version to use.

clone this repo in the desired location.\
Go into the cloned repo: `cd Pair`.\
Create a virtual environment using your preferred method i.e. using your IDE or via the commandline.\
Install the requirements: `pip install -r requirements.txt`\

## Dependencies

There are some dependencies present in the `requirements.txt`

- Pillow: For image manipulation and wide image support.

## Basic Example

To check a whole folder non-recursively:

````python
from storage import dupelicate

if __name__ == '__main__':
    dupelicate.find('path/to/your/folder')

````

this will print out the duplicates with a similarity value. In both the `Duplicate` and `Imagehash` class are some 
values you can change.

- `threshold`: How much of a pixel difference 2 images have to be, to be counted as being similar.
- `max_cores`: Maximum amount of cpu cores the program will use.
- `size`: the size of the resized image in pixels.

Keep in mind when changing the size of the hex will expand exponentially, change the threshold accordingly.


## inspiration
- [Implementation](https://www.hackerfactor.com/blog/index.php?/archives/529-Kind-of-Like-That.html)
