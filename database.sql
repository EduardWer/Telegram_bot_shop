CREATE TABLE IF NOT EXISTS Dolg(
    Dolg_id integer primary key autoincrement ,
    names varchar(100) not null
);

CREATE TABLE IF NOT EXISTS My_dolg(
    My_dolg_id integer primary key autoincrement,
    names varchar(100) not null
);


CREATE  table if not exists Users(
    User_id integer primary key autoincrement ,
    User_Log_parol varchar(50) not null,
    user_rol varchar(3) not null
);

CREATE TABLE if not exists  Cassa(
    Cassa_id integer primary key autoincrement,
    Cassa_many real not null default 0
);

CREATE TABLE if not exists  Karta(
    Karta_id integer primary key autoincrement,
    Karta_many real not null default 0
);



--insert into Users(user_log_parol, user_rol) values ('eduert:wer','adm')