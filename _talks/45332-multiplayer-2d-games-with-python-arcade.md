---
layout: talk
recordingconsent: true
talkid: 45332
title: Multiplayer 2D games with Python Arcade
track: general
type: talk

speakers:
- bio: ''
  company: ''
  name: Caleb Hattingh
  thumbnailUrl: caleb-hattingh.png
  twitter: caleb_hattingh
  url: http://pythonomicon.com

abstract: The Python Arcade library makes it very easy to create 2D games--especially
  for beginners--and there are many examples provided with the package.  This talk
  will show how to make a multiplayer computer game using Python Arcade, both over
  a local network, and also on the internet.
---
Computer games are the MOST fun when people can play together!

The Python Arcade library makes it very easy to create 2D games--especially for beginners--and there are many examples provided with the package.  This talk will show how to make a multiplayer computer game using Python Arcade, both over a local network, and also on the internet. The goal is to provide the basic understanding of what building blocks are required, and how to get the "simplest possible thing" working.

The primary concept to understand in the Arcade game engine is the decoupling of the "world update" from the screen drawing. This will be explained first. Once that is done, we'll set up a simple game where a player can move their avatar around on the screen.  Then, we'll add a second avatar and make that be controlled by a "computer player".  

With that out of the way, we'll explain that the "computer player" could instead be controlled by another human player over a network.  At this point we'll create a basic socket connection and show how your player's coordinates can be sent over a socket connection.  From here, we'll generalize the socket communication and create an intermediate server that can receive multiple connections from different players.  In the server, we will use the asyncio library to allow many concurrent connections to be created.
