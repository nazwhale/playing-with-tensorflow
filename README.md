# playing-with-tensorflow

### Aim

This is an exploratory repository with the aim of learning about the creation and optimisation of neural networks. I used the [MNIST](http://yann.lecun.com/exdb/mnist/) dataset of handwritten digits.  

### Experiences

Google's [introduction to Tensorflow](https://www.tensorflow.org/tutorials/) was fantastic, and I now feel like I have a grounding in the workings of a Neural Net, as well as some of the higher-level ways of optimising one. I'm also much more aware of the potential applications of Neural Nets, and more excited about deep learning in general. As a bonus I'm also much more comfortable with Python, a language which I hadn't previously used.

Unexpectedly, I learnt how to visualise the trained weights of my network. There are some very tiny, very interesting, 16x16 pixel images in the 'images' folder.

I also wrote a blog post on Medium about my experiences learning about Neural Nets. You can read it [here](https://medium.com/@nazwhale/neural-network-in-a-week-3ef84175191b).


### Networks
There are 2 neural nets in this repository:
- `MNIST_softmax_regression.py`
- `deep-convolutional-MNIST.py`

The former is a simple, one-layer network with an accuracy of around 91%.

The second is optimised, making use of 2 convolutional layers, ADAM gradient descent, and max-pooling. The accuracy is close to 98%.


### Installation

To run the neural networks you will need to have Tensorflow installed on your computer. You can do that by following the [installation instructions](https://www.tensorflow.org/install/) from Google.

```
$ git clone git@github.com:nazwhale/playing-with-tensorflow.git
$ cd playing-with-tensorflow
```
then, to run a network:
```
$ python MNIST_softmax_regression.py
or
$ python deep-convolutional-MNIST.py
```
