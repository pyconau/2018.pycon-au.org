---
layout: talk
recordingconsent: true
talkid: 45383
title: Weird and wonderful ways of deploying your Django site
track: django
type: talk

speakers:
- bio: I'm the technical director at Torchbox, a UK web agency. I also run the Wagtail
    CMS project. I wrote the theme tune to [Charlie and Lola](https://en.wikipedia.org/wiki/Charlie_and_Lola).
  company: Torchbox and Wagtail
  name: Tom Dyson
  thumbnailUrl: tom-dyson.png
  twitter: tomd
  url: https://torchbox.com

abstract: Deploying Django sites the traditional way is tricky for beginners and a
  hassle for even experienced developers. This talk will show you three easier routes
  to launching your beautiful new site, and teach you to impress your colleagues with
  buzzwords like 'Serverless', 'Docker' and 'SSG'.
---
Online support forums for Django are full of questions from developers who are delighted with the experience of building their first Django apps but frustrated with the hassles of deploying it. Compared to the experience of uploaded PHP files to a shared server, the standard experience of setting up Nginx, PostgreSQL, Gunicorn, Supervisor, firewalls, SSL certificates etc. can be painful for beginners and boring for experts.

In the last few years, several compelling alternatives to the traditional stack have become available. I'll demonstrate three main approaches:

 - user-friendly Docker-based platforms (in particular Dokku)
 - Serverless platforms (in particular Zappa)
 - Static Site Generation (in particular django-bakery and Netlify)

I'll go through the basic steps for using each of these, comparing the benefits and disadvantages of each. Attendees should leave with a broad understanding of each approach, and with a clutch of tips that will accelerate their next deployment.
