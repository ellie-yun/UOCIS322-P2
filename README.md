
# UOCIS322 - Project 2 #
> **Author: Ellie Yun, yyun@uoregon.edu**

Implementing the same "file checking" logic, which is implemented in Project 1, but using Flask.

Like Project 1, if a file (`docroot/name.extension`, any name, any extention or format) exists, transmit `200/OK` header followed by that file html. If the file doesn't exist, transmit an error code in the header along with the appropriate page html in the body. This will be done by creating error handlers that will be (or are) taught in class (refer to the recordings if needed). Also, the following two html files with the error messages is created:
    * `404.html` will display "File not found!"
    * `403.html` will display "File is forbidden!"

    ⚠️ NOTE: if a request contains illegal characters (// .. ~) anywhere (not just the beginning), the response should be 403.
    
    ⚠️ NOTE: it's okay if `//` doesn't work if it's at the beginning of the request since Flask will remove those.

## Basic Docker commands

* Get information about docker setup the machine

  ```
  docker info
  ```

* List running docker containers

  ```
  docker ps
  ```

* List all docker containers

  ```
  docker ps -a
  ```

* List images using

  ```
  docker images
  ```

* Build an image

  ```
  docker build -t <Tag name> path/
  ```

  or just do this if your `Dockerfile` is in the same directory:
  ```
  docker build -t <Tag Name> .
  ```

* Remove containers

  ```
  docker container rm <Container Name>
  ```

* Run containers
  ```
  docker run <Tag Name / Image ID>
  ```

  ```
  docker run -h CONTAINER1 -i -t debian /bin/bash
  docker run -h CONTAINER1 -i -t ubuntu /bin/bash
  ```

  Here, `-h` is used to specify a container name, `-t` to start with tty, and `-i` means interactive. Note: second times will be quick because of caching.

* Docker with networking

  ```
  docker run -h CONTAINER2 -i -t --net="bridge" debian /bin/bash
  ```

* When the containers are not running and when you're done, kill them using

  ```
  docker rm `docker ps --no-trunc -aq`
  ```

* Rename using

  ```
  docker rename name_v0 name_v1
  ```

* Start a container

  ```
  docker start <container name>
  ```

* Stop a container

  ```
  docker stop <container name>
  ```

# Creating images

* Create a `Dockerfile`. The name is case sensitive and it has to be `Dockerfile`

  ```
  vim Dockerfile
  ```

* The `FROM` command specifies the base image you are going to use. It can be an existing image, like ubuntu, alpine, debian, etc.

  ```
   FROM debian
  ```

* `CMD` command specifies all the commands you need to run

  ```
   CMD echo hello world
  ```

* Build the image with folder name (`.` in this case)

  ```
   docker build .
  ```

* Final output
  ```
  Successfully built e2e741ea5f6f  
  ```

* Run the image using the image ID (`e2e741ea5f6f` in this case) and a test name of your choice

  ```
  docker run --name <test name> e2e741ea5f6f
  ```

* Remove images using

  ```
  docker rmi <Image ID>
  ```

For more info refer to: https://docs.docker.com/engine/reference/builder/.

## Credits

Michal Young, Ram Durairajan, Steven Walton, Joe Istas.

