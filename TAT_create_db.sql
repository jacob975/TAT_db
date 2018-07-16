DROP database IF EXISTS `TAT`;              /* if the database exists, it will be drop*/
CREATE database TAT;
use TAT;

/*create the table targets*/

DROP TABLE IF EXISTS `targets`;           /* if the table exists, it will be drop*/
CREATE TABLE `targets`(
    `ID` int not null auto_increment primary key,
    `NAME` varchar(20) UNIQUE,  /*name of target*/
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



/*create the table data_file*/

DROP TABLE IF EXISTS `data_file`;        /* if the table exists, it will be drop*/
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
    `DATE-OBS` varchar(20),     /*YYYY/MM/DD*/
    `TIME-OBS`varchar(20),      /*total imaging time*/
    `MJD-OBS` DOUBLE,           /*Modified Julian Date*/
    `AIRMASS` DOUBLE,           
    `JD` DOUBLE,                /*Julian Date*/
    `subbed` boolean,           /*if the file has been subbed, it results True. Otherwise, it results False*/
    `divfitted` boolean         /*if the file has been divfitted, it results True. Otherwise, it results False*/

);

/*create the table observatory */

DROP TABLE IF EXISTS `observatory`;        /* if the table exists, it will be drop*/
CREATE TABLE `observatory`(
    `ID` int not null auto_increment primary key,
    `SITENAME` varchar(20) UNIQUE,      /*location of observer*/
    `SITELAT` varchar(20),      /*Latitude of the observer*/
    `SITELONG` varchar(20),     /*Longitude of the observer*/
    `SITEALT` varchar(20)          /*Altitude of rhe observer*/

);

/*insert the data into the table targets */

insert into targets (RA,`DEC`,NAME) values ('21:53:24','47:16:00','IC5146');
insert into targets (RA,`DEC`,NAME) values ('03:29:10','31:21:57','NGC1333A');
insert into targets (RA,`DEC`,NAME) values ('12:55:38','25:53:31','WD1253+261');
insert into targets (RA,`DEC`,NAME) values ('18:36:57','-28:55:42','SgrNova');
insert into targets (RA,`DEC`,NAME) values ('19:20:30','11:02:01','HH32');
insert into targets (RA,`DEC`,NAME) values ('08:22:27','13:44:07','KELT-17');
insert into targets (RA,`DEC`,NAME) values ('11:52:58.8','37:43:07.2','Groombridge1830');
insert into targets (RA,`DEC`,NAME) values ('20:06:15','44:27:24',  'KIC8462852');
insert into targets (RA,`DEC`,NAME) values ('21:29:58.42','51:03:59.8','PN');
insert into targets (RA,`DEC`,NAME) values ('21:06:53.9','38:44:57.9','61Cygni');
insert into targets (RA,`DEC`,NAME) values ('20:12:7', '38:21:18', 'NGC6888');

/*insert the data into the table observatory*/

insert into observatory (SITENAME,SITELAT,SITELONG,SITEALT) values ('TF','28.30','-16.51','2300');
insert into observatory (SITENAME,SITELAT,SITELONG,SITEALT) values ('LI-JIANG','26.69','100.03','3330');


/*grant the privilege to somebody*/

GRANT ALL PRIVILEGES ON TAT.* TO 'TAT'@'localhost' identified by '1234';
GRANT select ON TAT.* TO 'read'@'localhost' identified by'1234';
FLUSH PRIVILEGES;               /*refresh the user */
