# Tinkerpop, Gremlin, Python Example

A sandbox repo of how to use Gremlin in Python against the Tinkerpop 3.3.3 GraphDB.

I hope you find the examples helpful.  See the Jupyter notebook for a collection of example and explanations.

This repo assume you are running a local gremlin-server and the modern initialized db:

```./bin/gremlin-server.sh conf/gremlin-server-modern.yaml```

This will create the *modern* pre-initialized db as documented in the [Getting Started](http://tinkerpop.apache.org/docs/current/tutorials/getting-started/)
## Apache Tinkerpop

[Tinkerpop](http://tinkerpop.apache.org)

Graph computing framework for both graph databases and graph analytic systems.

From
```
Apache TinkerPop™ is an open source, vendor-agnostic, graph computing
framework distributed under the commercial friendly Apache2 license.
 When a data system is TinkerPop-enabled, its users are able to model
 their domain as a graph and analyze that graph using the Gremlin
 graph traversal language.
```


## AWS Neptune

All of this work in to get familiar with *Gremlin* in anticipation for working on the AWS Cloud GraphDB called *Neptune*

```
Amazon Neptune supports popular graph models Property Graph and
W3C's RDF, and their respective query languages Apache TinkerPop Gremlin
and SPARQL, allowing you to easily build queries that efficiently
navigate highly connected datasets.
```

[AWS Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/intro.html)

Running locally first, to learn how to interface Python, Gremlin is faster and cheaper than hitting Neptune immediately.

## Environment

I created this on MacOS and Python 3.6.1, with Apache Tinkerpop 3.3.3

## Instructions

- First run the gremlin server as shown above

- Second create a python virtualenv and install the requirements

- Third, run the simple_test.py file.

## Additional Reading

- http://tinkerpop.apache.org/docs/current/tutorials/getting-started/
- https://www.datastax.com/dev/blog/a-gremlin-implementation-of-the-gremlin-traversal-machine
- https://kelvinlawrence.net/book/Gremlin-Graph-Guide.html
- https://github.com/nedlowe/gremlin-python-example
- http://tinkerpop.apache.org/docs/3.3.3/reference/#gremlin-python
- https://docs.aws.amazon.com/neptune/latest/userguide/intro.html