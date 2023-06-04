import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color_data = data.Primary_Fur_Color.to_list()

fur_dict = [{'color': 'Gray',
            "count": 0},
            {'color': 'Cinnamon',
            "count": 0},
            {'color': 'Black',
            "count": 0}

            ]
for color in fur_color_data:
    if color == 'Gray':
        fur_dict[0]['count'] += 1
    if color == 'Black':
        fur_dict[2]['count'] += 1
    if color == 'Cinnamon':
        fur_dict[1]['count'] += 1

fur_table  = pandas.DataFrame(fur_dict)
fur_table.to_csv("fur_table.csv")




