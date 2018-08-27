---
video_url: https://youtu.be/tIgu7q38bUw
layout: talk
recordingconsent: true
talkid: 45338
title: Asyncio in (Micro)Python
track: iot
type: talk

speakers:
- bio: ''
  company: ''
  name: Matt Trentini
  thumbnailUrl: matt-trentini.png
  twitter: matt_trentini
  url: ''

video_url: https://youtu.be/tIgu7q38bUw
abstract: 'Asyncio is cool in Python. It''s super cool in MicroPython!


  Asyncio provides a way to achieve concurrency in a relatively simplistic fashion.
  However, first-time users still struggle with the concepts so let''s sort them out!
  Then we''ll see why it''s especially useful in an embedded environment.'
---
[PEP492](https://www.python.org/dev/peps/pep-0492/) discusses "coroutines with async and await syntax" and it's been with us since Python 3.5. However it's proven to be challenging for users, especially those that are unfamiliar with the concept of coroutines. This talk will start by explaining the basic syntax - in pure Python - and benefits that this coding technique provides. We'll also take a look at some of the more interesting libraries that make use of aysncio.

After the basic features are established we will then delve into how these techniques are _particularly_ useful in an embedded environment. Remarkably, MicroPython provides asyncio functionality on even the smallest supported devices. Embedded environments are typically limited in what concurrent facilities they can offer - so having such powerful concurrent facilities is a tremendous boon to the embedded developer. We'll consider the 'old' way of doing things (event loops?!) and compare them to asyncio equivalents. Then we'll look at some of the common use cases they can be applied to, like debouncing or asynchronous fading of LED's, scrolling of displays or any number of tasks that need to execute while also handling user input.

Time willing, we'll wrap up with some of the more advanced topics such as synchronisation primitives, task cancellation and asynchronous-safe exception handling.

Asyncio provides a simple, predictable way to write concurrent Python code that is lightweight and powerful. Come along and learn how to take advantage of this fantastic feature!
