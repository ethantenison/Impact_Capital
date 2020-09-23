import pandas as pd
import os

try:
	df = pd.read_csv('data/full_index.csv')
except FileNotFoundError:
	raise FileNotFoundError('Run the extract_eins.ipynb notebook to create the necessary index files')


def lookup(ein=None, tax_year=None):
	cond = True
	if ein is not None:
		cond = cond & df['EIN'] == ein
	if tax_year is not None:
		cond = cond & df['TAX_YEAR'] == tax_year

	if cond == True:
		# df.loc will error if we pass it just `True` so we must cope first
		return df
	
	return df.loc[cond]
