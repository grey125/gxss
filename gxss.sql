/*
SQLyog Ultimate v11.27 (32 bit)
MySQL - 5.5.53 : Database - gxss
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`gxss` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `gxss`;

/*Table structure for table `g_content` */

DROP TABLE IF EXISTS `g_content`;

CREATE TABLE `g_content` (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `message` varchar(255) DEFAULT NULL,
  `host` varchar(255) DEFAULT NULL,
  `username` varchar(255) DEFAULT NULL,
  `time_data` varchar(255) DEFAULT NULL,
  `js_name` varchar(255) DEFAULT NULL,
  `jm_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

/*Table structure for table `g_js` */

DROP TABLE IF EXISTS `g_js`;

CREATE TABLE `g_js` (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `username` varchar(255) DEFAULT NULL,
  `js_code` text,
  `time_data` varchar(255) DEFAULT NULL,
  `jm_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

/*Table structure for table `g_key` */

DROP TABLE IF EXISTS `g_key`;

CREATE TABLE `g_key` (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `auth_key` varchar(6) DEFAULT NULL,
  `status` int(5) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

/*Table structure for table `g_user` */

DROP TABLE IF EXISTS `g_user`;

CREATE TABLE `g_user` (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `username` varchar(10) DEFAULT NULL,
  `password` varchar(32) DEFAULT NULL,
  `auth_key` varchar(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
