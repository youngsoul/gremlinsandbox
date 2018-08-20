"""
http://tinkerpop.apache.org/docs/current/tutorials/getting-started/
http://tinkerpop.apache.org/docs/current/reference/#connecting-via-python

/Users/patryan/Development/apache/tinkerpop/apache-tinkerpop-gremlin-console-3.3.3
/Users/patryan/Development/apache/tinkerpop/apache-tinkerpop-gremlin-server-3.3.3
Start server like:
./bin/gremlin-server.sh conf/gremlin-server-modern.yaml

see the Getting started for the 'modern' default graph that is loaded.


https://www.datastax.com/dev/blog/a-gremlin-implementation-of-the-gremlin-traversal-machine

https://kelvinlawrence.net/book/Gremlin-Graph-Guide.html

https://github.com/nedlowe/gremlin-python-example
http://tinkerpop.apache.org/docs/3.3.3/reference/#gremlin-python



"""
from gremlin_python import statics
from gremlin_python.structure.graph import Graph
from gremlin_python.process.traversal import T, P, Operator, Order
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection

def vertex_to_json(vertex):
    # TODO - Almost certainly a better way of doing this
    values = vertex.valueMap(True).toList()[0]
    # values["id"] = vertex.id
    return values

# Establish a connection with Tinkerpop graph db
graph = Graph()
g = graph.traversal().withRemote(DriverRemoteConnection('ws://localhost:8182/gremlin','g'))

c = g.V().count().next()
print('\n')
print(f'Number of Vertices in graphdb: {c}')

# NOTE: g.V() always returns an iterable, even if its is just one
# These are 'shallow' versions of the Vertex references with id and label only
all_vertices = g.V()

# for each shallow Vertex, get the Vertex by id, and then get all of the properties of the Vertex
print('\n')
print("Print all verticies and their properties")
for x in all_vertices:
    print(f'V[id, label]: {x.id}, {x.label}')
    print(f'\t{vertex_to_json(g.V(x.id))}')


# get Vertex with id 1
vertex_1 = g.V(1)
print('\n')
print(type(vertex_1))

print('\n')
print("Print all values of Vertex with id=1")
print(vertex_1.valueMap(True).toList()[0])

#
print('\n')
print("How many people does marko know?")
print(g.V().has('name','marko').out('knows').count().next())

print('\n')
print("What are the names of the people that Marko knows?")
print("Using Marko node, out-going edge 'knows', in to the Vertices, get the name property ans list")
print(g.V(1).outE('knows').inV().values('name').toList())

print('\n')
print("Same as above with a slightly different syntax")
print(g.V(1).out('knows').values('name').toList())

print('\n')
print("Who does Marko know that is older than 30")
print(g.V(1).out('knows').has('age', P.gt(30)).values('name').toList())

print('\n')
print("list the people that are older than 30 from olders to youngest")
print(g.V().hasLabel('person').has('age',P.gt(30)).order().by('age',Order.decr).values('name').toList())

# By importing the statics of Gremlin-Python, the class prefixes can be omitted.
# for example P.gt because gt and Order.decr becomes decr, but the IDE has no idea and flags
# them as an error - but it will execute.
statics.load_statics(globals())


print('\n')
print("Same as above but after loading static globals for better syntax")
print(g.V().hasLabel('person').has('age',gt(30)).order().by('age',decr).values('name').toList())

print('\n')
print("What is the average age of the friends of the people who created LinkedProcess?")
print(g.V().has('name','lop').in_('created').out('knows').dedup().age.mean().next())

print('\n')
print("Rank all people by how central they are in the knows-subgraph.")
print(g.V().hasLabel('person').repeat(both('knows')).times(5).groupCount().by('name').next())
