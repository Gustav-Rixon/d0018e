-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jan 03, 2021 at 07:34 PM
-- Server version: 8.0.22-0ubuntu0.20.04.3
-- PHP Version: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `d0018e`
--

-- --------------------------------------------------------

--
-- Table structure for table `Categories`
--

CREATE TABLE `Categories` (
  `category_id` int NOT NULL,
  `category_name` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `Categories`
--

INSERT INTO `Categories` (`category_id`, `category_name`) VALUES
(1, 'Sword'),
(2, 'Explosives'),
(3, 'Flamethrower'),
(853432, 'Handgranat');

-- --------------------------------------------------------

--
-- Table structure for table `Customers`
--

CREATE TABLE `Customers` (
  `customer_id` int NOT NULL,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `email` varchar(128) NOT NULL,
  `owner_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `Customers`
--

INSERT INTO `Customers` (`customer_id`, `first_name`, `last_name`, `password`, `email`, `owner_id`) VALUES
(269, '123', '123', '123', 'victo@123r', 1),
(441, 'test', 'test', 'test', 'test@test.com', 1),
(1646, 'Gustav', 'Rixon', 'test', 'gustav.rixon@gmail.com', 1),
(2339, 'victor', 'longberg', '123', 'victor.longberg@gmail.com', 1),
(2530, 'aa', 'bb', 'aa', 'edison@mail.com', 1),
(3041, 'Gustavo', 'Pixel', '1', 'pixel@gmail.com', 1),
(3183, 'viclon', 'longberg', '123', 'viclon@gmail.com', 1),
(7534, 'aa', 'bb', 'aa', 'aa@bb.COM', 1);

-- --------------------------------------------------------

--
-- Table structure for table `Feedback`
--

CREATE TABLE `Feedback` (
  `feedback` smallint NOT NULL,
  `prod_id` int NOT NULL,
  `rating` varchar(45) NOT NULL,
  `comment` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `date` varchar(45) NOT NULL,
  `customer_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `Feedback`
--

INSERT INTO `Feedback` (`feedback`, `prod_id`, `rating`, `comment`, `date`, `customer_id`) VALUES
(10, 2, '1', 'test 123', '2021-01-03', 3183),
(12, 3, '5', 'Hot', '2020-01-02', 3041),
(38, 1, '5', 'thunderfury blessed blade of the windseeker!!!!!', '2021-01-03', 1646),
(39, 1, '5', 'thunderfury blessed blade of the windseeker!!!!!', '2021-01-03', 1646);

-- --------------------------------------------------------

--
-- Table structure for table `Orders`
--

CREATE TABLE `Orders` (
  `order_id` int NOT NULL,
  `order_status` int NOT NULL,
  `prod_id` int DEFAULT NULL,
  `pris_fast` int DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `customer_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `Orders`
--

INSERT INTO `Orders` (`order_id`, `order_status`, `prod_id`, `pris_fast`, `quantity`, `customer_id`) VALUES
(221, 1, 1, 1000, 1, 2530),
(367, 1, 2, 400, 5, 2339),
(446, 0, 1, NULL, 1, 2339),
(489, 1, 1, 1000, 10, 1646),
(579, 1, 3, 750, 12, 1646),
(672, 1, 1, 2000, 1, 3183),
(728, 1, 2, 400, 1, 2530),
(1277, 1, 1, 1000, 1, 1646),
(2181, 0, 5, NULL, 1, 3183),
(2255, 0, 1, NULL, 1, 7534),
(2309, 0, 1, NULL, 1, 441),
(3160, 1, 3, 750, 5, 1646),
(3192, 0, 2, NULL, 1, 3183),
(3326, 0, 1, NULL, 1, 1646),
(3810, 1, 1, 1000, 1, 3183),
(3908, 1, 1, 1000, 1, 1646),
(4001, 0, 1, NULL, 1, 7534),
(4055, 0, 1, NULL, 1, 1646),
(4183, 1, 1, 100, 6, 2339),
(4671, 1, 1, 1000, 20, 1646),
(4792, 1, 1, 2000, 20, 441),
(4806, 1, 2, 400, 1, 1646),
(4982, 1, 1, 1000, 12, 441),
(5150, 0, 5, NULL, 1, 1646),
(5542, 0, 1, NULL, 1, 441),
(5910, 0, 1, NULL, 1, 1646),
(5976, 1, 4, 50000000, 1, 3183),
(6169, 1, 4, 50000000, 499, 1646),
(6283, 1, 4, 50000000, 1, 3183),
(6351, 0, 4, NULL, 1, 2339),
(6978, 0, 5, NULL, 1, 1646),
(7355, 1, 1, 2000, 1, 3183),
(7505, 1, 2, 400, 31, 1646),
(7780, 1, 1, 1000, 1, 2530),
(7972, 1, 1, 1000, 10, 3041),
(8272, 0, 1, NULL, 1, 1646),
(8519, 1, 2, 500, 1, 1646),
(8557, 1, 3, 750, 6, 1646),
(8566, 1, 1, 1000, 5, 1646),
(8687, 1, 1, 1000, 1, 2339),
(8705, 1, 1, 1000, 21, 1646),
(8863, 1, 1, 1000, 1, 2530),
(9191, 0, 3, NULL, 1, 1646),
(9285, 0, 2, NULL, 1, 1646),
(9328, 1, 1, 1000, 1, 3183),
(9418, 0, 4, NULL, 1, 1646),
(9932, 1, 1, 2000, 10, 441);

-- --------------------------------------------------------

--
-- Table structure for table `Order_items`
--

CREATE TABLE `Order_items` (
  `order_item_id` int NOT NULL,
  `order_item_quantity` int NOT NULL,
  `prod_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `Order_items`
--

INSERT INTO `Order_items` (`order_item_id`, `order_item_quantity`, `prod_id`) VALUES
(446, 999, 1),
(2255, 1, 1),
(2309, 1000, 1),
(3192, 1, 2),
(3326, 100, 1),
(4001, 1, 1),
(4055, 30, 1),
(5542, 1, 1),
(5910, 20, 1),
(6351, 1001, 4),
(8272, 10, 1),
(9191, 98, 3),
(9285, 30, 2),
(9418, 1, 4);

-- --------------------------------------------------------

--
-- Table structure for table `Owner`
--

CREATE TABLE `Owner` (
  `owner_id` int NOT NULL,
  `name` varchar(45) NOT NULL,
  `email` varchar(128) NOT NULL,
  `password` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `Owner`
--

INSERT INTO `Owner` (`owner_id`, `name`, `email`, `password`) VALUES
(1, 'bob', 'bob@bob.com', 'bob');

-- --------------------------------------------------------

--
-- Table structure for table `Products`
--

CREATE TABLE `Products` (
  `prod_id` int NOT NULL,
  `prod_name` varchar(20) NOT NULL,
  `price` int NOT NULL,
  `img_url` varchar(255) DEFAULT NULL,
  `categorie_id` int NOT NULL,
  `prod_description` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `Products`
--

INSERT INTO `Products` (`prod_id`, `prod_name`, `price`, `img_url`, `categorie_id`, `prod_description`) VALUES
(1, 'Steel Sword', 1000, 'https://upload.wikimedia.org/wikipedia/commons/3/3a/Trp-Sword-14226124129-v06.png', 1, 'Ska du klappa ihjäl draken eller?'),
(2, 'Granada', 500, 'https://static.wikia.nocookie.net/miscreated/images/9/98/GrenadePickup_2048.png', 2, 'Makes big boom'),
(3, 'Flamenwaferer', 750, 'https://wasteland3.wiki.fextralife.com/file/Wasteland-3/army-flamethrower-heavy-gun-weapon-wasteland-3-wiki-guide-300px.png', 3, 'Keeps you warm!'),
(4, 'Laser Sword', 50000000, 'https://upload.wikimedia.org/wikipedia/commons/1/14/Lightsaber%2C_silver_hilt%2C_blue_blade.png', 1, 'Keep away from children.');

-- --------------------------------------------------------

--
-- Table structure for table `RelOwnProd`
--

CREATE TABLE `RelOwnProd` (
  `rel_own_prod_id` int NOT NULL,
  `owner_id` int NOT NULL,
  `prod_id` int NOT NULL,
  `stock` int NOT NULL
) ;

--
-- Dumping data for table `RelOwnProd`
--

INSERT INTO `RelOwnProd` (`rel_own_prod_id`, `owner_id`, `prod_id`, `stock`) VALUES
(1, 1, 1, 978),
(2, 1, 2, 999),
(3, 1, 3, 477),
(4, 1, 4, 998);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Categories`
--
ALTER TABLE `Categories`
  ADD PRIMARY KEY (`category_id`);

--
-- Indexes for table `Customers`
--
ALTER TABLE `Customers`
  ADD PRIMARY KEY (`customer_id`),
  ADD UNIQUE KEY `email_UNIQUE` (`email`),
  ADD UNIQUE KEY `customer_id_UNIQUE` (`customer_id`),
  ADD KEY `fk_Customers_Owner_idx` (`owner_id`);

--
-- Indexes for table `Feedback`
--
ALTER TABLE `Feedback`
  ADD PRIMARY KEY (`feedback`),
  ADD UNIQUE KEY `feedback_UNIQUE` (`feedback`),
  ADD KEY `fk_test_c` (`customer_id`),
  ADD KEY `prod_idx` (`prod_id`);

--
-- Indexes for table `Orders`
--
ALTER TABLE `Orders`
  ADD PRIMARY KEY (`order_id`),
  ADD UNIQUE KEY `order_id_UNIQUE` (`order_id`),
  ADD KEY `test02` (`prod_id`),
  ADD KEY `customer` (`customer_id`);

--
-- Indexes for table `Order_items`
--
ALTER TABLE `Order_items`
  ADD PRIMARY KEY (`order_item_id`),
  ADD KEY `fk_Order_items_Products` (`prod_id`);

--
-- Indexes for table `Owner`
--
ALTER TABLE `Owner`
  ADD PRIMARY KEY (`owner_id`),
  ADD UNIQUE KEY `owner_id_UNIQUE` (`owner_id`);

--
-- Indexes for table `Products`
--
ALTER TABLE `Products`
  ADD PRIMARY KEY (`prod_id`),
  ADD KEY `categorie_idx` (`categorie_id`);

--
-- Indexes for table `RelOwnProd`
--
ALTER TABLE `RelOwnProd`
  ADD PRIMARY KEY (`rel_own_prod_id`),
  ADD UNIQUE KEY `rel_own_prod_id_UNIQUE` (`rel_own_prod_id`),
  ADD UNIQUE KEY `rel_own_prod_id` (`rel_own_prod_id`),
  ADD KEY `fk_Order_items_Orders_idx` (`owner_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Feedback`
--
ALTER TABLE `Feedback`
  MODIFY `feedback` smallint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=40;

--
-- AUTO_INCREMENT for table `RelOwnProd`
--
ALTER TABLE `RelOwnProd`
  MODIFY `rel_own_prod_id` int NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Customers`
--
ALTER TABLE `Customers`
  ADD CONSTRAINT `fk_Customers_Owner` FOREIGN KEY (`owner_id`) REFERENCES `Owner` (`owner_id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Constraints for table `Feedback`
--
ALTER TABLE `Feedback`
  ADD CONSTRAINT `fk_Feedback_Customers` FOREIGN KEY (`customer_id`) REFERENCES `Customers` (`customer_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `fk_Feedback_Products` FOREIGN KEY (`prod_id`) REFERENCES `Products` (`prod_id`) ON DELETE CASCADE ON UPDATE RESTRICT;

--
-- Constraints for table `Orders`
--
ALTER TABLE `Orders`
  ADD CONSTRAINT `fk_Orders_Customers` FOREIGN KEY (`customer_id`) REFERENCES `Customers` (`customer_id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Constraints for table `Order_items`
--
ALTER TABLE `Order_items`
  ADD CONSTRAINT `fk_Order_items_Orders` FOREIGN KEY (`order_item_id`) REFERENCES `Orders` (`order_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `fk_Order_items_Products` FOREIGN KEY (`prod_id`) REFERENCES `Products` (`prod_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Products`
--
ALTER TABLE `Products`
  ADD CONSTRAINT `fk_Products_Categories` FOREIGN KEY (`categorie_id`) REFERENCES `Categories` (`category_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `fk_Products_RelOwnProd` FOREIGN KEY (`prod_id`) REFERENCES `RelOwnProd` (`prod_id`) ON DELETE CASCADE ON UPDATE RESTRICT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
