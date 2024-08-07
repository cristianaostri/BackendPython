-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: perfumeria
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.28-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `imagenes`
--

DROP TABLE IF EXISTS `imagenes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `imagenes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url_img` varchar(255) DEFAULT NULL,
  `texto_alt` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `imagenes`
--

LOCK TABLES `imagenes` WRITE;
/*!40000 ALTER TABLE `imagenes` DISABLE KEYS */;
INSERT INTO `imagenes` VALUES (1,'https://fraguru.com/mdimg/perfume/375x500.72158.jpg','Imagen 1'),(2,'https://fraguru.com/mdimg/perfume/375x500.16657.jpg','Imagen 2'),(3,'https://fraguru.com/mdimg/perfume/375x500.40031.jpg','Imagen 3'),(4,'https://fraguru.com/mdimg/perfume/375x500.55858.jpg','Imagen 4'),(5,'https://fraguru.com/mdimg/perfume/375x500.3747.jpg','Imagen 5'),(6,'https://fraguru.com/mdimg/perfume/375x500.1460.jpg','Imagen 6'),(7,'https://fraguru.com/mdimg/perfume/375x500.37735.jpg','Imagen 7'),(8,'https://fraguru.com/mdimg/perfume/375x500.39681.jpg','Imagen 8'),(9,'https://fraguru.com/mdimg/perfume/375x500.704.jpg','Imagen 9'),(10,'home/https://fraguru.com/mdimg/perfume/375x500.53.jpg','Imagen 10'),(11,'home/https://fraguru.com/mdimg/perfume/375x500.15210.jpg','Imagen 11');
/*!40000 ALTER TABLE `imagenes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productos`
--

DROP TABLE IF EXISTS `productos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `productos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(20) DEFAULT NULL,
  `precio_venta` decimal(10,2) DEFAULT NULL,
  `tipo` varchar(20) DEFAULT NULL,
  `imagen_url` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productos`
--

LOCK TABLES `productos` WRITE;
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` VALUES (1,'Perfume B',59.99,'hombre','https://fraguru.com/mdimg/perfume/375x500.16657.jpg'),(2,'Perfume A',49.99,'mujer','https://fraguru.com/mdimg/perfume/375x500.72158.jpg'),(3,'Perfume B',59.99,'hombre','https://fraguru.com/mdimg/perfume/375x500.16657.jpg'),(4,'Perfume A',49.99,'mujer','https://fraguru.com/mdimg/perfume/375x500.72158.jpg'),(5,'Perfume B',59.99,'hombre','https://fraguru.com/mdimg/perfume/375x500.16657.jpg'),(6,'Perfume A',49.99,'mujer','https://fraguru.com/mdimg/perfume/375x500.72158.jpg'),(7,'Perfume B',59.99,'hombre','https://fraguru.com/mdimg/perfume/375x500.16657.jpg');
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(30) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'Juan Perez','juan.perez@example.com','password1'),(2,'Ana Gomez','ana.gomez@example.com','password2'),(3,'Juan Perez','juan.perez@example.com','password1'),(4,'Ana Gomez','ana.gomez@example.com','password2'),(5,'John Doe','john.doe@example.com','caco123');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-29 17:52:34
