---
layout: talk
recordingconsent: true
talkid: 44892
title: Privacy Preserving Record Linkage
track: security
type: talk

speakers:
- bio: " I lead a small engineering focused team at Data61 called \"Confidential Computing\"\
    . We work on privacy preserving solutions:\r\n- federated machine learning using\
    \ partially homomorphic encryption with N1 Analytics\r\n- anonymous linking with\
    \ various open source components\r\n\r\nExhaustion is better than boredom.\r\n"
  company: Data61
  name: Brian Thorne
  thumbnailUrl: brian-thorne.png
  twitter: thorneynz
  url: http://brian.thorne.link

abstract: Record linkage is essential for organizations to collaborate and carry out
  joint analysis. Instead of trusting someone with lots of personally identifiable
  information like name/address we can learn the entity matching in a privacy preserving
  way. Let's talk about a Python implementation of that!
---


Say a medical researcher is trying to get good numbers on a hospitals’ patients following up with pharmaceutical purchases, they would need to link the medical and pharmaceutical records. This can easily be done using a shared unique identifier for each patient but that identifier might be private – or it might expressly not be allowed to be used for linkage purposes. 

We could use the individuals personally identifiable information like name, address, phone, email etc but again is very private information – and doubly so when combined with the sensitive nature of the medical information.

Instead we can use privacy preserving linkage which only learns the mapping between two datasets without revealing the individual personally identifiable information.

I’ll detail how this "privacy preserving linkage" thing works. Highlighting a really novel application of the bloom filter data structure. Go through the edge computation aspect of getting the data provider to transform their data, then compute the similarity on locality sensitive hashes.

My team and I have spent a while creating a Python/C implementation of anonymous linking libraries – they are open sourced on github. We’ve also created a REST api for it (closed source but will eventually be open as well) and have scaled this entity matching server to work with real world datasets – in the order of millions of entities being matched. I deployed this to kubernetes and horizontally scale the main computation work across multiple nodes using celery.

I'll share how we went about validating this software with organizations even though we couldn't see the data being linked.

The technology that is part of the stack which will be mentioned throughout includes:
- Python 3.6 server side
- cffi
- Python 2/3 on Windows for command line client
- celery, flask
- other services we use: redis, postgres, minio
- docker-compose/kubernetes
