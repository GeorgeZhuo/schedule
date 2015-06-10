/*
MySQL Data Transfer
Source Host: localhost
Source Database: todo
Target Host: localhost
Target Database: todo
Date: 2011/6/25 21:57:10
*/

SET FOREIGN_KEY_CHECKS=0;



-- ----------------------------
-- Table structure for finalschedule
-- ----------------------------
DROP TABLE IF EXISTS `finalschedule`;
CREATE TABLE `finalschedule` (
  `id` int(11) NOT NULL auto_increment,
  `s_name` varchar(10) DEFAULT NULL,
  `s_time` int DEFAULT NULL,
  `finish` int DEFAULT 0,
  `ischange` int DEFAULT 0,
  `person` varchar(10) DEFAULT NULL,    
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;



-- ----------------------------
-- Table structure for finaluser_data
-- ----------------------------
DROP TABLE IF EXISTS `finaluser_data`;
CREATE TABLE `finaluser_data` (
  `s_name` varchar(10) NOT NULL,
  `time_duty` int DEFAULT 0,
  `time_actual` int DEFAULT 0
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;



-- ----------------------------
-- Table structure for schedule
-- ----------------------------
DROP TABLE IF EXISTS `schedule`;
CREATE TABLE `schedule` (
  `id` int(11) NOT NULL auto_increment,
  `s_name` varchar(10) DEFAULT NULL,
  `s_time` int DEFAULT NULL,
  `keep` int DEFAULT 1,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;



-- ----------------------------
-- Table structure for user_data
-- ----------------------------
DROP TABLE IF EXISTS `user_data`;
CREATE TABLE `user_data` (
  `s_id` varchar(10) NOT NULL,
  `s_name` varchar(10) NOT NULL,
  `s_pass` varchar(10) NOT NULL,
  `s_type` int DEFAULT 0,
  `time_duty` int DEFAULT 0,
  PRIMARY KEY  (`s_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;



-- ----------------------------
-- Records 
-- ----------------------------
INSERT INTO `user_data` VALUES ('admin', '管理员', 'sacadmin', '1', '0');
INSERT INTO `user_data` VALUES ('sac', '公共帐号', 'sac', '2', '0');



-- ----------------------------
-- Table structure for sessions
-- ----------------------------
DROP TABLE IF EXISTS `sessions`;
CREATE TABLE sessions (
    session_id char(128) UNIQUE NOT NULL,
    atime timestamp NOT NULL default current_timestamp,
    data text
);
