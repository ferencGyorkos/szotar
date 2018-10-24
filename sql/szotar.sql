DROP TABLE IF EXISTS szotar;
CREATE TABLE szotar (
  id     SERIAL NOT NULL,
  magyar varchar(255),
  angol  varchar(255),
  PRIMARY KEY (id)
);