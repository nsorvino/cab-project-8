[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-8d59dc4de5201274e310e4c54b9627a8934c3b88527886e3b421487c677d23eb.svg)](https://classroom.github.com/a/-Nv0cKFk)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10766481&assignment_repo_type=AssignmentRepo)

```
Project Purpose: To locate potential locations for new elcectric vehicle charging statins by county in New Jersey.

Videos:
Proposal: https://www.youtube.com/watch?v=YO0EUpkoxio
Final Video: https://www.youtube.com/watch?v=rmVCuOyC-TQ

Instructions:

#install python pip and psycopg2 packages
sudo pacman -Syu
sudo pacman -S python-pip python-psycopg2

#install flask
pip install flask

#run the table creation and population script
./Team8.sh

#enter psql database
psql team8

#run flask application
EXPORT FLASK_APP=app.py
flask run

#Follow link in terminal to site.
```
Main Page:
![image](https://user-images.githubusercontent.com/123657245/235206116-53c25566-e55e-4942-a18e-ab0a2a38d05a.png)

Result Page:
![image](https://user-images.githubusercontent.com/123657245/235206958-4f04e93b-e721-4ffc-a59a-f989ed9b84b7.png)
