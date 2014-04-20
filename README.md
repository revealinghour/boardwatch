[boardwatch.in](http://boardwatch.in) is [distrowatch](http://distrowatch.com) for electronic boards like Arduino and BeagleBone Black.  

- - - 
#### Contributing a new board
* You will need grip installed. Install it using

		pip install grip
* Create a folder hierarchy as follows  
|-- arduino 
|     |-- uno 
|     |     |-- ArduinoUno_R3_Front.jpg
|     |     |-- index.html 
|     |     `-- index.md

* Copy the template index.md into the newly created index.md
* Use gfm to compile it into index.html

		grip --gfm --export index.md

