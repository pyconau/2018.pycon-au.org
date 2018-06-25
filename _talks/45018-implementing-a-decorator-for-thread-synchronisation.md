---
layout: talk
recordingconsent: false
talkid: 45018
title: Implementing a decorator for thread synchronisation
track: general
type: talk

speakers:
- bio: Graham is the author of mod_wsgi, the Apache module for hosting of Python web
    applications using the WSGI interface. He also has a keen interest in Docker and
    Platform as a Service (PaaS) technologies. He is currently a developer advocate
    for OpenShift at Red Hat.
  company: Red Hat
  name: Graham Dumpleton
  thumbnailUrl: graham-dumpleton.png
  twitter: GrahamDumpleton
  url: http://blog.dscpl.com.au

abstract: Using multithreading in Python applications? Interested in complex use cases
  for decorators and context managers? This talk will describe how the Java programming
  language "synchronized" keyword, for handling synchronisation in multithread applications,
  can be implemented in Python.
---
The existence of the global interpreter lock (GIL) in Python, and that basic operations on Python objects are atomic, simplifies to a degree the implementation of multithreaded applications. The need for synchronising the activity of threads can't be avoided entirely though.

In programming languages such as Java, the language provides syntactical support for annotating that methods, or blocks of code, can only be executed by one thread at a time. In Python there is no such language support.

In this talk, you will learn how Python decorators and context managers can be used to implement an equivalent of the ``synchronized`` keyword from the Java programming language. The decorator described will provide locking for an individual function when applied to a global function or static method, to an instance of a class when applied to an instance method, and, to the class when applied to a class method. The decorator can also be used as a context manager to provide locking for a block of code.

The talk will be of interest to developers looking for ways of simplifying how they implement locking in multithreaded applications, and to anyone looking for more complicated examples of using Python decorators.
