# Submask Enumeration

Sir yeh article **Bitmask DP ka sabse important trick** samjha raha hai:

> "Agar mere paas ek mask hai, toh uske saare subsets (submasks) efficiently kaise iterate karun?"

Normal way:

```python
for submask in range(1 << n):
    if (submask & mask) == submask:
        ...
```

Ye `O(2^n)` chalega.

CP-algorithms ek smarter trick batata hai:

```cpp
for (int s = mask; s; s = (s - 1) & mask)
{
    ...
}
```

Ye sirf actual submasks pe iterate karta hai. ([CP Algorithms][1])

---

## Example

Maan lo `mask = 10110`.

Iske submasks hain:

```text
10110
10100
10010
10000
00110
00100
00010
00000
```

Ab dekhte hain loop kya karta hai.

### Start

`s = 10110`

### Next

```text
s - 1

  10110
-     1
-------
  10101
```

Ab:

```text
10101 & 10110 = 10100
```

So next submask: `10100`.

### Next

```text
10100 - 1 = 10011
```

Ab:

```text
10011 & 10110 = 10010
```

So:

```text
10110
  ↓
10100
  ↓
10010
```

…and so on — saare submasks mil jayenge. ([CP Algorithms][1])

---

## Magic kya hai `(s - 1)` mein?

Ye sabse important part hai.

Aap jaante ho:

```text
10000 - 1 = 01111
10100 - 1 = 10011
```

Matlab:

1. rightmost set bit remove ho jata hai
2. uske right wale sab bits `1` ban jaate hain

Example: `10100`

```text
10100 - 1 = 10011
```

Ab problem: `10011` mein kuch bits aisi ho sakti hain jo original mask mein hi nahi thi.

Isliye `(s - 1) & mask` karte hain. Ye extra bits hata deta hai. ([CP Algorithms][1])

---

## Dry Run (small example)

Mask: `1101`

Start: `s = 1101`

### Iteration 1

Current: `1101`

```text
(1101 - 1) & 1101
= 1100 & 1101
= 1100
```

### Iteration 2

Current: `1100`

```text
(1100 - 1) & 1101
= 1011 & 1101
= 1001
```

### Iteration 3

Current: `1001`

```text
(1001 - 1) & 1101
= 1000 & 1101
= 1000
```

### Iteration 4

Current: `1000`

```text
(1000 - 1) & 1101
= 0111 & 1101
= 0101
```

### Final sequence

```text
1101
1100
1001
1000
0101
0100
0001
0000
```

Saare submasks aa gaye.

---

## Yeh DP mein kahan use hota hai?

Bahut baar:

```python
for mask in range(1 << n):
    sub = mask
    while sub:
        # sub is subset of mask
        sub = (sub - 1) & mask
```

Examples:

- Partition DP
- Merge DP
- State Compression DP
- SOS DP
- Minimum Incompatibility
- Parallel Courses II
- Beautiful Arrangement
- Traveling Salesman variations

---

## `O(3^n)` kyu hota hai?

Ye article ka second important point hai.

```python
for mask in range(1 << n):
    for sub in submasks(mask):
        ...
```

Total complexity: `O(3^n)`.

**Reason:** har bit ke 3 possibilities hain:

1. mask mein nahi hai
2. mask mein hai but submask mein nahi
3. mask aur submask dono mein hai

Har bit ke 3 choices, `n` bits:

```text
3 × 3 × 3 … n times = 3^n
```

Isliye total iterations: `O(3^n)`.
---