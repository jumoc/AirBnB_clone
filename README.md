<h1 align="center"> HBNB - The Console </h1>

# About

The AirBnB console is a CLI that allows you to manipulate
(create, update, delete and store) elements through JSON.

By doing this we're creating an interface to communicate to
the DataBase (Which is a file that gets manipulated).

# list of elements available

	* Amenity
	* City
	* Place
	* Review
	* State
	* User

# How to

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

<a href="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210220%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210220T165852Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=1b40add26a2f7572a1ccf99da05ce7388c79c1b75c892fe18f86cf3b4f7b10ba" alt="CACA" border="0"></a>

# Test

...
$ python3 -m unittest discover tests
...

# Authors

 	* **Juan Pablo Montoya**
	 	* <a href="https://twitter.com/Jumo0"> Twitter </a> & <a href="https://www.linkedin.com/in/jumoc/"> LinkedIn </a> & <a href="https://github.com/Jumoc"> GitHub </a>
	* **Alejandro Franco Cedeño**
		* <a href="https://twitter.com/afrancocedeno"> Twitter </a> & <a href="https://www.linkedin.com/in/afrancocedeno/"> LinkedIn </a> & <a href="https://github.com/afrancocedeno"> GitHub </a>
