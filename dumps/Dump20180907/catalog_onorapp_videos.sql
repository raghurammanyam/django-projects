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
-- Table structure for table `onorapp_videos`
--

DROP TABLE IF EXISTS `onorapp_videos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `onorapp_videos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(200) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `item_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `onorapp_videos_item_id_386ab657_fk_onorapp_categorylist_id` (`item_id`),
  KEY `onorapp_videos_user_id_e9293934_fk_onorapp_users_id` (`user_id`),
  CONSTRAINT `onorapp_videos_item_id_386ab657_fk_onorapp_categorylist_id` FOREIGN KEY (`item_id`) REFERENCES `onorapp_categorylist` (`id`),
  CONSTRAINT `onorapp_videos_user_id_e9293934_fk_onorapp_users_id` FOREIGN KEY (`user_id`) REFERENCES `onorapp_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `onorapp_videos`
--

LOCK TABLES `onorapp_videos` WRITE;
/*!40000 ALTER TABLE `onorapp_videos` DISABLE KEYS */;
INSERT INTO `onorapp_videos` VALUES (1,'https://www.youtube.com/watch?v=LTtR4foRsCw',1,'2018-08-31 03:23:47.165628','2018-08-31 03:23:47.165740',1,1),(2,'https://www.youtube.com/watch?v=LTtR4foRsCw',0,'2018-08-31 03:23:57.417695','2018-08-31 03:23:57.417780',1,1),(3,'https://www.youtube.com/watch?v=LTtR4foRsCw',0,'2018-08-31 03:24:06.658332','2018-08-31 03:24:06.658417',2,1),(4,'https://www.youtube.com/watch?v=LTtR4foRsCw',1,'2018-08-31 03:24:12.061240','2018-08-31 03:24:12.061323',2,1),(5,'https://www.youtube.com/watch?v=LTtR4foRsCw',1,'2018-08-31 03:27:51.012853','2018-08-31 03:27:51.012959',2,1),(6,'https://www.youtube.com/watch?v=LTtR4foRsCw',1,'2018-08-31 03:50:31.789733','2018-08-31 03:50:31.789844',3,1);
/*!40000 ALTER TABLE `onorapp_videos` ENABLE KEYS */;
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
