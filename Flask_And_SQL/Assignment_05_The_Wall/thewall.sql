-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: thewall
-- ------------------------------------------------------
-- Server version	5.7.19-log

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
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comments` (
  `comment_id` int(11) NOT NULL AUTO_INCREMENT,
  `message_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `comment` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`comment_id`),
  KEY `fk_comments_messages1_idx` (`message_id`),
  KEY `fk_comments_users1_idx` (`user_id`),
  CONSTRAINT `fk_comments_messages1` FOREIGN KEY (`message_id`) REFERENCES `messages` (`message_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `messages` (
  `message_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `message` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`message_id`),
  KEY `fk_messages_users_idx` (`user_id`),
  CONSTRAINT `fk_messages_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (1,1,'Lorem ipsum dolor sit amet consectetur adipisicing elit. Enim nam placeat hic vero qui reiciendis maiores obcaecati cum. Eveniet sed quibusdam praesentium atque enim voluptate ipsam aliquid, asperiores earum vel.','2018-07-22 17:11:39','2018-07-22 17:11:39'),(2,1,'Enim nam placeat hic vero qui reiciendis maiores obcaecati cum. Eveniet sed quibusdam praesentium atque enim voluptate ipsam aliquid, asperiores earum vel.','2018-07-22 17:11:50','2018-07-22 17:11:50'),(3,2,'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Possimus provident consequatur, rerum deserunt totam cum hic ducimus veniam consectetur incidunt? Consequatur quisquam nisi deleniti iure possimus architecto voluptas obcaecati ratione non vel illum sint, porro impedit excepturi inventore tempora et perferendis accusamus blanditiis. Aut esse dignissimos ipsum veritatis repellat excepturi harum eaque recusandae expedita atque! At commodi rem earum excepturi repellat voluptates ea nulla voluptatibus sed enim eaque dignissimos officiis accusamus, veritatis dolores quaerat quae, debitis voluptate doloribus voluptas beatae maxime magni, id quod. Ut enim fugit dolor. Adipisci alias ex et laudantium doloribus, provident, libero nemo ullam vitae odit fuga dolorum ducimus id saepe suscipit fugiat ipsa aliquam maiores voluptates nobis assumenda ipsum. Consectetur, iusto. Nobis itaque delectus aperiam doloremque dolorem perferendis adipisci necessitatibus animi quaerat. Aspernatur nemo, nulla rerum sunt eveniet sint nihil provident quia consectetur ipsum obcaecati itaque eaque inventore est tempora quo ex asperiores impedit. Accusantium.','2018-07-22 17:43:03','2018-07-22 17:43:03'),(4,2,'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Asperiores ut unde cumque quas incidunt est ex perferendis, ipsum possimus id sed veniam quis exercitationem explicabo, sunt nesciunt tempora culpa iure animi deserunt fuga minus fugit? Perspiciatis voluptas distinctio reprehenderit aspernatur nesciunt fugiat quae cum architecto ratione accusamus facere quo ullam eligendi culpa consectetur, iure, minus pariatur neque laudantium in vel odit ea. Porro quae illo provident, cupiditate, officiis quo veritatis eius eos, facere ratione sit!','2018-07-22 18:05:38','2018-07-22 18:05:38'),(5,1,'Having a good old time!','2018-07-22 18:07:10','2018-07-22 18:07:10');
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Eric','Greenhalgh','egreenhalgh@gmail.com','3828cbce68df9ffb3f356c0d336730ee','2018-07-22 16:56:05','2018-07-22 16:56:05'),(2,'Johnny','Appleseed','johnny@appleseed.com','de740abd574e12fb186dd0c91925211b','2018-07-22 17:40:50','2018-07-22 17:40:50'),(3,'Black','Widow','blackwidow@theweb.com','a076853864c6923ae439e4cc3aec78a5','2018-07-22 18:23:05','2018-07-22 18:23:05');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-07-22 19:12:30
