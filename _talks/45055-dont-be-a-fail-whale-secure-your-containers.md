---
layout: talk
recordingconsent: true
talkid: 45055
title: "Don\u2019t be a fail whale: secure your containers"
track: security
type: talk

speakers:
- bio: Sarah is a Security Architect at Versent, where she helps people move and run
    their stuff in the cloud securely. She has worked in Europe, New Zealand and Australia
    and in a previous life she was a network engineer and she still loves IT infrastructure,
    but now spends her spare time evangelising security to anyone who will listen
    and is a firm believer that security doesn't need to be really hard. Sarah spends
    her spare time eating hipster brunches and taking high teas.
  company: Versent
  name: Sarah Young
  thumbnailUrl: sarah-young.png
  twitter: _sarahyo
  url: ''

abstract: Containers are great technology, but they have specific security threats
  that need to be considered when implementing and running them. In this talk, I give
  an overview of how to effectively threat model for containers running python and
  some of the tools that you can use to counter them.
---
I know that threat modelling and security sounds like a rather dry topic, but it's a structured way of thinking about security threats that i feel it's really important developers start thinking about early in the delivery lifecycle (whichever model you're using). With containers, it's more likely that security tools need to be baked or added into container images early in the process so educating developers about this is - in my option - critical for the success of a continuous delivery model. Understanding that security risks to containers are different to virtual machines or the traditional monolithic application stack and that the traditional security toolset isn't necessarily effective any more is key, and one of the main threads of my talk. As I'm conscious this could be a a dry topic, my talk has many GIFs and memes. More seriously though, it includes relevant anecdotes and was developed with input from Python developers in both my professional and personal circle, to bring (where applicable) python-specific container security examples into the discussion.

A brief summary of the talk structure:

- Introduction to myself and the talk
- Overview of threat modelling
- Threat modelling for containers
- The difference between threats to containers, VMs and the traditional application stack
- Key security threats to containers in general
- Key security threats to containers running Python
- Tools to mitigate these threats
- Where these tools fit within the process
- Summary and close
