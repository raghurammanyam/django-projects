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
-- Table structure for table `onorapp_categorylistimages`
--

DROP TABLE IF EXISTS `onorapp_categorylistimages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `onorapp_categorylistimages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `images` varchar(100) DEFAULT NULL,
  `status` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `item_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `onorapp_categorylistimages_user_id_7dbd3dde_fk_onorapp_users_id` (`user_id`),
  KEY `onorapp_categorylist_item_id_c4a59900_fk_onorapp_c` (`item_id`),
  CONSTRAINT `onorapp_categorylist_item_id_c4a59900_fk_onorapp_c` FOREIGN KEY (`item_id`) REFERENCES `onorapp_categorylist` (`id`),
  CONSTRAINT `onorapp_categorylistimages_user_id_7dbd3dde_fk_onorapp_users_id` FOREIGN KEY (`user_id`) REFERENCES `onorapp_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `onorapp_categorylistimages`
--

LOCK TABLES `onorapp_categorylistimages` WRITE;
/*!40000 ALTER TABLE `onorapp_categorylistimages` DISABLE KEYS */;
INSERT INTO `onorapp_categorylistimages` VALUES (1,'image5/fashion2.jpg',1,'2018-08-21 03:56:32.507168','2018-08-21 03:56:32.507326',1,1),(2,'image5/fashion3.jpeg',1,'2018-08-21 03:56:52.281208','2018-08-21 03:56:52.281325',1,1),(3,'image5/fashion3_q3MuWoz.jpeg',1,'2018-08-21 03:57:06.037720','2018-08-21 03:57:06.037826',2,1),(4,'image5/fashion3_lS2NBU6.jpeg',1,'2018-08-21 03:57:10.499003','2018-08-21 03:57:10.499115',2,1),(5,'categorylistimages/rest2.jpg',0,'2018-09-02 09:46:16.368378','2018-09-02 09:46:16.368517',1,1),(6,'categorylistimages/rest2_1HHn8N7.jpg',1,'2018-09-02 09:47:03.030978','2018-09-02 09:47:03.031080',1,1),(7,'categorylistimages/rest2_jsWYAQj.jpg',1,'2018-09-02 09:47:06.997468','2018-09-02 09:47:06.997576',1,1),(8,'categorylistimages/rest2_4hM4Vps.jpg',1,'2018-09-02 09:47:09.598500','2018-09-02 09:47:09.598619',1,1),(9,'categorylistimages/rest2_3HeVMzw.jpg',1,'2018-09-02 09:47:11.364944','2018-09-02 09:47:11.365060',1,1),(10,'categorylistimages/rest2_cL3KaNa.jpg',1,'2018-09-02 09:47:16.623689','2018-09-02 09:47:16.623803',1,1),(11,'categorylistimages/rest2_QhP23Ze.jpg',1,'2018-09-02 09:47:22.570764','2018-09-02 09:47:22.570874',1,2),(12,'categorylistimages/rest2_sV5AUU3.jpg',1,'2018-09-02 09:47:27.736123','2018-09-02 09:47:27.736236',2,2),(13,'categorylistimages/rest2_Py0cJHM.jpg',1,'2018-09-02 09:47:30.369954','2018-09-02 09:47:30.370061',2,2),(14,'categorylistimages/rest2_rfJsX40.jpg',1,'2018-09-02 09:47:33.034385','2018-09-02 09:47:33.034500',2,2),(15,'categorylistimages/rest2_FAAdVNW.jpg',1,'2018-09-02 09:47:35.498917','2018-09-02 09:47:35.499046',2,2),(16,'categorylistimages/rest2_1KHvueh.jpg',1,'2018-09-02 09:48:21.015856','2018-09-02 09:48:21.015965',2,2),(17,'categorylistimages/rest2_o9ikegY.jpg',1,'2018-09-02 09:48:24.483207','2018-09-02 09:48:24.483318',2,2),(18,'categorylistimages/rest2_VL8rTDi.jpg',1,'2018-09-02 09:48:27.184164','2018-09-02 09:48:27.184275',2,2),(19,'categorylistimages/rest2_52PyqPk.jpg',1,'2018-09-02 09:48:30.132395','2018-09-02 09:48:30.132512',2,2),(20,'categorylistimages/rest2_ePo0mkU.jpg',1,'2018-09-02 09:48:35.570513','2018-09-02 09:48:35.570626',2,2),(21,'categorylistimages/rest2_F35N2Xd.jpg',1,'2018-09-03 04:59:03.775174','2018-09-03 04:59:03.775330',2,2),(22,'categorylistimages/rest2_GSDXxQR.jpg',1,'2018-09-03 05:00:19.594836','2018-09-03 05:00:19.594995',2,2);
/*!40000 ALTER TABLE `onorapp_categorylistimages` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-07 14:41:06
