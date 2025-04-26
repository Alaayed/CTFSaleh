### Functional Dependency

- Given attributes \( X \) and \( Y \), \( X -> Y \) means:  
  *for any two tuples, if they agree on \( X \), they must agree on \( Y \).*  
  We say **\( Y \) is functionally dependent on \( X \)**.

---

### Troublesome Functional Dependency

- A functional dependency \( X -> Y \) is considered **troublesome** when:
  - \( X -> Y \),
  - and **\( X \) is not a superkey**.
  
**Notes:**
- A **superkey** is a set of attributes that uniquely identifies a tuple.
- A **superkey** is a superset of a candidate key
- A **candidate key** is a *minimal* superkey (no extra attributes).
- If \( X \) is not a superkey, it's certainly not a candidate key either.

---
