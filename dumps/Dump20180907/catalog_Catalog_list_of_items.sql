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
-- Table structure for table `Catalog_list_of_items`
--

DROP TABLE IF EXISTS `Catalog_list_of_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Catalog_list_of_items` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) NOT NULL,
  `Mobile_no` varchar(50) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Banner` varchar(100) DEFAULT NULL,
  `Address` longtext NOT NULL,
  `Description` longtext NOT NULL,
  `status` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `Categorie_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Catalog_list_of_item_Categorie_id_4ce395cd_fk_Catalog_c` (`Categorie_id`),
  KEY `Catalog_list_of_items_user_id_0196ab19_fk_Catalog_users_id` (`user_id`),
  CONSTRAINT `Catalog_list_of_item_Categorie_id_4ce395cd_fk_Catalog_c` FOREIGN KEY (`Categorie_id`) REFERENCES `Catalog_categories` (`id`),
  CONSTRAINT `Catalog_list_of_items_user_id_0196ab19_fk_Catalog_users_id` FOREIGN KEY (`user_id`) REFERENCES `Catalog_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Catalog_list_of_items`
--

LOCK TABLES `Catalog_list_of_items` WRITE;
/*!40000 ALTER TABLE `Catalog_list_of_items` DISABLE KEYS */;
INSERT INTO `Catalog_list_of_items` VALUES (1,'j.khotel','9876564354','raghu@gmail.com','banner/esl6RYvpfzrest3.jpg','kukatpally','multicusine',1,'2018-08-11 06:22:51.105592','2018-08-11 06:22:51.105698',1,1),(2,'abhiruchi','9899564354','abhiruchi@gmail.com','banner/UgMQDAk2wNrest.jpeg','kukatpally','multicusine',1,'2018-08-11 06:24:08.711672','2018-08-11 06:24:08.711771',1,1);
/*!40000 ALTER TABLE `Catalog_list_of_items` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-07 14:41:09
