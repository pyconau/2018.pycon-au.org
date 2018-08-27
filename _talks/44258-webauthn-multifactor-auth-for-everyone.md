---
video_url: https://youtu.be/03sAfmCDjFg
layout: talk
recordingconsent: true
talkid: 44258
title: 'WebAuthn: Multi-factor Auth For Everyone'
track: security
type: talk

speakers:
- bio: "Hi, I'm Benno and I've done a few things.\r\n\r\nI've been a member of the\
    \ FreeBSD core team, I co-created Behave, I ported FreeBSD to the PowerPC and\
    \ I get far too interested in politics and especially elections.\r\n\r\nI currently\
    \ work at Yubico and have previously worked at iXsystems, Dell EMC and a bunch\
    \ of other places doing everything from FreeBSD kernel development to Python application\
    \ development to management and occasionally all three at once."
  company: Yubico
  name: Benno Rice
  thumbnailUrl: benno-rice.png
  twitter: jeamland
  url: ''

abstract: 'Everybody knows that passwords suck. Implementing better things, like multi-factor
  authentication, can be really tricky and require a bunch of specialist bits though.


  Or does it?


  The new WebAuthn standard makes it dead simple to add multi-factor authentication
  to your web app. Let''s find out how!'
---
The WebAuthn standard, now at Candidate Review stage at W3C, allows for great ease of accessing hardware security tokens, for example Yubikeys, from browsers. It also specifies everything that's needed in order to implement authentication workflows using these tokens.

This presentation will cover a brief history of multi-factor authentication and the issues it's had in adoption, then go into an overview of the WebAuthn spec and how it works and finally demonstrate how to integrate it into Django- and Flask-based web apps.
