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
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=133 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add user',3,'add_user'),(10,'Can change user',3,'change_user'),(11,'Can delete user',3,'delete_user'),(12,'Can view user',3,'view_user'),(13,'Can add group',4,'add_group'),(14,'Can change group',4,'change_group'),(15,'Can delete group',4,'delete_group'),(16,'Can view group',4,'view_group'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add categories',7,'add_categories'),(26,'Can change categories',7,'change_categories'),(27,'Can delete categories',7,'delete_categories'),(28,'Can view categories',7,'view_categories'),(29,'Can add main page',8,'add_mainpage'),(30,'Can change main page',8,'change_mainpage'),(31,'Can delete main page',8,'delete_mainpage'),(32,'Can view main page',8,'view_mainpage'),(33,'Can add users',9,'add_users'),(34,'Can change users',9,'change_users'),(35,'Can delete users',9,'delete_users'),(36,'Can view users',9,'view_users'),(37,'Can add carousels',10,'add_carousels'),(38,'Can change carousels',10,'change_carousels'),(39,'Can delete carousels',10,'delete_carousels'),(40,'Can view carousels',10,'view_carousels'),(41,'Can add item_ pics',11,'add_item_pics'),(42,'Can change item_ pics',11,'change_item_pics'),(43,'Can delete item_ pics',11,'delete_item_pics'),(44,'Can view item_ pics',11,'view_item_pics'),(45,'Can add roles',12,'add_roles'),(46,'Can change roles',12,'change_roles'),(47,'Can delete roles',12,'delete_roles'),(48,'Can view roles',12,'view_roles'),(49,'Can add categorie_curosels',13,'add_categorie_curosels'),(50,'Can change categorie_curosels',13,'change_categorie_curosels'),(51,'Can delete categorie_curosels',13,'delete_categorie_curosels'),(52,'Can view categorie_curosels',13,'view_categorie_curosels'),(53,'Can add list_ of_ items',14,'add_list_of_items'),(54,'Can change list_ of_ items',14,'change_list_of_items'),(55,'Can delete list_ of_ items',14,'delete_list_of_items'),(56,'Can view list_ of_ items',14,'view_list_of_items'),(57,'Can add Token',15,'add_token'),(58,'Can change Token',15,'change_token'),(59,'Can delete Token',15,'delete_token'),(60,'Can view Token',15,'view_token'),(61,'Can add site',16,'add_site'),(62,'Can change site',16,'change_site'),(63,'Can delete site',16,'delete_site'),(64,'Can view site',16,'view_site'),(65,'Can add social application',17,'add_socialapp'),(66,'Can change social application',17,'change_socialapp'),(67,'Can delete social application',17,'delete_socialapp'),(68,'Can view social application',17,'view_socialapp'),(69,'Can add social account',18,'add_socialaccount'),(70,'Can change social account',18,'change_socialaccount'),(71,'Can delete social account',18,'delete_socialaccount'),(72,'Can view social account',18,'view_socialaccount'),(73,'Can add social application token',19,'add_socialtoken'),(74,'Can change social application token',19,'change_socialtoken'),(75,'Can delete social application token',19,'delete_socialtoken'),(76,'Can view social application token',19,'view_socialtoken'),(77,'Can add email address',20,'add_emailaddress'),(78,'Can change email address',20,'change_emailaddress'),(79,'Can delete email address',20,'delete_emailaddress'),(80,'Can view email address',20,'view_emailaddress'),(81,'Can add email confirmation',21,'add_emailconfirmation'),(82,'Can change email confirmation',21,'change_emailconfirmation'),(83,'Can delete email confirmation',21,'delete_emailconfirmation'),(84,'Can view email confirmation',21,'view_emailconfirmation'),(85,'Can add roles',22,'add_roles'),(86,'Can change roles',22,'change_roles'),(87,'Can delete roles',22,'delete_roles'),(88,'Can view roles',22,'view_roles'),(89,'Can add categories',23,'add_categories'),(90,'Can change categories',23,'change_categories'),(91,'Can delete categories',23,'delete_categories'),(92,'Can view categories',23,'view_categories'),(93,'Can add carousel',24,'add_carousel'),(94,'Can change carousel',24,'change_carousel'),(95,'Can delete carousel',24,'delete_carousel'),(96,'Can view carousel',24,'view_carousel'),(97,'Can add users',25,'add_users'),(98,'Can change users',25,'change_users'),(99,'Can delete users',25,'delete_users'),(100,'Can view users',25,'view_users'),(101,'Can add category carousel',26,'add_categorycarousel'),(102,'Can change category carousel',26,'change_categorycarousel'),(103,'Can delete category carousel',26,'delete_categorycarousel'),(104,'Can view category carousel',26,'view_categorycarousel'),(105,'Can add main page carousel',27,'add_mainpagecarousel'),(106,'Can change main page carousel',27,'change_mainpagecarousel'),(107,'Can delete main page carousel',27,'delete_mainpagecarousel'),(108,'Can view main page carousel',27,'view_mainpagecarousel'),(109,'Can add category list images',28,'add_categorylistimages'),(110,'Can change category list images',28,'change_categorylistimages'),(111,'Can delete category list images',28,'delete_categorylistimages'),(112,'Can view category list images',28,'view_categorylistimages'),(113,'Can add category list',29,'add_categorylist'),(114,'Can change category list',29,'change_categorylist'),(115,'Can delete category list',29,'delete_categorylist'),(116,'Can view category list',29,'view_categorylist'),(117,'Can add videos',30,'add_videos'),(118,'Can change videos',30,'change_videos'),(119,'Can delete videos',30,'delete_videos'),(120,'Can view videos',30,'view_videos'),(121,'Can add registers',31,'add_registers'),(122,'Can change registers',31,'change_registers'),(123,'Can delete registers',31,'delete_registers'),(124,'Can view registers',31,'view_registers'),(125,'Can add news reader',32,'add_newsreader'),(126,'Can change news reader',32,'change_newsreader'),(127,'Can delete news reader',32,'delete_newsreader'),(128,'Can view news reader',32,'view_newsreader'),(129,'Can add users',33,'add_users'),(130,'Can change users',33,'change_users'),(131,'Can delete users',33,'delete_users'),(132,'Can view users',33,'view_users');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-07 14:41:02
