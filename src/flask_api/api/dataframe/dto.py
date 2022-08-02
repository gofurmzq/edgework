import json

def clean_result(path_file):
    result_kopi = path_file['Kopi']['Stock In'] + path_file['Kopi']['Stock Out']
    result_teh  = path_file['Teh']['Stock In'] + path_file['Teh']['Stock Out']
    result_susu = path_file['Susu']['Stock In'] + path_file['Susu']['Stock Out']
    

    path_file['Kopi']['Grand Total Kopi'] = result_kopi
    path_file['Teh']['Grand Total Teh'] = result_teh
    path_file['Susu']['Grand Total Susu'] = result_susu

    grand_stock_in = path_file['Kopi']['Stock In'] + path_file['Teh']['Stock In'] + path_file['Susu']['Stock In']
    grand_stock_out  = path_file['Kopi']['Stock Out'] + path_file['Teh']['Stock Out'] + path_file['Susu']['Stock Out']
      
    grand_total = result_kopi + result_teh + result_susu
    
    clear_activity = {}
    clear_activity = path_file
    clear_activity['grand_stock_in'] = grand_stock_in
    clear_activity['grand_stock_out'] = grand_stock_out
    clear_activity['grand_total']  = grand_total
    
    return clear_activity