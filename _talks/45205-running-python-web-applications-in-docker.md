---
video_url: https://youtu.be/9L6x2j-7eVQ
layout: talk
recordingconsent: true
talkid: 45205
title: Running Python web applications in Docker
track: general
type: talk

speakers:
- bio: ''
  company: Tidetech
  name: Tim Heap
  thumbnailUrl: tim-heap.png
  twitter: tim_heap
  url: https://timheap.me/

abstract: An introduction on running Python web applications in Docker, covering how
  to structure your project, running the project in both development and production,
  testing the project, and compiling static assets for your frontend.
---
Docker is an excellent tool for running Python applications, but it is a different environment compared to traditional Python projects, with a few unique challenges. This talk will cover the basics on getting a new Python project running in a Docker environment, from development through testing all the way to a production ready Docker image. I will introduce running companion services with `docker-compose`, how to run a test suite for your application, and briefly how to compile frontend assets using something like Node to be served by your Python application.

This talk will not cover deploying Docker containers on a container hosting service or other aspects of actually deploying a Docker image, only how to build a Docker based Python project. The audience should have a basic familiarity with building Python web applications, such as with Django or Flask. Familiarity with Docker is not essential.
