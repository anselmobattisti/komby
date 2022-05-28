# komby

## The Problem

**Finding all the possible partitions of a list maintaining in the partition the order of the elements in 
the original list.**

## Usage

**Code:**

```Python
    import Komby

    data = [1, 2, 3]

    print("Number of possible partitions: {}.\n".format(Komby.total_partitions(data)))

    partitions = Komby.partitions(data, True)

    print("Partitions:")
    for p in partitions:
        print("\t - {}".format(p))

```

**Output:**

```
Number of possible partitions: 4.

Partitions:
	 - [[1, 2, 3]]
	 - [[1, 2], [3]]
	 - [[1], [2, 3]]
	 - [[1], [2], [3]]
```

## Install 

You can install Komby easily via pip:

```shell
pip install -U komby
```