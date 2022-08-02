from .dto import clean_result
import json

def retrieve_activity(path_file):
    import pandas as pd
    df = pd.read_csv(path_file)
    
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
    clean_df = clean_result(df_json)
    keys_clean = clean_df.keys()
    item_list = []
    stock_in_list = []
    stock_out_list = []
    grand_total_list = []
    index_list = []
    value_sum = []
    for i in range(4):
        if i < 3:
            item_list.append(list(keys_clean)[i])
            stock_in_list.append(clean_df[item_list[i]]['Stock In'])
            stock_out_list.append(clean_df[item_list[i]]['Stock Out'])
            grand_total_list.append(clean_df[item_list[i]][list(clean_df[item_list[i]].keys())[2]])
            index_list.append(i)
            if i == 0:
                value_sum.append('Grand Total')
            else:
                value_sum.append(clean_df[list(keys_clean)[2+i]])    
        else:
            value_sum.append(clean_df[list(keys_clean)[2+i]]) 

    data = [[item_list[0], stock_in_list[0], stock_out_list[0], grand_total_list[0]], \
        [item_list[2], stock_in_list[2], stock_out_list[2], grand_total_list[2]], \
        [item_list[1], stock_in_list[1], stock_out_list[1], grand_total_list[1]], \
        [value_sum[0], value_sum[1],value_sum[2], value_sum[3]]]
    
    df = pd.DataFrame(data, columns=['ItemNo', 'Stock In', 'Stock Out', 'Grand Total'])
    
    return df
    
    