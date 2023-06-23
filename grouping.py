def grouping(total_group, df, concat_behavior):    
    
    #區分出可以被整除以及不能被整除的組別
    groups_count = Counter(df[concat_behavior])
    have_remainder = list()
    no_remainder = list()
    for i in groups_count:
        if groups_count[i]%total_group != 0:
            have_remainder.append(i)
        else:
            no_remainder.append(i)


    #創建一個df等等把分好的篩進去
    group_temp = pd.DataFrame()

    #不能被整除的組別分組
    for i in have_remainder:
        #叫出組別然後編號
        df_temp = df[df.groups == i]

        #計算用的info
        remainder = groups_count[i]%total_group #7
        avg_number = groups_count[i]-remainder #7260
        group_number = avg_number / total_group #330

        #一一塞進去group_temp
        for a in range(0,total_group):
            temp = df_temp[int(0+group_number*a):int(group_number*(a+1))]
            user_group = 'user_group {}'.format(a+1)
            temp_list = [user_group]*len(temp)
            temp['user_group'] = temp_list
            group_temp = pd.concat([group_temp,temp],axis=0)


        temp_df = df_temp
        for b in range(0,remainder):
            last_df = temp_df.tail(1)

            user_group_2 = 'user_group {}'.format(b+1)
            temp_list_2 = [user_group_2]*1
            last_df['user_group'] = temp_list_2
            temp_df = temp_df.iloc[:-1 , :]

            group_temp = pd.concat([group_temp,last_df], axis=0)

    #可以被整除的組別分組
    for i in no_remainder:
        #叫出組別然後編號
        df_temp = df[df.groups == i]

        #計算用的info
        remainder = groups_count[i]%total_group #7
        avg_number = groups_count[i]-remainder #7260
        group_number = avg_number / total_group #330

        #一一塞進去group_temp
        start=0
        for a in range(0,total_group):
            temp_3 = df_temp[int(0+group_number*a):int(group_number*(a+1))]
            user_group_3 = 'user_group {}'.format(a+1)
            temp_list_3 = [user_group_3]*len(temp_3)
            temp_3['user_group'] = temp_list_3
            group_temp = pd.concat([group_temp,temp_3],axis=0)  
    return group_temp
