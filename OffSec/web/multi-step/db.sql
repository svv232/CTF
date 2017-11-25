SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";
CREATE DATABASE IF NOT EXISTS `cs3284` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `cs3284`;

CREATE TABLE `users` (
`id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

INSERT INTO `users` (`id`, `username`, `password`) VALUES
(1, 'admin', 'C0rr3ctH0rseB@tt3rySt@p1e');

ALTER TABLE `users`
ADD PRIMARY KEY (`id`);

ALTER TABLE `users`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;

CREATE USER 'cs3284'@'localhost' IDENTIFIED BY 'cs3284';
GRANT ALL PRIVILEGES ON cs3284.* TO 'cs3284'@'localhost';
