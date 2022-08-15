-- MySQL Script generated by MySQL Workbench
-- Sun Aug 14 19:56:15 2022
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema controle_de_gastos
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema controle_de_gastos
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `controle_de_gastos` DEFAULT CHARACTER SET utf8 ;
USE `controle_de_gastos` ;

-- -----------------------------------------------------
-- Table `controle_de_gastos`.`mes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `controle_de_gastos`.`mes` (
  `id_mes` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_mes`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `controle_de_gastos`.`total_compra`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `controle_de_gastos`.`total_compra` (
  `id_compra` INT NOT NULL AUTO_INCREMENT,
  `compra` DECIMAL(10,2) ZEROFILL NOT NULL,
  `t_parcela` TINYINT(1) ZEROFILL NOT NULL,
  PRIMARY KEY (`id_compra`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `controle_de_gastos`.`categoria`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `controle_de_gastos`.`categoria` (
  `id_cat` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(255) NOT NULL,
  `limite_gasto` DECIMAL(10,2) ZEROFILL NOT NULL,
  `minimo_gasto` DECIMAL(10,2) NULL DEFAULT 0,
  PRIMARY KEY (`id_cat`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `controle_de_gastos`.`valor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `controle_de_gastos`.`valor` (
  `id_valor` INT NOT NULL AUTO_INCREMENT,
  `registro` DECIMAL(10,2) ZEROFILL NOT NULL,
  `mes` INT NOT NULL,
  `compra_total` INT NULL DEFAULT '1',
  `categoria` INT NOT NULL,
  `ano` YEAR NOT NULL,
  `nome_compra` VARCHAR(100) NULL DEFAULT 'N/A',
  PRIMARY KEY (`id_valor`),
  INDEX `fk_valor_mes_idx` (`mes` ASC) VISIBLE,
  INDEX `fk_valor_total_compra1_idx` (`compra_total` ASC) VISIBLE,
  INDEX `fk_valor_categoria1_idx` (`categoria` ASC) VISIBLE,
  CONSTRAINT `fk_valor_mes`
    FOREIGN KEY (`mes`)
    REFERENCES `controle_de_gastos`.`mes` (`id_mes`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_valor_total_compra1`
    FOREIGN KEY (`compra_total`)
    REFERENCES `controle_de_gastos`.`total_compra` (`id_compra`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_valor_categoria1`
    FOREIGN KEY (`categoria`)
    REFERENCES `controle_de_gastos`.`categoria` (`id_cat`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `controle_de_gastos`.`salario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `controle_de_gastos`.`salario` (
  `id_sal` INT NOT NULL AUTO_INCREMENT,
  `pagamento` DECIMAL(10,2) ZEROFILL NOT NULL,
  `mes` INT NOT NULL,
  `ano` YEAR NOT NULL,
  PRIMARY KEY (`id_sal`),
  INDEX `fk_salario_mes1_idx` (`mes` ASC) VISIBLE,
  CONSTRAINT `fk_salario_mes1`
    FOREIGN KEY (`mes`)
    REFERENCES `controle_de_gastos`.`mes` (`id_mes`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `controle_de_gastos`.`rendimento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `controle_de_gastos`.`rendimento` (
  `id_red` INT NOT NULL AUTO_INCREMENT,
  `valor` DECIMAL(10,2) ZEROFILL NOT NULL,
  `mes` INT NOT NULL,
  `ano` YEAR NOT NULL,
  PRIMARY KEY (`id_red`),
  INDEX `fk_rendimento_mes1_idx` (`mes` ASC) VISIBLE,
  CONSTRAINT `fk_rendimento_mes1`
    FOREIGN KEY (`mes`)
    REFERENCES `controle_de_gastos`.`mes` (`id_mes`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
