![HBNB](https://user-images.githubusercontent.com/69823997/108614204-c887e480-73c6-11eb-9d40-c6f38627d8f7.png)

<h1 align="center"> HBNB - The Console </h1>

# About

The AirBnB console is a CLI that allows you to manipulate (create, update, delete and store) elements through JSON. By doing this we're creating an interface to communicate to the DataBase (Which is a file that gets manipulated).

# list of elements available

	* Amenity
	* City
	* Place
	* Review
	* State
	* User

# How to
------------

* **interactive** mode execution:

------------

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

------------

* **non-interactive** mode execution:

------------
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```
# Project overview

![hbnb](https://user-images.githubusercontent.com/69823997/108603381-98642580-7375-11eb-9dba-f52d0f3f3074.png)

# Test

```
$ python3 -m unittest discover tests
```

# Authors

 	* Juan Pablo Montoya

		[Twitter:](https://twitter.com/Jumo0)
		[LinkedIn](https://www.linkedin.com/in/jumoc/)
		[Github](https://github.com/Jumoc)

	* Alejandro Franco Cedeño

		[Twitter](https://twitter.com/afrancocedeno
		[LinkedIn](https://www.linkedin.com/in/afrancocedeno/
		[GitHub](https://github.com/afrancocedeno
