-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema pieshopdb
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `pieshopdb` ;

-- -----------------------------------------------------
-- Schema pieshopdb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `pieshopdb` DEFAULT CHARACTER SET utf8mb3 ;
USE `pieshopdb` ;

-- -----------------------------------------------------
-- Table `pieshopdb`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pieshopdb`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL DEFAULT NULL,
  `last_name` VARCHAR(255) NULL DEFAULT NULL,
  `email` VARCHAR(255) NULL DEFAULT NULL,
  `password` VARCHAR(255) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 28
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `pieshopdb`.`pies`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pieshopdb`.`pies` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL DEFAULT NULL,
  `filling` VARCHAR(255) NULL DEFAULT NULL,
  `crust` VARCHAR(255) NULL DEFAULT NULL,
  `description` VARCHAR(255) NULL DEFAULT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_recipes_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_recipes_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `pieshopdb`.`users` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 34
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `pieshopdb`.`votes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pieshopdb`.`votes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `users_id` INT NOT NULL,
  `pies_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_users_has_pies_pies1_idx` (`pies_id` ASC) VISIBLE,
  INDEX `fk_users_has_pies_users1_idx` (`users_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_has_pies_pies1`
    FOREIGN KEY (`pies_id`)
    REFERENCES `pieshopdb`.`pies` (`id`),
  CONSTRAINT `fk_users_has_pies_users1`
    FOREIGN KEY (`users_id`)
    REFERENCES `pieshopdb`.`users` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
