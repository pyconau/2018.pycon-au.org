---
layout: talk
recordingconsent: true
talkid: 44212
title: Becoming a Multilingual SuperHero in Django
track: django
type: talk

speakers:
- bio: "**Why do you want this person to speak?**\r\n\r\nSanyam is a self-taught programmer\
    \ with a \"can-do\" attitude who developed his interest in Computer Science and\
    \ Software Development over the years. He mostly goes by CuriousLearner all over\
    \ the web and you might run into him at various Python Conferences and local meetups.\
    \ In his free time he contributes to FOSS. Some of his noticeable contributions\
    \ are in Gecko Engine from Mozilla and CPython.\r\n\r\nYou can read about his\
    \ latest hacking CPython and other projects at http://www.SanyamKhurana.com/blog\
    \ & http://medium.com/@CuriousLearner\r\n\r\n*Highlights*:\r\n\r\n  - Goes by\
    \ CuriousLearner all over the web.\r\n  - Bug Triager and contributor to CPython\
    \ (bugs.python.org)\r\n  - GSoC 2018 Mentor for Debian\r\n  - RGSoC 2016 Mentor\r\
    \n  - Mozilla Reps Mentor and contributor to Mozilla's GeckoEngine, Add-ons ecosystem,\
    \ and other few projects.\r\n  - Core-organizer for PyCon India 2016 & PyCon India\
    \ 2017\r\n  - Volunteer for PyCon India 2015."
  company: ''
  name: Sanyam Khurana
  thumbnailUrl: sanyam-khurana.png
  twitter: ErSanyamKhurana
  url: http://www.SanyamKhurana.com/blog

abstract: 'In this talk, we''ll see how we make a language agnostic backend, to serve
  our app in different languages, based on what language the client wants to communicate
  in.


  We''ll see how to support translation for static data and dynamic data, using various
  third-party services.'
---
You have got this super awesome REST API served through Django/DRF based project and suddenly these requirements come in:

We need to have a local support for the Chinese language!

In case, you've not written your application with localization and internationalization in mind, then  "Boy! You're in danger! You should better start praying to almighty to give you strength and endurance to support yet another language in your app".

In this talk, we'll see how do we support localization and serve our app in different languages, based on what language the client wants to communicate in. As a backend, we should be language agnostic and allow all clients to communicate with us in one of the languages we support.

We'll see how to support translation for static data (using makemessages / compilemessages) and dynamic data, using various third-party services such as django-translations and transifex.

Here, static data is translations for all the fields, error messages etc. that the app already has and dynamic data is the custom data input by the user in the app.

This would enable you to have your admin panel, as well as RESTful APIs, served in different languages.

