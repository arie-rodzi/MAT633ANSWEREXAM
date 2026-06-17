feb2025_questions = [
    {
        "question_no": "Question 1(a)",
        "topic": "Axiomatic Logic Assortments",
        "marks": "4",
        "question": """Determine whether each of the following statements is TRUE or FALSE.

i) The truth value of a fuzzy proposition is between -1 to 1.
ii) Generalized Hypothetical Syllogism can be represented as follows:
    Premise 1: IF P THEN Q
    Premise 2: IF Q THEN R
    Conclusion: IF P THEN R
iii) In classical logic, every statement is either true (1) or false (0).
iv) A fuzzy proposition can be represented as a fuzzy set.""",
        "answer": """**ANSWER SCHEME:**
i) **FALSE** `[B1]`
ii) **TRUE** `[B1]`
iii) **TRUE** `[B1]`
iv) **TRUE** `[B1]`"""
    },
    {
        "question_no": "Question 1(b)",
        "topic": "Structural Propositional Taxonomy",
        "marks": "4",
        "question": """State a difference between the atomic fuzzy proposition and compound fuzzy proposition. 
Give ONE appropriate example to illustrate the difference between propositions.""",
        "answer": """**ANSWER SCHEME:**
* **Atomic Fuzzy Proposition:** An atomic fuzzy proposition is a single (simple) statement in fuzzy logic involving a single variable and a fuzzy set. `[B1]`
  * *Example:* "Temperature is hot" `[M1]`
* **Compound Fuzzy Proposition:** A compound fuzzy proposition combines two or more atomic fuzzy propositions using logical connectives like AND, OR, and NOT. `[B1]`
  * *Example:* "Temperature is hot, and humidity is dry" `[M1]`"""
    },
    {
        "question_no": "Question 2(a)(i)",
        "topic": "Algebraic Sum Hedge Applications",
        "marks": "5",
        "question": """Let a set of smartphones be defined as $X=\{x_{1},x_{2},x_{3},x_{4},x_{5}\}$. The linguistic variable of these smartphones are defined as cheap and powerful, where:
$$cheap=\frac{0.35}{x_{1}}+\frac{1}{x_{2}}+\frac{0.5}{x_{3}}+\frac{0.7}{x_{4}}+\frac{0.6}{x_{5}}$$
$$\\text{and powerful} =\\frac{0.9}{x_{1}}+\frac{0.2}{x_{2}}+\frac{0.7}{x_{3}}+\frac{0.5}{x_{4}}+\frac{0.6}{x_{5}}.$$

Suppose the linguistic hedges "very" and "somewhat" are represented by $\\mu_{very}(x)=\\mu(x)^{2}$ and $\\mu_{somewhat}(x)=\\sqrt{\\mu(x)}$ respectively.
Determine the fuzzy set "somewhat cheap or not very powerful" using the combination of basic operator for fuzzy complement and Algebraic Sum ($s_{AS}(a,b)=a+b-ab$) for s-norm.""",
        "answer": """**ANSWER SCHEME:**
* **Somewhat cheap:** $\\frac{\\sqrt{0.35}}{x_1} + \\frac{\\sqrt{1}}{x_2} + \\frac{\\sqrt{0.5}}{x_3} + \\frac{\\sqrt{0.7}}{x_4} + \\frac{\\sqrt{0.6}}{x_5} = \\frac{0.5916}{x_1} + \\frac{1}{x_2} + \\frac{0.7071}{x_3} + \\frac{0.8367}{x_4} + \\frac{0.7746}{x_5}$ `[M1]`
* **Not very powerful:** $\\mu_{\\text{very}} = 0.9^2=0.81 \\implies 1 - 0.81 = 0.19$ for $x_1$, etc.
  $= \\frac{0.19}{x_1} + \\frac{0.96}{x_2} + \\frac{0.51}{x_3} + \\frac{0.75}{x_4} + \\frac{0.64}{x_5}$ `[M1]`
* **Algebraic Sum Implementation ($a+b-ab$):** `[M1]`
  * $x_1: 0.5916 + 0.19 - (0.5916 \\times 0.19) = 0.6692$
  * $x_2: 1 + 0.96 - (1 \\times 0.96) = 1$
  * $x_3: 0.7071 + 0.51 - (0.7071 \\times 0.51) = 0.8565$
  * $x_4: 0.8367 + 0.75 - (0.8367 \\times 0.75) = 0.9592$
  * $x_5: 0.7746 + 0.64 - (0.7746 \\times 0.64) = 0.9189$ `[M1]`

**Final Set:**
$$\\text{somewhat cheap or not very powerful} = \\frac{0.6692}{x_{1}}+\frac{1}{x_{2}}+\frac{0.8565}{x_{3}}+\frac{0.9592}{x_{4}}+\frac{0.9189}{x_{5}} \\text{ `[A1]`}$$"""
    },
    {
        "question_no": "Question 2(a)(ii)",
        "topic": "Dubois-Prade T-Norm Multi-Criteria Decisions",
        "marks": "5",
        "question": """Ali is looking for a smartphone with "cheap and very powerful" characteristics. Using the Dubois-Prade class:
$$t_{DPC}(a,b)=\\frac{ab}{\\max(a,b,0.6)}$$
for fuzzy intersection, determine the smartphone that Ali should buy.""",
        "answer": """**ANSWER SCHEME:**
Evaluating $t_{DPC}(\\mu_{\\text{cheap}}, \\mu_{\\text{very powerful}})$ entry-wise:
* $x_1: \\frac{0.35 \\times 0.81}{\\max(0.35, 0.81, 0.6)} = \\frac{0.2835}{0.81} = 0.35$
* $x_2: \\frac{1 \\times 0.04}{\\max(1, 0.04, 0.6)} = \\frac{0.04}{1.0} = 0.04$
* $x_3: \\frac{0.5 \\times 0.49}{\\max(0.5, 0.49, 0.6)} = \\frac{0.245}{0.6} = 0.4083$
* $x_4: \\frac{0.7 \\times 0.25}{\\max(0.7, 0.25, 0.6)} = \\frac{0.175}{0.7} = 0.25$
* $x_5: \\frac{0.6 \\times 0.36}{\\max(0.6, 0.36, 0.6)} = \\frac{0.216}{0.6} = 0.36$ `[M1, A1]`

$$\\text{cheap and very powerful} = \\frac{0.35}{x_{1}}+\frac{0.04}{x_{2}}+\frac{0.4083}{x_{3}}+\frac{0.25}{x_{4}}+\frac{0.36}{x_{5}} \\text{ `[A1]`}$$
**Decision:** Ali should buy smartphone $x_{3}$ as it possesses the maximum fuzzy value within the given set ($0.4083$). `[A1]`"""
    },
    {
        "question_no": "Question 2(b)",
        "topic": "Syntactic Logical Composition Combinations",
        "marks": "4",
        "question": """Let X, Y and Z be fuzzy sets. Determine the fuzzy proposition of **"(x is X and z is not Z) or (y is Y)"** using the following combinations:

i) Basic fuzzy operators for fuzzy t-norm, s-norm, and complement.
ii) Algebraic Product ($t_{AP}(a,b)=ab$) for fuzzy t-norm, Einstein Sum ($S_{ES}(a,b)=\\frac{a+b}{1+ab}$) for fuzzy s-norm and basic fuzzy complement.""",
        "answer": """**ANSWER SCHEME:**
**i) Basic Fuzzy Operators:**
$$\\mu_{(X\\cap\\overline{Z})\\cup Y}(x,y,z)=(\\mu_{X}(x)\\cap\\mu_{\\overline{Z}}(z))\\cup\\mu_{Y}(y)$$
$$=\\max\\{[\\min(\\mu_{X}(x),1-\\mu_{Z}(z))],\\mu_{Y}(y)\\} \\text{ `[M1, A1]`}$$

**ii) Algebraic Product & Einstein Sum:**
$$\\mu_{(X\\cap\\overline{Z})\\cup Y}(x,y,z)=\\frac{\\mu_{X}(x)\\cdot(1-\\mu_{Z}(z))+\\mu_{Y}(y)}{1+(\\mu_{X}(x)\\cdot(1-\\mu_{Z}(z))\\cdot\\mu_{Y}(y))} \\text{ `[M1, A1]`}$$"""
    },
    {
        "question_no": "Question 2(c)",
        "topic": "Mamdani Relational Profile Synthesis",
        "marks": "6",
        "question": """Given fuzzy sets 'heavy' and 'fast' be defined on $x\\in[0,10]$ and $y\\in[0,5]$, respectively where:
$$\\mu_{heavy}(x)=\\begin{cases}0&;0\\le x\\le5\\\\ \\frac{x-5}{2}&;5\\le x\\le7\\\\ 1&;7\\le x\\le10\\end{cases}$$
$$\\text{and } \\mu_{fast}(y)=\\begin{cases}y-2&;&2\\le y\\le3\\\\ 4-y&;&3\\le y\\le4\\\\ 0&;y<2 \\text{ and } y>4\\end{cases}$$

Construct the fuzzy relation of "IF x is not heavy, THEN y is fast" using the basic fuzzy complement and Mamdani Product Implication ($\\mu_{Q_{CP}}(x,y)=\\mu_{FP_{1}}(x)\\cdot\\mu_{FP_{2}}(y)$) where it is appropriate.""",
        "answer": """**ANSWER SCHEME:**
* **Fuzzy Complement (not heavy):**
$$\\mu_{\\overline{heavy}}(x)=1-\\mu_{heavy}(x)=\\begin{cases}1&;0\\le x\\le5\\\\ \\frac{7-x}{2}&;5\\le x\\le7\\\\ 0&;7\\le x\\le10\\end{cases} \\text{ `[M1, A1]`}$$

* **Mamdani Product Relation:** `[M2]`
$$\\mu_{\\overline{heavy}\\rightarrow fast}(x,y) = \\begin{cases} y-2 &; 0 \\le x \\le 5, 2 \\le y \\le 3 \\\\ 4-y &; 0 \\le x \\le 5, 3 \\le y \\le 4 \\\\ \\frac{(7-x)(y-2)}{2} &; 5 \\le x \\le 7, 2 \\le y \\le 3 \\\\ \\frac{(7-x)(4-y)}{2} &; 5 \\le x \\le 7, 3 \\le y \\le 4 \\\\ 0 &; \\text{otherwise} \\end{cases} \\text{ `[M1, A1]`}$$"""
    },
    {
        "question_no": "Question 3(a)",
        "topic": "Yager-Lukasiewicz Matrix Projections",
        "marks": "5",
        "question": """Let X and Y be two discrete fuzzy sets that are defined on $X=\{x_{1},x_{2}\}$ and $Y=\{y_{1},y_{2},y_{3}\}$, respectively, where:
$$X=\\frac{0.3}{x_{1}}+\\frac{0.7}{x_{2}} \\text{ and } Y=\\frac{0.9}{y_{1}}+\\frac{1}{y_{2}}+\frac{0.2}{y_{3}}.$$

Construct "IF x is X THEN y is not Y" using the Yager fuzzy complement ($c_{w}(a)=\\sqrt{1-a^{2}}$) and the Lukasiewicz Implication ($\\mu_{Q_{L}}(x,y)=\\min[1,1-\\mu_{FP_{1}}(x)+\\mu_{FP_{2}}(y)]$) where it is appropriate.""",
        "answer": """**ANSWER SCHEME:**
* **Yager Complement of Y:**
$$\\overline{Y} = \\frac{\\sqrt{1-0.9^2}}{y_1} + \\frac{\\sqrt{1-1^2}}{y_2} + \\frac{\\sqrt{1-0.2^2}}{y_3} = \\frac{0.4359}{y_1} + \\frac{0}{y_2} + \\frac{0.9798}{y_3} \\text{ `[M1]`}$$

* **Lukasiewicz Implication Matrix calculation:** $\\min[1, 1 - \\mu_X(x) + \\mu_{\\overline{Y}}(y)]$ `[M2, A1]`
  * For $x_1\\,(\\mu=0.3)$:
    * $y_1: \\min[1, 1 - 0.3 + 0.4359] = 1$
    * $y_2: \\min[1, 1 - 0.3 + 0] = 0.7$
    * $y_3: \\min[1, 1 - 0.3 + 0.9798] = 1$
  * For $x_2\\,(\\mu=0.7)$:
    * $y_1: \\min[1, 1 - 0.7 + 0.4359] = 0.7359$
    * $y_2: \\min[1, 1 - 0.7 + 0] = 0.3$
    * $y_3: \\min[1, 1 - 0.7 + 0.9798] = 1$

$$\\mu_{X\\rightarrow\\overline{Y}}(x,y)=\\frac{1}{(x_{1},y_{1})}+\\frac{0.7}{(x_{1},y_{2})}+\\frac{1}{(x_{1},y_{3})}+\\frac{0.7359}{(x_{2},y_{1})}+\\frac{0.3}{(x_{2},y_{2})}+\\frac{1}{(x_{2},y_{3})} \\text{ `[A1]`}$$"""
    },
    {
        "question_no": "Question 3(b)",
        "topic": "Generalized Modus Ponens Deductions",
        "marks": "5",
        "question": """Suppose C and D be fuzzy sets that defined on $C=\{c_{1},c_{2},c_{3}\}$ and $D=\{d_{1},d_{2},d_{3}\}$, respectively.
Let the implication of "IF c is C THEN d is D" as follow:
$$C\\rightarrow D=\\frac{0.15}{(c_{1},d_{1})}+\\frac{0.55}{(c_{1},d_{3})}+\\frac{0.4}{(c_{2},d_{1})}+\\frac{0.2}{(c_{2},d_{2})}+\\frac{0.5}{(c_{3},d_{1})}+\\frac{0.8}{(c_{3},d_{2})}+\\frac{0.3}{(c_{3},d_{3})}$$
Given a statement "c is $\\tilde{C}$" where $\\tilde{C}=\\frac{0.3}{c_{1}}+\\frac{0.8}{c_{2}}+\\frac{0.5}{c_{3}}$.
Derive a conclusion "d is $\\tilde{D}$" using the Generalized Modus Ponens.""",
        "answer": """**ANSWER SCHEME:**
Using Generalized Modus Ponens: $\\mu_{\\tilde{D}}(d) = \\sup_{c \\in C} \\min[\\mu_{\\tilde{C}}(c), \\mu_{C\\rightarrow D}(c,d)]$ `[M1, B1]`

* **For $d_1$:** $\\max(\\min[0.3, 0.15], \\min[0.8, 0.4], \\min[0.5, 0.5]) = \\max(0.15, 0.4, 0.5) = 0.5$ `[M1]`
* **For $d_2$:** $\\max(\\min[0.3, 0], \\min[0.8, 0.2], \\min[0.5, 0.8]) = \\max(0, 0.2, 0.5) = 0.5$
* **For $d_3$:** $\\max(\\min[0.3, 0.55], \\min[0.8, 0], \\min[0.5, 0.3]) = \\max(0.3, 0, 0.3) = 0.3$ `[A1]`

$$\\tilde{D} = \\frac{0.5}{d_{1}}+\\frac{0.5}{d_{2}}+\\frac{0.3}{d_{3}} \\text{ `[A1]`}$$"""
    },
    {
        "question_no": "Question 3(c)(i)",
        "topic": "Reichenbach Rule-Based Modeling",
        "marks": "8",
        "question": """Let M, N and P be fuzzy sets defined on $x\\in[0,8]$, $y\\in[0,10]$ and $z\\in[0,10]$ respectively, where $\\mu_{M}(x)=\\frac{8-x}{8}$, $\\mu_{N}(y) = \\mu_N(y: 1,4,6)$, and $\\mu_{P}(z)=\\frac{z^{2}}{100}$.

Obtain the membership function "IF (x is M and y is N) THEN z is P" using the Algebraic Product ($t_{AP}(a,b)=ab$) for the t-norm and Reichenbach Implication ($\\mu_{Q_{R}}(x,y)=1-\\mu_{FP_{1}}(x)+\\mu_{FP_{1}}(x)\\cdot\\mu_{FP_{2}}(y)$) for the IF-THEN rule.""",
        "answer": """**ANSWER SCHEME:**
* **Triangular Membership function $\\mu_N(y: 1,4,6)$:** `[B1]`
$$\\mu_N(y) = \\begin{cases} \\frac{y-1}{3} &; 1 \\le y \\le 4 \\\\ \\frac{6-y}{2} &; 4 \\le y \\le 6 \\\\ 0 &; y < 1, y > 6 \\end{cases}$$

* **T-norm Intersection $(M \\cap N)$ via Algebraic Product:** `[M1, A1]`
$$\\mu_{M \\cap N}(x,y) = \\begin{cases} \\frac{(8-x)(y-1)}{24} &; 0 \\le x \\le 8, 1 \\le y \\le 4 \\\\ \\frac{(8-x)(6-y)}{16} &; 0 \\le x \\le 8, 4 \\le y \\le 6 \\\\ 0 &; y < 1, y > 6 \\end{cases}$$

* **Reichenbach Implication Formulation:** $\\mu(x,y,z) = 1 - \\mu_{M\\cap N}(x,y) + \\mu_{M\\cap N}(x,y)\\cdot\\mu_P(z)$ `[M1]`
$$\\mu(x,y,z) = \\begin{cases} 1 - \\frac{(8-x)(y-1)}{24} + \\frac{(8-x)(y-1)z^2}{2400} &; 0 \\le x \\le 8, 1 \\le y \\le 4, 0 \\le z \\le 10 \\\\ 1 - \\frac{(8-x)(6-y)}{16} + \\frac{(8-x)(6-y)z^2}{1600} &; 0 \\le x \\le 8, 4 \\le y \\le 6, 0 \\le z \\le 10 \\\\ 1 &; 0 \\le x \\le 8, y < 1 \\text{ or } y > 6, 0 \\le z \\le 10 \\end{cases} \\text{ `[M2, A2]`}$$"""
    },
    {
        "question_no": "Question 3(c)(ii)",
        "topic": "Reichenbach Rule-Based Modeling",
        "marks": "2",
        "question": """Determine the implication value when $x=2$, $y=5$ and $z=6$ for the function obtained in Question 3(c)(i).""",
        "answer": """**ANSWER SCHEME:**
For $x=2, y=5, z=6$, we use the segment $4 \\le y \\le 6$:
$$\\mu(2,5,6) = 1 - \\frac{(8-2)(6-5)}{16} + \\frac{(8-2)(6-5)(6^2)}{1600}$$
$$= 1 - \\frac{6}{16} + \\frac{6 \\times 36}{1600} = 1 - 0.375 + 0.135 = 0.76 \\text{ `[M1, A1]`}$$"""
    },
    {
        "question_no": "Question 4(a)",
        "topic": "Einstein-Dienes Tensor Construction",
        "marks": "7",
        "question": """Let $A=\{a_{1},a_{2}\}$, $B=\{b_{1},b_{2}\}$ and $C=\{c_{1},c_{2}\}$ be three discrete fuzzy sets where:
$$A=\\frac{0.7}{a_{1}}+\\frac{0.9}{a_{2}}, B=\\frac{0.5}{b_{1}}+\\frac{0.4}{b_{2}} \\text{ and } C=\\frac{0.6}{c_{1}}+\\frac{0.2}{c_{2}}$$

Construct the fuzzy relation R for the rule, "IF a is A and b is B THEN c is C" where the Einstein Product ($t_{EP}(a,b)=\\frac{ab}{2-(a+b-ab)}$) and the Dienes-Rescher implication ($\\mu_{Q_{D}}(x,y)=\\max[1-\\mu_{FP1}(x),\\mu_{FP2}(y)]$) are used for the t-norm and the implication, respectively.""",
        "answer": """**ANSWER SCHEME:**
* **Einstein Product Intersection $(A \\cap B)$:** `[M1, A1]`
  * $(a_1, b_1): \\frac{0.7 \\times 0.5}{2 - (0.7 + 0.5 - 0.35)} = \\frac{0.35}{1.15} = 0.3043$
  * $(a_1, b_2): \\frac{0.7 \\times 0.4}{2 - (0.7 + 0.4 - 0.28)} = \\frac{0.28}{1.18} = 0.2373$
  * $(a_2, b_1): \\frac{0.9 \\times 0.5}{2 - (0.9 + 0.5 - 0.45)} = \\frac{0.45}{1.05} = 0.4286$
  * $(a_2, b_2): \\frac{0.9 \\times 0.4}{2 - (0.9 + 0.4 - 0.36)} = \\frac{0.36}{1.06} = 0.3396$
$$\\mu_{A \\cap B}(a,b) = \\frac{0.3043}{(a_1, b_1)} + \\frac{0.2373}{(a_1, b_2)} + \\frac{0.4286}{(a_2, b_1)} + \\frac{0.3396}{(a_2, b_2)} \\text{ `[A1]`}$$

* **Dienes-Rescher Implication $(A \\cap B) \\rightarrow C$ Matrix:** $\\max[1 - \\mu_{A\\cap B}(a,b), \\mu_C(c)]$ `[M1, A1]`
  * For $(a_1, b_1)$ [$1-0.3043 = 0.6957$]: $c_1 = \\max(0.6957, 0.6) = 0.6957$; $c_2 = \\max(0.6957, 0.2) = 0.6957$
  * For $(a_1, b_2)$ [$1-0.2373 = 0.7627$]: $c_1 = \\max(0.7627, 0.6) = 0.7627$; $c_2 = \\max(0.7627, 0.2) = 0.7627$
  * For $(a_2, b_1)$ [$1-0.4286 = 0.5714$]: $c_1 = \\max(0.5714, 0.6) = 0.6$; $c_2 = \\max(0.5714, 0.2) = 0.5714$
  * For $(a_2, b_2)$ [$1-0.3396 = 0.6604$]: $c_1 = \\max(0.6604, 0.6) = 0.6604$; $c_2 = \\max(0.6604, 0.2) = 0.6604$

$$R = \\frac{0.6957}{a_{1}b_{1}c_{1}}+\\frac{0.6957}{a_{1}b_{1}c_{2}}+\\frac{0.7627}{a_{1}b_{2}c_{1}}+\\frac{0.7627}{a_{1}b_{2}c_{2}}+\\frac{0.6}{a_{2}b_{1}c_{1}}+\\frac{0.5714}{a_{2}b_{1}c_{2}}+\\frac{0.6604}{a_{2}b_{2}c_{1}}+\\frac{0.6604}{a_{2}b_{2}c_{2}} \\text{ `[M1, A1]`}$$"""
    },
    {
        "question_no": "Question 4(b)",
        "topic": "Einstein-Dienes Tensor Construction",
        "marks": "5",
        "question": """Given a statement "c is $\\tilde{C}$" where $\\tilde{C}=\\frac{0.3}{c_{1}}+\\frac{0.8}{c_{2}}$.
Derive a conclusion "a is $\\tilde{A}$ and b is $\\tilde{B}$" using the Generalized Modus Tollens.""",
        "answer": """**ANSWER SCHEME:**
Using Generalized Modus Tollens: $\\mu_{\\tilde{A} \\cap \\tilde{B}}(a,b) = \\sup_{c \\in C} \\min[\\mu_{\\overline{C}}(c), \\mu_{R}(a,b,c)]$ `[B1]`
* Note: $\\mu_{\\overline{C}}(c) = \\frac{1-0.3}{c_1} + \\frac{1-0.8}{c_2} = \\frac{0.7}{c_1} + \\frac{0.2}{c_2}$ `[M1]`

Composition computations over each coordinate pair:
* $(a_1, b_1): \\max(\\min[0.7, 0.6957], \\min[0.2, 0.6957]) = \\max(0.6957, 0.2) = 0.6957$ `[M1]`
* $(a_1, b_2): \\max(\\min[0.7, 0.7627], \\min[0.2, 0.7627]) = \\max(0.7, 0.2) = 0.7627$
* $(a_2, b_1): \\max(\\min[0.7, 0.6], \\min[0.2, 0.5714]) = \\max(0.6, 0.2) = 0.5714$ 
* $(a_2, b_2): \\max(\\min[0.7, 0.6604], \\min[0.2, 0.6604]) = \\max(0.6604, 0.2) = 0.6604$ `[M1]`

**Derived Conclusion Set:**
$$\\mu_{\\tilde{A}\\cap\\tilde{B}}(a,b) = \\frac{0.6957}{a_{1}b_{1}}+\\frac{0.7627}{a_{1}b_{2}}+\\frac{0.5714}{a_{2}b_{1}}+\\frac{0.6604}{a_{2}b_{2}} \\text{ `[A1]`}$$"""
    }
]
