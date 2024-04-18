avg_vol = get_avg(df_cha, 2010)
Q5_ANSWER = avg_vol['tsla_vol']
print(f"Q5_ANSWER:{Q5_ANSWER}")
Q5_ANSWER = '?'

avg_vol_2008 = get_avg(df_cha, 2008)
avg_vol_2018 = get_avg(df_cha, 2018)
Q6_ANSWER = round(avg_vol_2008['v_vol'] / avg_vol_2018['v_vol'], 1)
Q6_ANSWER = '?'

tsla_2010 = df_cha.loc['2010', 'tsla']
#print(tsla_2010)
Q7_ANSWER = tsla_2010.dropna().shape[0]
print(f"Q7_ANSWER:{Q7_ANSWER}")
Q7_ANSWER = '?'
