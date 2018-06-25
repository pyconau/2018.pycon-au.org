---
layout: talk
recordingconsent: true
talkid: 41898
title: Python in Chromium
track: general
type: talk

speakers:
- bio: "I'm a Software Engineer at Google where I currently serve as a Tech Lead on\
    \ the ChromeOS team. My previous projects have included Chrome's CSS engine, where\
    \ I worked in the Python Code Generation part of the codebase. I also volunteer\
    \ at GPN and NCSS, where I teach students how to code with Python.\r\n\r\nI've\
    \ been working on Chromium for 5 years, and I've never given a talk at PyCon before,\
    \ but am eager to try :)"
  company: ''
  name: Sasha Morrissey
  thumbnailUrl: sasha-morrissey.png
  twitter: ''
  url: ''

abstract: Chromium started as a C++ project, and now has over 22,000 Python files,
  which has grown exponentially over time. In this talk, I'll go through the ways
  we use Python in Chrome, the pros/cons, and what I've learned in the transition
  to a full-fledged Python developer.
---
Chromium started as a C++ project, and now has over [22,000 Python files](https://cs.chromium.org/search/?q=lang:%5Epython$&all=1&sq=package:chromium&type=cs), which has grown exponentially over time as Python has become a more and more popular language for use in large projects.

In Chrome, we use Python for 3 main things:

* Code generation (e.g. custom scripts, protos, jinja2)
* Tools (e.g. checkout, sync, configure, build, analyze, etc)
* Infrastructure (e.g. our testing system, bug tracker, and code review tool)

In my talk, I'll go through each of these areas, the pros/cons of using Python, and what I've learned in the unexpected transition from a C++ developer to a Python developer.
