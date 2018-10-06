-- MySQL dump 10.13  Distrib 5.7.23, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: catalog
-- ------------------------------------------------------
-- Server version	5.7.23-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `onorapp_users`
--

DROP TABLE IF EXISTS `onorapp_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `onorapp_users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `mobile_no` varchar(10) NOT NULL,
  `address` longtext NOT NULL,
  `emailId` varchar(254) NOT NULL,
  `password` varchar(254) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `role_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `onorapp_users_emailId_f3ddc49d_uniq` (`emailId`),
  KEY `onorapp_users_role_id_5ac3be17_fk_onorapp_roles_id` (`role_id`),
  CONSTRAINT `onorapp_users_role_id_5ac3be17_fk_onorapp_roles_id` FOREIGN KEY (`role_id`) REFERENCES `onorapp_roles` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `onorapp_users`
--

LOCK TABLES `onorapp_users` WRITE;
/*!40000 ALTER TABLE `onorapp_users` DISABLE KEYS */;
INSERT INTO `onorapp_users` VALUES (1,'rakesh','reddy','9994445557','kukatpally','ganeshsingamaneni5@gmail.com','pbkdf2_sha256$120000$r0ZnZNcnR35K$g/TgwlFjfV4B+3IDGJetWa0BO5r4JZS0VPLM0ilXLQo=',1,'2018-08-17 04:06:24.819981','2018-09-04 03:05:34.420221',1),(2,'ganesh','reddy','9646765689','kukatpally','ganesh1995.55@gmail.com','pbkdf2_sha256$120000$jttIsOmmW0ud$Sjn3VSOa89dMVbaGAqxYbqKT+Ef5OXokLFsLoi32NIE=',1,'2018-08-17 04:12:38.094179','2018-08-29 04:03:18.623135',1),(3,'ganesh','reddy','9646765689','kukatpally','kirany879@gmail.com','$6$qbSKYC0818mtD5Pr$Lpmyc44WWEs2fId.5RtzihPN7/YEvRWZhniJiHLtET.E7GfNZUg9gE8xFNYjPAN8qDYcIc35Q0FFCMxcIW3qx1',1,'2018-08-17 04:14:07.199897','2018-08-17 04:14:07.199992',1),(4,'ganesh','reddy','9646765689','kukatpally','sheeram000@gmail.com','$6$Bytwa4u9QuF7KkZU$41HNPS3yM2NJQ7Zk2aHEd6iKMlGZ9L1gHkhrCb7zjCG2v0g6P.1cv1u2yTMTYTrlDinvOAvA6Fi/d4tOc1xUY.',1,'2018-08-17 04:25:05.407838','2018-08-17 04:25:05.407916',1),(5,'rakesh','reddy','9646765689','kukatpally','manyamraghuram99@gmail.com','$6$gGo95U4uBoDMalRX$wXZ1x80bHKmQB2STCpzYuN1G/JQptfSGalkRqVpFpvsjgB569hwXyprLWYz4vbLkfk3mf6lTQxJvSevJ4ViwV/',1,'2018-08-17 04:58:36.875218','2018-08-17 04:58:36.875329',1),(6,'rakesh','reddy','9646765689','kukatpally','manyamraghuram62@gmail.com','$6$WrLKkdZUmBlSsoAv$CcdXyw3Y0zeAZmp1kVAOWnB9QNy.HBS6.95kjlYx93PAY34tSGP9.vepVt8forCYAZdRNSl2f7TJNvfvtGwIc/',1,'2018-08-17 04:59:30.385422','2018-08-17 04:59:30.385518',1),(7,'rakesh','reddy','9646765689','kukatpally','ganesh1995@gmail.com','$6$WhK/DEsRKJoHgqbL$iqpMaPlRk.hb8K0iZZu4qZCWj3kEfy4COcC5E3yj3G6eCx1WxTr6HOCgZtnPLCalq7f0T/ZRROAYyvvKIefo0.',1,'2018-08-17 06:15:15.906916','2018-08-17 06:15:15.906998',1),(8,'manyam','raghuram','9899677654','nizampet','manyamraghuram@gmail.com','pbkdf2_sha256$120000$Yeyo7UlI0C3y$up7e2/WafXCqYRHYjf2+zF5Yfkx1WoeGLaWYp67+T8w=',0,'2018-08-29 04:06:59.035379','2018-09-04 03:07:41.411810',1),(9,'manyam','raghuram','9899677654','nizampet','manyamraghuram6@gmail.com','pbkdf2_sha256$120000$3jKw2bup18fu$HiYm6hnsrQdO3MitsPTPvoZFqZDTvTlgxHROa/XHMH0=',1,'2018-08-29 04:16:31.835203','2018-08-29 04:16:31.835319',1);
/*!40000 ALTER TABLE `onorapp_users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-07 14:41:01
