## Usage
- Copy / Clone repository onto computer  
- Make sure Python 3 is installed (download [here](https://www.python.org/downloads/))
- Copy JSON data file(s) into folder
- In powershell navigate to folder (`cd insert/path/here/`)
- run `./parse.py data1.json ... datan.json`

## Tips
You can configure the script to combine data or not (not will be faster) as well as if to output the results to file (output.txt), what to name the output file, and if to output to command line. 

## Notes
If powershell gives you an error saying `cmdlet` not found, then run the following command: `$env:PATHEXT += ";.py"`. This will allow powershell to run python scripts as executables.

The script will combine all data passed as arguments into combined.json

If you want to configure the script manually, look for `CONFIGURATION` in the source code (parse.py)!
