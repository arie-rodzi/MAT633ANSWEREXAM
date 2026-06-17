questions = [
    {
        "question_no": "Question 1(a)",
        "topic": "Logic Foundations Assessment",
        "marks": "4",
        "question": """State whether each of the following statements is TRUE or FALSE.

i) Logic is the study of the principle of reasoning, which deals with either true or false structure of propositions.
ii) In classical logic, truth values of propositions are true and false.
iii) Logic formulas that produce true proposition regardless of the truth values of basic propositions participating in the formula are called tautologies.
iv) Fuzzy logic allows the true value of proposition to take any value in real numbers.""",
        "answer": """**ANSWER SCHEME:**
i) **TRUE** `[B1]`
ii) **FALSE** `[B1]`
iii) **TRUE** `[B1]`
iv) **FALSE** `[B1]`"""
    },
    {
        "question_no": "Question 1(b)",
        "topic": "Linguistic Variables and Values",
        "marks": "4",
        "question": """Give ONE example of linguistic variable and its THREE linguistic values.""",
        "answer": """**ANSWER SCHEME:**
* **Linguistic variable:** The speed of car `[1M]`
* **Linguistic values:** slow, medium, high `[3M]`
*(or any relevant examples)*"""
    },
    {
        "question_no": "Question 2(a)",
        "topic": "Membership Functions and Core Operators",
        "marks": "5",
        "question": """Let A, B, C and D be fuzzy sets. Determine the membership functions that correspond to the given fuzzy propositions by using the basic fuzzy intersection, basic fuzzy union, and basic fuzzy complement to represent the operator "and", "or", and "not", respectively.

i) (w is B and y is not C) or z is not D.
ii) (x is not A or w is not B) and (y is C and z is D).""",
        "answer": """**ANSWER SCHEME:**
* **i)** $=(\\mu_{B}(w)\\wedge\\mu_{\\overline{C}}(y))\\vee\\mu_{\\overline{D}}(z)$
  $=max\\{min(\\mu_{B}(w),1-\\mu_{c}(y)),1-\\mu_{D}(z)\\}$ `[M2, A1]`
* **ii)** $=(\\mu_{\\overline{A}}(x)\\vee\\mu_{\\overline{B}}(w))\\wedge(\\mu_{C}(y)\\wedge\\mu_{D}(z))$
  $=min\\{max(\\mu_{\\overline{A}}(x),\\mu_{\\overline{B}}(w)),min(\\mu_{C}(y),\\mu_{D}(z))\\}$
  $=min\\{max(1-\\mu_{A}(x),1-\\mu_{B}(w)),min(\\mu_{c}(y),\\mu_{D}(z))\\}$ `[M1, A1]`"""
    },
    {
        "question_no": "Question 2(b)",
        "topic": "Discrete Hedge Modifications",
        "marks": "10",
        "question": """Let Tasty and Cheap be two discrete fuzzy set that is defined on $X=\\{x_{1},x_{2},x_{3},x_{4}\\}$, where:
$$Tasty=\\frac{0.1}{x_{1}}+\\frac{0.9}{x_{2}}+\\frac{0.2}{x_{3}}+\\frac{0.4}{x_{4}}$$
$$\\text{Cheap} = \\frac{0.5}{x_{1}}+\\frac{0.3}{x_{2}}+\\frac{0.1}{x_{3}}+\\frac{0.7}{x_{4}}$$

Suppose the linguistic hedges "very" is represented by $\\mu_{very}(x)=\\mu(x)^{2}$. Using combination Algebraic Product $(t_{ap}(a,b)=ab)$ for the t-norm, basic fuzzy union, and basic fuzzy complement, determine the fuzzy sets for:
i) Not (very Tasty or Cheap).
ii) Very Tasty and Not Cheap.""",
        "answer": """**ANSWER SCHEME:**
* Pre-calculating core elements:
  $\\text{Very Tasty} = \\frac{0.01}{x_{1}}+\\frac{0.81}{x_{2}}+\\frac{0.04}{x_{3}}+\\frac{0.16}{x_{4}}$ `[M1]`
  $\\text{Not Cheap} = \\frac{0.5}{x_{1}}+\\frac{0.7}{x_{2}}+\\frac{0.9}{x_{3}}+\\frac{0.3}{x_{4}}$ `[M1]`

* **i) Not (very Tasty or Cheap):**
  $=1-(\\mu_{Very\\ Tasty\\ OR\\ Cheap}(x)) = 1-max(\\mu_{Very\\ Tasty}(x),\\mu_{Cheap}(x))$
  $=1-max\\left(\\frac{(0.01,0.5)}{x_{1}}+\\frac{(0.81,0.3)}{x_{2}}+\\frac{(0.04,0.1)}{x_{3}}+\\frac{(0.16,0.7)}{x_{4}}\\right)$
  $=1-\\left(\\frac{0.5}{x_{1}}+\\frac{0.81}{x_{2}}+\\frac{0.1}{x_{3}}+\\frac{0.7}{x_{4}}\\right) = \\frac{0.5}{x_{1}}+\\frac{0.19}{x_{2}}+\\frac{0.9}{x_{3}}+\\frac{0.3}{x_{4}}$ `[M2, A2]`

* **ii) Very Tasty and Not Cheap:**
  $=\\mu_{very\\ Tasty\\ AND\\ Not\\ Cheap}(x) = \\mu_{very\\ Tasty}(x)\\cdot(1-\\mu_{Cheap}(x))$
  $=\\left(\\frac{0.01}{x_{1}}+\\frac{0.81}{x_{2}}+\\frac{0.04}{x_{3}}+\\frac{0.16}{x_{4}}\\right) \\cdot \\left(\\frac{0.5}{x_{1}}+\\frac{0.7}{x_{2}}+\\frac{0.9}{x_{3}}+\\frac{0.3}{x_{4}}\\right)$
  $= \\frac{0.005}{x_{1}}+\\frac{0.567}{x_{2}}+\\frac{0.036}{x_{3}}+\\frac{0.048}{x_{4}}$ `[M2, A2]`"""
    },
 {
        "question_no": "Question 2(c)",
        "topic": "Custom Implication Operator Formulation",
        "question": r"""Let $P=\{p_1, p_2, p_3\}$ and $Q=\{q_1, q_2, q_3\}$ where these discrete sets are defined as:
$$P = \frac{0.1}{p_1} + \frac{0.8}{p_2} + \frac{0.3}{p_3}$$
$$Q = \frac{1}{q_1} + \frac{0.5}{q_2} + \frac{0.2}{q_3}$$

Derive the implication of "IF (p is P) THEN (q is Q)" using the following formula:
$$\mu_{\rightarrow}(x,y) = 1 - \min( \max(\mu_A(x), \mu_B(y)), \min(1 - \mu_A(x), \mu_B(y)) )$$""",
        "answer": r"""**ANSWER SCHEME:**

Evaluating the mapping matrix entry-by-entry using the given formulation:

| Row Element | $q_1$ ($\mu_Q = 1.0$) | $q_2$ ($\mu_Q = 0.5$) | $q_3$ ($\mu_Q = 0.2$) |
| :--- | :--- | :--- | :--- |
| **$p_1$ ($\mu_P = 0.1$)** | $1 - \min(1, 0.9) = 0.1$ | $1 - \min(0.5, 0.5) = 0.5$ | $1 - \min(0.2, 0.2) = 0.8$ |
| **$p_2$ ($\mu_P = 0.8$)** | $1 - \min(1, 0.2) = 0.8$ | $1 - \min(0.8, 0.2) = 0.8$ | $1 - \min(0.8, 0.2) = 0.8$ |
| **$p_3$ ($\mu_P = 0.3$)** | $1 - \min(1, 0.7) = 0.3$ | $1 - \min(0.5, 0.5) = 0.5$ | $1 - \min(0.3, 0.2) = 0.8$ |

---

### Deployed Fuzzy Relation Matrix Result:

$$\mu_{P\rightarrow Q}(p,q) = \begin{bmatrix} 0.1 & 0.5 & 0.8 \\ 0.8 & 0.8 & 0.8 \\ 0.3 & 0.5 & 0.8 \end{bmatrix}$$

*Alternative Algebraic Expression:*
$$\mu_{P\rightarrow Q}(p,q) = \frac{0.1}{p_1q_1} + \frac{0.8}{p_2q_1} + \frac{0.3}{p_3q_1} + \frac{0.5}{p_1q_2} + \frac{0.8}{p_2q_2} + \frac{0.5}{p_3q_2} + \frac{0.8}{p_1q_3} + \frac{0.8}{p_2q_3} + \frac{0.8}{p_3q_3}$$

`[M6, A4]`"""
    },
    {
        "question_no": "Question 3(a)",
        "topic": "Continuous Zadeh Implication Systems",
        "marks": "5",
        "question": """Suppose the fuzzy IF-THEN rule given by "IF the academic performance is excellent THEN the possibility of getting the job is high" where:
$$\\mu_{excellent}(x)=\\begin{cases}\\frac{x-6}{2} & ; 6\\le x\\le8 \\\\ 9-x & ; 8<x\\le9 \\\\ 0 & ; otherwise\\end{cases} \\quad \\text{and} \\quad \\mu_{high}(z)=\\begin{cases}0 & ; 0\\le z\\le0.5 \\\\ \\frac{z-0.5}{0.5} & ; 0.5\\le z\\le1\\end{cases}$$

Construct the fuzzy relation of the above rule using Zadeh implication $(\\mu_{Q_{Z}}(x,y)=max\\{min[\\mu_{FP_{1}}(x),\\mu_{FP_{2}}(y)],1-\\mu_{FP_{1}}(x)\\})$ for the implication.""",
        "answer": """**ANSWER SCHEME:**
Applying Zadeh combination formula systematically across ranges:
* **For $6 \\le x \\le 8, 0 \\le z \\le 0.5$:**
  $= max\\{min(\\frac{x-6}{2},0), 1 - \\frac{x-6}{2}\\} = max\\{0, \\frac{8-x}{2}\\} = \\frac{8-x}{2}$
* **For $6 \\le x \\le 8, 0.5 \\le z \\le 1$:**
  $= max\\{min(\\frac{x-6}{2},\\frac{z-0.5}{0.5}), \\frac{8-x}{2}\\}$
* **For $8 < x \\le 9, 0 \\le z \\le 0.5$:**
  $= max\\{min(9-x,0), 1-(9-x)\\} = max\\{0, x-8\\} = x-8$
* **For $8 < x \\le 9, 0.5 \\le z \\le 1$:**
  $= max\\{min(9-x,\\frac{z-0.5}{0.5}), x-8\\}$

$$\\mu_{excellent \\rightarrow high}(x,z)=\\begin{cases} \\frac{8-x}{2} & ; 6\\le x\\le8, 0 \\le z \\le 0.5 \\\\ max\\{min(\\frac{x-6}{2},\\frac{z-0.5}{0.5}), \\frac{8-x}{2}\\} & ; 6\\le x\\le8, 0.5 \\le z \\le 1 \\\\ x-8 & ; 8 < x\\le9, 0 \\le z \\le 0.5 \\\\ max\\{min(9-x,\\frac{z-0.5}{0.5}), x-8\\} & ; 8 < x\\le9, 0.5 \\le z \\le 1 \\\\ 1 & ; otherwise \\end{cases}$$ `[M3, A2]`"""
    },
    {
        "question_no": "Question 3(b)(i)",
        "topic": "Algebraic Mamdani Rule Compositions",
        "marks": "13",
        "question": """Let A, B and C be three fuzzy sets defined by the following membership functions:
$$\\mu_{A}(x)=\\mu_{A}(x:0,1,5,7), \\quad \\mu_{B}(y)=\\mu_{B}(y:0,6,10) \\quad \\text{and} \\quad \\mu_{c}(z)=\\mu_{c}(z:0,3,7)$$
where $x\\in[0,10]$, $y\\in[0,12]$ and $z\\in[0,10]$.

Given the IF-THEN rule "IF < x is A AND y is B > THEN < z is C >", obtain the membership function for the IF-THEN rule using the Algebraic Product; $(t_{ap}(a,b)=ab)$ and Mamdani Product Implication $(\\mu_{Q_{sP}}(x,y)=\\mu_{FP_{1}}(x)\\cdot\\mu_{FP_{2}}(y))$.""",
        "answer": """**ANSWER SCHEME:**
Piecewise definitions derived from core coordinate vectors:
$$\\mu_{A}(x)=\\begin{cases}x & ; 0\\le x\\le1 \\\\ 1 & ; 1\\le x\\le5 \\\\ \\frac{7-x}{2} & ; 5\\le x\\le7 \\\\ 0 & ; otherwise\\end{cases} \\quad \\mu_{B}(y)=\\begin{cases}\\frac{y}{6} & ; 0\\le y\\le6 \\\\ \\frac{10-y}{4} & ; 6\\le y\\le10 \\\\ 0 & ; otherwise\\end{cases} \\quad \\mu_{c}(z)=\\begin{cases}\\frac{z}{3} & ; 0\\le z\\le3 \\\\ \\frac{7-z}{4} & ; 3\\le z\\le7 \\\\ 0 & ; otherwise\\end{cases}$$

Intermediary step $A \\cap B$ via $t_{ap}(a,b) = a \\cdot b$:
* $0 \\le x \\le 1, 0 \\le y \\le 6 \\implies \\frac{xy}{6}$
* $0 \\le x \\le 1, 6 \\le y \\le 10 \\implies \\frac{10x-xy}{4}$
* $1 \\le x \\le 5, 0 \\le y \\le 6 \\implies \\frac{y}{6}$
* $1 \\le x \\le 5, 6 \\le y \\le 10 \\implies \\frac{10-y}{4}$
* $5 \\le x \\le 7, 0 \\le y \\le 6 \\implies \\frac{7y-xy}{12}$
* $5 \\le x \\le 7, 6 \\le y \\le 10 \\implies \\frac{(7-x)(10-y)}{8}$

Final mapping $\\mu_{A \\cap B \\rightarrow C}(x,y,z) = \\mu_{A \\cap B}(x,y) \\cdot \\mu_C(z)$:
* $\\frac{xyz}{18}$ ; $0 \\le x \\le 1, 0 \\le y \\le 6, 0 \\le z \\le 3$
* $\\frac{7xy-xyz}{24}$ ; $0 \\le x \\le 1, 0 \\le y \\le 6, 3 \\le z \\le 7$
* $\\frac{10xz-xyz}{12}$ ; $0 \\le x \\le 1, 6 \\le y \\le 10, 0 \\le z \\le 3$
* $\\frac{(10x-xy)(7-z)}{16}$ ; $0 \\le x \\le 1, 6 \\le y \\le 10, 3 \\le z \\le 7$
* $\\frac{yz}{18}$ ; $1 \\le x \\le 5, 0 \\le y \\le 6, 0 \\le z \\le 3$
* $\\frac{7y-yz}{24}$ ; $1 \\le x \\le 5, 0 \\le y \\le 6, 3 \\le z \\le 7$
* $\\frac{10z-yz}{12}$ ; $1 \\le x \\le 5, 6 \\le y \\le 10, 0 \\le z \\le 3$
* $\\frac{10-y}{4}$ ; $1 \\le x \\le 5, 6 \\le y \\le 10, 3 \\le z \\le 7$
* $\\frac{7yz-xyz}{36}$ ; $5 \\le x \\le 7, 0 \\le y \\le 6, 0 \\le z \\le 3$
* $\\frac{(7y-xy)(7-z)}{48}$ ; $5 \\le x \\le 7, 0 \\le y \\le 6, 3 \\le z \\le 7$
* $\\frac{(7-x)(10-y)z}{24}$ ; $5 \\le x \\le 7, 6 \\le y \\le 10, 0 \\le z \\le 3$
* $\\frac{(7-x)(10-y)(7-z)}{32}$ ; $5 \\le x \\le 7, 6 \\le y \\le 10, 3 \\le z \\le 7$
* $0$ ; otherwise `[M8, A3]`"""
    },
    {
        "question_no": "Question 3(b)(ii)",
        "topic": "Evaluating Continuous Relations",
        "marks": "2",
        "question": """Find the membership value of the implication if the input values are set $x=3$, $y=7$ and $z=2$.""",
        "answer": """**ANSWER SCHEME:**
Identify coordinates map into active region $1 \\le x \\le 5$, $6 \\le y \\le 10$, and $0 \\le z \\le 3$:
$$\\mu_{A\\cap B\\rightarrow C}(3,7,2)=\\frac{10z-yz}{12}=\\frac{10(2)-(7)(2)}{12}=\\frac{20-14}{12} = 0.5$$ `[M1, A1]`"""
    },
{
        "question_no": "Question 4(a)",
        "topic": "Dubois-Prade Dienes-Rescher Systems",
        "question": r"""Let $A=\{a_{1},a_{2}\}$, $B=\{b_{1},b_{2}\}$ and $C=\{c_{1},c_{2}\}$ where:
$$A=\frac{0.4}{a_{1}}+\frac{0.7}{a_{2}}, \quad B=\frac{0.9}{b_{1}}+\frac{0.2}{b_{2}} \quad \text{and} \quad C=\frac{0.7}{c_{1}}+\frac{0.4}{c_{2}}$$

Compute IF (a is A and b is B) THEN (c is not C) using the Dubois-Prade class $\left(t_{a}(a,b)=\frac{ab}{\max(a,b,\alpha)}\right)$ at $\alpha=1$ for t-norm, basic fuzzy complement for complement, and Dienes-Rescher implication $(\mu_{O_{D}}(x,y)=\max[1-\mu_{FP_{1}}(x),\mu_{FP_{2}}(y)])$ for the implication.""",
        "answer": r"""**ANSWER SCHEME:**

### Step 1: Intermediary t-norm intersections via Dubois-Prade class ($\alpha=1$)
* $a_1 b_1: \frac{0.4 \times 0.9}{\max(0.4, 0.9, 1)} = \frac{0.36}{1} = 0.36$
* $a_2 b_1: \frac{0.7 \times 0.9}{\max(0.7, 0.9, 1)} = \frac{0.63}{1} = 0.63$
* $a_1 b_2: \frac{0.4 \times 0.2}{\max(0.4, 0.2, 1)} = \frac{0.08}{1} = 0.08$
* $a_2 b_2: \frac{0.7 \times 0.2}{\max(0.7, 0.2, 1)} = \frac{0.14}{1} = 0.14$

**Resulting Antecedent Intersection Matrix ($A \cap B$):**

| Element | $b_1$ | $b_2$ |
| :--- | :---: | :---: |
| **$a_1$** | 0.36 | 0.08 |
| **$a_2$** | 0.63 | 0.14 |

---

### Step 2: Complement State Evaluation
$$\text{not } C = \frac{1-0.7}{c_1} + \frac{1-0.4}{c_2} = \frac{0.3}{c_1} + \frac{0.6}{c_2}$$

---

### Step 3: Implication Matrix Composition via $\max(1-\mu_{A\cap B}, \mu_{\overline{C}})$
* $a_1 b_1 \rightarrow c_1: \max(1-0.36, 0.3) = \max(0.64, 0.3) = 0.64$
* $a_1 b_1 \rightarrow c_2: \max(1-0.36, 0.6) = \max(0.64, 0.6) = 0.64$
* $a_2 b_1 \rightarrow c_1: \max(1-0.63, 0.3) = \max(0.37, 0.3) = 0.37$
* $a_2 b_1 \rightarrow c_2: \max(1-0.63, 0.6) = \max(0.37, 0.6) = 0.60$
* $a_1 b_2 \rightarrow c_1: \max(1-0.08, 0.3) = \max(0.92, 0.3) = 0.92$
* $a_1 b_2 \rightarrow c_2: \max(1-0.08, 0.6) = \max(0.92, 0.6) = 0.92$
* $a_2 b_2 \rightarrow c_1: \max(1-0.14, 0.3) = \max(0.86, 0.3) = 0.86$
* $a_2 b_2 \rightarrow c_2: \max(1-0.14, 0.6) = \max(0.86, 0.6) = 0.86$

---

### Deployed Comprehensive Solution System Matrix

| Antecedent Matrix ($x$) | Weight $\mu_{A \cap B}(x)$ | Relation Result $\mu_{\rightarrow}(x, c_1)$ | Relation Result $\mu_{\rightarrow}(x, c_2)$ |
| :--- | :---: | :---: | :---: |
| **$a_1b_1$** | 0.36 | **0.64** | **0.64** |
| **$a_2b_1$** | 0.63 | **0.37** | **0.60** |
| **$a_1b_2$** | 0.08 | **0.92** | **0.92** |
| **$a_2b_2$** | 0.14 | **0.86** | **0.86** |

`[M4, A2]`"""
    },
    {
        "question_no": "Question 4(b)",
        "topic": "Generalized Modus Ponens Composition Rules",
        "marks": "12",
        "question": """Derive a conclusion in the form of "c is not C" if given a statement "a is A' and b is B'" such that:
$$A'=\\frac{0.3}{a_{1}}+\\frac{0.6}{a_{2}} \\quad \\text{and} \\quad \\text{B'} = \\frac{0.7}{b_{1}}+\\frac{0.4}{b_{2}}$$""",
        "answer": """**ANSWER SCHEME:**
* Intermediary observation layer $A' \\cap B'$ using Dubois-Prade ($\\alpha=1$):
  * $a_1 b_1: \\frac{0.3 \\times 0.7}{max(0.3, 0.7, 1)} = 0.21$
  * $a_2 b_1: \\frac{0.6 \\times 0.7}{max(0.6, 0.7, 1)} = 0.42$
  * $a_1 b_2: \\frac{0.3 \\times 0.4}{max(0.3, 0.4, 1)} = 0.12$
  * $a_2 b_2: \\frac{0.6 \\times 0.4}{max(0.6, 0.4, 1)} = 0.24$
  $$A' \\cap B' = \\frac{0.21}{a_{1}b_{1}}+\\frac{0.42}{a_{2}b_{1}}+\\frac{0.12}{a_{1}b_{2}}+\\frac{0.24}{a_{2}b_{2}}$$

* Formulate conclusion using Compositional Rule of Inference via $C' = \\max_{a,b} [ \\min( \\mu_{A'\\cap B'}(a,b), \\mu_{(A\\cap B)\\rightarrow \\overline{C}}(a,b,c) ) ]$:
  * **For target element $c_1$:**
    * $a_1 b_1: min(0.21, 0.64) = 0.21$
    * $a_2 b_1: min(0.42, 0.37) = 0.37$
    * $a_1 b_2: min(0.12, 0.92) = 0.12$
    * $a_2 b_2: min(0.24, 0.86) = 0.24$
    $$\\mu_{C'}(c_1) = max(0.21, 0.37, 0.12, 0.24) = 0.37$$
  * **For target element $c_2$:**
    * $a_1 b_1: min(0.21, 0.64) = 0.21$
    * $a_2 b_1: min(0.42, 0.6) = 0.42$
    * $a_1 b_2: min(0.12, 0.92) = 0.12$
    * $a_2 b_2: min(0.24, 0.86) = 0.24$
    $$\\mu_{C'}(c_2) = max(0.21, 0.42, 0.12, 0.24) = 0.42$$

$$\\text{Final Derived Conclusion } C' = \\frac{0.37}{c_1} + \\frac{0.42}{c_2}$$ `[M4, A2]`"""
    }
]
