-- Script para inserir os arquivos CSV dentro do banco de dados automaticamente.

USE tgr;
DELETE FROM vilao WHERE ID != 0;
ALTER TABLE vilao AUTO_INCREMENT=1;
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/viloes.csv'
INTO TABLE vilao
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(nome, hp, atk, defe, defe_magica, valor_soco, valor_chute);

DELETE FROM npc WHERE ID != 0;
ALTER TABLE npc AUTO_INCREMENT=1;
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/npcs.csv'
INTO TABLE npc
FIELDS TERMINATED BY '\n'
LINES TERMINATED BY '\n'
(nome);

DELETE FROM item WHERE ID != 0;
ALTER TABLE item AUTO_INCREMENT=1;
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/itens.csv'
INTO TABLE item
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(nome, dano, valor, npc_id, vilao_id);

