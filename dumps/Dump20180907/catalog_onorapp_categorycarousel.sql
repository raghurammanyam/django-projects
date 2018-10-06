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
-- Table structure for table `onorapp_categorycarousel`
--

DROP TABLE IF EXISTS `onorapp_categorycarousel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `onorapp_categorycarousel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `slide` varchar(100) DEFAULT NULL,
  `status` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `category_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `onorapp_categorycaro_category_id_88a7137e_fk_onorapp_c` (`category_id`),
  KEY `onorapp_categorycarosuel_user_id_8f435a20_fk_onorapp_users_id` (`user_id`),
  CONSTRAINT `onorapp_categorycaro_category_id_88a7137e_fk_onorapp_c` FOREIGN KEY (`category_id`) REFERENCES `onorapp_categories` (`id`),
  CONSTRAINT `onorapp_categorycarosuel_user_id_8f435a20_fk_onorapp_users_id` FOREIGN KEY (`user_id`) REFERENCES `onorapp_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `onorapp_categorycarousel`
--

LOCK TABLES `onorapp_categorycarousel` WRITE;
/*!40000 ALTER TABLE `onorapp_categorycarousel` DISABLE KEYS */;
INSERT INTO `onorapp_categorycarousel` VALUES (1,'image3/rest.jpeg',1,'2018-08-20 05:44:21.652213','2018-08-20 05:44:21.652367',1,1),(2,'image3/rest3.jpg',1,'2018-08-20 05:44:59.194921','2018-08-20 05:44:59.195001',1,1),(3,'image3/rest2.jpg',1,'2018-08-20 05:45:17.277143','2018-08-20 05:45:17.277256',1,1),(4,'image3/rest2_R7x3Zl5.jpg',1,'2018-08-20 11:40:30.296682','2018-08-20 11:40:30.296829',2,1),(5,'image3/fashion3.jpeg',1,'2018-08-20 11:40:45.876790','2018-08-20 11:40:45.876902',2,1),(6,'image3/fashion2.jpg',1,'2018-08-20 11:41:10.009761','2018-08-20 11:41:10.009897',2,1),(7,'image3/fashion2_NaoEFbC.jpg',1,'2018-08-20 11:41:15.166181','2018-08-20 11:41:15.166296',2,1);
/*!40000 ALTER TABLE `onorapp_categorycarousel` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-07 14:41:07
