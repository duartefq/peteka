![peteka](https://dl.dropboxusercontent.com/u/85402777/peteca.png) Peteka > Screen Layouts
========

Connection
----------

- **ENGINE:** django.db.backends.mysql
- **NAME:** jobr2d2_PETEKA
- **USER:** jobr2d2_2261
- **PASSWORD:** 22GI
- **HOST:** 54.245.230.200
- **PORT:** 3306

Tables
----------

* Employee:

	| EMPLOYEE     | 
	| -------------|
	| ID           |
	| NAME         |
	| EMAIL        |
	| PASSWORD     | 

* Supervisor|Employee relation

	|SUPERVISOR_EMPLOYEE|
	|-------------------|
	|ID                 |
	|SUPERVISOR_ID      |
	|SUPERVISOR_ID      |

* Document:

	| DOCUMENT             | 
	| ---------------------|
	| ID                   |
	| TITLE                |
	| INSTRUCTIONS         |
	| REQUEST_DATE         |
	| DUE_DATE             |
	| SITUATION            | 
	| APPROVED             | 
	| PDF                  | 
	| RESPONSIBLE_ID       |
	| REQUESTER_ID         |

	- **SITUATION:** Requested/Done
	- **APPROVED:** Yes/Not

SQL by manage.py
---------

'''
BEGIN;
CREATE TABLE `department_employee` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(200) NOT NULL,
    `email` varchar(200) NOT NULL,
    `password` varchar(50) NOT NULL
);

CREATE TABLE `department_supervisor_employee` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `supervisor_id` integer NOT NULL,
    `employee_id` integer NOT NULL
);

ALTER TABLE `department_supervisor_employee` ADD CONSTRAINT `supervisor_id_refs_id_3085327b` FOREIGN KEY (`supervisor_id`) REFERENCES `department_employee` (`id`);
ALTER TABLE `department_supervisor_employee` ADD CONSTRAINT `employee_id_refs_id_3085327b` FOREIGN KEY (`employee_id`) REFERENCES `department_employee` (`id`);


CREATE TABLE `department_document` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `title` varchar(200) NOT NULL,
    `instructions` varchar(1240) NOT NULL,
    `request_date` datetime NOT NULL,
    `due_date` datetime NOT NULL,
    `situation` integer NOT NULL,
    `approved` integer NOT NULL,
    `pdf` varchar(100) NOT NULL,
    `responsible_id` integer NOT NULL,
    `requester_id` integer NOT NULL
);


ALTER TABLE `department_document` ADD CONSTRAINT `responsible_id_refs_id_c7d82ff6` FOREIGN KEY (`responsible_id`) REFERENCES `department_employee` (`id`);
ALTER TABLE `department_document` ADD CONSTRAINT `requester_id_refs_id_c7d82ff6` FOREIGN KEY (`requester_id`) REFERENCES `department_employee` (`id`);

COMMIT;


'''
