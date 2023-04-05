# import sys
# sys.path.append("../")
# import refinitiv.data.eikon as ek
# import refinitiv.data as rd
# import datetime as dt
# import pandas as pd
# import requests
# import json




# def get_anbima():
  
#   link_IRFM  = "https://adata-precos-prod.s3.amazonaws.com/arquivos/indices-historico/IRFM-HISTORICO.xls"
#   link_IMAB5 = "https://adata-precos-prod.s3.amazonaws.com/arquivos/indices-historico/IMAB5-HISTORICO.xls"
#   link_IHFA  = "https://adata-precos-prod.s3.amazonaws.com/arquivos/indices-historico/IHFA-HISTORICO.xls"
  
#   links = [link_IRFM,link_IMAB5,link_IHFA]
  
#   file_path_loads = ["data/raw/12_tabela_anbima_irfm.xls",
#                     "data/raw/12_tabela_anbima_imab5.xls",
#                     "data/raw/12_tabela_anbima_ihfa.xls"]

#   i = 0
#   for link in links: 
#       resp = requests.get(link)
#       with open(file_path_loads[i],"wb") as output:
#           output.write(resp.content)
#           i = i+1

# def consulta_bc(codigo_bcb):
#     url = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.{}/dados?formato=json'.format(codigo_bcb)
#     df = pd.read_json(url)
#     df['data'] = pd.to_datetime(df['data'], dayfirst=True)
#     df.set_index('data', inplace=True)
#     return df
  
# def get_cdi():
  
#   #get the cdi dataframe
#   df_cdi = consulta_bc(12)
#   file_path_load = "data/raw/12_tabela_bacen_cdi.csv"
  
#   # #Define new Feature Column df_cdi
#   df_cdi["data"] = df_cdi.index
  
#   df_cdi.to_csv(file_path_load,index=False)
#   return df_cdi

# def get_bolsa():
  
#   #gET THE aPP KEY
#   with open("credentials/refinitv.json") as f:
#     info = json.load(f)
#   APP_KEY = info["APP_KEY"]    
#   #print(APP_KEY)
#   #Get the Datetime
#   start_date = "2013-01-01"
#   end_date = dt.datetime.strftime(dt.datetime.today(),"%Y-%m-%d")
  
#   rd.open_session(app_key=APP_KEY)
#   instrumentos = [".IFIX",".BVSP",".SP500"]
#   ts = pd.DataFrame()
#   df = pd.DataFrame()
#   for r in instrumentos:
#     try:
#         ts = ek.get_timeseries(r,'CLOSE',start_date=start_date,end_date=end_date,interval='daily')
#         ts.rename(columns = {'CLOSE': r}, inplace = True)
#         if len(ts):
#             df = pd.concat([df, ts], axis=1)
#         else:
#             df = ts
#     except:
#         pass
#   rd.close_session()
  
#   #Add Data from index to column
#   df["data"] = df.index
#   file_path_load = "data/raw/12_tabela_refiniv_bolsa.csv"
#   df.to_csv(file_path_load,index=False)