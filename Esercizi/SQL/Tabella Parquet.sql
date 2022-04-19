-- Creazione tabella in Parquet

 CREATE TABLE database_esempio.nuova_tabella_parquet( 
   `id` string,                                
   `altro_campo` string,                
   `campo_timestamp` timestamp,                   
   `campo_date` date,                          
   `altra_date` date)                            
 PARTITIONED BY (                                   
  `colonna_da_partitioning` string)
 STORED AS PARQUET;

-- Inserire il contenuto di una tabella dentro un altra

INSERT INTO tabella_da_riempire
SELECT * FROM tabella_con_i_dati;

