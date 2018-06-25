---
layout: talk
recordingconsent: true
talkid: 45062
title: 'Context Managers: You Can Write Your Own!'
track: general
type: talk

speakers:
- bio: Daniel is a Production Engineer at Facebook. He grew up in Townsville but moved
    to Melbourne for university. He is passionate about learning new Python features
    and teaching them to as many people as he can. He can't wait to live in an electric
    van with solar panels one day.
  company: ''
  name: Daniel Porteous
  thumbnailUrl: daniel-porteous.png
  twitter: banool1
  url: https://dport.me

abstract: Did you know context managers go beyond `with open('myfile.txt', 'r') as
  f`? In fact, you can even write your own! Context managers are an amazing tool for
  managing resources safely. They make your code look great, and they're now easier
  to write than ever thanks to contextlib! Come get contextual!
---
Many Python newcomers won't have seen a context manager other than `with open('myfile.txt', 'r') as f`, and might not even know that what they've been using all this time is a context manager. Context managers can be an extremely powerful tool and can save beginning programmers a lot of grief. 

During this talk we'll briefly discuss existing context managers, starting with the basics, like opening files. We'll 
then move on to more obscure examples such as those in the `threading` module or `contextlib.suppress`. After this we'll launch into writing our own context managers!

First we'll do it the hard way, with `__init__`, `__enter__`, and `__exit__` methods on a class. Then we'll see how easily it can be done with `contextlib.contextmanager` and `yield`. Once you see how easy it is you'll be kicking yourself for not using them more!

After this talk you should be inspired to use context managers to manage your own resources safely and make your code much prettier.
