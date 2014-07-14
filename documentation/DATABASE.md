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
	| TODO         | 
	| PENDING      | 
	| DONE         | 
	| SUBORDINATES |
	| SUPERVISORS  |

	- **TODO:** List of all documents to do.
	- **PENDING:** List of all documents waiting for approval
	- **DONE:** List of all completed and approved documents

* Document:

	| DOCUMENT             | 
	| ---------------------|
	| ID                   |
	| TITLE                |
	| INSTRUCTIONS         |
	| REQUEST_DATE         |
	| DUE_DATE             |
	| RESPONSIBLE_EMPLOYEE |
	| REQUESTER_EMPLOYEE   |
	| SITUATION            | 
	| APPROVED             | 
	| FILE                 | 

	- **SITUATION:** Requested/Done
	- **APPROVED:** Yes/Not
