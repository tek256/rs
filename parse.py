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

def merge_files(dst, filepath):
    result = list()
    with open(filepath, 'r') as infile:
        result.extend(json.load(infile))

    with open(dst, 'w') as output:
        json.dump(result, output);



file_count = len(sys.argv) - 1
drop_dict = {}
result = list()

for f in range(1, len(sys.argv)):
    result.extend(parse_file(sys.argv[f], drop_dict))
    print(sys.argv[f])
    if(file_count > 1):
        with open("combined.json", 'w') as output:
            json.dump(result, output)

pretty_print(drop_dict)
