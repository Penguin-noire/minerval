-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost
-- Généré le : ven. 06 déc. 2024 à 10:38
-- Version du serveur : 10.4.32-MariaDB
-- Version de PHP : 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `minesoft`
--

-- --------------------------------------------------------

--
-- Structure de la table `campus`
--

-- Création de la base de données

CREATE TABLE `campus` (
  `id` int(200) NOT NULL,
  `nom_campus` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Index pour la table `campus`
ALTER TABLE `campus`
  ADD PRIMARY KEY (`id`);

-- AUTO_INCREMENT pour la table `campus`
ALTER TABLE `campus`
  MODIFY `id` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

-- Structure de la table `departement_fac`
CREATE TABLE `departement_fac` (
  `id` int(11) NOT NULL,
  `nom_dep` varchar(250) NOT NULL,
  `sigle_dep` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Index pour la table `departement_fac`
ALTER TABLE `departement_fac`
  ADD PRIMARY KEY (`id`);

-- AUTO_INCREMENT pour la table `departement_fac`
ALTER TABLE `departement_fac`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

-- Structure de la table `faculte`
CREATE TABLE `faculte` (
  `id` int(200) NOT NULL,
  `nom_fac` varchar(250) NOT NULL,
  `sigle_fac` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Index pour la table `faculte`
ALTER TABLE `faculte`
  ADD PRIMARY KEY (`id`);

-- AUTO_INCREMENT pour la table `faculte`
ALTER TABLE `faculte`
  MODIFY `id` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

-- Structure de la table `option_institut`
CREATE TABLE `option_institut` (
  `id` int(200) NOT NULL,
  `nom_institut` varchar(250) NOT NULL,
  `sigle` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Index pour la table `option_institut`
ALTER TABLE `option_institut`
  ADD PRIMARY KEY (`id`);

-- AUTO_INCREMENT pour la table `option_institut`
ALTER TABLE `option_institut`
  MODIFY `id` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

-- Insertion des données dans les tables
INSERT INTO `campus` (`id`, `nom_campus`) VALUES (1, 'Kamenge');
INSERT INTO `departement_fac` (`id`, `nom_dep`, `sigle_dep`) VALUES
(1, 'Réseaux et Télécommunication', 'RT'),
(2, 'Génie logiciel', 'GL');
INSERT INTO `faculte` (`id`, `nom_fac`, `sigle_fac`) VALUES
(1, 'Faculté des sciences économiques et de gestion', 'FSEG'),
(2, 'Faculté des études de développement', 'FED'),
(3, 'Faculté des sciences et Technologie', 'FST');
INSERT INTO `option_institut` (`id`, `nom_institut`, `sigle`) VALUES
(1, 'Assistance Sociale et Développement', 'ASD'),
(2, 'Finance et comptabilité', 'FC');

-- Création d'une procédure stockée
DELIMITER //
CREATE PROCEDURE GetAllFacultes()
BEGIN
    SELECT * FROM faculte;
END //
DELIMITER ;

-- Création d'un trigger
DELIMITER //
CREATE TRIGGER BeforeInsertDepartement
BEFORE INSERT ON departement_fac
FOR EACH ROW
BEGIN
    SET NEW.sigle_dep = UPPER(NEW.sigle_dep);
END //
DELIMITER ;

-- Fin du script