---
layout: talk
recordingconsent: true
talkid: 45179
title: Resurrecting the dead with deep learning
track: general
type: talk

speakers:
- bio: I have recently finished my bachelors degree at SRM University, India. I have
    previously spent a semester studying at the Massachusetts Institute of Technology,
    interned at the MIT Media Lab, Carnegie Mellon University's Institute for Software
    Research and Wolfram Research. I have also started Next Tech Lab, a student-run
    research lab at my university, mentoring and leading over 200 members working
    in fields like AI, AR/VR, IoT etc.
  company: Next Tech Lab
  name: Aditthya Ramakrishnan
  thumbnailUrl: aditthya-ramakrishnan.png
  twitter: ad137hya
  url: https://www.linkedin.com/in/aditthya

abstract: We will use powerful techniques in deep learning to create language models
  and use them to generate literature in the style of Nietzsche; Rap in the style
  of Eminem & Compose music inspired by Mozart. The results are so remarkable that
  it's sometimes hard to tell generated text from the real thing.
---
Recently, results of projects like twitter.com/deepdrumpf and twitter.com/deeplearnbern have shown how neural networks can generate remarkable text by being trained on corpora of literature, MIDI files, tweets etc.

In this talk, we will dive deep into character-level modelling based on recurrent neural networks using Keras with a TensorFlow backend. We will build multi-layer LSTMs and train it over a corpus of text to generate remarkable results. We will cover basic theory of neural networks, backpropagation, RNN/LSTMs, dataset preparation and training. I will explain how the network models a probability distribution to generate text character by character and also discuss hyper-parameter tuning (especially Softmax temperature) to control the output.

People have used these techniques to - 
1) Generate literature in the style of dead writers and poets like Nietzsche, Shakespeare and Robert Frost.
2) Generate beautiful AI composed music inspired by the likes of Mozart, Beethoven and Bach. 
3) Generate lyrics and rap by training on Lennon-McCartney & Hamilton songs respectively.

Sometimes when given a prompt, these networks can also effectively hallucinate text that the author of the input corpus might have said when given the same prompt.

There will be live examples and a few more interesting uses of this technique.

Prior knowledge of linear algebra and a basic overview of machine learning is helpful but not necessary.

I will also provide a Github repo with the code from the talk and provide links to trained models of the live examples for attendees to experiment with and build upon.

