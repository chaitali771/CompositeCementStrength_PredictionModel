from src.data_ingestion import data_ingestion

def main():  #function def 
  # step1 :data ingestion
  df = data_ingestion()
  print(df.head())


main()       #function calling