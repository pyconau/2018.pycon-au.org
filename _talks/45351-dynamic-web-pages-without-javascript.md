---
layout: talk
recordingconsent: true
talkid: 45351
title: Dynamic web pages without Javascript
track: django
type: talk

speakers:
- bio: Tim has been using Django for nearly 10 years, and first used it in anger in
    a previous role as a system administrator. Since concentrating on development
    a few years ago, Tim has worked on a variety of Django projects for both the private
    and public sector. Tim has worked as a mentor at DjangoGirls, and loves to help
    people discover Python and Django.
  name: Tim Bell
  thumbnailUrl: tim-bell.png
  twitter: timb07
  url: https://github.com/timb07

abstract: Intercooler is a Javascript library that allows you to make dynamic web
  pages without writing any JS yourself. This talk demonstrates how to use Intercooler
  to add dynamic functionality to a Django app. It will also cover a number of apps
  that make using Intercooler with Django even easier.
---
Dynamic web pages can provide an excellent user experience; they update in response to user interaction without reloading whole pages from the server. Single Page Apps exploit this to the utmost.

However Single Page Apps usually require the app to be designed from the start around whichever libraries (both client-side and server-side) are being used. But for a new Django developer who's just finished a Django tutorial, it's hard to see how that kind of functionality can be achieved without throwing out Django's view and template system entirely.

[Intercooler](http://intercoolerjs.org/) provides a way to add dynamic functionality to web pages while still using simple Django views and templates. By using HTML attributes, many common types of dynamic interaction can be achieved with Intercooler without writing any Javascript at all. Building on the same technologies used to deliver non-dynamic web pages, Intercooler allows dynamic features to be added incrementally, and without the steep learning curve of many client-side UI libraries.

This talk covers using Intercooler to add dynamic functionality to a Django app, as well as a number of apps that make using Intercooler with Django even easier.
