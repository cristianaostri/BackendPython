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
-- Table structure for table `carritos`
--

DROP TABLE IF EXISTS `carritos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `carritos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` datetime DEFAULT NULL,
  `total` decimal(10,2) DEFAULT NULL,
  `id_usuario` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_usuario` (`id_usuario`),
  CONSTRAINT `carritos_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `carritos_ibfk_2` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carritos`
--

LOCK TABLES `carritos` WRITE;
/*!40000 ALTER TABLE `carritos` DISABLE KEYS */;
INSERT INTO `carritos` VALUES (12,'2024-06-20 10:00:00',150.00,1),(13,'2024-06-21 11:30:00',200.00,2),(14,'2024-06-22 14:45:00',75.00,3),(15,'2024-06-23 16:10:00',90.00,4),(16,'2024-06-24 18:25:00',120.00,5),(17,'2024-06-20 10:00:00',150.00,1),(18,'2024-06-21 11:30:00',200.00,2),(19,'2024-06-22 14:45:00',75.00,3),(20,'2024-06-23 16:10:00',90.00,4),(21,'2024-06-24 18:25:00',120.00,5);
/*!40000 ALTER TABLE `carritos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categoria`
--

DROP TABLE IF EXISTS `categoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categoria` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `detalle` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categoria`
--

LOCK TABLES `categoria` WRITE;
/*!40000 ALTER TABLE `categoria` DISABLE KEYS */;
INSERT INTO `categoria` VALUES (1,'Perfume','Fragancias para hombres y mujeres'),(2,'Cosméticos','Productos de maquillaje y cuidado de la piel'),(3,'Cuidado del cabello','Champús, acondicionadores y tratamientos para el cabello'),(4,'Cuidado personal','Productos para la higiene personal y el cuidado diario'),(5,'Accesorios','Accesorios para la aplicación de productos cosméticos'),(6,'Perfume','Fragancias para hombres y mujeres'),(7,'Cosméticos','Productos de maquillaje y cuidado de la piel'),(8,'Cuidado del cabello','Champús, acondicionadores y tratamientos para el cabello'),(9,'Cuidado personal','Productos para la higiene personal y el cuidado diario'),(10,'Accesorios','Accesorios para la aplicación de productos cosméticos'),(11,'Perfume','Fragancias para hombres y mujeres'),(12,'Cosméticos','Productos de maquillaje y cuidado de la piel'),(13,'Cuidado del cabello','Champús, acondicionadores y tratamientos para el cabello'),(14,'Cuidado personal','Productos para la higiene personal y el cuidado diario'),(15,'Accesorios','Accesorios para la aplicación de productos cosméticos'),(16,'Perfume','Fragancias para hombres y mujeres'),(17,'Cosméticos','Productos de maquillaje y cuidado de la piel'),(18,'Cuidado del cabello','Champús, acondicionadores y tratamientos para el cabello'),(19,'Cuidado personal','Productos para la higiene personal y el cuidado diario'),(20,'Accesorios','Accesorios para la aplicación de productos cosméticos');
/*!40000 ALTER TABLE `categoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalle_carrito`
--

DROP TABLE IF EXISTS `detalle_carrito`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalle_carrito` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cantidad` int(11) DEFAULT NULL,
  `precio_unitario` decimal(10,2) DEFAULT NULL,
  `id_carrito` int(11) NOT NULL,
  `id_producto` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_carrito` (`id_carrito`),
  KEY `id_producto` (`id_producto`),
  CONSTRAINT `detalle_carrito_ibfk_1` FOREIGN KEY (`id_carrito`) REFERENCES `carritos` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `detalle_carrito_ibfk_2` FOREIGN KEY (`id_producto`) REFERENCES `productos` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `detalle_carrito_ibfk_3` FOREIGN KEY (`id_carrito`) REFERENCES `carritos` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `detalle_carrito_ibfk_4` FOREIGN KEY (`id_producto`) REFERENCES `productos` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalle_carrito`
--

LOCK TABLES `detalle_carrito` WRITE;
/*!40000 ALTER TABLE `detalle_carrito` DISABLE KEYS */;
/*!40000 ALTER TABLE `detalle_carrito` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `marca`
--

DROP TABLE IF EXISTS `marca`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `marca` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `detalle` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `marca`
--

LOCK TABLES `marca` WRITE;
/*!40000 ALTER TABLE `marca` DISABLE KEYS */;
INSERT INTO `marca` VALUES (1,'Chanel','Marca de lujo conocida por sus perfumes y cosméticos'),(2,'Dior','Marca de lujo especializada en perfumes y moda'),(3,'Lancome','Marca francesa de cosméticos y perfumes'),(4,'Estee Lauder','Empresa estadounidense de productos de belleza y cuidado de la piel'),(5,'L\'Oreal','Marca global de cosméticos y cuidado personal'),(6,'Chanel','Marca de lujo conocida por sus perfumes y cosméticos'),(7,'Dior','Marca de lujo especializada en perfumes y moda'),(8,'Lancome','Marca francesa de cosméticos y perfumes'),(9,'Estee Lauder','Empresa estadounidense de productos de belleza y cuidado de la piel'),(10,'L\'Oreal','Marca global de cosméticos y cuidado personal'),(11,'Chanel','Marca de lujo conocida por sus perfumes y cosméticos'),(12,'Dior','Marca de lujo especializada en perfumes y moda'),(13,'Lancome','Marca francesa de cosméticos y perfumes'),(14,'Estee Lauder','Empresa estadounidense de productos de belleza y cuidado de la piel'),(15,'L\'Oreal','Marca global de cosméticos y cuidado personal'),(16,'Chanel','Marca de lujo conocida por sus perfumes y cosméticos'),(17,'Dior','Marca de lujo especializada en perfumes y moda'),(18,'Lancome','Marca francesa de cosméticos y perfumes'),(19,'Estee Lauder','Empresa estadounidense de productos de belleza y cuidado de la piel'),(20,'L\'Oreal','Marca global de cosméticos y cuidado personal'),(21,'Chanel','Marca de lujo conocida por sus perfumes y cosméticos'),(22,'Dior','Marca de lujo especializada en perfumes y moda'),(23,'Lancome','Marca francesa de cosméticos y perfumes'),(24,'Estee Lauder','Empresa estadounidense de productos de belleza y cuidado de la piel'),(25,'L\'Oreal','Marca global de cosméticos y cuidado personal');
/*!40000 ALTER TABLE `marca` ENABLE KEYS */;
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
  `stock` int(11) NOT NULL,
  `precio_venta` decimal(10,2) DEFAULT NULL,
  `id_usuario` int(11) NOT NULL,
  `id_categoria` int(11) NOT NULL,
  `id_marca` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_usuario` (`id_usuario`),
  KEY `id_categoria` (`id_categoria`),
  KEY `id_marca` (`id_marca`),
  CONSTRAINT `productos_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `productos_ibfk_2` FOREIGN KEY (`id_categoria`) REFERENCES `categoria` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `productos_ibfk_3` FOREIGN KEY (`id_marca`) REFERENCES `marca` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `productos_ibfk_4` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `productos_ibfk_5` FOREIGN KEY (`id_categoria`) REFERENCES `categoria` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `productos_ibfk_6` FOREIGN KEY (`id_marca`) REFERENCES `marca` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productos`
--

LOCK TABLES `productos` WRITE;
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` VALUES (12,'Chanel No. 5',100,120.00,1,1,1),(13,'Dior Sauvage',150,100.00,2,1,2),(14,'Lancome Mascara',200,30.00,3,2,3),(15,'Estee Lauder Serum',50,75.00,4,4,4),(16,'L\'Oreal Shampoo',300,20.00,5,3,5),(17,'Jean Paul',25,800.00,1,2,3),(18,'Chanel No. 2',2,275.00,1,2,3);
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
  `contraseña` varchar(50) NOT NULL,
  `comentario` text DEFAULT NULL,
  `categoria` varchar(50) NOT NULL,
  `edad` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'Johnathan Doe','johnathan.doe@example.com','password1','Me encanta este sitio','Cliente',28),(2,'Bob Smith','bob.smith@example.com','password2','Servicio rápido','Cliente',34),(3,'Carol White','carol.white@example.com','password3','Buenos productos','Empleado',45),(4,'David Brown','david.brown@example.com','password4','Muy recomendable','Cliente',22),(5,'Eva Green','eva.green@example.com','password5','Excelentes precios','Cliente',30),(6,'John Doe','john.doe@example.com','password123','Comentario','Cliente',30),(7,'John Doe','john.doe@example.com','supersecurepassword','Excelente servicio','Cliente',29),(15,'John Doe','john.doe@example.com','supersecurepassword','Excelente servicio','Cliente',29),(16,'John Doe','john.doe@example.com','supersecurepassword','Excelente servicio','Cliente',29);
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

-- Dump completed on 2024-06-23  5:27:27
