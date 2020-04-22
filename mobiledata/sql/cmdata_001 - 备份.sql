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
CREATE DATABASE IF NOT EXISTS `cmdata` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `cmdata`;


-- 导出  表 cmdata.auth_group 结构
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

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
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  cmdata.auth_user 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  cmdata.auth_user_user_permissions 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;


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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

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
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

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
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  cmdata.django_session 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;

-- 导出  表 cmdata.cm_channel 结构
CREATE TABLE IF NOT EXISTS `cm_channel` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '1',
  `channelnum` int(11) NOT NULL,
  `description` varchar(20) NOT NULL,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 正在导出表  cmdata.cm_channel 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `cm_channel` DISABLE KEYS */;
REPLACE INTO `cm_channel` (`id`, `channelnum`, `description`, `addtime`) VALUES
	(1, 100039, 'cms推cm', NULL),
	(2, 100005, '电池医生渠道', NULL),
	(3, 100003, '手助全渠道', NULL),
	(4, 2010000002, '豌豆荚', NULL),
	(5, 000000, '默认渠道', NULL),
	(6, 2010000006, '百度', NULL),
	(7, 2010000005, '应用宝', NULL);
/*!40000 ALTER TABLE `cm_channel` ENABLE KEYS */;

-- 导出  表 cmdata.cm_filetype 结构
CREATE TABLE IF NOT EXISTS `cm_filetype` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '1',
  `type` varchar(20) NOT NULL,
  `description` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `cm_plugin` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '1',
  `publishid` int(11) NOT NULL,
  `pluginver` varchar(20) NOT NULL,
  `hostver` varchar(20) NOT NULL,
  `pluginpath` varchar(200) NOT NULL,
  `pluginmd5` varchar(30) NOT NULL,
  `plugintype` varchar(20) NOT NULL,
  `pluginsize` varchar(20) NOT NULL,
  `channel` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `cm_procduct` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '1',
  `procductname` varchar(20) NOT NULL,
  `description` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `cm_publishrecord` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '1',
  `publishtime` datetime NOT NULL,
  `filetype` varchar(20) NOT NULL,
  `channel` varchar(20) NOT NULL,
  `details` varchar(6000) NOT NULL,
  `filepath` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `cm_sidebar` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '1',
  `name` varchar(20) CHARACTER SET utf8 NOT NULL,
  `url` varchar(100) CHARACTER SET utf8 NOT NULL,
  `blank` varchar(20) CHARACTER SET utf8 NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


REPLACE INTO `cm_sidebar` (`id`, `name`, `url`, `blank`, `group_id`) VALUES
	(1, '渠道查询', 'http://127.0.0.1:8080/cm/channel/', '', 1),
	(2, '插件查询', 'http://127.0.0.1:8080/cm/plugin/', '', 1),
	(3, 'apk包查询', 'http://127.0.0.1:8080/cm/package/', '', 1),
	(4, '宿主查询', 'http://127.0.0.1:8080/cm/host/', '', 1),
	(5, 'apk包解析', 'http://127.0.0.1:8080/cm/tool/packagedetail/', '', 2),
	(6, '提测合格率', 'http://update.rdev.kingsoft.net:8089/addstats/', '', 3),
	(7, '手机资产列表', 'http://update.rdev.kingsoft.net:8089/phonemanager/index', '', 3),
	(8, '手助发布记录', 'http://update.rdev.kingsoft.net:8089/fileapp/file/publishlist/', '', 3);
	
CREATE TABLE IF NOT EXISTS `cm_sidebargroup` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '1',
  `group` varchar(20) NOT NULL,
  `blank` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*!40000 ALTER TABLE `cm_sidebargroup` DISABLE KEYS */;
REPLACE INTO `cm_sidebargroup` (`id`, `group`, `blank`) VALUES
	(1, '查询', ''),
	(2, '工具', ''),
	(3, '外链', '');
/*!40000 ALTER TABLE `cm_sidebargroup` ENABLE KEYS */;

CREATE TABLE IF NOT EXISTS `cm_plugintype` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '1',
  `name` varchar(20) NOT NULL,
  `description` varchar(20) NOT NULL,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `cm_hostver` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '1',
  `hostver` varchar(20) NOT NULL,
  `addtime` datetime DEFAULT NULL,
  `status` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `cm_apkver` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '1',
  `apkver` varchar(20) NOT NULL,
  `addtime` datetime DEFAULT NULL,
  `status` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `cm_pluginver` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '1',
  `pluginver` varchar(20) NOT NULL,
  `addtime` datetime DEFAULT NULL,
  `status` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `cm_iidcode` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '1',
  `iidcode` varchar(20) NOT NULL,
  `addtime` datetime DEFAULT NULL,
  `status` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



