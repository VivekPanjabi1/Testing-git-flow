# Regression Scenarios — ADSAT-16
## Validate division by zero handling in `calculate_ratio`

**Source:** Jira ticket ADSAT-16  
**Function under test:** `calculate_ratio(numerator, denominator)`

---

### Scenario 1 — Positive: valid division returns correct ratio

**Requirement (ADSAT-16):** For valid inputs, `calculate_ratio` must return numerator divided by denominator. Specifically, `calculate_ratio(10, 2)` returns `5`.

**Preconditions:**
- The `calculate_ratio` function is importable from the `calculator` module.
- The denominator is a non-zero integer.

**Steps:**
1. Call `calculate_ratio(10, 2)`.

**Expected result:**
- The return value equals `5`.

---

### Scenario 2 — Positive (parametrised): additional valid inputs return correct ratios

**Requirement (ADSAT-16):** For valid inputs, `calculate_ratio` must return numerator divided by denominator.

**Preconditions:**
- The denominator is non-zero.

**Steps:**
1. Call `calculate_ratio` with each of the following `(numerator, denominator, expected)` triples:
   - `(0, 5, 0)` — zero numerator
   - `(9, 3, 3)` — exact integer division
   - `(-10, 2, -5)` — negative numerator
   - `(10, -2, -5)` — negative denominator

**Expected result:**
- Each call returns the corresponding `expected` value.

---

### Scenario 3 — Negative: zero denominator raises `ValueError`

**Requirement (ADSAT-16):** `calculate_ratio(10, 0)` must raise `ValueError`.

**Preconditions:**
- The denominator is `0`.

**Steps:**
1. Call `calculate_ratio(10, 0)`.

**Expected result:**
- A `ValueError` is raised.

---

### Scenario 4 — Negative: `ValueError` message explains denominator cannot be zero

**Requirement (ADSAT-16):** The error message must explain that the denominator cannot be zero.

**Preconditions:**
- The denominator is `0`.

**Steps:**
1. Call `calculate_ratio(10, 0)` inside a `pytest.raises` context.
2. Inspect the string representation of the raised exception.

**Expected result:**
- The exception message contains wording that communicates the denominator cannot be zero (case-insensitive match on `"denominator"` and `"zero"`).

---

### Scenario 5 — Edge: zero denominator with zero numerator still raises `ValueError`

**Requirement (ADSAT-16):** The function must reject a denominator of zero regardless of the numerator value.

**Preconditions:**
- Both numerator and denominator are `0`.

**Steps:**
1. Call `calculate_ratio(0, 0)`.

**Expected result:**
- A `ValueError` is raised (the zero-denominator guard takes precedence).
