---
video_url: https://youtu.be/ceJ-vy7fvus
layout: talk
recordingconsent: true
talkid: 45392
title: 'Task Queues: A Celery Story'
track: general
type: talk

speakers:
- bio: Tom is in his final year Software Engineering and Mathematics at the University
    of Queensland, while working in development and devops roles at Polymathian, an
    industrial mathematics company. As a Pythonista by day and a Haskeller by night,
    he loves any way he can put maths into his software - by types, functional programming,
    or just writing mathematical code.
  company: Polymathian/UQ
  name: Tom Manderson
  thumbnailUrl: tom-manderson.png
  twitter: TRManderson
  url: https://trm.io

abstract: Python has a surprisingly large number of task queue libraries, but Celery
  reigns supreme. Unfortunately, there are a few use cases where it's remarkably bad.
  Learn about why you might want a task queue (and when you definitely don't), when
  Celery is appropriate, and what you can do when it's not.
---
At my work, we've used Celery as the foundation of our task queueing/tracking system for years now, but we finally reached a point where the quirks of Celery are too much. Because of this, I had to spend two weeks at work researching different task queue systems, and have since implemented two options other than Celery that are about to enter production use. In the time doing this, I've gathered useful insights about several task queueing libraries and their uses.

I will introduce the use case for task queues, and explicitly point out when they're not applicable. I will then give a basic overview of the Celery library and its use case, but will then cover where it fell short in our specific use case. I will then point out ways to deal with the particular failings of Celery, and focus on how we solved our issues (using RQ) and the differences between the Celery and RQ model.

The talk will assume a solid understanding of Python, though nothing more advanced than decorators will be covered.
