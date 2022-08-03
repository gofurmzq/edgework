import pandas as pd

df = pd.read_csv ("src/flask_api/models/inventory_activity.csv")
clear_df = df[df.columns[1:4]]

df_json = {}
len_row = len(clear_df['ActivityType'])
for row in range(len_row):
    activity_type = clear_df['ActivityType'][row]
    item_no = clear_df['ItemNo'][row]
    quantity = clear_df['Quantity'][row]
    if df_json and item_no in df_json:
        if activity_type in df_json[item_no]:
            update_quantity = df_json[item_no][activity_type]
            df_json[item_no][activity_type] = update_quantity + quantity
        else:
            df_json[item_no][activity_type] = quantity
    else:
        df_json[item_no] = {activity_type : quantity}

