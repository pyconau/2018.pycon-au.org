---
video_url: https://youtu.be/Rm4t_5uVqTU
layout: talk
recordingconsent: true
talkid: 45066
title: Danger Will Robinson! Warning! Warning! Warning! (What Python warnings are,
  why you should turn them on and how to create your own)
track: general
type: talk

speakers:
- bio: "Peter Lovett is an accomplished programmer, developer, speaker and educator.\
    \ He has more than a third of a century of paid programming experience, working\
    \ with many languages, from Assembler and C to Perl, C++, Java and Python. The\
    \ son of a programmer all three of his sons can program in Python.\r\n\r\nHe brings\
    \ wide and diverse experience, deep technical knowledge, an engaging presentation\
    \ and directly useful information to his audiences.\r\n\r\nHe has spoken at 6\
    \ of the 8 PyConAu's and has spoken at Linux Conf Au.\r\n\r\nHe runs training\
    \ courses through his company, Plus Plus in Australia and New Zealand, running\
    \ courses for some of Australia and New Zealand's biggest companies, and has trained\
    \ thousands of people in C, C++, Java and Python.\r\n\r\n He can be found at www.plusplus.com.au\r\
    \n"
  company: Plus Plus Pty Ltd
  name: Peter Lovett
  thumbnailUrl: peter-lovett.png
  twitter: ''
  url: https://www.plusplus.com.au

abstract: Python's warnings mechanism is an important part of creating robust, reliable,
  production grade code. Unfortunately, it's also one of the most under-used standard
  libraries. Help find the bugs and errors with warnings! Ignore them at your peril!
  Suitable for beginner to intermediate.
---
Python's warnings mechanism is an important part of creating robust, reliable, production grade code. Unfortunately, it's also one of the least known and one of the most under-used standard libraries. Help find the bugs and errors with warnings! What bugs are lurking in your code? Ignore them at your peril!
Suitable for beginner to intermediate.
This talk will cover the basics of the warning mechanism, system-generated and user-generated warnings, how to turn them on and off , and how to filter and log warnings.

- Give me all the warnings! Why you want the warnings - what can go wrong if you don't know about them, or if you ignore them.
- The history of the warnings module, PEP 230 and more.
- The warnings mechanism - how it works. Turning them on and off.
- The kinds of warnings
    - examples of system warnings.
    - deprecation warnings (if you learn nothing else, turn this on).
    - all about the bytes
    - py3k warnings.
    - How to generate your own warnings.
    - Other kinds of warnings.
- Controlling warnings with the environment variable.
- Changes to warnings in different versions (2.7, 3.2, 3.6, changes coming in 3.7)
- More advanced warnings control - filtering warnings, creating your own filters, formatting warnings, understanding the stack, testing that your warnings work, the context manager.
- Adding warnings into the logging framework.
- How warnings are used in conjunction with testing, logging, asserts and exceptions.

