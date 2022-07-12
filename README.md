# dotmotif-overloaded
An operator-overloading DSL for motif construction with [DotMotif](https://github.com/aplbrain/dotmotif)


```python
m = MotifCreator()

ab = m.A >> m.B         # A connects to B
m.A |= m.C              # A does not connect to C
ab['foo'] = 'bar'       # the AB edge has an attribute `foo` equal to `bar`
m.A['baz'] >= 4         # the A vertex has an attribute `baz` gteq to 4
```
