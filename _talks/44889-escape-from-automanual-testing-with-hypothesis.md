---
video_url: https://youtu.be/U_KhEi2vRT8
slides_url: https://github.com/Zac-HD/slides/blob/master/pyconau-2018-hypothesis.pdf
layout: talk
recordingconsent: true
talkid: 44889
title: Escape from auto-manual testing with Hypothesis!
track: general
type: talk

speakers:
- bio: "Hi!  I've been writing Python for around five years now, with a focus on open\
    \ source tools for fun and TB-scale data analysis on Australia's national supercomputer.\
    \  I started using Hypothesis in 2016 to test my scientific code, and joined the\
    \ project as a maintainer in early 2017.\r\n\r\nI currently work as a researcher\
    \ in the 3A Institute (3ainstitute.org) at the Australian National University\
    \ - studying autonomy, agency, and assurance in the context of data and artificial\
    \ intelligence.  I also offer consulting on software correctness in Python for\
    \ commercial and open source projects - especially around property-based testing,\
    \ continuous deployment, static analysis, and development process.\r\n\r\nOn weekends,\
    \ I enjoy reading, cooking, eating, and hiking, climbing, swimming, or just sleeping\
    \ - preferably far out of phone range!"
  company: 3A Institute, Australian National University
  name: Zac Hatfield-Dodds
  thumbnailUrl: zac-hatfielddodds.jpg
  twitter: ''
  url: ''

abstract: "Have you ever wanted someone else to write your test cases? There\u2019\
  s a library for that!\n\nYou declare a strategy for inputs - from \u2018an integer\u2019\
  \ to \u2018matching this regex\u2019 to \u2018Django model\u2019; Hypothesis finds\
  \ bugs and reports minimal failing examples. Too good to be true? Come see for yourself!"
---
If you’ve ever written some tests, or discovered that tested code can still have bugs, this talk - and Hypothesis - is for you. Hypothesis lets you write tests that should pass for every case… then finds bugs by generating inputs you wouldn’t have looked for. Even better, you get to save time by writing fewer (but more powerful) tests, so this process improves your productivity as well as your code!

* Write your first property-based test: example code and an overview of common tactics.
* Describing inputs: from using and composing strategies, to defining your own or inferring them from other code
* Use at scale: performance tips, debugging tools, and model checking an API
* Behind the curtain: a short overview of how Hypothesis finds minimal counter-examples

You’ll be ready to find real bugs by half way through this talk; and by the last slide you’ll be ready to use Hypothesis in ways we never imagined.  Finally, there will be dedicated Q&A - testing anything from web apps to big data pipelines, Hypothesis in other languages, or even how to get involved in the project (with mentoring!) - before leaving to drag the world kicking and screaming into a new and terrifying age of high quality software.
