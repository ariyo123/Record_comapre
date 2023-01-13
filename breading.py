import pandas as pd
df1 = pd.read_csv("bvn_data.txt.csv")

df2 = pd.read_csv("icad_data.txt.csv")
print(df1)
print(df2)


common_df = pd.merge(df1, df2, on='BVN', how='inner')
print(common_df)
common_df.rename(columns={'first_name_y': 'first_name'}, inplace=True)
common_df.rename(columns={'Middle_name_y': 'Middle_name'}, inplace=True)
common_df.rename(columns={'Surname_y': 'Surname'}, inplace=True)
common_df.rename(columns={'DOB_y': 'DOB'}, inplace=True)
common_df.rename(columns={'account': 'Account'}, inplace=True)
common_df.rename(columns={'bank': 'bank'}, inplace=True)
print(common_df)
df = common_df.drop_duplicates(subset=['BVN']).reset_index(drop=True)
df = df.drop(['first_name_x', 'Middle_name_x', 'Surname_x', 'DOB_x'], axis=1, inplace=False)


print(df)

df.to_csv('icad_data_final.csv', index=False)

common_df1 = pd.merge(df1, df2, on='BVN', how='inner')
common_df1.rename(columns={'first_name_x': 'first_name'}, inplace=True)
common_df1.rename(columns={'Middle_name_x': 'Middle_name'}, inplace=True)
common_df1.rename(columns={'Surname_x': 'Surname'}, inplace=True)
common_df1.rename(columns={'DOB_x': 'DOB'}, inplace=True)
common_df1.rename(columns={'account': 'Account'}, inplace=True)
common_df1.rename(columns={'bank': 'bank'}, inplace=True)
print(common_df1)
df = common_df1.drop_duplicates(subset=['BVN']).reset_index(drop=True)

df = df.drop(['first_name_y', 'Middle_name_y', 'Surname_y', 'DOB_y', 'Account', 'Bank'], axis=1, inplace=False)
print(df)

df.to_csv('bvn_data_final.csv', index=False)