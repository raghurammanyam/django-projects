from tabula import read_pdf,convert_into
df = read_pdf("/home/hp/carat/hh.pdf",stream=True,sep='|',squeeze =True,header=None,pages="2")
a=df.iloc[0:44,0:3]
#convert_into("/home/hp/carat/2012.pdf", "ooa.csv", output_format="csv")
df.to_csv("gan.csv",index=False)
print(a)
print("-------------------------------------------------------------------------------------------------------")
print(df)


