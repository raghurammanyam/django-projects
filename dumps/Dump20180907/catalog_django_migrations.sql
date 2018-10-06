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
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'Catalog','0001_initial','2018-08-10 10:27:43.404088'),(2,'contenttypes','0001_initial','2018-08-10 10:27:44.215787'),(3,'auth','0001_initial','2018-08-10 10:27:55.418276'),(4,'admin','0001_initial','2018-08-10 10:27:58.082670'),(5,'admin','0002_logentry_remove_auto_add','2018-08-10 10:27:58.152130'),(6,'admin','0003_logentry_add_action_flag_choices','2018-08-10 10:27:58.236007'),(7,'contenttypes','0002_remove_content_type_name','2018-08-10 10:28:00.016142'),(8,'auth','0002_alter_permission_name_max_length','2018-08-10 10:28:00.175544'),(9,'auth','0003_alter_user_email_max_length','2018-08-10 10:28:00.317785'),(10,'auth','0004_alter_user_username_opts','2018-08-10 10:28:00.377771'),(11,'auth','0005_alter_user_last_login_null','2018-08-10 10:28:01.154001'),(12,'auth','0006_require_contenttypes_0002','2018-08-10 10:28:01.204051'),(13,'auth','0007_alter_validators_add_error_messages','2018-08-10 10:28:01.273602'),(14,'auth','0008_alter_user_username_max_length','2018-08-10 10:28:01.447797'),(15,'auth','0009_alter_user_last_name_max_length','2018-08-10 10:28:01.665059'),(16,'sessions','0001_initial','2018-08-10 10:28:02.452418'),(17,'Catalog','0002_auto_20180810_1101','2018-08-10 11:01:29.801753'),(18,'account','0001_initial','2018-08-14 04:31:11.110476'),(19,'account','0002_email_max_length','2018-08-14 04:31:11.319920'),(20,'authtoken','0001_initial','2018-08-14 04:31:12.624300'),(21,'authtoken','0002_auto_20160226_1747','2018-08-14 04:31:13.772539'),(22,'sites','0001_initial','2018-08-14 04:31:14.151830'),(23,'sites','0002_alter_domain_unique','2018-08-14 04:31:14.508487'),(24,'onorapp','0001_initial','2018-08-17 03:59:21.408402'),(25,'onorapp','0002_auto_20180813_0659','2018-08-17 03:59:22.688321'),(26,'onorapp','0003_auto_20180816_0922','2018-08-17 03:59:26.824186'),(27,'onorapp','0004_auto_20180816_0944','2018-08-17 03:59:31.188744'),(28,'onorapp','0005_auto_20180817_1109','2018-08-24 09:32:05.570831'),(29,'onorapp','0006_auto_20180818_1006','2018-08-24 09:32:08.041982'),(30,'onorapp','0007_carousel_name','2018-08-24 09:32:09.043722'),(31,'onorapp','0008_auto_20180820_1005','2018-08-24 09:32:13.474039'),(32,'onorapp','0009_auto_20180821_0725','2018-08-24 09:32:15.203854'),(33,'onorapp','0010_auto_20180822_0627','2018-08-24 09:32:22.391262'),(34,'onorapp','0011_auto_20180822_0722','2018-08-24 09:32:22.559259'),(35,'onorapp','0012_categories_show_in_mainpage','2018-08-24 09:32:23.741949'),(36,'onorapp','0013_registers','2018-08-28 03:15:27.687861'),(37,'onorapp','0014_auto_20180827_1045','2018-08-28 03:15:29.709638'),(38,'onorapp','0015_auto_20180827_1107','2018-08-28 03:15:29.815496'),(39,'onorapp','0016_remove_categorycarousel_active_show','2018-08-28 03:15:31.210476'),(40,'onorapp','0017_auto_20180828_0406','2018-08-28 04:07:13.692567'),(41,'onorapp','0018_carousel_url','2018-08-28 11:39:57.050774'),(42,'onorapp','0019_auto_20180829_0359','2018-08-29 03:59:24.181733'),(43,'onorapp','0019_auto_20180829_0859','2018-08-29 09:00:03.122429'),(44,'onorapp','0020_auto_20180830_0359','2018-08-30 03:59:46.839670'),(45,'onorapp','0021_registers_file','2018-08-30 10:26:34.465044'),(46,'onorapp','0022_categorylist_videourl','2018-08-31 03:45:46.591832'),(47,'onorapp','0018_auto_20180828_0551','2018-09-02 09:37:49.378752'),(48,'onorapp','0019_auto_20180828_0553','2018-09-02 09:37:50.658586'),(49,'onorapp','0023_auto_20180904_0331','2018-09-04 03:31:40.557456'),(50,'myapp','0001_initial','2018-09-06 09:01:27.156926');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-07 14:41:03
