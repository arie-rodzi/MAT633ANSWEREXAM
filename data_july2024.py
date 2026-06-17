questions = [
    {
        "question_no": "Question 1(a)",
        "topic": "Fuzzy Taxonomy Assessment",
        "marks": "4",
        "question": """Determine whether each of the following statements is TRUE or FALSE.

i) Linguistic variables formulate vague descriptions in natural languages with precise mathematical terms.
ii) Linguistic variables and linguistic hedges are equivalent in terms of its definition.
iii) Compound fuzzy propositions create relations between different sizes of fuzzy set.
iv) The truth value of fuzzy proposition is either true or false only.""",
        "answer": """**ANSWER SCHEME:**
i) **TRUE** `[B1]`
ii) **FALSE** `[B1]`
iii) **FALSE** `[B1]`
iv) **FALSE** `[B1]`"""
    },
    {
        "question_no": "Question 1(b)",
        "topic": "Hedges and Baseline Propositions",
        "marks": "4",
        "question": """Explain each of the following terms along with an example.

i) The linguistic hedges.
ii) The atomic fuzzy proposition.""",
        "answer": """**ANSWER SCHEME:**
* **i) The linguistic hedges:** Words that are used to modify primary baseline linguistic labels to make terms more descriptive and precise. `[A1]`
  * *Example:* "very" slow, "not" fast, "slightly" sweet. `[A1]`
* **ii) The atomic fuzzy proposition:** A simple single independent statement mapping a physical variable to a fuzzy label without connectives. `[A1]`
  * *Example:* x is A. `[A1]`"""
    },
    {
        "question_no": "Question 2(a)",
        "topic": "Calculus of Hedges & Base Operations",
        "marks": "10",
        "question": """Let A and B be two discrete fuzzy sets defined on $X \\in \\{2, 4, 6, 8, 10\\}$ where $\\mu_A(x) = \\frac{1}{x}$ and $\\mu_B(x) = \\frac{x}{10}$. Suppose the linguistic hedges "very" and "somewhat" are represented by $\\mu_{very}(x) = (\\mu(x))^2$ and $\\mu_{somewhat}(x) = \\sqrt{\\mu(x)}$, respectively.

Using the combination of basic operators for fuzzy t-norm, s-norm, and complement, determine the fuzzy sets for the following:
i) A and very B.
ii) Somewhat A or not very B.""",
        "answer": """**ANSWER SCHEME:**
* Baseline Expanded Sets:
  $A = \\frac{0.5}{2} + \\frac{0.25}{4} + \\frac{0.17}{6} + \\frac{0.125}{8} + \\frac{0.1}{10}$
  $B = \\frac{0.2}{2} + \\frac{0.4}{4} + \\frac{0.6}{6} + \\frac{0.8}{8} + \\frac{1.0}{10}$
* Derived elements:
  $\\text{very } B = \\frac{0.04}{2} + \\frac{0.16}{4} + \\frac{0.36}{6} + \\frac{0.64}{8} + \\frac{1.0}{10}$
  $\\text{somewhat } A = \\frac{\\sqrt{0.5}}{2} + \\frac{\\sqrt{0.25}}{4} + \\frac{\\sqrt{0.17}}{6} + \\frac{\\sqrt{0.125}}{8} + \\frac{\\sqrt{0.1}}{10} = \\frac{0.71}{2} + \\frac{0.5}{4} + \\frac{0.41}{6} + \\frac{0.35}{8} + \\frac{0.32}{10}$
  $\\text{not very } B = \\frac{1-0.04}{2} + \\frac{1-0.16}{4} + \\frac{1-0.36}{6} + \\frac{1-0.64}{8} + \\frac{1-1}{10} = \\frac{0.96}{2} + \\frac{0.84}{4} + \\frac{0.64}{6} + \\frac{0.36}{8} + \\frac{0.0}{10}$

* **i) A and very B:**
  $= \\min(\\mu_A(x), \\mu_{\\text{very } B}(x)) = \\frac{\\min(0.5, 0.04)}{2} + \\frac{\\min(0.25, 0.16)}{4} + \\frac{\\min(0.17, 0.36)}{6} + \\frac{\\min(0.125, 0.64)}{8} + \\frac{\\min(0.1, 1.0)}{10}$
  $= \\frac{0.04}{2} + \\frac{0.16}{4} + \\frac{0.17}{6} + \\frac{0.125}{8} + \\frac{0.1}{10}$ `[M2, A2]`

* **ii) Somewhat A or not very B:**
  $= \\max(\\mu_{\\text{somewhat } A}(x), \\mu_{\\text{not very } B}(x))$
  $= \\frac{\\max(0.71, 0.96)}{2} + \\frac{\\max(0.5, 0.84)}{4} + \\frac{\\max(0.41, 0.64)}{6} + \\frac{\\max(0.35, 0.36)}{8} + \\frac{\\max(0.32, 0.0)}{10}$
  $= \\frac{0.96}{2} + \\frac{0.84}{4} + \\frac{0.64}{6} + \\frac{0.36}{8} + \\frac{0.32}{10}$ `[M2, A2]`"""
    },
    {
        "question_no": "Question 2(b)",
        "topic": "Parameterized Triad Combination Models",
        "marks": "4",
        "question": """Let X, Y and Z be fuzzy sets with the fuzzy proposition:
$$\\text{"(x is not X and z is Z) or (y is not Y)"}$$
Determine the symbolic membership function formulation by using the following normative combinations:

i) The combination of basic fuzzy operators for fuzzy t-norm, s-norm, and complement.
ii) The combination of Algebraic Product ($t_{ap}(a,b) = ab$) for fuzzy t-norm, Einstein Sum ($s_{es}(a,b) = \\frac{a+b}{1+ab}$) for fuzzy s-norm, and the basic operator for fuzzy complement.""",
        "answer": """**ANSWER SCHEME:**
* **i) Basic Operators:**
  $= \\max\\{[\\min(1 - \\mu_X(x), \\mu_Z(z))], 1 - \\mu_Y(y)\\}$ `[M1, A1]`
* **ii) Algebraic Product & Einstein Sum:**
  Let $T = (1 - \\mu_X(x)) \\cdot \\mu_Z(z)$ and $S = 1 - \\mu_Y(y)$
  $= \\frac{T + S}{1 + T \\cdot S} = \\frac{((1 - \\mu_X(x)) \\cdot \\mu_Z(z)) + (1 - \\mu_Y(y))}{1 + ((1 - \\mu_X(x)) \\cdot \\mu_Z(z) \\cdot (1 - \\mu_Y(y)))}$ `[M1, A1]`"""
    }
]