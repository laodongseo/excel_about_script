need_cols = ['AA','BB','CC']
df = pd.DataFrame(np.random.randint(80, 120, size=(6, 4)),
			  columns=pd.MultiIndex.from_product([['English','Chinese'],['Y','N']]))



wai_cols = set((df.columns.get_level_values(0)))
for wai_col in wai_cols:
	df_duo_data = df[wai_col].copy() # 外层索引 是df数据
	nei_cols = df_duo_data.columns.tolist() # df数据的表头是内层索引

	# 添加缺失的列
	add_cols = set(need_cols) -set(nei_cols)
	for add_col in add_cols:
		df_duo_data[add_col] = 0

	# 构造二维索引
	mulindex = pd.MultiIndex.from_product([[wai_col],df_duo_data.columns.tolist()])
	df_duo_data.columns=mulindex
	print(df_duo_data)
