---
layout: talk
recordingconsent: true
talkid: 45063
title: Refactoring Code With the Standard Library
track: general
type: talk

speakers:
- bio: "I am a Production Engineer at Facebook working on our Python Foundation team,\
    \ building tools and improving support for Python, both outside the company and\
    \ within Facebook's shared codebase. I\u2019ve had the opportunity to learn and\
    \ grow in multiple sectors of the industry over the past decade, including storage,\
    \ telecommunications, network security, and video games."
  company: Facebook
  name: John Reese
  thumbnailUrl: john-reese.png
  twitter: n7cmdr
  url: https://jreese.sh

abstract: What if you could refactor your entire code base, safely and automatically?
  How much old code could you fix or replace if you didn't need to worry about updating
  every reference by hand? I'll show you how a concrete syntax tree (CST) can help
  you do just that using only the standard Python library.
---
Python includes a concrete syntax tree (CST) in the standard library, useful for mass refactoring code bases of all sizes. I'll walk through the differences between abstract and concrete syntax trees (AST and CST), why a CST is useful for refactoring, and how you can build basic refactoring tools on top of a CST to modify your entire code base quickly and safely. Lastly, I'll demonstrate what's possible with these tools, including upgrading code to new interfaces, or wholesale movement of code between modules.
