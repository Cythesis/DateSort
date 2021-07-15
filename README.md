# DateSort

DateSort is a python script used to convert yearly values organized in square format to a single list.
![alt text](https://github.com/Cythesis/DateSort/blob/main/images/introduction.png?raw=true)

## Installation

[Python 3.9](https://www.python.org/downloads/) and Pandas is needed to use this script.

```bash
pip install pandas
```

## Usage

The script has x inputs:

### The file directory
This includes the name of the input file itself. The name of the input file alone is enough if the file is in the same directory.

### Sheet name
The name of the sheet being converted.
![alt text](https://github.com/Cythesis/DateSort/blob/main/images/sheetName.png?raw=true)

### The start and end year
The year range you would like the script to find

### Excel column of the year
The column which contains the year (column numbering start with 0)
![alt text](https://github.com/Cythesis/DateSort/blob/main/images/columnName.png?raw=true)

### Offset between the year and data
The cell offset between the year and data (difference)
![alt text](https://github.com/Cythesis/DateSort/blob/main/images/rowOffset.png?raw=true)

### The output column name
Any name desired.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

