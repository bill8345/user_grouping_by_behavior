# Description
Divided users into several groups which have the same composition for user characteristics.
# Requirement module
- import pandas
- import numpy
- from collections import Counter
# The information of the modules in this repo
This repo has two modules, grouping and adjust_number.
1. __*grouping(total_group, df, concat_behavior)*__
   - _total_group_: the number of groups you want to get.
   - _df_: pandas DataFrame including the user you want to divide and all user characteristics you want to keep.
   - _concat_behavior_: the name of the column that included the concat-value of all user characteristics.
2. __*adjust(df, total_group, total_user_number)*__
   - _df_: the pandas DataFrame you want to adjust.
   - _total_group_: the number of groups you want to get.
   - _total_user_number_: The original number of all users.
# How to use it
First, you need to import these two modules, grouping and adjust_number. 
You need to prepare a pandas DataFrame including the user you want to divide and all user characteristics you want to keep because we use pandas DataFrame to group the user. Then, you need to create a new column that included the new value which is the concat-value of all user characteristics.

You must use the module of grouping first then use the module of adjust_number to adjust the user amount.
- The module of grouping can divide users into several groups which have the same composition for user behavior but do not have the same user amount.
- The module of adjust_number can help to adjust the number of users in each group to equal.

