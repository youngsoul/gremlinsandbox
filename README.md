# Tinkerpop, Gremlin, Python Example

A sandbox repo of how to use Gremlin in Python against the Tinkerpop GraphDB.

This repo assume you are running a local gremlin-server and the modern initialized db:

```./bin/gremlin-server.sh conf/gremlin-server-modern.yaml```

This will create the *modern* pre-initialized db as documented in the [Getting Started](http://tinkerpop.apache.org/docs/current/tutorials/getting-started/)

## AWS Neptune

All of this work in to get familiar with *Gremlin* in anticipation for working on the AWS Cloud GraphDB called *Neptune*

[AWS Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/intro.html)

Running locally first, to learn how to interface Python, Gremlin is faster and cheaper than hitting Neptune immediately.

## Environment

I created this on MacOS and Python 3.6.1

## Instructions

- First run the gremlin server as shown above

- Second create a python virtualenv and install the requirements

- Third, run the simple_test.py file.

## Additional Reading

- https://www.datastax.com/dev/blog/a-gremlin-implementation-of-the-gremlin-traversal-machine
- https://kelvinlawrence.net/book/Gremlin-Graph-Guide.html
- https://github.com/nedlowe/gremlin-python-example
- http://tinkerpop.apache.org/docs/3.3.3/reference/#gremlin-python
- https://docs.aws.amazon.com/neptune/latest/userguide/intro.html