**0. Modulus Formula**
- (a % b) = a - (b * math.floor(a / b))

---

**1. Sum of First n Natural Numbers**  
- sum(i=1 to n) = n(n + 1) / 2

---

**2. Sum of Squares of First n Natural Numbers**  
- sum(i=1 to n) = n(n + 1)(2n + 1) / 6

---

**3. The total number of pairs in an array of size (n)**  
- (n(n-1))/2

---

**4. Sum of Cubes of First n Natural Numbers**
- sum(i=1 to n) = (n(n + 1)/2)^2

---

**5. Number of Pairs (i < j) in Array of Size n**  
- Total Pairs = n(n - 1) / 2

---

**6. Number of Subarrays in an Array of Length n**  
- Total Subarrays = n(n + 1) / 2

---

**7. Number of Substrings in a String of Length n**  
- Total Substrings = n(n + 1) / 2

---

**8. Power of 2 (for Bitmasking / Subsets)**  
- 2^k = 1 << k

---

**9. Modular Arithmetic (mod p, p is prime)**  
- Fermat’s Little Theorem:  
  [ a^(p - 1) ≡ 1 mod p ]
  → Modular Inverse:  
  [ a^(-1) ≡ a^(p - 2) mod p ]

---

**10. Sum of Geometric Progression (GP)**  
- [ a + ar + ar^2 + ... + ar^(n-1) = a * (r^n - 1) / (r - 1), r ≠ 1 ]

---

**11. Number of Digits in Base b**  
- [ digits = floor(log_b(n)) + 1 ]

---

**12. Bitmasking Shortcuts**
- (i & 1) → i % 2
- (i >> 1) → i // 2
- (1 << i) → 2^i

---

**Note**:  
- Formulas with `n(n + 1)/2` are triangular by nature. Useful in combinations, subarrays, and pairing logic.
