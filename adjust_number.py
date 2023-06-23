from drop import *

def adjust(df, total_group, total_user_number):  
    #計算現在的每組人數，區分成要減少、要增加的組與不變的組
    user_group_count = Counter(df['user_group'])
    drop_group = list()
    add_on_group = list()
    no_change_group = list()
    for i in user_group_count:
        if user_group_count[i] > int(len(df)/total_group):
            drop_group.append(i)
        elif user_group_count[i] < int(len(df)/total_group):
            add_on_group.append(i)
        else:
            no_change_group.append(i)

    need_drop_df = pd.DataFrame()
    need_add_df = pd.DataFrame()
    no_change_df = pd.DataFrame()

    for i in drop_group:
        temp_1 = df[df.user_group == i]
        need_drop_df = pd.concat([need_drop_df, temp_1])
    for j in add_on_group:
        temp_2 = df[df.user_group == j]
        need_add_df = pd.concat([need_add_df, temp_2])
    for k in no_change_group:   
        temp_3 = df[df.user_group == k]
        no_change_df = pd.concat([no_change_df, temp_3])
        
    df_finally = pd.DataFrame()

    #準備一個df來裝每組多出來的
    df_supply = pd.DataFrame()
    target_num = total_user_number/total_group

    for i in drop_group:
        temp = df[df.user_group == i]
        df_supply = pd.concat([df_supply,drop_function(temp, target_num)],axis=0)

    #把有多出來的組別中多出來的人數踢掉
    for j in drop_group:
        temp = need_drop_df[need_drop_df.user_group == j]
        drop_num = len(temp) - target_num
        temp = temp.iloc[:-int(drop_num) , :]
        df_finally = pd.concat([df_finally, temp])

    #少的組別補人進去
    for k in add_on_group:
        temp_1 = need_add_df[need_add_df.user_group == k]
        add_num = target_num - len(temp_1)

        #從最後面開始抓人進去
        temp_2 = df_supply.tail(int(add_num))
        temp_1 = temp_1.append(temp_2, ignore_index = True)

        temp_list = [k]*len(temp_1)
        temp_1['user_group'] = temp_list

        df_finally = pd.concat([df_finally, temp_1],axis=0)

        #把補過的人從supply當中刪掉，避免同一個人被捕兩次
        df_supply = df_supply.iloc[:-int(add_num),:]

    #把不用作任何變動的組別放到最終的df中
    for l in no_change_group:
        temp = no_change_df[no_change_df.user_group == l]
        df_finally = pd.concat([df_finally, temp], axis=0)
    return df_finally
