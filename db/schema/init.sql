CREATE DATABASE pythonDb;
use pythonDb;

CREATE USER 'user_api'@'localhost' IDENTIFIED WITH mysql_native_password BY '123';
GRANT ALL PRIVILEGES ON *.* TO 'user_api'@'localhost' WITH GRANT OPTION;
CREATE USER 'user_api'@'%' IDENTIFIED WITH mysql_native_password BY '123';
GRANT ALL PRIVILEGES ON *.* TO 'user_api'@'%' WITH GRANT OPTION;

CREATE TABLE IF NOT EXISTS `Tweet`(
    `Id`                VARCHAR(36) NOT NULL,
    `TweetInfo`         JSON NOT NULL,
    `TweetTokenization` JSON NOT NULL,
    PRIMARY KEY(`Id`),
    UNIQUE INDEX `Id_UNIQUE` (`Id` ASC)
    ) ENGINE = InnoDB DEFAULT CHARSET = utf8 COLLATE=utf8_bin;

GRANT ALL ON *.* TO 'user_api'@'%' ;

FLUSH PRIVILEGES;