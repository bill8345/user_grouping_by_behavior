def drop_function(drop_df, target_num):
    drop_num = len(drop_df) - target_num
    temp_df = drop_df.tail(int(drop_num))
    return temp_df
