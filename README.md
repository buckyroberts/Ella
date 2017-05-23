![](http://i.imgur.com/4WG89Km.png)

## Introduction

Ella is a self-improving decision organism.

## Overview

This program is designed to iterate through a dataset and may choose to perform an action based on analysis of the data.
  
- **Condition** - expression to be evaluated 
- **Action** - function that will be invoked if the related _condition_ evaluates to true
- **Neuron** - pairing of an action to one or more conditions
- **Brain** - collection of all neurons

## Diagram of Basic Neuron

![](http://i.imgur.com/wzIT8Av.png)

## Example Usage

Ella works by first analyzing the dataset provided by the user:
```json
[
  {"date": "1/1/17", "price": 25.48, "volume": 5500},
  {"date": "1/2/17", "price": 19.64, "volume": 1600},
  {"date": "1/3/17", "price": 25.57, "volume": 4800},
  {"date": "1/4/17", "price": 32.63, "volume": 2100},
  {"date": "1/5/17", "price": 29.85, "volume": 3700}
]
```

She will then begin building the neurons by first generating random conditions based on the data.
```
volume > 3700
price < 19.64
```

Once conditions have been created, they are mapped to an action (creating the full neuron):
```
volume > 3700 - BUY
price < 19.64 - SELL
```

Ella will continue to create neurons until all actions have been mapped to a condition and the brain is complete. This
will ensure that the brain will have the ability to perform all possible functions.

Once full brain has been constructed, Ella will iterate over the dataset row by row and invoke all action events (fire
the neuron) if a condition is met. Therefore for each row analyzed, Ella may invoke multiple, a single, or no action 
events depending on how many conditions were met. 

Example using the above neurons and dataset:
```
Starting value:
$1000.00
 
Conditions:
volume > 3700 - BUY
price < 19.64 - SELL
 
---------- ANALYSIS ----------
 
Day 1 - {'price': 25.48, 'volume': 5500}
volume 5500 > 3700 -> BUY
 
Day 2 - {'price': 19.64, 'volume': 1600}
> NO ACTION
 
Day 3 - {'price': 25.57, 'volume': 4800}
volume 4800 > 3700 -> BUY
 
Day 4 - {'price': 32.63, 'volume': 2100}
> NO ACTION
 
Day 5 - {'price': 29.85, 'volume': 3700}
> NO ACTION
 
---------- RESULTS ----------
 
Final value:
$1008.65
```

## Developers

Feel free to contribute any by providing any bug fixes, suggestions, ideas, or anything else that may be of help.

Also, please note that this is just a small program I wrote this morning because I was bored waiting for the hockey game 
to start. It will most likely not be actively maintained, however I will check back frequently for pull requests and may
also add some new features in my spare time. 

- Python 3.6 (or newer) required

## Links

- [Support](https://www.patreon.com/thenewboston)
- [thenewboston.com](https://thenewboston.com/)
- [Facebook](https://www.facebook.com/TheNewBoston-464114846956315/)
- [Twitter](https://twitter.com/bucky_roberts)
- [Google+](https://plus.google.com/+BuckyRoberts)
- [reddit](https://www.reddit.com/r/thenewboston/)
