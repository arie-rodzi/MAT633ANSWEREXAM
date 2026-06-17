questions = [
    {
        "question_no": "Question 1(a)",
        "topic": "Axiomatic Logic Assortments",
        "question": r"""Determine whether each of the following statements is TRUE or FALSE:

* Linguistic variables can have values that are expressed as words from natural languages.
* A compound fuzzy proposition is a statement which can be described as "$x$ is $A$".
* The atomic fuzzy proposition must be considered as a fuzzy relation.
* Fuzzy logic provides a foundation for approximate reasoning with imprecise propositions using fuzzy set theory as the principal tool.""",
        "answer": r"""**SUGGESTED ANSWER:**

* Linguistic variables can have values that are expressed as words from natural languages. **TRUE**
* A compound fuzzy proposition is a statement which can be described as "$x$ is $A$". **FALSE** *(Note: This describes an atomic proposition)*
* The atomic fuzzy proposition must be considered as a fuzzy relation. **FALSE**
* Fuzzy logic provides a foundation for approximate reasoning with imprecise propositions using fuzzy set theory as the principal tool. **TRUE**"""
    },
  {
        "question_no": "Question 1(b)",
        "topic": "Structural Propositional Taxonomy",
        "marks": "4",
        "question": r"""Briefly explain the General Hypothetical Syllogism in fuzzy logic. Then give ONE (1) example of the proposition in fuzzy logic.""",
        "answer": r"""**SUGGESTED ANSWER:**

**Explanation:**
Given a fuzzy relation $A \rightarrow B$ in universe $U \times V$ (representing the premise: "IF $x$ is $A$ THEN $y$ is $B$") and a fuzzy relation $B \rightarrow C$ in universe $V \times W$ (representing the premise: "IF $y$ is $B$ THEN $z$ is $C$"), the General Hypothetical Syllogism derives a fuzzy relation $A \rightarrow C$ in universe $U \times W$ representing the valid conclusion: "IF $x$ is $A$ THEN $z$ is $C$".

**Symbolic Framework:**
$$\begin{aligned}
\text{PREMISE 1:} & \quad \text{IF } X \text{ is } A \text{ \text{THEN} } Y \text{ is } B \\\\
\text{PREMISE 2:} & \quad \text{IF } Y \text{ is } B \text{ \text{THEN} } Z \text{ is } C \\\\ \hline
\text{CONCLUSION:} & \quad \text{IF } X \text{ is } A \text{ \text{THEN} } Z \text{ is } C
\end{aligned}$$

**Demonstrative Example:**
* **Premise 1:** IF today is **Cloudy**, THEN the room temperature is **Cool**.
* **Premise 2:** IF the room temperature is **Cool**, THEN the air conditioner usage is **Low**.
* **Conclusion:** IF today is **Cloudy**, THEN the air conditioner usage is **Low**."""
    },
    {
        "question_no": "Question 2(a)",
        "topic": "Syntactic Logical Composition Combinations",
        "question": r"""Let $A$, $B$, and $C$ be fuzzy sets. Determine the membership function for the following fuzzy proposition where "and", "or", and "not" are defined by the basic fuzzy operations:

$$\text{"Not } (a \text{ is } A \text{ or } b \text{ is } B) \text{ and } (a \text{ is not } A \text{ or } c \text{ is } C)\text{"}$$""",
        "answer": r"""**SUGGESTED ANSWER:**

Using standard operators where intersection uses minimum, union uses maximum, and complement uses standard negation:

$$\begin{aligned}
\mu_{(A \lor B)' \land (A' \lor C)}(a,b,c) &= \min\left[ \mu_{(A \lor B)'}(a,b), \, \mu_{A' \lor C}(a,c) \right] \\\\
&= \min\left[ 1 - \max(\mu_A(a), \mu_B(b)), \, \max(1 - \mu_A(a), \mu_C(c)) \right]
\end{aligned}$$"""
    },
    {
        "question_no": "Question 2(b)(i)",
        "topic": "Algebraic Sum Hedge Applications",
        "question": r"""Let $A$ and $B$ be discrete fuzzy sets defined on $X = \{x_1, x_2, x_3, x_4\}$, where:
$$A = \frac{0.4}{x_1} + \frac{0.7}{x_2} + \frac{0.3}{x_3} + \frac{0.8}{x_4} \quad \text{and} \quad B = \frac{0.4}{x_1} + \frac{0.7}{x_2} + \frac{0.3}{x_3} + \frac{0.5}{x_4}$$

Suppose the linguistic hedges "very", "somewhat", and "not" are represented by $\mu_{\text{very}}(x) = (\mu(x))^2$, $\mu_{\text{somewhat}}(x) = \sqrt{\mu(x)}$, and $\mu_{\text{not}}(x) = 1 - \mu(x)$. 

Using the combination of the Algebraic Product $t_{\text{AP}}(a, b) = ab$ for the $t$-norm, basic fuzzy union, and basic fuzzy complement, determine the fuzzy set for: **Very $A$ and somewhat $B$**.""",
        "answer": r"""**SUGGESTED ANSWER:**

* **Step 1: Compute individual components**
  * $\mu_{\text{very } A}(x) = (\mu_A(x))^2 = [0.16, 0.49, 0.09, 0.64]$
  * $\mu_{\text{somewhat } B}(x) = \sqrt{\mu_B(x)} = [0.6325, 0.8367, 0.5477, 0.7071]$

* **Step 2: Apply the Algebraic Product t-norm ($a \cdot b$) entry-wise**
  * $x_1: 0.16 \times 0.6325 = 0.1008$
  * $x_2: 0.49 \times 0.8367 = 0.4116$
  * $x_3: 0.09 \times 0.5477 = 0.0495$
  * $x_4: 0.64 \times 0.7071 = 0.4544$

**Final Resulting Set:**
$$\text{Very } A \text{ and somewhat } B = \frac{0.1008}{x_1} + \frac{0.4116}{x_2} + \frac{0.0495}{x_3} + \frac{0.4544}{x_4}$$"""
    },
    {
        "question_no": "Question 2(b)(ii)",
        "topic": "Algebraic Sum Hedge Applications",
        "question": r"""Using the same definitions provided in Question 2(b)(i), determine the fuzzy set for: **Somewhat not $A$ or not somewhat $B$**.""",
        "answer": r"""**SUGGESTED ANSWER:**

* **Step 1: Compute individual components**
  * $\mu_{\text{not } A}(x) = 1 - \mu_A(x) = [0.6, 0.3, 0.7, 0.2]$
  * $\mu_{\text{somewhat not } A}(x) = \sqrt{1 - \mu_A(x)} = [0.7746, 0.5477, 0.8367, 0.4472]$
  * $\mu_{\text{not somewhat } B}(x) = 1 - \sqrt{\mu_B(x)} = [0.3675, 0.1633, 0.4523, 0.2929]$

* **Step 2: Apply the standard fuzzy union s-norm (maximum) entry-wise**
  * $x_1: \max(0.7746, 0.3675) = 0.7746$
  * $x_2: \max(0.5477, 0.1633) = 0.5477$
  * $x_3: \max(0.8367, 0.4523) = 0.8367$
  * $x_4: \max(0.4472, 0.2929) = 0.4472$

**Final Resulting Set:**
$$\text{Somewhat not } A \text{ or not somewhat } B = \frac{0.7746}{x_1} + \frac{0.5477}{x_2} + \frac{0.8367}{x_3} + \frac{0.4472}{x_4}$$"""
    },
    {
        "question_no": "Question 2(c)",
        "topic": "Yager-Lukasiewicz Matrix Projections",
        "question": r"""Let $X = \{x_1, x_2, x_3\}$ and $Y = \{y_1, y_2, y_3\}$ be discrete fuzzy sets where:
$$X = \frac{0.3}{x_1} + \frac{0.7}{x_2} \quad \text{and} \quad Y = \frac{0.9}{y_1} + \frac{1}{y_2} + \frac{0.2}{y_3}$$

Using the Sugeno Class $C_{\lambda} = \frac{1-a}{1+\lambda a}$ with $\lambda = 2$ for the fuzzy complement, and the Gödel Implication:
$$\mu_{Q_G}(x, y) = \begin{cases} 1 & \text{if } \mu_{FP_1}(x) \le \mu_{FP_2}(y) \\\\ \mu_{FP_2}(y) & \text{otherwise} \end{cases}$$

obtain the membership function matrix for the fuzzy IF-THEN rule: $\text{IF } \langle x \text{ is not } X \rangle \text{ THEN } \langle y \text{ is } Y \rangle$.""",
        "answer": r"""**SUGGESTED ANSWER:**

* **Step 1: Compute the Sugeno Complement of $X$ ($\lambda = 2$)**
  * $\mu_{\tilde{X}}(x_1) = \frac{1 - 0.3}{1 + 2(0.3)} = \frac{0.7}{1.6} = 0.4375$
  * $\mu_{\tilde{X}}(x_2) = \frac{1 - 0.7}{1 + 2(0.7)} = \frac{0.3}{2.4} = 0.125$
  
  $$\tilde{X} = \frac{0.4375}{x_1} + \frac{0.125}{x_2}$$

* **Step 2: Generate Relation Matrix via Gödel Implication**
  Comparing antecedent vector $[0.4375, 0.125]$ against consequent vector $[0.9, 1.0, 0.2]$:

| Antecedent / Consequent | $y_1 \, (0.9)$ | $y_2 \, (1.0)$ | $y_3 \, (0.2)$ |
| :--- | :---: | :---: | :---: |
| **$x_1 \, (0.4375)$** | $1.0$ | $1.0$ | $0.2$ |
| **$x_2 \, (0.125)$** | $1.0$ | $1.0$ | $1.0$ |

**Final Analytical Form:**
$$\mu_{\tilde{X} \to Y}(x,y) = \frac{1}{(x_1,y_1)} + \frac{1}{(x_1,y_2)} + \frac{0.2}{(x_1,y_3)} + \frac{1}{(x_2,y_1)} + \frac{1}{(x_2,y_2)} + \frac{1}{(x_2,y_3)}$$"""
    },
    {
        "question_no": "Question 3(a)",
        "topic": "Generalized Modus Ponens Deductions",
        "question": r"""Suppose $C$ and $D$ are discrete fuzzy sets defined on $C = \{c_1, c_2\}$ and $D = \{d_1, d_2, d_3\}$, respectively. Let the fuzzy implication relation $C \to D$ be configured as follows:
$$C \to D = \frac{0.4}{(c_1,d_1)} + \frac{0.3}{(c_1,d_2)} + \frac{0.2}{(c_1,d_3)} + \frac{0.5}{(c_2,d_1)} + \frac{1}{(c_2,d_2)} + \frac{0.35}{(c_2,d_3)}$$

Given an observed statement "$d$ is $\tilde{D}$" where $\tilde{D} = \frac{0.13}{d_1} + \frac{0.33}{d_3}$, derive the conclusion "$c$ is $\tilde{C}$" using the Generalized Modus Tollens framework.""",
        "answer": r"""**SUGGESTED ANSWER:**

Using the compositional rule of inference for Generalized Modus Tollens:
$$\mu_{\tilde{C}}(c) = \max_{d \in D} \left[ \min\left(\mu_{C \to D}(c, d), \, \mu_{\tilde{D}}(d)\right) \right]$$

We evaluate the composition matching with the observation vector $\tilde{D} = [0.13, 0, 0.33]$:
* **For element $c_1$:**
  $$\max\left(\min(0.4, 0.13), \min(0.3, 0), \min(0.2, 0.33)\right) = \max(0.13, 0, 0.2) = 0.2$$
* **For element $c_2$:**
  $$\max\left(\min(0.5, 0.13), \min(1, 0), \min(0.35, 0.33)\right) = \max(0.13, 0, 0.33) = 0.33$$

**Derived Conclusion Set:**
$$\tilde{C} = \frac{0.2}{c_1} + \frac{0.33}{c_2}$$"""
    },
    {
        "question_no": "Question 3(b)",
        "topic": "Mamdani Relational Profile Synthesis",
        "question": r"""Let fuzzy sets 'strong' and 'stable' be defined on continuous universes $x \in [0,100]$ and $y \in [0,10]$ respectively, where:
$$\mu_{\text{strong}}(x) = \begin{cases} \frac{x}{70} & 0 \le x \le 70 \\\\ 1 & 70 \le x \le 100 \end{cases} \quad \text{and} \quad \mu_{\text{stable}}(y) = \begin{cases} \frac{y}{5} & 0 \le y \le 5 \\\\ 1 & 5 \le y \le 10 \end{cases}$$

Using the Dienes-Rescher implication $\mu_{Q_D}(x, y) = \max(1 - \mu_{\text{FP}_1}(x), \mu_{\text{FP}_2}(y))$, construct the structural fuzzy relation of the following linguistic rule: **"IF the economy is very strong, THEN the Ringgit is stable"**.""",
        "answer": r"""**SUGGESTED ANSWER:**

* **Step 1: Compute the modified antecedent "very strong"**
  $$\mu_{\text{very strong}}(x) = (\mu_{\text{strong}}(x))^2 = \begin{cases} \frac{x^2}{4900} & 0 \le x \le 70 \\\\ 1 & 70 \le x \le 100 \end{cases}$$

* **Step 2: Construct the Dienes-Rescher relation profile via piecewise synthesis**
  $$\mu_{\text{very strong} \to \text{stable}}(x, y) = \max(1 - \mu_{\text{very strong}}(x), \, \mu_{\text{stable}}(y))$$
  
  Evaluating across cross-product continuous boundary segments yields:
  $$\mu_{\text{very strong} \to \text{stable}}(x, y) = \begin{cases} 
  \max\left(1 - \frac{x^2}{4900}, \frac{y}{5}\right) & 0 \le x \le 70, \; 0 \le y \le 5 \\\\ 
  1 & 0 \le x \le 100, \; 5 \le y \le 10 \\\\ 
  \frac{y}{5} & 70 \le x \le 100, \; 0 \le y \le 5 \\\\ 
  0 & \text{otherwise} 
  \end{cases}$$"""
    },
    {
        "question_no": "Question 3(c)",
        "topic": "Reichenbach Rule-Based Modeling",
        "question": r"""Let $A$, $B$, and $C$ be continuous fuzzy sets defined on $x \in [0,8]$, $y \in [0,10]$, and $z \in [0,10]$ respectively, where:
$$\mu_A(x) = \begin{cases} \frac{x}{3} & 0 \le x \le 3 \\\\ 1 & 3 \le x \le 5 \\\\ \frac{8-x}{3} & 5 \le x \le 8 \end{cases} \quad \mu_B(y) = \begin{cases} \frac{y}{5} & 0 \le y \le 5 \\\\ \frac{10-y}{5} & 5 \le y \le 10 \end{cases}$$
$$\text{and} \quad \mu_C(z) = \begin{cases} \frac{z-3}{5} & 3 \le z \le 8 \\\\ \frac{10-z}{2} & 8 \le z \le 10 \\\\ 0 & \text{otherwise} \end{cases}$$

Obtain the comprehensive system membership function for the complex rule **"IF $\langle x \text{ is } A \text{ or } y \text{ is } B \rangle$ THEN $\langle z \text{ is } C \rangle$**", using the Yager Class $s_w(a, b) = \min(1, (a^w + b^w)^{1/w})$ where $w = 1$ for the s-norm, and the Mamdani Min implication $\mu_{Q_{\text{MM}}}(x, y) = \min(\mu_{\text{FP}_1}(x), \mu_{\text{FP}_2}(y))$ for the operational logical link.""",
        "answer": r"""**SUGGESTED ANSWER:**

* **Step 1: Determine the compound antecedent ($A \cup B$) via Yager s-norm ($w=1$)**
  When $w=1$, the expression yields the bounded sum operator: $\min(1, \mu_A(x) + \mu_B(y))$.
  $$\mu_{A \cup B}(x, y) = \begin{cases} 
  \frac{5x+3y}{15} & 0 \le x \le 3, \; 0 \le y \le 5 \\\\ 
  \frac{5x-3y+30}{15} & 0 \le x \le 3, \; 5 \le y \le 10 \\\\ 
  1 & 3 \le x \le 5, \; 0 \le y \le 10 \\\\ 
  \frac{40-5x+3y}{15} & 5 \le x \le 8, \; 0 \le y \le 5 \\\\ 
  \frac{70-5x-3y}{15} & 5 \le x \le 8, \; 5 \le y \le 10 
  \end{cases}$$

* **Step 2: Embed using the Mamdani Min Implication Rule**
  $\mu_{R}(x,y,z) = \min[\mu_{A \cup B}(x,y), \, \mu_C(z)]$
  
  $$\mu_{A \cup B \to C}(x, y, z) = \begin{cases} 
  \min\left(\frac{5x+3y}{15}, \frac{z-3}{5}\right) & 0 \le x \le 3, \; 0 \le y \le 5, \; 3 \le z \le 8 \\\\ 
  \min\left(\frac{5x+3y}{15}, \frac{10-z}{2}\right) & 0 \le x \le 3, \; 0 \le y \le 5, \; 8 \le z \le 10 \\\\ 
  \min\left(\frac{5x-3y+30}{15}, \frac{z-3}{5}\right) & 0 \le x \le 3, \; 5 \le y \le 10, \; 3 \le z \le 8 \\\\ 
  \min\left(\frac{5x-3y+30}{15}, \frac{10-z}{2}\right) & 0 \le x \le 3, \; 5 \le y \le 10, \; 8 \le z \le 10 \\\\ 
  \frac{z-3}{5} & 3 \le x \le 5, \; 0 \le y \le 10, \; 3 \le z \le 8 \\\\ 
  \frac{10-z}{2} & 3 \le x \le 5, \; 0 \le y \le 10, \; 8 \le z \le 10 \\\\ 
  \min\left(\frac{40-5x+3y}{15}, \frac{z-3}{5}\right) & 5 \le x \le 8, \; 0 \le y \le 5, \; 3 \le z \le 8 \\\\ 
  \min\left(\frac{40-5x+3y}{15}, \frac{10-z}{2}\right) & 5 \le x \le 8, \; 0 \le y \le 5, \; 8 \le z \le 10 \\\\ 
  \min\left(\frac{70-5x-3y}{15}, \frac{z-3}{5}\right) & 5 \le x \le 8, \; 5 \le y \le 10, \; 3 \le z \le 8 \\\\ 
  \min\left(\frac{70-5x-3y}{15}, \frac{10-z}{2}\right) & 5 \le x \le 8, \; 5 \le y \le 10, \; 8 \le z \le 10 \\\\
  0 & \text{otherwise}
  \end{cases}$$"""
    },
    {
        "question_no": "Question 4",
        "topic": "Einstein-Dienes Tensor Construction",
        "question": r"""Let $A = \{a_1, a_2\}$, $B = \{b_1, b_2\}$, and $C = \{c_1, c_2\}$ be three discrete fuzzy sets where:
$$A = \frac{0.3}{a_1} + \frac{0.5}{a_2}, \quad B = \frac{0.2}{b_1} + \frac{0.7}{b_2}, \quad \text{and} \quad C = \frac{0.4}{c_1} + \frac{0.6}{c_2}$$

Compute the full system output relation for the rule: $\text{IF } \langle a \text{ is } A \text{ and } b \text{ is } B \rangle \text{ THEN } \langle c \text{ is } C \rangle$ using the Dubois-Prade class $t_{\alpha}(a, b) = \frac{ab}{\max(a, b, \alpha)}$ at parameter constraint $\alpha = 1$ for the $t$-norm step, and the Zadeh implication mapping rule $\mu_{Q_Z}(x, y) = \max(\min(\mu_{\text{FP}_1}(x), \mu_{\text{FP}_2}(y)), 1 - \mu_{\text{FP}_1}(x))$ for generating the implication matrix.""",
        "answer": r"""**SUGGESTED ANSWER:**

* **Step 1: Compute Antecedent Intersection ($A \cap B$)**
  Using Dubois-Prade ($t_{\alpha=1}(a, b) = \frac{ab}{\max(a,b,1)} = ab$), which simplifies directly to the algebraic product format:
  * $(a_1, b_1) = 0.3 \times 0.2 = 0.06$
  * $(a_1, b_2) = 0.3 \times 0.7 = 0.21$
  * $(a_2, b_1) = 0.5 \times 0.2 = 0.10$
  * $(a_2, b_2) = 0.5 \times 0.7 = 0.35$
  
  $$A \cap B = \frac{0.06}{a_1b_1} + \frac{0.21}{a_1b_2} + \frac{0.1}{a_2b_1} + \frac{0.35}{a_2b_2}$$

* **Step 2: Generate Zadeh Implication Mapping**
  Evaluating $\max[\min(\mu_{A \cap B}, \mu_C), \, 1 - \mu_{A \cap B}]$ point-by-point against consequent vector $C = [0.4, 0.6]$:
  * **For element $a_1b_1 \, (\mu = 0.06)$:**
    * $c_1: \max(\min(0.06, 0.4), 1 - 0.06) = \max(0.06, 0.94) = 0.94$
    * $c_2: \max(\min(0.06, 0.6), 1 - 0.06) = \max(0.06, 0.94) = 0.94$
  * **For element $a_1b_2 \, (\mu = 0.21)$:**
    * $c_1: \max(\min(0.21, 0.4), 1 - 0.21) = \max(0.21, 0.79) = 0.79$
    * $c_2: \max(\min(0.21, 0.6), 1 - 0.21) = \max(0.21, 0.79) = 0.79$
  * **For element $a_2b_1 \, (\mu = 0.10)$:**
    * $c_1: \max(\min(0.1, 0.4), 1 - 0.1) = \max(0.1, 0.9) = 0.90$
    * $c_2: \max(\min(0.1, 0.6), 1 - 0.1) = \max(0.1, 0.9) = 0.90$
  * **For element $a_2b_2 \, (\mu = 0.35)$:**
    * $c_1: \max(\min(0.35, 0.4), 1 - 0.35) = \max(0.35, 0.65) = 0.65$
    * $c_2: \max(\min(0.35, 0.6), 1 - 0.35) = \max(0.35, 0.65) = 0.65$

**Final Tensor Matrix Representation:**

| Cross-Product Antecedent Element | $c_1 \, (0.4)$ | $c_2 \, (0.6)$ |
| :--- | :---: | :---: |
| **$a_1b_1 \, (0.06)$** | $0.94$ | $0.94$ |
| **$a_1b_2 \, (0.21)$** | $0.79$ | $0.79$ |
| **$a_2b_1 \, (0.10)$** | $0.90$ | $0.90$ |
| **$a_2b_2 \, (0.35)$** | $0.65$ | $0.65$ |"""
    }
]
