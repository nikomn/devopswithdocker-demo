# devopswithdocker-demo

Very simple demo project made as part of course DevOps with Docker.

I had no other project that seemed suitable, so made this one. It's
just a simple parakeet program that repeats everything the user enters.
Not really useful and I might build something bigger out of this sometime.
For now this should be ok as the real goal is to try to get an app running
in docker.

# Usage

You can build with command

```bash
$ docker build . -t devopswithdocker-demo
```

And after this it can be run with

```bash
$ docker run -it devopswithdocker-demo
```

# Using from dockerhub version

The image should also be in dockerhub, and you can also just use that with

```bash
$ docker run -it nikomn/devopswithdocker-demo
```
