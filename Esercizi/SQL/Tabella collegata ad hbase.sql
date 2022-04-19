--Tabella esempio, collegata ad hbase

CREATE EXTERNAL TABLE tabella_esempio(
id string, --CAMPO NECESSARIO
valore_timestamp timestamp, --CAMPO NECESSARIO
altro_campo string,
altro_campo1 string
)
ROW FORMAT SERDE -- Per indicare che è una tabella collegata ad Hbase
'org.apache.hadoop.hive.hbase.HBaseSerDe'
STORED BY -- Per indicare che è una tabella collegata ad Hbase
'org.apache.hadoop.hive.hbase.HBaseStorageHandler'
WITH SERDEPROPERTIES ( --Qui bisogna effettuare il mapping tra le colonne della tabella hbase e i campi della tabella
'hbase.columns.mapping'=':key,:timestamp, attr:altro_campo,attr:altroc_campo1,', 'serialization.format'='1')
TBLPROPERTIES (
'COLUMN_STATS_ACCURATE'='{\"BASIC_STATS\":\"true\"}',
'hbase.table.name'='nometabella:nomecolonna') -- Qui si indica la tabella di Hbase di riferimento