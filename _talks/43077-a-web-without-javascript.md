---
video_url: https://youtu.be/2XSeNQyPlTY
layout: talk
recordingconsent: true
talkid: 43077
title: A Web without JavaScript
track: general
type: talk

speakers:
- bio: Dr Russell Keith-Magee is a 12 year veteran of the Django core team, and for
    5 years, was President of the Django Software Foundation. He's also the founder
    of the BeeWare project, developing GUI tools to support the development of Python
    software. He lives in Perth, Western Australia with his wife, two children, and
    two animals that claim to be cats but have almost no feline properties.
  company: BeeWare Project
  name: Russell Keith-Magee
  thumbnailUrl: russell-keithmagee.png
  twitter: freakboy3742
  url: https://cecinestpasun.com

abstract: 'In the browser, you can use any programming language you want... as long
  as it''s JavaScript.


  But what if you want to use a different language? In this talk, you''ll learn how
  you can break out of the monolingual environment provided by the browser, and use
  Python (or any other language) instead.'
---
The world is filled with programming languages. There are object-oriented languages; there are functional languages; there are logical languages... the list goes on. Every language has strengths and weaknesses. Any moderately popular language will be popular because there is some problem domain where it's strengths provide a significant advantage. And for most of the history of computing, you were largely free to choose the programming language that was a good match for your specific problems.

Then came the web - an environment where only JavaScript was available. 20 years ago, when JavaScript was only being used to do minor animation effects, that wasn't really a problem. However, the demands of modern web design require moving more and more business logic into the browser.

What do you do if your business logic isn't a good match for JavaScript's capabilities, or if you have a significant body of existing business logic that is written in Python, not Javascript? Do you have to re-implement all your existing logic? Or are there ways to get your non-Javascript code running in the browser?

In this talk, you'll learn about a range of techniques that can be used to execute Python code in the browser, including some options that are starting to emerge from the browser standardization process. 

