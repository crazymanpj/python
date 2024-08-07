-- --------------------------------------------------------
-- 主机:                           127.0.0.1
-- 服务器版本:                        5.1.45-community - MySQL Community Server (GPL)
-- 服务器操作系统:                      Win32
-- HeidiSQL 版本:                  8.0.0.4458
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- 导出 cmdata 的数据库结构
CREATE DATABASE IF NOT EXISTS `cmdata` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `cmdata`;


-- 导出  表 cmdata.auth_group 结构
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- 正在导出表  cmdata.auth_group 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;


-- 导出  表 cmdata.auth_group_permissions 结构
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- 正在导出表  cmdata.auth_group_permissions 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;


-- 导出  表 cmdata.auth_permission 结构
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=latin1;

-- 正在导出表  cmdata.auth_permission 的数据：~42 rows (大约)
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
REPLACE INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(1, 'Can add log entry', 1, 'add_logentry'),
	(2, 'Can change log entry', 1, 'change_logentry'),
	(3, 'Can delete log entry', 1, 'delete_logentry'),
	(4, 'Can add permission', 2, 'add_permission'),
	(5, 'Can change permission', 2, 'change_permission'),
	(6, 'Can delete permission', 2, 'delete_permission'),
	(7, 'Can add user', 3, 'add_user'),
	(8, 'Can change user', 3, 'change_user'),
	(9, 'Can delete user', 3, 'delete_user'),
	(10, 'Can add group', 4, 'add_group'),
	(11, 'Can change group', 4, 'change_group'),
	(12, 'Can delete group', 4, 'delete_group'),
	(13, 'Can add content type', 5, 'add_contenttype'),
	(14, 'Can change content type', 5, 'change_contenttype'),
	(15, 'Can delete content type', 5, 'delete_contenttype'),
	(16, 'Can add session', 6, 'add_session'),
	(17, 'Can change session', 6, 'change_session'),
	(18, 'Can delete session', 6, 'delete_session'),
	(19, 'Can add publish record', 7, 'add_publishrecord'),
	(20, 'Can change publish record', 7, 'change_publishrecord'),
	(21, 'Can delete publish record', 7, 'delete_publishrecord'),
	(22, 'Can add plugin', 8, 'add_plugin'),
	(23, 'Can change plugin', 8, 'change_plugin'),
	(24, 'Can delete plugin', 8, 'delete_plugin'),
	(25, 'Can add package', 9, 'add_package'),
	(26, 'Can change package', 9, 'change_package'),
	(27, 'Can delete package', 9, 'delete_package'),
	(28, 'Can add side bar group', 10, 'add_sidebargroup'),
	(29, 'Can change side bar group', 10, 'change_sidebargroup'),
	(30, 'Can delete side bar group', 10, 'delete_sidebargroup'),
	(31, 'Can add side bar', 11, 'add_sidebar'),
	(32, 'Can change side bar', 11, 'change_sidebar'),
	(33, 'Can delete side bar', 11, 'delete_sidebar'),
	(34, 'Can add procduct', 12, 'add_procduct'),
	(35, 'Can change procduct', 12, 'change_procduct'),
	(36, 'Can delete procduct', 12, 'delete_procduct'),
	(37, 'Can add file type', 13, 'add_filetype'),
	(38, 'Can change file type', 13, 'change_filetype'),
	(39, 'Can delete file type', 13, 'delete_filetype'),
	(40, 'Can add channel', 14, 'add_channel'),
	(41, 'Can change channel', 14, 'change_channel'),
	(42, 'Can delete channel', 14, 'delete_channel');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;


-- 导出  表 cmdata.auth_user 结构
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

-- 正在导出表  cmdata.auth_user 的数据：~2 rows (大约)
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
REPLACE INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
	(1, 'pbkdf2_sha256$30000$Hps3ovOkECjE$xfBF2bkjmoRFZDDfcX+RWJuMXAFgMdlm7FCEEuOUFuk=', '2016-11-17 02:46:03', 0, 'pangjian@kingsoft.com', 'pangjian', '', 'pangjian@kingsoft.com', 0, 1, '2016-10-29 08:03:01'),
	(2, 'pbkdf2_sha256$30000$DH5w4CIA0t7U$adD9TuMjoy8da6EDkNwwSJVxkYQmiExa05LRgDP68EA=', NULL, 1, 'pangjian', '', '', 'pang456jian@163.com', 1, 1, '2016-11-02 10:52:45');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;


-- 导出  表 cmdata.auth_user_groups 结构
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- 正在导出表  cmdata.auth_user_groups 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;


-- 导出  表 cmdata.auth_user_user_permissions 结构
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- 正在导出表  cmdata.auth_user_user_permissions 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;


-- 导出  表 cmdata.cm_channel 结构
CREATE TABLE IF NOT EXISTS `cm_channel` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '1',
  `channelnum` int(11) NOT NULL,
  `description` varchar(20) NOT NULL,
  `addtime` datetime DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

-- 正在导出表  cmdata.cm_channel 的数据：~10 rows (大约)
/*!40000 ALTER TABLE `cm_channel` DISABLE KEYS */;
REPLACE INTO `cm_channel` (`id`, `channelnum`, `description`, `addtime`, `status`) VALUES
	(1, 100039, 'cms推cm', NULL, 1),
	(2, 100005, '电池医生渠道', NULL, 1),
	(3, 100003, '手助全渠道', NULL, 1),
	(4, 2010000002, '豌豆荚', NULL, 1),
	(5, 0, '默认渠道', NULL, 1),
	(6, 2010000006, '百度', NULL, 1),
	(7, 2010000005, '应用宝', NULL, 1),
	(8, 24343322, '测试', '2016-11-14 11:19:53', 0),
	(11, 2010000613, '360手机助手', '2016-11-17 02:59:40', 1),
	(12, 2010003660, 'qq浏览器', '2016-11-17 03:55:24', 1);
/*!40000 ALTER TABLE `cm_channel` ENABLE KEYS */;


-- 导出  表 cmdata.cm_filetype 结构
CREATE TABLE IF NOT EXISTS `cm_filetype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(20) NOT NULL,
  `description` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- 正在导出表  cmdata.cm_filetype 的数据：~2 rows (大约)
/*!40000 ALTER TABLE `cm_filetype` DISABLE KEYS */;
REPLACE INTO `cm_filetype` (`id`, `type`, `description`) VALUES
	(1, 'package', '安装包'),
	(2, 'plugin', '插件');
/*!40000 ALTER TABLE `cm_filetype` ENABLE KEYS */;


-- 导出  表 cmdata.cm_hostver 结构
CREATE TABLE IF NOT EXISTS `cm_hostver` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '1',
  `hostver` varchar(20) NOT NULL,
  `addtime` datetime DEFAULT NULL,
  `status` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- 正在导出表  cmdata.cm_hostver 的数据：~8 rows (大约)
/*!40000 ALTER TABLE `cm_hostver` DISABLE KEYS */;
REPLACE INTO `cm_hostver` (`id`, `hostver`, `addtime`, `status`) VALUES
	(1, '10100036', '2016-11-01 17:56:43', 1),
	(2, '45443332', '2016-11-01 17:56:57', 1),
	(3, '44455333', '2016-11-01 17:57:06', 1),
	(4, '11111111', '2016-11-14 11:59:02', 0),
	(5, '12223344', '2016-11-14 12:20:21', 0),
	(6, '10100038', '2016-11-17 06:12:07', 1),
	(7, '10100040', '2016-11-17 06:21:09', 1),
	(8, '10100035', '2016-11-17 06:34:19', 1);
/*!40000 ALTER TABLE `cm_hostver` ENABLE KEYS */;


-- 导出  表 cmdata.cm_package 结构
CREATE TABLE IF NOT EXISTS `cm_package` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `publishid` int(11) NOT NULL,
  `apkver` varchar(20) NOT NULL,
  `packagepath` varchar(200) NOT NULL,
  `hostver` varchar(20) NOT NULL,
  `packagemd5` varchar(20) NOT NULL,
  `packagesize` varchar(20) NOT NULL,
  `channel` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;

-- 正在导出表  cmdata.cm_package 的数据：~22 rows (大约)
/*!40000 ALTER TABLE `cm_package` DISABLE KEYS */;
REPLACE INTO `cm_package` (`id`, `publishid`, `apkver`, `packagepath`, `hostver`, `packagemd5`, `packagesize`, `channel`) VALUES
	(1, 20, '51481004', 'd:\\kuaipan\\python\\mobiledata\\common\\CleanMaster-v51481004-sj-100003-uL.apk', 'False', '50cf809fbf884389c131', '19749818', '100005'),
	(2, 21, '51481004', 'd:\\kuaipan\\python\\mobiledata\\common\\CleanMaster-v51481004-sj-100003-uL.apk', 'False', '50cf809fbf884389c131', '19749818', '100003'),
	(3, 22, '51481004', 'd:\\kuaipan\\python\\mobiledata\\common\\CleanMaster-v51481004-sj-100003-uL.apk', 'False', '50cf809fbf884389c131', '19749818', '100003'),
	(4, 23, '51481004', 'd:\\kuaipan\\python\\mobiledata\\common\\CleanMaster-v51481004-sj-100003-uL.apk', 'False', '50cf809fbf884389c131', '19749818', '100003'),
	(5, 24, '51481004', 'd:\\kuaipan\\python\\mobiledata\\common\\CleanMaster-v51481004-sj-100003-uL.apk', 'False', '50cf809fbf884389c131', '19749818', '100003'),
	(6, 25, '51481004', 'd:\\kuaipan\\python\\mobiledata\\common\\CleanMaster-v51481004-sj-100003-uL.apk', '10100036', '50cf809fbf884389c131', '19749818', '100003'),
	(7, 26, '51481004', 'd:\\kuaipan\\python\\mobiledata\\common\\CleanMaster-v51481004-sj-100003-uL.apk', '10100036', '50cf809fbf884389c131', '19749818', '2010000002'),
	(8, 27, '51481004', 'd:\\kuaipan\\python\\mobiledata\\common\\CleanMaster-v51481004-sj-100003-uL.apk', '10100036', '50cf809fbf884389c131', '19749818', '2010000002'),
	(9, 27, '51481004', 'd:\\kuaipan\\python\\mobiledata\\common\\CleanMaster-v51481004-sj-100003-uL.apk', '10100036', '50cf809fbf884389c131', '19749818', '0'),
	(10, 28, '51481004', 'd:\\kuaipan\\python\\mobiledata\\common\\CleanMaster-v51481004-sj-100003-uL.apk', '10100036', '50cf809fbf884389c131', '19749818', '2010000002'),
	(11, 28, '51481004', 'd:\\kuaipan\\python\\mobiledata\\common\\CleanMaster-v51481004-sj-100003-uL.apk', '10100036', '50cf809fbf884389c131', '19749818', '0'),
	(12, 29, '51481004', 'd:\\kuaipan\\python\\mobiledata\\common\\CleanMaster-v51481004-sj-100003-uL.apk', '10100036', '50cf809fbf884389c131', '19749818', '2010000002'),
	(13, 29, '51481004', 'd:\\kuaipan\\python\\mobiledata\\common\\CleanMaster-v51481004-sj-100003-uL.apk', '10100036', '50cf809fbf884389c131', '19749818', '0'),
	(14, 30, '51481004', 'd:\\kuaipan\\python\\mobiledata\\common\\CleanMaster-v51481004-sj-100003-uL.apk', '10100036', '50cf809fbf884389c131', '19749818', '2010000002'),
	(15, 30, '51481004', 'd:\\kuaipan\\python\\mobiledata\\common\\CleanMaster-v51481004-sj-100003-uL.apk', '10100036', '50cf809fbf884389c131', '19749818', '0'),
	(16, 42, '51421007', 'ftp://ftpadm@10.60.80.70/cm_china/cc_5142_kpyd_rb/20161013.7/channel/100003/CleanMaster-v51421007-sj-100003-uL.apk', 'False', 'e10063078f93c0019b17', '21321250', '0'),
	(17, 43, '51451026', 'ftp://10.60.80.70/cm_china/cc_5147_ad_rb/20161110.26/channel/100000/CleanMaster-v51451026-cu-100000-uL.apk', '10100038', '8579efe440c87810ff26', '20114462', '2010000613'),
	(18, 44, '51451026', 'ftp://10.60.80.70/cm_china/cc_5147_ad_rb/20161110.26/channel/100000/CleanMaster-v51451026-cu-100000-uL.apk', '10100038', '8579efe440c87810ff26', '20114462', '2010000613'),
	(19, 44, '51451026', 'ftp://10.60.80.70/cm_china/cc_5147_ad_rb/20161110.26/channel/100000/CleanMaster-v51451026-cu-100000-uL.apk', '10100038', '8579efe440c87810ff26', '20114462', '2010003660'),
	(20, 45, '51451026', 'ftp://10.60.80.70/cm_china/cc_5145_rb/20161104.34/channel/100000/CleanMaster-v51451026-cu-100000-uL.apk', '10100037', '74bdbb6211540810b2ae', '23001159', '0'),
	(21, 50, '30151008', 'c:\\Users\\kingsoft\\Desktop\\cmsecurity_cn.apk', '10100016', '3189114fd218b620c2d2', '9188687', '2010003660'),
	(22, 51, '51421007', 'd:\\kuaipan\\python\\mobiledata\\download\\CleanMaster-v51421007-sj-100003-uL.apk', 'False', 'e10063078f93c0019b17', '21321250', '100039');
/*!40000 ALTER TABLE `cm_package` ENABLE KEYS */;


-- 导出  表 cmdata.cm_plugin 结构
CREATE TABLE IF NOT EXISTS `cm_plugin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `publishid` int(11) NOT NULL,
  `pluginver` varchar(20) NOT NULL,
  `hostver` varchar(20) NOT NULL,
  `pluginpath` varchar(200) NOT NULL,
  `pluginmd5` varchar(30) NOT NULL,
  `plugintype` varchar(20) NOT NULL,
  `pluginsize` varchar(20) NOT NULL,
  `channel` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- 正在导出表  cmdata.cm_plugin 的数据：~7 rows (大约)
/*!40000 ALTER TABLE `cm_plugin` DISABLE KEYS */;
REPLACE INTO `cm_plugin` (`id`, `publishid`, `pluginver`, `hostver`, `pluginpath`, `pluginmd5`, `plugintype`, `pluginsize`, `channel`) VALUES
	(1, 37, '10010216100121', '10100036\r\n', 'ftp://10.60.80.70/cm_china/cc_5142_kpyd_rb/20161009.3/cm_plugin_uniform_10010216100121_16100903.so.lzma', '51d5100c0c7bc9e0db538275ee1bb7', 'uniform', '4255819', '100005'),
	(2, 40, '10010216100121', '10100036\r\n', 'ftp://10.60.80.70/cm_china/cc_5142_kpyd_rb/20161009.3/cm_plugin_uniform_10010216100121_16100903.so.lzma', '51d5100c0c7bc9e0db538275ee1bb7', 'uniform', '4255819', '2010000002'),
	(3, 41, '10010216100121', '10100036\r\n', 'ftp://10.60.80.70/cm_china/cc_5142_kpyd_rb/20161009.3/cm_plugin_uniform_10010216100121_16100903.so.lzma', '51d5100c0c7bc9e0db538275ee1bb7', 'uniform', '4255819', '2010000002'),
	(4, 46, '10010216111108', '10100040\r\n', 'ftp://10.60.80.70/cm_china/cc_5151_rb/20161111.8/cm_plugin_uniform_10010216111108_16111108.so.lzma', 'a92198d9267742396405f7f2984a07', 'uniform', '3745924', '100003'),
	(5, 47, '10010516100210', '10100035\r\n', 'ftp://10.60.80.70/cm_china/cc_5145_rb/20160930.10/cm_plugin_news_10010516100210_16093010.so.lzma', '413ea28e892f4279fe5a092e5205a1', 'news', '794279', '2010000002'),
	(6, 48, '10010216100210', '10100035\r\n', 'ftp://10.60.80.70/cm_china/cc_5145_rb/20160930.10/cm_plugin_uniform_10010216100210_16093010.so.lzma', '60955cc1606ae24843d1f025da0666', 'uniform', '4287966', '2010000002'),
	(7, 49, '10010616100210', '10100035\r\n', 'ftp://10.60.80.70/cm_china/cc_5145_rb/20160930.10/cm_plugin_ironman_10010616100210_16093010.so.lzma', 'f473a43d4a20d05471516bc1978d86', 'ironman', '146055', '2010000613');
/*!40000 ALTER TABLE `cm_plugin` ENABLE KEYS */;


-- 导出  表 cmdata.cm_plugintype 结构
CREATE TABLE IF NOT EXISTS `cm_plugintype` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '1',
  `name` varchar(20) NOT NULL,
  `description` varchar(20) NOT NULL,
  `addtime` datetime DEFAULT NULL,
  `status` int(11) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- 正在导出表  cmdata.cm_plugintype 的数据：~1 rows (大约)
/*!40000 ALTER TABLE `cm_plugintype` DISABLE KEYS */;
REPLACE INTO `cm_plugintype` (`id`, `name`, `description`, `addtime`, `status`) VALUES
	(1, 'uniform', '测试', '2016-11-01 17:13:38', 1);
/*!40000 ALTER TABLE `cm_plugintype` ENABLE KEYS */;


-- 导出  表 cmdata.cm_procduct 结构
CREATE TABLE IF NOT EXISTS `cm_procduct` (
  `id` int(11) NOT NULL,
  `procductname` varchar(20) NOT NULL,
  `description` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  cmdata.cm_procduct 的数据：~1 rows (大约)
/*!40000 ALTER TABLE `cm_procduct` DISABLE KEYS */;
REPLACE INTO `cm_procduct` (`id`, `procductname`, `description`) VALUES
	(1, 'cm', '猎豹清理大师');
/*!40000 ALTER TABLE `cm_procduct` ENABLE KEYS */;


-- 导出  表 cmdata.cm_publishrecord 结构
CREATE TABLE IF NOT EXISTS `cm_publishrecord` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `publishtime` datetime NOT NULL,
  `filetype` varchar(20) NOT NULL,
  `channel` varchar(20) NOT NULL,
  `details` varchar(6000) NOT NULL,
  `filepath` varchar(200) NOT NULL,
  `user` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8;

-- 正在导出表  cmdata.cm_publishrecord 的数据：~51 rows (大约)
/*!40000 ALTER TABLE `cm_publishrecord` DISABLE KEYS */;
REPLACE INTO `cm_publishrecord` (`id`, `publishtime`, `filetype`, `channel`, `details`, `filepath`, `user`) VALUES
	(1, '2016-10-26 16:00:00', '安装包', '电池医生渠道', '测试', 'ftp://ftpadm@10.60.80.70/cm_china/cc_5142_kpyd_rb/20161013.7/channel/100003/CleanMaster-v51421007-sj-100003-uL.apk', NULL),
	(2, '2016-10-26 16:00:00', '安装包', '电池医生渠道', '测试', 'ftp://ftpadm@10.60.80.70/cm_china/cc_5142_kpyd_rb/20161013.7/channel/100003/CleanMaster-v51421007-sj-100003-uL.apk', NULL),
	(3, '2016-10-26 16:00:00', '安装包', '电池医生渠道', '测试', 'ftp://ftpadm@10.60.80.70/cm_china/cc_5142_kpyd_rb/20161013.7/channel/100003/CleanMaster-v51421007-sj-100003-uL.apk', NULL),
	(4, '2016-10-26 16:00:00', '安装包', '电池医生渠道', '测试', 'ftp://ftpadm@10.60.80.70/cm_china/cc_5142_kpyd_rb/20161013.7/channel/100003/CleanMaster-v51421007-sj-100003-uL.apk', NULL),
	(5, '2016-10-27 16:00:00', '安装包', '手助全渠道', '测试', 'ftp://ftpadm@10.60.80.70/cm_china/cc_5142_kpyd_rb/20161013.7/channel/100003/CleanMaster-v51421007-sj-100003-uL.apk', NULL),
	(6, '2016-10-11 16:00:00', '安装包', '电池医生渠道', '线程vv', 'ftp://ftpadm@10.60.80.70/cm_china/cc_5142_kpyd_rb/20161013.7/channel/100003/CleanMaster-v51421007-sj-100003-uL.apk', NULL),
	(7, '2016-10-26 16:00:00', '安装包', '百度', '电费', 'ftp://ftpadm@10.60.80.70/cm_china/cc_5142_kpyd_rb/20161013.7/channel/100003/CleanMaster-v51421007-sj-100003-uL.apk', NULL),
	(8, '2016-10-26 16:00:00', '安装包', '豌豆荚', 'sdv', 'ftp://ftpadm@10.60.80.70/cm_china/cc_5142_kpyd_rb/20161013.7/channel/100003/CleanMaster-v51421007-sj-100003-uL.apk', NULL),
	(9, '2016-10-27 16:00:00', '安装包', '电池医生渠道', '三等份', 'ftp://ftpadm@10.60.80.70/cm_china/cc_5142_kpyd_rb/20161013.7/channel/100003/CleanMaster-v51421007-sj-100003-uL.apk', NULL),
	(10, '2016-10-26 16:00:00', '安装包', '电池医生渠道', 'xcvd', 'ftp://ftpadm@10.60.80.70/cm_china/cc_5142_kpyd_rb/20161013.7/channel/100003/CleanMaster-v51421007-sj-100003-uL.apk', NULL),
	(11, '2016-10-24 16:00:00', '安装包', '豌豆荚', 'vbn', 'ftp://ftpadm@10.60.80.70/cm_china/cc_5142_kpyd_rb/20161013.7/channel/100003/CleanMaster-v51421007-sj-100003-uL.apk', NULL),
	(12, '2016-10-24 16:00:00', '安装包', '电池医生渠道', '搜房', 'ftp://ftpadm@10.60.80.70/cm_china/cc_5142_kpyd_rb/20161013.7/channel/100003/CleanMaster-v51421007-sj-100003-uL.apk', NULL),
	(13, '2016-10-19 16:00:00', '安装包', '电池医生渠道', '三等份', 'ftp://ftpadm@10.60.80.70/cm_china/cc_5142_kpyd_rb/20161013.7/channel/100003/CleanMaster-v51421007-sj-100003-uL.apk', NULL),
	(14, '2016-10-20 16:00:00', '安装包', '百度', '三分', 'd:\\kuaipan\\python\\mobiledata\\common\\CleanMaster-v51481004-sj-100003-uL.apk', NULL),
	(15, '2016-10-18 16:00:00', '安装包', '默认渠道', '三等份', 'd:\\kuaipan\\python\\mobiledata\\common\\CleanMaster-v51481004-sj-100003-uL.apk', NULL),
	(16, '2016-10-25 16:00:00', '安装包', '电池医生渠道', 'xcvxcv', 'd:\\kuaipan\\python\\mobiledata\\common\\CleanMaster-v51481004-sj-100003-uL.apk', NULL),
	(17, '2016-10-26 08:00:00', '安装包', '电池医生渠道', 'xxx', 'xxx', NULL),
	(18, '2016-10-26 08:00:00', '安装包', '电池医生渠道', 'xxx', 'xxx', NULL),
	(19, '2016-10-18 16:00:00', '安装包', '手助全渠道', 'xcvxcv', 'd:\\kuaipan\\python\\mobiledata\\common\\CleanMaster-v51481004-sj-100003-uL.apk', NULL),
	(20, '2016-10-18 16:00:00', '安装包', '电池医生渠道', 'xcvxv', 'd:\\kuaipan\\python\\mobiledata\\common\\CleanMaster-v51481004-sj-100003-uL.apk', NULL),
	(21, '2016-10-18 16:00:00', '安装包', '手助全渠道', 'xcvxv', 'd:\\kuaipan\\python\\mobiledata\\common\\CleanMaster-v51481004-sj-100003-uL.apk', NULL),
	(22, '2016-10-18 16:00:00', '安装包', '手助全渠道', 'xcvxv', 'd:\\kuaipan\\python\\mobiledata\\common\\CleanMaster-v51481004-sj-100003-uL.apk', NULL),
	(23, '2016-10-11 16:00:00', '安装包', '手助全渠道', 'svxc', 'd:\\kuaipan\\python\\mobiledata\\common\\CleanMaster-v51481004-sj-100003-uL.apk', NULL),
	(24, '2016-10-11 16:00:00', '安装包', '手助全渠道', 'svxc', 'd:\\kuaipan\\python\\mobiledata\\common\\CleanMaster-v51481004-sj-100003-uL.apk', NULL),
	(25, '2016-10-03 16:00:00', '安装包', '手助全渠道', 'sdfe', 'd:\\kuaipan\\python\\mobiledata\\common\\CleanMaster-v51481004-sj-100003-uL.apk', NULL),
	(26, '2016-10-18 16:00:00', '安装包', '豌豆荚', 'sfe', 'd:\\kuaipan\\python\\mobiledata\\common\\CleanMaster-v51481004-sj-100003-uL.apk', 'pangjian'),
	(27, '2016-10-16 16:00:00', '安装包', '豌豆荚', 'sdfsd', 'd:\\kuaipan\\python\\mobiledata\\common\\CleanMaster-v51481004-sj-100003-uL.apk', 'pangjian'),
	(28, '2016-10-16 16:00:00', '安装包', '默认渠道\r\n', 'sdfsd', 'd:\\kuaipan\\python\\mobiledata\\common\\CleanMaster-v51481004-sj-100003-uL.apk', 'pangjian'),
	(29, '2016-10-16 16:00:00', '安装包', '默认渠道\r\n', 'sdfsd', 'd:\\kuaipan\\python\\mobiledata\\common\\CleanMaster-v51481004-sj-100003-uL.apk', 'pangjian'),
	(30, '2016-10-16 16:00:00', '安装包', '豌豆荚\r\n默认渠道\r\n', 'sdfsd', 'd:\\kuaipan\\python\\mobiledata\\common\\CleanMaster-v51481004-sj-100003-uL.apk', 'pangjian'),
	(31, '2016-11-14 16:00:00', '插件', '手助全渠道\r\n', '微软', 'ftp://10.60.80.70/cm_china/cc_5142_kpyd_rb/20161009.3/cm_plugin_uniform_10010216100121_16100903.so.lzma', ''),
	(32, '2016-11-21 16:00:00', '插件', '手助全渠道\r\n', '三分', 'ftp://10.60.80.70/cm_china/cc_5142_kpyd_rb/20161009.3/cm_plugin_uniform_10010216100121_16100903.so.lzma', ''),
	(33, '2016-11-21 16:00:00', '插件', '手助全渠道\r\n', 'xcvsdds', 'ftp://10.60.80.70/cm_china/cc_5142_kpyd_rb/20161009.3/cm_plugin_uniform_10010216100121_16100903.so.lzma', ''),
	(34, '2016-11-21 16:00:00', '插件', '手助全渠道\r\n', '三等份', 'ftp://10.60.80.70/cm_china/cc_5142_kpyd_rb/20161009.3/cm_plugin_uniform_10010216100121_16100903.so.lzma', ''),
	(35, '2016-11-21 16:00:00', '插件', '手助全渠道\r\n', '锁定', 'ftp://10.60.80.70/cm_china/cc_5142_kpyd_rb/20161009.3/cm_plugin_uniform_10010216100121_16100903.so.lzma', ''),
	(36, '2016-11-22 16:00:00', '插件', '手助全渠道\r\n', '三等份', 'ftp://10.60.80.70/cm_china/cc_5142_kpyd_rb/20161009.3/cm_plugin_uniform_10010216100121_16100903.so.lzma', ''),
	(37, '2016-11-15 16:00:00', '插件', '电池医生渠道\r\n', '三等份', 'ftp://10.60.80.70/cm_china/cc_5142_kpyd_rb/20161009.3/cm_plugin_uniform_10010216100121_16100903.so.lzma', ''),
	(38, '2016-11-10 11:41:35', ' 插件', '手助全渠道', '相当大的', 'sdfefefe', 'sdve'),
	(39, '2016-11-15 16:00:00', '插件', '', '三等份似懂非懂', 'ftp://10.60.80.70/cm_china/cc_5142_kpyd_rb/20161009.3/cm_plugin_uniform_10010216100121_16100903.so.lzma', ''),
	(40, '2016-11-25 16:00:00', '插件', '豌豆荚\r\n', '水电费', 'ftp://10.60.80.70/cm_china/cc_5142_kpyd_rb/20161009.3/cm_plugin_uniform_10010216100121_16100903.so.lzma', ''),
	(41, '2016-11-29 16:00:00', '插件', '豌豆荚\r\n', '四大神兽', 'ftp://10.60.80.70/cm_china/cc_5142_kpyd_rb/20161009.3/cm_plugin_uniform_10010216100121_16100903.so.lzma', ''),
	(42, '2016-11-16 16:00:00', '安装包', '默认渠道\r\n', '水电费', 'ftp://ftpadm@10.60.80.70/cm_china/cc_5142_kpyd_rb/20161013.7/channel/100003/CleanMaster-v51421007-sj-100003-uL.apk', 'pangjian'),
	(43, '2016-11-13 16:00:00', '安装包', '360手机助手\r\n', '更换百度广点通sdk', 'ftp://10.60.80.70/cm_china/cc_5147_ad_rb/20161110.26/channel/100000/CleanMaster-v51451026-cu-100000-uL.apk', 'pangjian'),
	(44, '2016-11-10 16:00:00', '安装包', '360手机助手\r\nqq浏览器\r\n', '更换百度广点通', 'ftp://10.60.80.70/cm_china/cc_5147_ad_rb/20161110.26/channel/100000/CleanMaster-v51451026-cu-100000-uL.apk', 'pangjian'),
	(45, '2016-11-08 16:00:00', '安装包', '默认渠道\r\n', '全网包', 'ftp://10.60.80.70/cm_china/cc_5145_rb/20161104.34/channel/100000/CleanMaster-v51451026-cu-100000-uL.apk', 'pangjian'),
	(46, '2016-11-10 16:00:00', '插件', '手助全渠道\r\n', '修复软管崩溃', 'ftp://10.60.80.70/cm_china/cc_5151_rb/20161111.8/cm_plugin_uniform_10010216111108_16111108.so.lzma', 'pangjian'),
	(47, '2016-11-29 16:00:00', '插件', '豌豆荚\r\n', '新闻', 'ftp://10.60.80.70/cm_china/cc_5145_rb/20160930.10/cm_plugin_news_10010516100210_16093010.so.lzma', 'pangjian'),
	(48, '2016-11-28 16:00:00', '插件', '豌豆荚\r\n', '新闻结果页', 'ftp://10.60.80.70/cm_china/cc_5145_rb/20160930.10/cm_plugin_uniform_10010216100210_16093010.so.lzma', 'pangjian'),
	(49, '2016-11-27 16:00:00', '插件', '360手机助手\r\n', '充电屏保', 'ftp://10.60.80.70/cm_china/cc_5145_rb/20160930.10/cm_plugin_ironman_10010616100210_16093010.so.lzma', 'pangjian'),
	(50, '2016-11-22 16:00:00', '安装包', 'qq浏览器\r\n', '测试', 'c:\\Users\\kingsoft\\Desktop\\cmsecurity_cn.apk', 'pangjian'),
	(51, '2016-11-22 16:00:00', '安装包', 'cms推cm\r\n', '测试', 'd:\\kuaipan\\python\\mobiledata\\download\\CleanMaster-v51421007-sj-100003-uL.apk', '');
/*!40000 ALTER TABLE `cm_publishrecord` ENABLE KEYS */;


-- 导出  表 cmdata.cm_sidebar 结构
CREATE TABLE IF NOT EXISTS `cm_sidebar` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `url` varchar(100) NOT NULL,
  `blank` varchar(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  cmdata.cm_sidebar 的数据：~8 rows (大约)
/*!40000 ALTER TABLE `cm_sidebar` DISABLE KEYS */;
REPLACE INTO `cm_sidebar` (`id`, `name`, `url`, `blank`, `group_id`) VALUES
	(1, '渠道查询', 'channelsearch.html', '', 1),
	(2, '插件查询', 'pluginsearch.html', '', 1),
	(3, 'apk包查询', 'packagesearch.html', '', 1),
	(4, '宿主查询', 'hostsearch.html', '', 1),
	(5, 'apk包解析', '#', '', 2),
	(6, '提测合格率', 'http://update.rdev.kingsoft.net:8089/addstats/', '', 3),
	(7, '手机资产列表', 'http://update.rdev.kingsoft.net:8089/phonemanager/index', '', 3),
	(8, '手助发布记录', 'http://update.rdev.kingsoft.net:8089/fileapp/file/publishlist/', '', 3);
/*!40000 ALTER TABLE `cm_sidebar` ENABLE KEYS */;


-- 导出  表 cmdata.cm_sidebargroup 结构
CREATE TABLE IF NOT EXISTS `cm_sidebargroup` (
  `id` int(11) NOT NULL,
  `group` varchar(20) NOT NULL,
  `blank` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  cmdata.cm_sidebargroup 的数据：~3 rows (大约)
/*!40000 ALTER TABLE `cm_sidebargroup` DISABLE KEYS */;
REPLACE INTO `cm_sidebargroup` (`id`, `group`, `blank`) VALUES
	(1, '查询', ''),
	(2, '工具', ''),
	(3, '外链', '');
/*!40000 ALTER TABLE `cm_sidebargroup` ENABLE KEYS */;


-- 导出  表 cmdata.django_admin_log 结构
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- 正在导出表  cmdata.django_admin_log 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;


-- 导出  表 cmdata.django_content_type 结构
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

-- 正在导出表  cmdata.django_content_type 的数据：~14 rows (大约)
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
REPLACE INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
	(1, 'admin', 'logentry'),
	(4, 'auth', 'group'),
	(2, 'auth', 'permission'),
	(3, 'auth', 'user'),
	(14, 'cm', 'channel'),
	(13, 'cm', 'filetype'),
	(9, 'cm', 'package'),
	(8, 'cm', 'plugin'),
	(12, 'cm', 'procduct'),
	(7, 'cm', 'publishrecord'),
	(11, 'cm', 'sidebar'),
	(10, 'cm', 'sidebargroup'),
	(5, 'contenttypes', 'contenttype'),
	(6, 'sessions', 'session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;


-- 导出  表 cmdata.django_migrations 结构
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

-- 正在导出表  cmdata.django_migrations 的数据：~13 rows (大约)
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
REPLACE INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(1, 'contenttypes', '0001_initial', '2016-10-26 03:43:52'),
	(2, 'auth', '0001_initial', '2016-10-26 03:43:55'),
	(3, 'admin', '0001_initial', '2016-10-26 03:43:56'),
	(4, 'admin', '0002_logentry_remove_auto_add', '2016-10-26 03:43:56'),
	(5, 'contenttypes', '0002_remove_content_type_name', '2016-10-26 03:43:56'),
	(6, 'auth', '0002_alter_permission_name_max_length', '2016-10-26 03:43:56'),
	(7, 'auth', '0003_alter_user_email_max_length', '2016-10-26 03:43:57'),
	(8, 'auth', '0004_alter_user_username_opts', '2016-10-26 03:43:57'),
	(9, 'auth', '0005_alter_user_last_login_null', '2016-10-26 03:43:57'),
	(10, 'auth', '0006_require_contenttypes_0002', '2016-10-26 03:43:57'),
	(11, 'auth', '0007_alter_validators_add_error_messages', '2016-10-26 03:43:57'),
	(12, 'auth', '0008_alter_user_username_max_length', '2016-10-26 03:43:57'),
	(13, 'sessions', '0001_initial', '2016-10-26 03:43:57');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;


-- 导出  表 cmdata.django_session 结构
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- 正在导出表  cmdata.django_session 的数据：~2 rows (大约)
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
REPLACE INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
	('i6lcy1eza4zeo22tn6ym0sqte3phbhxg', 'Y2Y2NTViZDg3YzhjZTU3Y2M5NjU2ZjAzNDRiZjAzMzcyYTYxMGJkZTp7Il9hdXRoX3VzZXJfaGFzaCI6Ijk1M2VkYmI1NjMxYTBkZDUxNWYyOTZmZjE2MjU3YzAwYzFlNTlkYjkiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2016-12-01 02:46:03'),
	('s7pkc2q0iwqffxidw6u1zo0yg357rsos', 'Y2Y2NTViZDg3YzhjZTU3Y2M5NjU2ZjAzNDRiZjAzMzcyYTYxMGJkZTp7Il9hdXRoX3VzZXJfaGFzaCI6Ijk1M2VkYmI1NjMxYTBkZDUxNWYyOTZmZjE2MjU3YzAwYzFlNTlkYjkiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2016-11-12 08:03:22');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
