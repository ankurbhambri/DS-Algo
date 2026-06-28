## Eulerian Path = Aisa path jo graph ki har edge ko exactly ek baar visit kare.

- Edges ko ek hi baar traverse karna hai. 
- Vertices ko multiple times visit kar sakte ho.

#### Example:

```
A ----- B
|       |
|       |
D ----- C
```

Edges:

```
AB, BC, CD, DA
```

Ek Eulerian Path:

```
A → B → C → D → A
```

Yahan har edge exactly ek baar use hui.


## Eulerian Circuit = Agar path jahan se start hua wahi end bhi ho, to usse Eulerian Circuit (Cycle) kehte hain.

#### Example:

```
A → B → C → D → A

Start = End = A

```

## Eulerian Path kab exist karta hai? Undirected graph ke liye:

### Case 1: Eulerian Circuit:

- Graph connected ho (isolated vertices ignore karte hain)
- Sab vertices ki degree even ho

To Eulerian Circuit exist karta hai.

Example

```
A ---- B
|      |
|      |
D ---- C
```

Degree:

```
A = 2
B = 2
C = 2
D = 2
```

Sab even ⇒ Eulerian Circuit.

### Case 2: Eulerian Path (but not Circuit):

- Graph connected ho
- Exactly 2 vertices odd degree ki ho

To Eulerian Path exist karega.

Path odd vertex se start hoga aur doosre odd vertex par khatam.

#### Example:

```
A ---- B ---- C
```

Degrees

```
A = 1
B = 2
C = 1
```

Odd vertices:

```
A
C
```

Eulerian Path:

A → B → C

### Case 3: No Eulerian Path

- Agar odd degree vertices 2 se zyada hain
- To Eulerian Path possible nahi.

Example

```
    B
   /
A-C-D
```

Suppose degrees:

```
A = 1
B = 1
C = 3
D = 1
```

Odd vertices = 4

Here, Eulerian Path is impossible.

### Quick Rule

| Odd Degree Vertices | Result |
|---|---|
| 0 | Eulerian Circuit |
| 2 | Eulerian Path |
| >2 | Impossible |


### Eulerian Path vs Hamiltonian Path

| Eulerian | Hamiltonian |
|----------|-------------|
| Edge visit karni hoti hai | Vertex visit karna hota hai |
| Har edge exactly once | Har vertex exactly once |
| Vertex repeat ho sakta hai | Vertex repeat nahi ho sakta |
| Degree se existence check ho sakti hai | Simple rule nahi hai |


#### Example

Graph:

```
    1
   / \
  2---3
   \
    4
```

Degrees:

```
1 = 2
2 = 3
3 = 2
4 = 1
```
Odd vertices:

```
2, 4
```

Exactly 2 odd vertices ⇒ Eulerian Path exists, but Eulerian Circuit does not.