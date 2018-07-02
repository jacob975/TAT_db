DROP TABLE IF EXISTS `targets`;
CREATE TABLE `targets`(
    `ID` int not null auto_increment primary key,
    `NAME` varchar(20),         /*name of target*/
    `RA` varchar(20),           /*Right Ascension of target*/
    `DEC` varchar(20),          /*Declination of target*/
    `MAGNITUDE` FLOAT,          /*Absolute Magnitude of target*/
    `PERIOD` FLOAT,             /*Period of Magitude changing*/
    `TYPE` varchar(20),         /*Type of target: star, galaxy...*/
    `BFE0` FLOAT,               /*best exposure time for filter 0*/
    `N0` varchar(2),             /*filter0*/	
    `BFE1` FLOAT,               /*best exposure time for filter 1*/
    `N1` varchar(2),             /*filter1*/ 
    `BFE2` FLOAT,               /*best exposure time for filter 2*/
    `N2` varchar(2),             /*filter2*/
    `BFE3` FLOAT,               /*best exposure time for filter 3*/
    `N3` varchar(2),             /*filter3*/
    `BFE4` FLOAT,               /*best exposure time for filter 4*/
    `N4` varchar(2),             /*filter4*/
    `BFE5` FLOAT,               /*best exposure time for filter 5*/
    `N5` varchar(2),             /*filter5*/
    `BFE6` FLOAT,               /*best exposure time for filter 6*/
    `N6` varchar(2)             /*filter6*/
);




DROP TABLE IF EXISTS `data_file`;
CREATE TABLE `data_file`(
    `ID` int not null auto_increment primary key,
    `FILENAME` varchar(80) UNIQUE,
    `FILEPATH` varchar(80),
    `FILTER` varchar(20),       /*filter*/
    `RA` varchar(20),           /*Right Ascension of target*/
    `DEC` varchar(20),          /*Declination of target*/
    `SITENAME` varchar(20),     /*location of observer*/
    `CCDTEMP` FLOAT,            /*CCD temperature*/
    `EXPTIME` FLOAT,            /*exposure time*/
    `DATE-OBS` varchar(20),         /*YYYY/MM/DD*/
    `TIME-OBS`varchar(20),           /*total imaging time*/
    `MJD-OBS` DOUBLE,
    `AIRMASS` DOUBLE,
    `JD` DOUBLE,
    `subbed` boolean,
    `divfitted` boolean

);

DROP TABLE IF EXISTS `observatory`;
CREATE TABLE `observatory`(
    `id` int not null auto_increment primary key,
    `SITENAME` varchar(20) UNIQUE,      /*location of observer*/
    `SITELAT` varchar(20),      /*Latitude of the observer*/
    `SITELONG` varchar(20),     /*Longitude of the observer*/
    `SITEALT` varchar(20)          /*Altitude of rhe observer*/

);


GRANT ALL PRIVILEGES ON TAT.* TO 'TAT'@'localhost' identified by '1234';
GRANT select ON TAT.* TO 'read'@'localhost' identified by'1234';
FLUSH PRIVILEGES;
