-- phpMyAdmin SQL Dump
-- version 4.6.5.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 07, 2018 at 06:46 PM
-- Server version: 10.1.21-MariaDB
-- PHP Version: 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `edulab`
--

-- --------------------------------------------------------

--
-- Table structure for table `dataanalyst_ncr`
--

CREATE TABLE `dataanalyst_ncr` (
  `job_id` int(4) NOT NULL,
  `job_title` text NOT NULL,
  `experience_required` varchar(20) NOT NULL,
  `company_name` text NOT NULL,
  `link_page` text NOT NULL,
  `keyskills` text,
  `job_description` text,
  `salary` text NOT NULL,
  `last_updated_on` datetime DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1 ROW_FORMAT=COMPACT;

-- --------------------------------------------------------

--
-- Table structure for table `location_jobs`
--

CREATE TABLE `location_jobs` (
  `job_id` int(4) NOT NULL,
  `locn_id` int(2) NOT NULL,
  `location` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `dataanalyst_ncr`
--
ALTER TABLE `dataanalyst_ncr`
  ADD PRIMARY KEY (`job_id`);

--
-- Indexes for table `location_jobs`
--
ALTER TABLE `location_jobs`
  ADD PRIMARY KEY (`job_id`,`locn_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `dataanalyst_ncr`
--
ALTER TABLE `dataanalyst_ncr`
  MODIFY `job_id` int(4) NOT NULL AUTO_INCREMENT;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `location_jobs`
--
ALTER TABLE `location_jobs`
  ADD CONSTRAINT `location_jobs_ibfk_1` FOREIGN KEY (`job_id`) REFERENCES `dataanalyst_ncr` (`job_id`) ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
