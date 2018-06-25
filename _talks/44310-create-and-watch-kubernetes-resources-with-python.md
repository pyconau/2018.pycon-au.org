---
layout: talk
recordingconsent: true
talkid: 44310
title: Create and Watch Kubernetes Resources With Python
track: general
type: talk

speakers:
- bio: ''
  company: Ucroo
  name: Oliver Nagy
  thumbnailUrl: oliver-nagy.png
  twitter: ''
  url: ''

abstract: 'A practical guide to using the Kubernetes API from Python in production.


  Batteries are included: Python code, service account manifests, Dockerfile and

  all commands to deploy directly to Google Kubernetes Engine (no affiliation).'
---
Kubernetes has ranked as one of the top 25 Go projects on Github for a while
now. However, the Kubernetes API itself is language agnostic and auto-generated
clients exist for many languages, including Python.

In this talk I will show how you can query deployments, watch for changes, and
launch your own deployments with only a few lines of Python code.

The presentation comes with batteries included. It will not only show the code
but include everything you need to run it inside Kubernetes itself, like
Dockerfiles and service account manifests. I will use the Google Kubernetes
Engine (GKE) for the demo.

By the end of the talk, you will know how to interact with the Kubernetes API
from Python and how to deploy that program onto Kubernetes itself. From there
it is only a small step to modify the code and create, watch or update pods,
ingresses, namespaces, replica sets or any other Kubernetes resource.
