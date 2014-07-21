![peteka](https://dl.dropboxusercontent.com/u/85402777/peteca.png) Peteka
========

Web application that manages document storage, workflow, approval for an organization.
http://peteka.j43.ca/

Developers
-----------

* [Joabe Mendes](https://github.com/JoabMendes)
* [Duarte Fernandes](https://github.com/duartefq)
* [Eric White](https://github.com/ewhite05/)


Request Details
-----------

The organization is strictly hierarchical. Every employee has exactly one supervisor. Supervisors initiate document prouduction requests. A supervisor can can request any subordinate (direct or indirect) to produce a document. Document production requests include a "Title", "Instructions" and a time stamp when the request was made.

When an employee logs into the web application, he or she is presented with a dashboard that has 3 sections, "To Do", "Pending", and "Completed".

The "To Do" section contains a list of tasks the employee has to complete. This could be producing a new document; reviewing and approving (or rejecting) a document that a subordinate has created or revised; revising a document that was rejected by a superior.

The "Pending" section contains a list of all the documents that this employee has produced, or reviewed and approved that is still waiting further approval by one more superiors.

The "Completed" section contains a list of the doucments that this employee has produced, or reviewed and approved that has been fully approved by all supervisors in the chain.

The application should have a publically visible page that lists all of the fully reviewed and approved documents.

Employees produce or revise documents by uploading a .PDF file.

When a supervisor rejects a document, he or she will have to complete a "Comments" field. A document can be recjected more than once. The comment history should be available.

Employees should have the option to receive email notificaitons whenever their "To Do" list changes.

The dashborad page should be dynamically updated without the user having to manually refresh the page.

One user should have the capability to add new users and set up the supervisory relationships.