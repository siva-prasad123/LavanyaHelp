/*
SQLyog Enterprise - MySQL GUI v6.56
MySQL - 5.0.67-community-nt : Database - service_portal
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`service_portal` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `service_portal`;

/*Table structure for table `product` */

DROP TABLE IF EXISTS `product`;

CREATE TABLE `product` (
  `id` int(11) NOT NULL auto_increment,
  `shop_id` varchar(100) default NULL,
  `pname` varchar(1000) default NULL,
  `price` varchar(1000) default NULL,
  `available` varchar(1000) default NULL,
  `usage` varchar(1000) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `product` */

insert  into `product`(`id`,`shop_id`,`pname`,`price`,`available`,`usage`) values (1,'1','cooking oil','145','12','cocking'),(2,'1','soap','12','12','batching');

/*Table structure for table `product_book` */

DROP TABLE IF EXISTS `product_book`;

CREATE TABLE `product_book` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` varchar(1000) default NULL,
  `product_id` varchar(1000) default NULL,
  `shop_id` varchar(1000) default NULL,
  `date` varchar(1000) default NULL,
  `status` varchar(1000) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `product_book` */

insert  into `product_book`(`id`,`user_id`,`product_id`,`shop_id`,`date`,`status`) values (1,'1','2','1','2024-02-28 18:55:41','Accepted');

/*Table structure for table `register` */

DROP TABLE IF EXISTS `register`;

CREATE TABLE `register` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(1000) default NULL,
  `email` varchar(1000) default NULL,
  `mobile` varchar(1000) default NULL,
  `address` varchar(1000) default NULL,
  `username` varchar(200) default NULL,
  `password` varchar(1000) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `register` */

insert  into `register`(`id`,`name`,`email`,`mobile`,`address`,`username`,`password`) values (1,'customer','customer@gmail.com','1234567890','hyd','customer','123');

/*Table structure for table `service` */

DROP TABLE IF EXISTS `service`;

CREATE TABLE `service` (
  `id` int(11) NOT NULL auto_increment,
  `service` varchar(1000) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `service` */

insert  into `service`(`id`,`service`) values (1,'plumber'),(2,'Electrician');

/*Table structure for table `service_book` */

DROP TABLE IF EXISTS `service_book`;

CREATE TABLE `service_book` (
  `id` int(11) NOT NULL auto_increment,
  `userid` varchar(1000) default NULL,
  `service_id` varchar(1000) default NULL,
  `date` varchar(1000) default NULL,
  `status` varchar(1000) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `service_book` */

insert  into `service_book`(`id`,`userid`,`service_id`,`date`,`status`) values (1,'1','1','2024-02-28 18:44:27','Accepted'),(2,'1','1','2024-02-28 20:25:44','waiting');

/*Table structure for table `skregister` */

DROP TABLE IF EXISTS `skregister`;

CREATE TABLE `skregister` (
  `id` int(11) NOT NULL auto_increment,
  `shopname` varchar(1000) default NULL,
  `email` varchar(1000) default NULL,
  `address` varchar(1000) default NULL,
  `mobile` varchar(1000) default NULL,
  `username` varchar(1000) default NULL,
  `password` varchar(1000) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `skregister` */

insert  into `skregister`(`id`,`shopname`,`email`,`address`,`mobile`,`username`,`password`) values (1,'GKV Shop','GkvTechSolutions@gmail.com','Mansanpally','1234567890','gkv','123');

/*Table structure for table `sregister` */

DROP TABLE IF EXISTS `sregister`;

CREATE TABLE `sregister` (
  `id` int(11) NOT NULL auto_increment,
  `service` varchar(1000) default NULL,
  `email` varchar(1000) default NULL,
  `username` varchar(1000) default NULL,
  `password` varchar(1000) default NULL,
  `w_hours` varchar(1000) default NULL,
  `cost` varchar(1000) default NULL,
  `mobile` varchar(1000) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `sregister` */

insert  into `sregister`(`id`,`service`,`email`,`username`,`password`,`w_hours`,`cost`,`mobile`) values (1,'Electrician','kishangadicherla508@gmail.com','kishan','123','6hr','1500','9876786543'),(2,'plumber','venkat@gmail.com','venkat','123','7hr','1700','96402572921');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
