import json
import sys

def dict_contains(test_dict, test_value):
    for key in test_dict:
        if key == test_value:
            return True
    return False

def parse_file(file_location, dictionary):
    with open(file_location) as json_file:
        data = json.load(json_file)

    for row in data:
        data_type = row['eventId']
        if not dict_contains(dictionary, data_type):
            item_dict = {}

            for drop in row['drops']:
                item_dict[drop['id']] = drop['qty']

            dictionary[data_type] = item_dict
        else:
            item_dict = dictionary[data_type]

            for drop in row['drops']:
                d_id = drop['id']
                d_qty = drop['qty']

                if dict_contains(item_dict, d_id):
                    value = item_dict[d_id] + d_qty
                    item_dict[d_id] = value
                else:
                    item_dict[d_id] = d_qty
            dictionary[data_type] = item_dict

    return data


def pretty_print(dictionary):
    with open('rsitems.json') as f:
        rs_list = json.load(f)

        for key, row in dictionary.items():
            print("--", key, "--")
            for item_id, qty in row.items():
                item_name = ''
                for rs_key, rs_row in rs_list.items():
                    if int(rs_key) == item_id:
                        item_name = rs_row['name']
                        break
                print(item_name, ":", qty)   


def pretty_output(dict, output_path):
    with open('rsitems.json') as f:
        rs_list = json.load(f)

    out_file = open(output_path, "w")
    for key, row in dict.items():
        out_file.write(f"\n-- {key} --\n")
        for item_id, qty in row.items():
            item_name = ''
            for rs_key, rs_row in rs_list.items():
                if int(rs_key) == item_id:
                    item_name = rs_row['name']
                    break
            out_file.write(f"{item_name}: {qty}\n") 
    

# --- CONFIGURATION --- 
# If to combine json files
combine_data = True

# If to output results to a text file for future reference
output_path = "output.txt"
output_to_file = True

# If to output to terminal/command line
output_to_cmd = True

# --- END OF CONFIGURATION --- 

# Calculated things (not configuration)
file_count = len(sys.argv) - 1
drop_dict = {}
result = list()

# For each file passed on the command line
for f in range(1, len(sys.argv)):
    # If multiple files and combining 
    if(file_count > 1 and combine_data):
        # Parse file and add to resulting json array
        result.extend(parse_file(sys.argv[f], drop_dict))
    else:
        parse_file(sys.argv[f], drop_dict)

# Write the combined data
if(combine_data and file_count > 1):
    with open("combined.json", 'w') as output:
            json.dump(result, output)

# If we should output to the command line 
if(output_to_cmd):
    pretty_print(drop_dict)

# If we should output to file
if(output_to_file):
    pretty_output(drop_dict, output_path)
