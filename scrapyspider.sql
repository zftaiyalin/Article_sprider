/*
 Navicat Premium Data Transfer

 Source Server         : 本地Mysql
 Source Server Type    : MySQL
 Source Server Version : 50719
 Source Host           : localhost
 Source Database       : scrapyspider

 Target Server Type    : MySQL
 Target Server Version : 50719
 File Encoding         : utf-8

 Date: 09/18/2017 17:30:11 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `article`
-- ----------------------------
DROP TABLE IF EXISTS `article`;
CREATE TABLE `article` (
  `add_time` datetime DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `article_spider_table`
-- ----------------------------
DROP TABLE IF EXISTS `article_spider_table`;
CREATE TABLE `article_spider_table` (
  `title` varchar(200) DEFAULT NULL,
  `create_date` date NOT NULL,
  `url` varchar(300) DEFAULT NULL,
  `url_object_id` varchar(50) DEFAULT NULL,
  `front_image_url` varchar(300) NOT NULL DEFAULT 'i',
  `front_image_path` varchar(200) NOT NULL DEFAULT 'i',
  `comment_nums` int(11) NOT NULL DEFAULT '0',
  `fav_nums` int(11) NOT NULL DEFAULT '0',
  `praise_nums` int(11) NOT NULL DEFAULT '0',
  `tags` varchar(200) NOT NULL DEFAULT 'i',
  `content` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `zhihu_answer`
-- ----------------------------
DROP TABLE IF EXISTS `zhihu_answer`;
CREATE TABLE `zhihu_answer` (
  `zhihu_id` bigint(20) NOT NULL,
  `url` varchar(300) NOT NULL,
  `question_id` bigint(20) NOT NULL,
  `author_id` varchar(100) DEFAULT NULL,
  `content` longtext NOT NULL,
  `praise_num` int(11) NOT NULL,
  `comments_num` int(11) NOT NULL,
  `create_time` date NOT NULL,
  `update_time` date NOT NULL,
  `crawl_time` datetime NOT NULL,
  `crawl_update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`zhihu_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `zhihu_question`
-- ----------------------------
DROP TABLE IF EXISTS `zhihu_question`;
CREATE TABLE `zhihu_question` (
  `zhihu_id` bigint(20) NOT NULL,
  `topics` varchar(255) DEFAULT NULL,
  `url` varchar(300) NOT NULL,
  `title` varchar(200) NOT NULL,
  `content` longtext NOT NULL,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `answer_num` int(11) NOT NULL,
  `comments_num` int(11) NOT NULL,
  `watch_user_num` int(11) NOT NULL,
  `click_num` int(11) NOT NULL,
  `crawl_time` datetime NOT NULL,
  PRIMARY KEY (`zhihu_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
