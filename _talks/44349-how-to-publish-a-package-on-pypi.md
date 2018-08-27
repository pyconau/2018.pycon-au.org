---
video_url: https://youtu.be/QgZ7qv4Cd0Y
layout: talk
recordingconsent: true
talkid: 44349
title: How To Publish A Package On PyPI
track: general
type: talk

speakers:
- bio: Mark is a Developer Advocate for Nexmo, specialising in Python and Java, but
    also dabbling in Go and a few other things. He's interested in system architecture
    and scalability, and when he's not programming you'll probably find him building
    a mechanical keyboard from scratch.
  company: Nexmo
  name: Mark Smith
  thumbnailUrl: mark-smith.png
  twitter: judy2k
  url: ''

abstract: Starting with nothing, we'll build a package and publish it on PyPI using
  current best practices! Learn how to structure, document and test your project on
  different platforms. Discover the difference between `setup.py` and `Pipfile`. Finally,
  use CookieCutter to avoid doing it twice (or even once)!
---
Always wanted to publish a package on PyPI, but didn't know where to start?
This talk is for you! Starting with nothing, we'll build a package and publish it on PyPI using current best practices.

Publishing a package on PyPI used to be a cargo cult. (And often still is!) Instead of copying and pasting from other projects' `setup.py` without fully understanding what's happening, discover how to package your code for PyPI from scratch - then learn how to avoid doing any of this completely! (But now know you'll know what's going on).

* _Why_ should you package your code for PyPI?
* How to structure your project and your code, including why you need a `src` folder!
* Discover what goes in your `Pipfile` and your `setup.py`, and why. Learn
  the difference between installing your library to use it, and installing it to develop on it.
* Write tests for your project, and run them using Tox.
* Ensure your code will work in different on different platforms with
  Continuous Integration!
* Document your code so people won't ask you loads of questions!
* How to actually get your code on PyPI using Twine. Configure your machine
  for PyPI and test your package release on the PyPI test server.
* Finally, learn how avoid doing any of this yourself (or avoid doing it
  twice) using CookieCutter templates.

By the end of this talk, you'll be so comfortable packaging projects you won't avoid writing `setup.py` files any more! Maybe you'll even start writing new code just so you can publish it on PyPI!
