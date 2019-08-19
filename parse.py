import json


def dict_contains(test_dict, test_value):
    for key in test_dict:
        if key == test_value:
            return True
    return False


with open('data.json') as json_file:
    data = json.load(json_file)
    unique_events = {}

    for row in data:
        data_type = row['eventId']
        if not dict_contains(unique_events, data_type):
            item_dict = {}

            for drop in row['drops']:
                item_dict[drop['id']] = drop['qty']

            unique_events[data_type] = item_dict
        else:
            item_dict = unique_events[data_type]

            for drop in row['drops']:
                d_id = drop['id']
                d_qty = drop['qty']

                if dict_contains(item_dict, d_id):
                    value = item_dict[d_id] + d_qty
                    item_dict[d_id] = value
                else:
                    item_dict[d_id] = d_qty
            unique_events[data_type] = item_dict

    with open('rsitems.json') as f:
        rs_list = json.load(f)

        for key, row in unique_events.items():
            print("--", key, "--")
            for item_id, qty in row.items():
                item_name = ''
                for rs_key, rs_row in rs_list.items():
                    if int(rs_key) == item_id:
                        item_name = rs_row['name']
                        break
                print(item_name, ":", qty)
