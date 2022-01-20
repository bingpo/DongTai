CREATE TABLE `project_version_control` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '自增主键',
  `version` varchar(63) DEFAULT NULL COMMENT '版本号',
  `component_name` varchar(255) DEFAULT NULL COMMENT 'sql名',
  `component_version_hash` varchar(255) DEFAULT NULL COMMENT 'sql哈希值',
  `additional` varchar(255) DEFAULT NULL COMMENT '额外注释',
  `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `project_version_control_UN` (`component_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
