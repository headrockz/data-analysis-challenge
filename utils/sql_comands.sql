--  table agencia
CREATE TABLE "agencias" (
	"id_agencia"	INTEGER NOT NULL,
	"nome_instituicao"	TEXT,
	"municipio"	TEXT NOT NULL,
	"uf"	TEXT NOT NULL,
	PRIMARY KEY("id_agencia" AUTOINCREMENT)
);


-- table postos
CREATE TABLE IF NOT EXISTS "postos" (
	"id_postos"	INTEGER NOT NULL,
	"nome_instituicao"	TEXT,
	"municipio"	TEXT NOT NULL,
	"uf"	TEXT NOT NULL,
	PRIMARY KEY("id_postos" AUTOINCREMENT)
);

-- table postos eletronicos
CREATE TABLE "postos_eletronicos" (
	"id_postose"	INTEGER NOT NULL,
	"nome_instituicao"	TEXT,
	"municipio"	TEXT NOT NULL,
	"uf"	TEXT NOT NULL,
	PRIMARY KEY("id_postose" AUTOINCREMENT)
);

-- table municipio
CREATE TABLE "municipios" (
	"id_municipio"	INTEGER NOT NULL,
	"municipio"	TEXT NOT NULL,
	"uf"	TEXT NOT NULL,
	PRIMARY KEY("id_municipio" AUTOINCREMENT)
);

-- table bancos
CREATE TABLE "bancos" (
	"id_banco"	INTEGER NOT NULL,
	"qtde_agencias"	INTEGER,
	"qtde_postos"	INTEGER,
	"qtde_postosele"	INTEGER,
	"fk_municipio"	INTEGER NOT NULL,
	PRIMARY KEY("id_banco" AUTOINCREMENT)
);

-- table populacao
CREATE TABLE "populacao_municipal" (
	"id_populacao"	INTEGER NOT NULL,
	"populacao"	INTEGER NOT NULL,
	"coeficiente_populacional"	INTEGER NOT NULL,
	"fk_municipio"	INTEGER NOT NULL,
	FOREIGN KEY("populacao") REFERENCES "municipios"("id_municipio"),
	PRIMARY KEY("id_populacao" AUTOINCREMENT)
);

-- table idh
CREATE TABLE "idh" (
	"id_idh"	INTEGER NOT NULL,
	"idh"	REAL NOT NULL,
	"fk_municipio"	INTEGER NOT NULL,
	PRIMARY KEY("id_idh" AUTOINCREMENT)
);



-- view para ver a quantidade total de agencias, postos e postos eletronicos por municipio
CREATE VIEW IF NOT EXISTS nivel_bancarizacao
	as 
	SELECT  ((sum(b.qtde_agencias) + sum(b.qtde_postos) + sum(b.qtde_postosele))) as 'bancarizacao', fk_municipio from bancos b
	GROUP by fk_municipio;