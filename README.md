# flask_scrappy
this is base on scrappy that used for vietnam stock market aggregator 

# Engine service
Docker image with uWSGI and Nginx for Flask web applications in Python 3.6, Python 3.5 and Python 2.7 running in a single container. Optionally using Alpine Linux

#General Instruction
please install docker for full running in local machine

<pre>
  $ docker version
    Client:
     Version:	17.12.0-ce
     API version:	1.35
     Go version:	go1.9.2
     Git commit:	c97c6d6
     Built:	Wed Dec 27 20:03:51 2017
     OS/Arch:	darwin/amd64

    Server:
     Engine:
      Version:	17.12.0-ce
      API version:	1.35 (minimum version 1.12)
      Go version:	go1.9.2
      Git commit:	c97c6d6
      Built:	Wed Dec 27 20:12:29 2017
      OS/Arch:	linux/amd64
      Experimental:	true
$ docker-compose version
docker-compose version 1.18.0, build 8dd22a9
docker-py version: 2.6.1
CPython version: 2.7.12
OpenSSL version: OpenSSL 1.0.2j  26 Sep 2016
</pre>

#Simple Architecture 

+------------------------------- docker container ----------------------------+
+-------------+       +------------+         +--------------+     +-----------+
|             |       |            |         |              |     |           |
|    nginx    +-------+  gunicorn  +---------+  flask app   +-----+   mongo   |
|             |       |            |         |              |     |           |
+-------------+       +------------+         +--------------+     +-----------+

# Quick start

Pull build and up
<pre>
$ git clone  

</pre>

