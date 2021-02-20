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

<a href="![hbnb](https://user-images.githubusercontent.com/69823997/108603381-98642580-7375-11eb-9dba-f52d0f3f3074.png)
" alt="CACA" border="0"></a>

# Test

```
$ python3 -m unittest discover tests
```

# Authors
 	* **Juan Pablo Montoya**
	 	* <a href="https://twitter.com/Jumo0"> Twitter </a> & <a href="https://www.linkedin.com/in/jumoc/"> LinkedIn </a> & <a href="https://github.com/Jumoc"> GitHub </a>
	* **Alejandro Franco Cedeño**
		* <a href="https://twitter.com/afrancocedeno"> Twitter </a> & <a href="https://www.linkedin.com/in/afrancocedeno/"> LinkedIn </a> & <a href="https://github.com/afrancocedeno"> GitHub </a>
