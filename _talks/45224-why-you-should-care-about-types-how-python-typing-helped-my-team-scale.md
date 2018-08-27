---
video_url: https://youtu.be/h1cD3a7ys8Q
layout: talk
recordingconsent: true
talkid: 45224
title: 'Why you should care about types: How Python typing helped my team scale'
track: general
type: talk

speakers:
- bio: | 
    Luka Steric is a Software Engineer at Facebook. He joined the London
    office in 2016 after receiving his Master’s Degree in Computer Science
    from the University of Zagreb (Croatia). During his time in university
    his focus was mainly on bioinformatics, especially next-gen DNA
    sequence assemblers. Before joining Facebook he interned at the Genome
    Institute of Singapore and at the International Monetary Fund in
    Washington DC. He is now part of the Dumont team and works on
    automated x-repo testing, scenario verification and product
    monitoring. He is also an Open Source contributor to various Python
    projects like Typeshed and Black.


  company: Facebook
  name: Luka Sterbic
  thumbnailUrl: luka-sterbic.png
  twitter: ''
  url: https://github.com/Sterbic

abstract: "By now you have probably all heard about Python static typing. But why\
  \ should you care? Are types in Python even Pythonic? Is Python turning into Java?\
  \ In this talk I\u2019ll try to answer these questions and explain how type annotations\
  \ helped my team scale 4x and make developers happier."
---
By now you have probably all heard about Python static typing. But why should you care? Are types in Python even Pythonic? Is Python turning into Java? Type annotations are Pythonic, trust Guido's word for it, and Python is definitely not turning into Java.

The greatest benefit of types in large Python codebases is the fact that the input and output structures of a function are obvious from just looking at the signature. In the untyped world the definition for the class you are looking for may be N jumps away, hidden somewhere deep in the codebase, and you don't have a direct reference to it. In the best possible case grepping for it will yield just a few results and you will be able to spot what you are looking for. In the worst case though, you will have hundreds of hits and you will have to start your application and inspect the type at runtime to figure out what is going on, which make the development cycle slow and tedious.

Come to this talk if you want to know more about the typing system in Python, how to gradually add it to your codebase and what benefits will your team get in the long run! I will also cover some advanced tools like the runtime type collection system, MonkeyType, and the just open sourced type checker, Pyre!
