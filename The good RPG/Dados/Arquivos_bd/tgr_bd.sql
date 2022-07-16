-- MySQL Script generated by MySQL Workbench
-- Thu Jul  7 21:40:43 2022
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema tgr
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema tgr
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `tgr` DEFAULT CHARACTER SET utf8 ;
USE `tgr` ;

-- -----------------------------------------------------
-- Table `tgr`.`npc`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tgr`.`npc` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `nome_UNIQUE` (`nome` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tgr`.`vilao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tgr`.`vilao` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(255) NOT NULL,
  `hp` TINYINT UNSIGNED NOT NULL,
  `atk` TINYINT UNSIGNED NOT NULL,
  `defe` TINYINT UNSIGNED NOT NULL,
  `valor_soco` TINYINT UNSIGNED NOT NULL,
  `valor_chute` TINYINT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tgr`.`item`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tgr`.`item` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(100) NOT NULL,
  `dano` TINYINT UNSIGNED NOT NULL,
  `valor` TINYINT UNSIGNED NOT NULL,
  `npc_id` INT UNSIGNED NOT NULL,
  `vilao_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `nome_UNIQUE` (`nome` ASC) VISIBLE,
  INDEX `fk_item_npc_idx` (`npc_id` ASC) VISIBLE,
  INDEX `fk_item_vilao1_idx` (`vilao_id` ASC) VISIBLE,
  CONSTRAINT `fk_item_npc`
    FOREIGN KEY (`npc_id`)
    REFERENCES `tgr`.`npc` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_item_vilao1`
    FOREIGN KEY (`vilao_id`)
    REFERENCES `tgr`.`vilao` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tgr`.`inventario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tgr`.`inventario` (
  `id_slot` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `nome_slot` VARCHAR(150) NOT NULL,
  `gold` TINYINT UNSIGNED NULL DEFAULT 0,
  PRIMARY KEY (`id_slot`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tgr`.`inventario_item`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tgr`.`inventario_item` (
  `inventario_id_slot` INT UNSIGNED NOT NULL,
  `item_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`inventario_id_slot`, `item_id`),
  INDEX `fk_inventario_has_item_item1_idx` (`item_id` ASC) VISIBLE,
  INDEX `fk_inventario_has_item_inventario1_idx` (`inventario_id_slot` ASC) VISIBLE,
  CONSTRAINT `fk_inventario_has_item_inventario1`
    FOREIGN KEY (`inventario_id_slot`)
    REFERENCES `tgr`.`inventario` (`id_slot`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_inventario_has_item_item1`
    FOREIGN KEY (`item_id`)
    REFERENCES `tgr`.`item` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
