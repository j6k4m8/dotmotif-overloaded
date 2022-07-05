# dotmotif-overloaded
An operator-overloading DSL for motif construction with [DotMotif](https://github.com/aplbrain/dotmotif)


```python
m = MotifCreator()

ab = m.A >> m.B
m.A |= m.C
ab['foo'] = 'bar'
m.A['baz'] = 'qux'
```
