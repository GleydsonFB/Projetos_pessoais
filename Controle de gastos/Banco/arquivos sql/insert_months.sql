USE controle_de_gastos;
DELETE FROM mes WHERE id_mes != 0;
ALTER TABLE mes AUTO_INCREMENT=1;
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/mes.csv'
INTO TABLE mes
FIELDS TERMINATED BY ','
LINES TERMINATED BY ','
(nome);