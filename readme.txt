Task CLI
https://roadmap.sh/projects/task-tracker

This is a simple command line interface to work with objects in a JSON file.

To interact with the CLI, open the project directory in a terminal and execute with "Python3 taskcli.py", followed by your desired command.

Commands:

Add an object:
* add (description)

Update an object's description:
* update (id) (description)

Delete an object:
* delete (id)

Change an object's status:
* mark (id) ("todo","in-progress","done")

List all objects:
* list

List objects with a specific status:
* list ("todo","in-progress","done")

Objects:

Each object in the JSON file contains the following attributes:

-id
-description
-status
-createdAt
-updatedAt