DROP DATABASE IF EXISTS `TAT`;
CREATE DATABASE `TAT`;
USE `TAT`;

DROP TABLE IF EXISTS `targets`;
CREATE TABLE `targets`(
    `id` int not null auto_increment primary key,
    `NAME` varchar(20),         /*name of target*/
    `RA` varchar(20),           /*Right Ascension of target*/
    `DEC` varchar(20),          /*Declination of target*/
    `MAGNITUDE` FLOAT,          /*Absolute Magnitude of target*/
    `PERIOD` FLOAT,             /*Period of Magitude changing*/
    `type` varchar(20),         
    `BFE` Float                 /*best exposure time for filter*/

); 
	
DROP TABLE IF EXISTS `data_file`;
CREATE TABLE `data_file`(
    `id` int not null auto_increment primary key,
    `FILENAME` varchar(80) UNIQUE,
    `FILTER` varchar(20),       /*filter*/
    `RA` varchar(20),           /*Right Ascension of target*/
    `DEC` varchar(20),          /*Declination of target*/
    `SITENAME` varchar(20),     /*location of observer*/
    `CCDTEMP` FLOAT,            /*CCD temperature*/
    `EXPTIME` FLOAT,            /*exposure time*/
    `DATE-OBS` varchar(20),         /*YYYY/MM/DD*/
    `TIME-OBS`varchar(20),           /*total imaging time*/
    `MJD-OBS` DOUBLE,
    `JD` DOUBLE,
    `subbed` boolean,
    `divfitted` boolean

);
CREATE TABLE `observersite`(
    `id` int not null auto_increment primary key,
    `SITENAME` varchar(20) UNIQUE,      /*location of observer*/
    `SITELAT` varchar(20),      /*Latitude of the observer*/
    `SITELONG` varchar(20),     /*Longitude of the observer*/
    `SITEALT` varchar(20)          /*Altitude of rhe observer*/

);


GRANT USAGE ON *.* TO 'TAT'@'localhost' IDENTIFIED BY '1234';
GRANT USAGE ON *.* TO 'read'@'localhost' IDENTIFIED BY '1234';
DROP USER 'TAT'@'localhost';
CREATE USER 'TAT'@'localhost' IDENTIFIED BY '1234';
DROP USER 'read'@'localhost';
CREATE USER 'read'@'localhost' IDENTIFIED BY '1234';
GRANT ALL PRIVILEGES ON TAT.* TO 'TAT'@'localhost';
GRANT select ON TAT.* TO 'read'@'localhost' identified by'1234';
FLUSH PRIVILEGES;
