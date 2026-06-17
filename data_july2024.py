# data_july2024.py
# Official MAT633 Examination Session Data Registry - July 2024

questions = [
    {
        "question_no": "Question 1(a)",
        "topic": "Fuzzy Taxonomy Assessment",
        "marks": "4",
        "question": r"""Determine whether each of the following statements is TRUE or FALSE.

i) Linguistic variables formulate vague descriptions in natural languages with precise mathematical terms.
ii) Linguistic variables and linguistic hedges are equivalent in terms of its definition.
iii) Compound fuzzy propositions create relations between different sizes of fuzzy set.
iv) The truth value of fuzzy proposition is either true or false only.""",
        "answer": r"""**ANSWER SCHEME:**
i) **TRUE** `[B1]`
ii) **FALSE** `[B1]`
iii) **FALSE** `[B1]`
iv) **FALSE** `[B1]`"""
    },
    {
        "question_no": "Question 1(b)",
        "topic": "Hedges and Baseline Propositions",
        "marks": "4",
        "question": r"""Explain each of the following terms along with an example.

i) The linguistic hedges.
ii) The atomic fuzzy proposition.""",
        "answer": r"""**ANSWER SCHEME:**
* **i) The linguistic hedges:** Words that are used to modify primary baseline linguistic labels to make terms more descriptive and precise. `[A1]`
  * *Example:* "very" slow, "not" fast, "slightly" sweet. `[A1]`
* **ii) The atomic fuzzy proposition:** A simple single independent statement mapping a physical variable to a fuzzy label without connectives. `[A1]`
  * *Example:* $x$ is $A$. `[A1]`"""
    },
    {
        "question_no": "Question 2(a)",
        "topic": "Calculus of Hedges & Base Operations",
        "marks": "10",
        "question": r"""Let A and B be two discrete fuzzy set defined on $X=\{2,4,6,8,10\}$ where $\mu_{A}(x)=\frac{1}{x}$ and $\mu_{B}(x)=\frac{x}{10}$. Suppose the linguistic hedges "very" and "somewhat" are represented by $\mu_{very}(x)=\mu(x)^{2}$ and $\mu_{somewhat}(x)=\sqrt{\mu(x)}$, respectively. Using the combination of basic operator for fuzzy intersection, fuzzy union and fuzzy complement, determine the fuzzy set for the following:

i) A and very B.
ii) Somewhat A or not very B.""",
        "answer": r"""**ANSWER SCHEME:**

* **i) A and very B:**
  $$\mu_{\text{very } B}(x) = [\mu_B(x)]^2 = \frac{0.04}{2} + \frac{0.16}{4} + \frac{0.36}{6} + \frac{0.64}{8} + \frac{1}{10} \quad \text{`[M1, A1]`}$$
  $$\mu_{A \text{ and very } B}(x) = \min(\mu_A(x), \mu_{\text{very } B}(x))$$
  $$A \text{ and very } B = \frac{0.04}{2} + \frac{0.16}{4} + \frac{0.17}{6} + \frac{0.125}{8} + \frac{0.1}{10} \quad \text{`[M1, A1]`}$$

* **ii) Somewhat A or not very B:**
  $$\mu_{\text{somewhat } A}(x) = \sqrt{\mu_A(x)} = \frac{0.71}{2} + \frac{0.5}{4} + \frac{0.41}{6} + \frac{0.35}{8} + \frac{0.32}{10} \quad \text{`[M1]`}$$
  $$\mu_{\text{not very } B}(x) = 1 - \mu_{\text{very } B}(x) = \frac{0.96}{2} + \frac{0.84}{4} + \frac{0.64}{6} + \frac{0.36}{8} + \frac{0}{10}$$
  $$\mu_{\text{somewhat } A \text{ or not very } B}(x) = \max(\mu_{\text{somewhat } A}(x), \mu_{\text{not very } B}(x))$$
  $$\text{somewhat } A \text{ or not very } B = \frac{0.96}{2} + \frac{0.84}{4} + \frac{0.64}{6} + \frac{0.36}{8} + \frac{0.32}{10} \quad \text{`[M1, A1]`}$$"""
    },
    {
        "question_no": "Question 2(b)",
        "topic": "Parameterized Triad Combination Models",
        "marks": "4",
        "question": r"""Let X, Y and Z be fuzzy sets with the fuzzy proposition as "(x is not X and z is Z) or (y is not Y)". Determine the membership function by using the following combinations.

i) The combination of basic fuzzy operators for fuzzy t-norm, s-norm, and complement.
ii) The combination of Algebraic product ($t_{ap}(a,b)=ab$) for fuzzy t-norm, Einstein Sum ($S_{es}(a,b)=\frac{a+b}{1+ab}$) for fuzzy s-norm and basic fuzzy complement.""",
        "answer": r"""**ANSWER SCHEME:**
* **i) Basic Fuzzy Operators Layout:**
  $$\mu(x,y,z) = \max\left\{[\min(1-\mu_X(x), \mu_Z(z))], 1-\mu_Y(y)\right\} \quad \text{`[M1, A1]`}$$

* **ii) Algebraic Product & Einstein Sum Layout:**
  $$\mu(x,y,z) = \frac{(1-\mu_X(x))\cdot\mu_Z(z) + (1-\mu_Y(y))}{1 + ((1-\mu_X(x))\cdot\mu_Z(z)\cdot(1-\mu_Y(y)))} \quad \text{`[M1, A1]`}$$"""
    },
   {
        "question_no": "Question 2(c)",
        "topic": "Mamdani Relation for Cloudy and Dry",
        "marks": "6",
        "question": r"""Given fuzzy set 'cloudy' and 'dry' be defined by the following membership functions:
$$\mu_{\text{cloudy}}(x)=\begin{cases} \frac{x-2}{3} & \text{if } 2\le x\le5 \\ 1 & \text{if } 5 < x\le7 \\ 0 & \text{otherwise} \end{cases}$$

$$\mu_{\text{dry}}(y)=\begin{cases} 1 & \text{if } 0 \le y \le 0.5 \\ 2(1-y) & \text{otherwise} \end{cases}$$
where $x\in[0,10]$ and $y\in[0,1]$. Construct the fuzzy relation of "IF the x is cloudy, THEN the y is not dry" using the basic fuzzy complement and Mamdani Min implication $\mu_{Q_{MM}}(x,y)=\min(\mu_{FP_1}(x),\mu_{FP_2}(y))$ where appropriate.""",
        "answer": r"""**ANSWER SCHEME:**
* **Step 1: Compute Fuzzy Complement for "not dry"** [cite: 66]
  $$\mu_{\text{not dry}}(y) = 1 - \mu_{\text{dry}}(y) = \begin{cases} 0 & \text{if } 0 \le y \le 0.5 \\\\ 2y - 1 & \text{if } 0.5 < y \le 1 \end{cases} \quad \text{`[M2]`}$$ [cite: 68]

* **Step 2: Construct Mamdani Relation $\mu_{\text{cloudy} \rightarrow \text{not dry}}(x,y)$** [cite: 66]
  $$\mu_{\text{cloudy} \rightarrow \text{not dry}}(x,y) = \begin{cases} \min\left(\frac{x-2}{3}, 2y-1\right) & \text{if } 2 \le x \le 5, \; 0.5 < y \le 1 \\\\ 2y-1 & \text{if } 5 < x \le 7, \; 0.5 < y \le 1 \\\\ 0 & \text{otherwise} \end{cases} \quad \text{`[M2, A2]`}$$ [cite: 82, 85, 86]"""
    },
    {
        "question_no": "Question 3(a)",
        "topic": "Discrete Fuzzy Implication Formulation",
        "marks": "5",
        "question": r"""Let X and Y be two discrete fuzzy sets that is defined on $X=\{x_1,x_2,x_3\}$ and $Y=\{y_1,y_2,y_3\}$, respectively, where:
$$X=\frac{0.3}{x_1}+\frac{0.1}{x_2}+\frac{0.5}{x_3} \quad \text{and} \quad Y=\frac{0.7}{y_1}+\frac{1}{y_2}+\frac{0.2}{y_3}$$
Construct $IF \langle x \text{ is } X \rangle THEN \langle y \text{ is not } Y \rangle$ using the combination of basic fuzzy complement and the following implication formula:
$$\mu_Q(x,y)=\max[\min\{1-\mu_{FP_1}(x),\max(\mu_{FP_1}(x),\mu_{FP_2}(y))\},\mu_{FP_2}(y)]$$""",
        "answer": r"""**ANSWER SCHEME:**
* **First Derivative (Complement of Y):**
  $$\mu_{\overline{Y}}(y) = \frac{0.3}{y_1} + \frac{0}{y_2} + \frac{0.8}{y_3} \quad \text{`[M1]`}$$

* **Implication Value Computation Matrix:**
  $$\begin{array}{c|ccc} \mu_{X \rightarrow \overline{Y}}(x,y) & y_1(0.3) & y_2(0) & y_3(0.8) \\ \hline x_1(0.3) & 0.3 & 0.3 & 0.8 \\ x_2(0.1) & 0.3 & 0.1 & 0.8 \\ x_3(0.5) & 0.5 & 0.5 & 0.8 \end{array} \quad \text{`[M3]`}$$

* **Final Symbolic Vector Formulation:**
  $$X \rightarrow \overline{Y} = \frac{0.3}{x_1y_1}+\frac{0.3}{x_1y_2}+\frac{0.8}{x_1y_3}+\frac{0.3}{x_2y_1}+\frac{0.1}{x_2y_2}+\frac{0.8}{x_2y_3}+\frac{0.5}{x_3y_1}+\frac{0.5}{x_3y_2}+\frac{0.8}{x_3y_3} \quad \text{`[A1]`}$$"""
    },
    {
        "question_no": "Question 3(b)",
        "topic": "Boundary Condition Variable Deduction",
        "marks": "5",
        "question": r"""Let C and D be fuzzy sets where:
$$C=\frac{0.1}{c_1}+\frac{0.8}{c_2}+\frac{0.5}{c_3} \quad \text{and} \quad D=\frac{\alpha}{d_1}+\frac{\beta}{d_2}$$
Given the implication of $IF \langle c \text{ is } C \rangle THEN \langle d \text{ is } D \rangle$ using the Mamdani Min implication as follow:
$$C\rightarrow D=\frac{0.1}{(c_1,d_1)}+\frac{0.1}{(c_1,d_2)}+\frac{0.8}{(c_2,d_1)}+\frac{0.6}{(c_2,d_2)}+\frac{0.5}{(c_3,d_1)}+\frac{0.5}{(c_3,d_2)}$$
Determine the possible value(s) of $\alpha$ and $\beta$.""",
        "answer": r"""**ANSWER SCHEME:**
By breaking down the evaluation intersections using $\min(\mu_C(c_i), \mu_D(d_j))$:

* **For element $c_1$ ($0.1$):**
  $$\min(0.1, \alpha) = 0.1 \implies \alpha \ge 0.1$$
  $$\min(0.1, \beta) = 0.1 \implies \beta \ge 0.1$$
* **For element $c_2$ ($0.8$):**
  $$\min(0.8, \alpha) = 0.8 \implies \alpha \ge 0.8$$
  $$\min(0.8, \beta) = 0.6 \implies \beta = 0.6 \quad \text{`[M3]`}$$
* **For element $c_3$ ($0.5$):**
  $$\min(0.5, \alpha) = 0.5 \implies \alpha \ge 0.5$$
  $$\min(0.5, \beta) = 0.5 \implies \beta \ge 0.5$$

* **Conclusion:**
  Since $\alpha \ge 0.1$, $\alpha \ge 0.8$ and $\alpha \ge 0.5$, we get $\mathbf{\alpha \ge 0.8}$.
  For $\beta$, the exact boundary match forces $\mathbf{\beta = 0.6}$. `[A2]`"""
    },
  {
        "question_no": "Question 3(c)",
        "topic": "Continuous Composition Profile",
        "marks": "10",
        "question": r"""Let M, N and P be fuzzy sets defined on $x\in[0,8]$, $y\in[0,10]$ and $z\in[0,10]$ respectively, where:
$$\mu_{M}(x)=\begin{cases} x & \text{if } 0\le x < 1 \\ 1 & \text{if } 1\le x\le3 \\ 4-x & \text{if } 3\le x\le4 \\ 0 & \text{otherwise} \end{cases}$$

$$\mu_{N}(y)=\begin{cases} \frac{y-1}{3} & \text{if } 1 \le y \le 4 \\ \frac{6-y}{2} & \text{if } 4 < y \le 6 \\ 0 & \text{otherwise} \end{cases}$$

$$\mu_{P}(z)=\begin{cases} \frac{z-3}{2} & \text{if } 3\le z\le5 \\ \frac{7-z}{2} & \text{if } 5 < z\le7 \\ 0 & \text{otherwise} \end{cases}$$

i) Obtain the membership function for the IF-THEN rule $IF \langle x \text{ is } M \text{ and } y \text{ is } N \rangle THEN \langle z \text{ is } P \rangle$ using the Algebraic Product ($t_{ap}(a,b)=ab$) for the t-norm and Mamdani Product implication ($\mu_{Q_{AP}}(x,y)=\mu_{FP_1}(x)\cdot\mu_{FP_2}(y)$).
ii) Hence, determine the implication value when $x=2, y=2$ and $z=6$.""",
        "answer": r"""**ANSWER SCHEME:**

**i) Membership Function Matrix Formulation:** [cite: 139]
Using Algebraic Product $T_{ap}(x,y) = \mu_M(x) \cdot \mu_N(y)$ followed by Mamdani Product Implication with $z$, the system expands into the piecewise profile below: [cite: 139]

$$\mu_{(M \cap N) \rightarrow P}(x,y,z) = \begin{cases} 
\frac{(xy-x)(z-3)}{6} & \text{if } 0 \le x \le 1, \; 1 \le y \le 4, \; 3 \le z \le 5 \\\\ 
\frac{(xy-x)(7-z)}{6} & \text{if } 0 \le x \le 1, \; 1 \le y \le 4, \; 5 \le z \le 7 \\\\ 
\frac{(6x-xy)(z-3)}{4} & \text{if } 0 \le x \le 1, \; 4 \le y \le 6, \; 3 \le z \le 5 \\\\ 
\frac{(6x-xy)(7-z)}{4} & \text{if } 0 \le x \le 1, \; 4 \le y \le 6, \; 5 \le z \le 7 \\\\ 
\frac{(y-1)(z-3)}{6} & \text{if } 1 \le x \le 3, \; 1 \le y \le 4, \; 3 \le z \le 5 \\\\ 
\frac{(y-1)(7-z)}{6} & \text{if } 1 \le x \le 3, \; 1 \le y \le 4, \; 5 \le z \le 7 \\\\ 
\frac{(6-y)(z-3)}{4} & \text{if } 1 \le x \le 3, \; 4 \le y \le 6, \; 3 \le z \le 5 \\\\ 
\frac{(6-y)(7-z)}{4} & \text{if } 1 \le x \le 3, \; 4 \le y \le 6, \; 5 \le z \le 7 \\\\ 
\frac{(4-x)(y-1)(z-3)}{6} & \text{if } 3 \le x \le 4, \; 1 \le y \le 4, \; 3 \le z \le 5 \\\\ 
\frac{(4-x)(y-1)(7-z)}{6} & \text{if } 3 \le x \le 4, \; 1 \le y \le 4, \; 5 \le z \le 7 \\\\ 
\frac{(4-x)(6-y)(z-3)}{4} & \text{if } 3 \le x \le 4, \; 4 \le y \le 6, \; 3 \le z \le 5 \\\\ 
\frac{(4-x)(6-y)(7-z)}{4} & \text{if } 3 \le x \le 4, \; 4 \le y \le 6, \; 5 \le z \le 7 \\\\ 
0 & \text{otherwise} 
\end{cases} \quad \text{`[M2, M3, A1]`}$$ [cite: 151, 152, 179]

**ii) Value Evaluation for $x=2, y=2, z=6$:** [cite: 180]
The coordinates fall directly inside the range: $1 \le x \le 3, \; 1 \le y \le 4, \; 5 \le z \le 7$. [cite: 181]
$$\mu(2,2,6) = \frac{(y-1)(7-z)}{6} = \frac{(2-1)(7-6)}{6} = \frac{1}{6} \quad \text{`[M1, A1]`}$$ [cite: 181, 184]"""
    },
    {
        "question_no": "Question 4",
        "topic": "Generalized Modus Ponens Evaluation",
        "marks": "12",
        "question": r"""Let $V=\{v_1,v_2,v_3\}$ and $W=\{w_1,w_2\}$ where:
$$V=\frac{0.2}{v_1}+\frac{0.1}{v_2}+\frac{0.5}{v_3} \quad \text{and} \quad W=\frac{0.3}{w_1}+\frac{0.5}{w_2}$$
a) Compute $IF \langle v \text{ is not } V \rangle THEN \langle w \text{ is } W \rangle$ using basic fuzzy complement for complement and Lukasiewicz Implication $\mu_{Q_L}(x,y)=\min[1,1-\mu_{FP_1}(x)+\mu_{FP_2}(y)]$ for implication.
b) Derive a conclusion in the form of "w is W'" if given a fact statement "v is V'" such that $V'=\frac{0.7}{v_1}+\frac{0.6}{v_2}+\frac{0.6}{v_3}$ using generalized modus ponens.""",
        "answer": r"""**ANSWER SCHEME:**

* **a) Lukasiewicz Implication Matrix:**
  $$\overline{V} = \frac{0.8}{v_1} + \frac{0.9}{v_2} + \frac{0.5}{v_3} \quad \text{`[M1, A1]`}$$
  Using $\min[1, 1 - \mu_{\overline{V}}(v_i) + \mu_W(w_j)]$:
  $$\overline{V} \rightarrow W = \frac{0.5}{v_1w_1}+\frac{0.7}{v_1w_2}+\frac{0.4}{v_2w_1}+\frac{0.6}{v_2w_2}+\frac{0.8}{v_3w_1}+\frac{1}{v_3w_2} \quad \text{`[M2, A1]`}$$

* **b) Generalized Modus Ponens (Composition $V' \circ (\overline{V} \rightarrow W)$):**
  Using max-min intersection matrix properties:
  $$\begin{array}{c|cc} \min(V'_i, R_{ij}) & w_1 & w_2 \\ \hline v_1 (0.7) & \min(0.7,0.5)=0.5 & \min(0.7,0.7)=0.7 \\ v_2 (0.6) & \min(0.6,0.4)=0.4 & \min(0.6,0.6)=0.6 \\ v_3 (0.6) & \min(0.6,0.8)=0.6 & \min(0.6,1.0)=0.6 \end{array} \quad \text{`[M3, M1]`}$$
  $$\mu_{W'}(w) = \frac{\max(0.5, 0.4, 0.6)}{w_1} + \frac{\max(0.7, 0.6, 0.6)}{w_2}$$
  $$W' = \frac{0.6}{w_1} + \frac{0.7}{w_2} \quad \text{`[A1]`}$$"""
    }
]
