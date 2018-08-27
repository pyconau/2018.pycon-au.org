---
video_url: https://youtu.be/KBGNO-uzgVE
layout: talk
recordingconsent: true
talkid: 45261
title: 'All in the Timing: Side-Channel Attacks'
track: general
type: talk

speakers:
- bio: Philip is a Senior Apiarist with the BeeWare Project, an organizer for DjangoCon
    US, and the Co-Founder of Bay Bridge Python. He has spoken at over a dozen conferences
    worldwide, including multiple PyCons and DjangoCons. He works for Patreon in San
    Francisco.
  company: ''
  name: Philip James
  thumbnailUrl: philip-james.png
  twitter: phildini
  url: ''

abstract: "Here, you\u2019ll learn about a category of security issue known as side\
  \ channel attacks. You\u2019ll be amused to see how features like automatic data\
  \ compression, short-circuit execution, and deterministic hashing can be abused\
  \ to bypass security systems. No security background knowledge is required."
---

"Never write your own cryptography!" is an oft-heard cry in the computer security space. But why is that? In this talk, we'll cover some of the ways you can write software using algorithms and approaches that are mathematically perfect, but which, due to implementation artifacts, leave your applications exposed.

We'll start with the mother of all timing attacks, password forms and non-constant time, to give the audience a foundation on what timing attacks are. From there, we'll explore real-world attacks in the KeyCzar library, the BREACH attack, and PYTHONHASHSEED. All examples will show python code or pseudocode where appropriate, and will be abased on real-world attacks.

We'll finish with a discussion of Spectre, a recent class of side channel attack that required patches and reboots across the majority of computers on the web – including the complete reboot of many cloud providers.

Our hope is that the audience will come away with a clearer understanding of this corner of the world of computer security, and will have a better answer to "Why shouldn't I build my own cryptography software?"
