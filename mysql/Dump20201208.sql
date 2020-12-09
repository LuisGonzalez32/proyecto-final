CREATE DATABASE  IF NOT EXISTS `tienda` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `tienda`;
-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: localhost    Database: tienda
-- ------------------------------------------------------
-- Server version	8.0.21

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
-- Table structure for table `carrito`
--

DROP TABLE IF EXISTS `carrito`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `carrito` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_cliente` int NOT NULL,
  `id_producto` int NOT NULL,
  `cantidad` int NOT NULL,
  `costo_total` decimal(15,2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_id_cliente_idx` (`id_cliente`),
  KEY `fk_id_producto_idx` (`id_producto`),
  CONSTRAINT `fk_id_cliente` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`id`),
  CONSTRAINT `fk_id_producto` FOREIGN KEY (`id_producto`) REFERENCES `productos` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carrito`
--

LOCK TABLES `carrito` WRITE;
/*!40000 ALTER TABLE `carrito` DISABLE KEYS */;
/*!40000 ALTER TABLE `carrito` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categorias`
--

DROP TABLE IF EXISTS `categorias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categorias` (
  `id` int NOT NULL AUTO_INCREMENT,
  `categoria` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categorias`
--

LOCK TABLES `categorias` WRITE;
/*!40000 ALTER TABLE `categorias` DISABLE KEYS */;
INSERT INTO `categorias` VALUES (25,'telefono'),(26,'videojuego'),(27,'computadora');
/*!40000 ALTER TABLE `categorias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cliente`
--

DROP TABLE IF EXISTS `cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cliente` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `apellido` varchar(45) NOT NULL,
  `usuario` varchar(45) NOT NULL,
  `contrasenia` varchar(45) NOT NULL,
  `correo` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente`
--

LOCK TABLES `cliente` WRITE;
/*!40000 ALTER TABLE `cliente` DISABLE KEYS */;
INSERT INTO `cliente` VALUES (12,'adrian','camacho','adrian','adrian123','adrian@hotmail.com');
/*!40000 ALTER TABLE `cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `compras`
--

DROP TABLE IF EXISTS `compras`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `compras` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_detalles_pago` int NOT NULL,
  `id_producto` int NOT NULL,
  `cantidad` int NOT NULL,
  `costo_total` decimal(15,2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_detalles_pago_idx` (`id_detalles_pago`),
  KEY `id_productoo_idx` (`id_producto`),
  CONSTRAINT `id_detalles_pago` FOREIGN KEY (`id_detalles_pago`) REFERENCES `detalles_pago` (`id`),
  CONSTRAINT `productos` FOREIGN KEY (`id_producto`) REFERENCES `productos` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=128 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `compras`
--

LOCK TABLES `compras` WRITE;
/*!40000 ALTER TABLE `compras` DISABLE KEYS */;
INSERT INTO `compras` VALUES (123,106,35,1,1111.00),(124,106,38,1,1500.00),(125,106,37,1,500.00),(126,107,34,1,1000.00),(127,107,36,2,800.00);
/*!40000 ALTER TABLE `compras` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalles_pago`
--

DROP TABLE IF EXISTS `detalles_pago`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalles_pago` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_cliente` int NOT NULL,
  `pais` varchar(45) NOT NULL,
  `ciudad` varchar(45) NOT NULL,
  `direccion` varchar(45) NOT NULL,
  `tarjeta_credito` int NOT NULL,
  `hora_compra` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cliente_idx` (`id_cliente`),
  CONSTRAINT `client` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=108 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalles_pago`
--

LOCK TABLES `detalles_pago` WRITE;
/*!40000 ALTER TABLE `detalles_pago` DISABLE KEYS */;
INSERT INTO `detalles_pago` VALUES (106,12,'sivar','san sivar','escalon',3240,'2020-12-08 18:21:36'),(107,12,'sivar','san sivar','escalon',54321,'2020-12-08 18:24:01');
/*!40000 ALTER TABLE `detalles_pago` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `factura`
--

DROP TABLE IF EXISTS `factura`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `factura` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_detalles_pago` int NOT NULL,
  `total_pago` decimal(15,2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_detalles_pago_idx` (`id_detalles_pago`),
  KEY `detalles__pago _idx` (`id_detalles_pago`),
  CONSTRAINT `detalles__pago ` FOREIGN KEY (`id_detalles_pago`) REFERENCES `detalles_pago` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=62 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `factura`
--

LOCK TABLES `factura` WRITE;
/*!40000 ALTER TABLE `factura` DISABLE KEYS */;
INSERT INTO `factura` VALUES (60,106,3111.00),(61,107,1800.00);
/*!40000 ALTER TABLE `factura` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productos`
--

DROP TABLE IF EXISTS `productos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `productos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `id_categoria` int NOT NULL,
  `descripcion` varchar(45) NOT NULL,
  `precio` decimal(15,2) NOT NULL,
  `cantidad_disponible` int NOT NULL,
  `ultima_actualizacion` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_categoria_idx` (`id_categoria`),
  CONSTRAINT `id_categoria` FOREIGN KEY (`id_categoria`) REFERENCES `categorias` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productos`
--

LOCK TABLES `productos` WRITE;
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` VALUES (34,'samsung s20',25,'samsung s20 negro',1000.00,191,'2020-12-08 18:24:01'),(35,'iphone 12',25,'iphone 12 blanco',1111.00,346,'2020-12-08 18:21:36'),(36,'Xbox Series X',26,'1TB',400.00,238,'2020-12-08 18:24:01'),(37,'ps5',26,'version digital',500.00,185,'2020-12-08 18:21:36'),(38,'macbook pro',27,'256 GB',1500.00,295,'2020-12-08 18:21:36');
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `view_carrito`
--

DROP TABLE IF EXISTS `view_carrito`;
/*!50001 DROP VIEW IF EXISTS `view_carrito`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `view_carrito` AS SELECT 
 1 AS `idCliente`,
 1 AS `nombreCliente`,
 1 AS `nombreProducto`,
 1 AS `cantidad`,
 1 AS `costo_total`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `view_compras`
--

DROP TABLE IF EXISTS `view_compras`;
/*!50001 DROP VIEW IF EXISTS `view_compras`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `view_compras` AS SELECT 
 1 AS `idCliente`,
 1 AS `nombreCliente`,
 1 AS `nombreProducto`,
 1 AS `cantidad`,
 1 AS `costo_total`,
 1 AS `tarjeta_credito`,
 1 AS `pais`,
 1 AS `ciudad`,
 1 AS `direccion`,
 1 AS `hora_compra`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `view_productos`
--

DROP TABLE IF EXISTS `view_productos`;
/*!50001 DROP VIEW IF EXISTS `view_productos`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `view_productos` AS SELECT 
 1 AS `id`,
 1 AS `nombre`,
 1 AS `categoria`,
 1 AS `descripcion`,
 1 AS `precio`,
 1 AS `cantidad`,
 1 AS `ultima_actualizacion`*/;
SET character_set_client = @saved_cs_client;

--
-- Dumping routines for database 'tienda'
--

--
-- Final view structure for view `view_carrito`
--

/*!50001 DROP VIEW IF EXISTS `view_carrito`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_carrito` AS select `cliente`.`id` AS `idCliente`,`cliente`.`nombre` AS `nombreCliente`,`productos`.`nombre` AS `nombreProducto`,`carrito`.`cantidad` AS `cantidad`,`carrito`.`costo_total` AS `costo_total` from ((`carrito` join `cliente` on((`carrito`.`id_cliente` = `cliente`.`id`))) join `productos` on((`carrito`.`id_producto` = `productos`.`id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_compras`
--

/*!50001 DROP VIEW IF EXISTS `view_compras`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_compras` AS select `cliente`.`id` AS `idCliente`,`cliente`.`nombre` AS `nombreCliente`,`productos`.`nombre` AS `nombreProducto`,`compras`.`cantidad` AS `cantidad`,`compras`.`costo_total` AS `costo_total`,`detalles_pago`.`tarjeta_credito` AS `tarjeta_credito`,`detalles_pago`.`pais` AS `pais`,`detalles_pago`.`ciudad` AS `ciudad`,`detalles_pago`.`direccion` AS `direccion`,`detalles_pago`.`hora_compra` AS `hora_compra` from ((((`detalles_pago` join `compras` on((`detalles_pago`.`id` = `compras`.`id_detalles_pago`))) join `factura` on((`detalles_pago`.`id` = `factura`.`id_detalles_pago`))) join `cliente` on((`detalles_pago`.`id_cliente` = `cliente`.`id`))) join `productos` on((`compras`.`id_producto` = `productos`.`id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_productos`
--

/*!50001 DROP VIEW IF EXISTS `view_productos`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_productos` AS select `productos`.`id` AS `id`,`productos`.`nombre` AS `nombre`,`categorias`.`categoria` AS `categoria`,`productos`.`descripcion` AS `descripcion`,`productos`.`precio` AS `precio`,`productos`.`cantidad_disponible` AS `cantidad`,`productos`.`ultima_actualizacion` AS `ultima_actualizacion` from (`productos` join `categorias` on((`productos`.`id_categoria` = `categorias`.`id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-08 18:27:06
