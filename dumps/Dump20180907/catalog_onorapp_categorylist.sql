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
-- Table structure for table `onorapp_categorylist`
--

DROP TABLE IF EXISTS `onorapp_categorylist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `onorapp_categorylist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `mobile` varchar(10) NOT NULL,
  `email` varchar(254) NOT NULL,
  `description` longtext NOT NULL,
  `images` varchar(100) DEFAULT NULL,
  `status` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `category_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `latitude` varchar(100) NOT NULL,
  `longitude` varchar(100) NOT NULL,
  `address` longtext NOT NULL,
  `external_url` varchar(200) NOT NULL,
  `show_in_mainpage_carousel` tinyint(1) NOT NULL,
  `internal_url` varchar(200) NOT NULL,
  `videourl` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `onorapp_categorylist_user_id_2b9055b9_fk_onorapp_users_id` (`user_id`),
  KEY `onorapp_categorylist_category_id_c7b7643f_fk_onorapp_c` (`category_id`),
  CONSTRAINT `onorapp_categorylist_category_id_c7b7643f_fk_onorapp_c` FOREIGN KEY (`category_id`) REFERENCES `onorapp_categories` (`id`),
  CONSTRAINT `onorapp_categorylist_user_id_2b9055b9_fk_onorapp_users_id` FOREIGN KEY (`user_id`) REFERENCES `onorapp_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `onorapp_categorylist`
--

LOCK TABLES `onorapp_categorylist` WRITE;
/*!40000 ALTER TABLE `onorapp_categorylist` DISABLE KEYS */;
INSERT INTO `onorapp_categorylist` VALUES (1,'jk','9994445561','ganeshsingamaneni5@gmail.com','gf jadfj gvkjdf bg','image4/optical.jpeg',1,'2018-08-21 03:20:10.258443','2018-08-21 03:20:10.258564',1,1,'d jbgfvbdfgbhj','jhbdgjbdjsbgs','dfknjbvjd','',1,'',''),(2,'mike','9994445561','ganeshsingamaneni5@gmail.com','gf jadfj gvkjdf bg','image4/optical_fBJlUm7.jpeg',1,'2018-08-21 03:20:57.760379','2018-08-21 03:20:57.760466',1,1,'d jbgfvbdfgbhj','jhbdgjbdjsbgs','dfknjbvjd','',1,'',''),(3,'mike','9994445561','ganeshsingamaneni5@gmail.com','gf jadfj gvkjdf bg','image4/optical_riuXFqM.jpeg',1,'2018-08-21 03:22:25.177524','2018-08-21 03:22:25.177631',2,1,'d jbgfvbdfgbhj','jhbdgjbdjsbgs','dfknjbvjd','',1,'',''),(4,'ikea','9994445561','ganeshsingamaneni5@gmail.com','gf jadfj gvkjdf bg','image4/optical_PUGwKjX.jpeg',1,'2018-08-21 03:22:54.311029','2018-08-21 03:22:54.311131',2,1,'d jbgfvbdfgbhj','jhbdgjbdjsbgs','dfknjbvjd','',1,'',''),(5,'j.k restaurant','8767564545','ganeshsingamaneni5@gmail.com','gf jadfj gvkjdf b','categorylist/book.jpeg',0,'2018-09-04 03:40:24.412714','2018-09-04 03:40:24.412865',NULL,1,'d jbgfvbdfgbhj','jhbdgjbdjsbgfirsts','dfknjbvjd','http://localhost:8000/login',1,'http://localhost:8000/login','http://localhost:8000/login');
/*!40000 ALTER TABLE `onorapp_categorylist` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-07 14:41:08
