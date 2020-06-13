-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jun 13, 2020 at 07:44 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.2.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dailyblogs`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sno` int(50) NOT NULL,
  `name` text NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone_num` varchar(50) NOT NULL,
  `msg` text NOT NULL,
  `date` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`sno`, `name`, `email`, `phone_num`, `msg`, `date`) VALUES
(1, 'First Post', 'firstpost@gmail.com', '1234567890', 'Hi there! This is a first post', '2020-06-06 13:19:29'),
(5, 'Hi', 'hi@gmail.com', '1717171718', 'HI! A message from hi', '2020-06-06 13:34:19'),
(6, 'Hi', 'hi@gmail.com', '1717171718', 'HI! A message from hi', '2020-06-06 14:13:55'),
(7, 'Hi', 'hi@gmail.com', '1212121212', 'HI! A hi from hi', '2020-06-07 17:36:54'),
(8, 'Hi', 'hi@gmail.com', '1212121212', 'HI! A hi from hi', '2020-06-07 18:00:35'),
(9, 'Hi', 'hi@gmail.com', '1212121212', 'HI! A hi from hi', '2020-06-07 18:01:21'),
(10, 'Hi', 'hi@gmail.com', '1212121212', 'HI! A hi from hi', '2020-06-07 18:03:02'),
(11, 'Test name', 'test@gmail.com', '1111111111', 'Hi there! This is a test message. Hope this will work.\r\n', '2020-06-07 21:23:21'),
(12, 'Test name', 'test@gmail.com', '1111111111', 'Hi there! This is a test message. Hope this will work.\r\n', '2020-06-07 21:25:07'),
(13, 'Test name', 'test@gmail.com', '1111111111', 'Hi there! This is a test message. Hope this will work.\r\n', '2020-06-07 21:25:17'),
(14, 'Test name', 'test@gmai', '', '', '2020-06-07 21:26:41'),
(15, 'Test name', 'test@gmail.com', '12345678909', 'hi this is a test message hope this will work!', '2020-06-07 21:27:23'),
(16, 'test name', 'test@gmail.com', '9429523840', 'This is a trial message to test message flashing', '2020-06-08 14:17:13'),
(17, 'test name', 'test@gmail.com', '9429523840', 'This is a trial message to test message flashing', '2020-06-08 14:19:34'),
(18, 'test name', 'test@email.com', '1717171717', 'Hope this will work!', '2020-06-11 12:03:15'),
(19, 'test name', 'test@email.com', '1717171717', 'Hope this will work!', '2020-06-11 12:04:38'),
(20, 'Again', 'dontknow@gmail.com', '1717171718', 'The dash will come this time', '2020-06-11 12:05:41'),
(21, 'Hi', 'test@gmail.com', '1111111111', 'Hope this will work', '2020-06-12 11:13:17'),
(22, 'Hi', 'test@gmail.com', '1111111111', 'Hope this will work', '2020-06-12 11:14:11'),
(23, 'Hi', 'test@gmail.com', '1111111111', 'Hope this will work', '2020-06-12 11:15:44'),
(24, 'Hi', 'test@gmail.com', '1111111111', 'Hope this will work', '2020-06-12 11:16:15'),
(25, 'Hi', 'test@gmail.com', '1111111111', 'Hope this will work', '2020-06-12 11:17:00'),
(26, '', '', '', '', '2020-06-12 11:21:48');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(11) NOT NULL,
  `title` text NOT NULL,
  `tagline` text NOT NULL,
  `slug` varchar(25) NOT NULL,
  `content` text NOT NULL,
  `img_file` varchar(25) NOT NULL,
  `credit` text NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `title`, `tagline`, `slug`, `content`, `img_file`, `credit`, `date`) VALUES
(1, 'Aatmanirbhar Bharat', 'Current pandemic situation & boycott Chinese products', 'boycott-chineseprod', 'China is a country which is known for it\'s low of coast products. Majority of the countries were using the stuff which China produces and it produces almost every-thing from tiny pin to heavy machines. \r\nThey growths their economy by exporting this low of coasts products. \r\nMain three reasons to boycott China products:\r\n1) India-China border dispute,\r\n2) To boost India\'s economy &\r\n3) To keep the country\'s money within country.\r\n\r\n>> India-China border dispute:\r\nThe border dispute between India and China has been going on for years and one of the main reasons for not concluding this dispute may be the stuff which makes China.  India is one of the largest consumers of Chinese goods.  Indians benefit China by importing these low of coast items from China.  And China uses the same money to conspire against India.  If this money stops flowing to China, then the conspiracies being hatched by China for India can be reduced.\r\n\r\n>> To boost India\'s economy:\r\n India\'s economy has declined in times of pandemic like Corona.  If at such a time we start using indigenous goods instead of using imported products from other countries, then economy of the country will grow rapidly and there will be a lot of employment opportunities in the country. \r\n\r\n>> To keep the country\'s money within country:\r\n The money earned by the people of India, goes to the owners of the Chinese company and the Chinese government by importing Chinese stuff.  Instead, if we start buying things from indigenous companies like Tata, Patanjali, Reliance, etc., the country\'s money will go to the people of the country instead of going abroad.  We can use that money again for the development and interest of the country. \r\n\r\n We all know that, in the beginning it\'ll be difficult for all of us to use Indian products because it\'s costly compare to the Chinese low of coast products. So, by using Indian products; we will contribute for #AatmanirbharBharat.\r\n', 'boycottchina.jpg', 'Admin', '2020-06-09 19:57:19'),
(2, 'How to run a business successfully?', '\"5 rules to run business that were adopted by billionaires\"', 'business-rules', ' In today\'s 21st century, everybody wants to do business.  Many of them started as well, but due to lake of business and management skills, their business is not able to achieve success or if they get, it is not upto a large scale. Businessmen like Ratan Tata, Mukesh Ambani, Jeff Bezoz & Warren Buffett have boosted their business profits.\r\n\r\n Some of the things are common among all these businessmen and that\'s their management skills, management ideas & management strategy. If they did not adopt this management ideas, then their company would not have touched the height and they would not be able to become some of world\'s richest persons.\r\n\r\n Warren Buffett is famous over the world for his management skills. Let\'s have a brief eye on their management ideas which will help us to develop our bussinesses.\r\n\r\n 1). Make the right choice of business.\r\n Choosing the right business is as important as the money required to a humble 8 innovative business start-up. If wedo don\'t make the choice of business thoughtfully, then after some time our business can be in loss, so make the choose bussiness very thoughtfully.\r\n\r\n 2). Assign the work to right person\r\n After the choice of business, most important is to divide the work. Identify your empolyee correctly. And according to that, assign them work.  If we ask a manager to do technical work and production to a person who is good in management, then we will never going to get great achievement. So, distribution of the work is very important.\r\n \r\n 3). Encourage employees to do good work.\r\n If we will take care of our employees then we never have to take care of our customers; because, our employees will do this. If we appreciate them for their work, then our employees will works at their best & that\'s main reason behind the growth of the company, so we have to encourage our employee.\r\n\r\n 4). Keep learning new things from all the people which are associated with our business & appreciate their ideas.\r\n The best way to grow the business is continue to taking new ideas and suggestions. Once in a week organize a meeting with employees about their thoughts and ideas; and as an output, new ideas will come to our way. this will help us to grow our business.\r\n\r\n 5). Keep an eye on your competitor.\r\n Most new start-up businesses get tied up because they do not take their competitor seriously. observe the way they attracts customer and they works. Keep your business updated.', 'business.jpeg', 'Admin', '2020-06-09 15:56:57');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `sno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
