---
video_url: https://youtu.be/lmcgtUw5djw
layout: talk
recordingconsent: true
talkid: 42582
title: Describing Descriptors
track: general
type: talk

speakers:
- bio: "Full-stack Python/Django Developer.\r\nInterested in web security and clean\
    \ APIs.\r\nSydneysider.\r\nPassionate about inline hockey."
  company: ''
  name: Matthew Egan
  thumbnailUrl: matthew-egan.png
  twitter: NullMatthew
  url: https://mattjegan.com/

abstract: Descriptors are a little known feature of Python. They provide a way for
  a programmer to customize the storage and retrieval of different instance variables.
  In this talk, you will learn about the descriptor protocol, what it can be used
  for, and how to implement a descriptor.
---
Oftentimes beginner programmers go through traditional features when learning a language. For Python beginners this might involve variables, control structures like if-statements, while and for loops, dictionaries, and finally classes. However, if we read the Python documentation we find that another feature that can be used in Python is that of the descriptor protocol. Descriptors allow the programmer to override the storing and retrieving of different class instance variables such that special behaviours can be followed. For example, we might want some variable to follow some special validation. We could do this using `__setattr__` on the containing class but perhaps we want to reuse the validation in another class, or we want other validations for other variables and we don't want `__setattr__` to become a huge if/elif/else block. In this talk, I will walk attendees through what a descriptor is, what use cases they can use them in, how to implement a descriptor, and common descriptors in the Python ecosystem that users may or may not have identified as descriptors (often just referred to as *magic*).
