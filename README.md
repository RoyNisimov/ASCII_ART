# ASCII Art CLI
A simple CLI for creating ASCII art.

# Installation
Use `git clone https://github.com/RoyNisimov/ASCII_ART`
and then do: `pip install -r requirements.txt`

# Usage
Run main.py with the flags you want
```
usage: main.py [-h] [--in_f IN_F] [--out OUT] [--sf SF] [--charset CHARSET] [--font FONT] [--font_size FONT_SIZE] [--density_algorithm {Average,Luminance}]

Simple CLI to create ASCII art

optional arguments:
  -h, --help            show this help message and exit
  --in_f IN_F           The input filepath
  --out OUT             The output filepath
  --sf SF               The scale factor
  --charset CHARSET     The charset used
  --font FONT           The font
  --font_size FONT_SIZE
                        The font size
  --density_algorithm {Average,Luminance}
                        How to calculate the density
```

