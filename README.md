## Usage
- Copy / Clone repository onto computer  
- Make sure Python 3 is installed  
- Copy JSON data file(s) into folder
- In powershell navigate to folder (`cd insert/path/here/`)
- run `./parse.py data1.json ... datan.json`
## NOTE
If powershell gives you an error saying `cmdlet` not found, then run the following command: `$env:PATHEXT += ";.py"`. This will allow powershell to run python scripts as executables.

The script will combine all data passed as arguments into combined.json
