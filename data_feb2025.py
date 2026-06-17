questions = [
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
        "question": """State a difference between the atomic fuzzy proposition and compound fuzzy proposition. Give an appropriate example to illustrate the difference.""",
        "answer": """**ANSWER SCHEME:**
* **Atomic Fuzzy Proposition:** An atomic fuzzy proposition is a single (simple) statement in fuzzy logic involving a single linguistic variable assigned to a single fuzzy label. `[B1]`
  * *Example:* "Temperature is hot" `[M1]`
* **Compound Fuzzy Proposition:** A statement consisting of multiple atomic fuzzy propositions linked using connectivity mapping rules (such as and, or, not). `[B1]`
  * *Example:* "Temperature is hot AND humidity is low" `[M1]`"""
    },
    {
        "question_no": "Question 2(a)(i)",
        "topic": "Algebraic Sum Hedge Applications",
        "marks": "5",
        "question": """Let a universe of smartphones be defined as $X = \\{x_1, x_2, x_3, x_4, x_5\\}$. The linguistic variables of these smartphones are defined as cheap and powerful, where:
$$\\text{cheap} = \\frac{0.35}{x_1} + \\frac{1}{x_2} + \\frac{0.5}{x_3} + \\frac{0.7}{x_4} + \\frac{0.6}{x_5}$$
$$\\text{powerful} = \\frac{0.9}{x_1} + \\frac{0.2}{x_2} + \\frac{0.7}{x_3} + \\frac{0.5}{x_4} + \\frac{0.6}{x_5}$$

Suppose the linguistic hedges "very" and "somewhat" are represented by $\\mu_{very}(x) = \\mu(x)^2$ and $\\mu_{somewhat}(x) = \\sqrt{\\mu(x)}$, respectively. Determine the fuzzy set "somewhat cheap or not very powerful" using the combination of basic operator for fuzzy complement and Algebraic Sum ($s_{as}(a,b) = a + b - ab$) for the s-norm.""",
        "answer": """**ANSWER SCHEME:**
* Constituent value vectors:
  $\\mu_{\\text{somewhat cheap}} = \\frac{\\sqrt{0.35}}{x_1} + \\frac{\\sqrt{1}}{x_2} + \\frac{\\sqrt{0.5}}{x_3} + \\frac{\\sqrt{0.7}}{x_4} + \\frac{\\sqrt{0.6}}{x_5} = \\frac{0.5916}{x_1} + \\frac{1.0}{x_2} + \\frac{0.7071}{x_3} + \\frac{0.8367}{x_4} + \\frac{0.7746}{x_5}$ `[M1]`
  $\\mu_{\\text{not very powerful}} = \\frac{1-0.9^2}{x_1} + \\frac{1-0.2^2}{x_2} + \\frac{1-0.7^2}{x_3} + \\frac{1-0.5^2}{x_4} + \\frac{1-0.6^2}{x_5} = \\frac{0.19}{x_1} + \\frac{0.96}{x_2} + \\frac{0.51}{x_3} + \\frac{0.75}{x_4} + \\frac{0.64}{x_5}$ `[M1]`
* Merging entry-wise via Algebraic Sum ($a + b - ab$):
  * $x_1: 0.5916 + 0.19 - (0.5916 \\times 0.19) = 0.6692$
  * $x_2: 1.0 + 0.96 - (1.0 \\times 0.96) = 1.0$
  * $x_3: 0.7071 + 0.51 - (0.7071 \\times 0.51) = 0.8565$
  * $x_4: 0.8367 + 0.75 - (0.8367 \\times 0.75) = 0.9592$
  * $x_5: 0.7746 + 0.64 - (0.7746 \\times 0.64) = 0.9189$ `[M1]`
* Final evaluation array:
  $= \\frac{0.6692}{x_1} + \\frac{1}{x_2} + \\frac{0.8565}{x_3} + \\frac{0.9592}{x_4} + \\frac{0.9189}{x_5}$ `[A2]`"""
    },
    {
        "question_no": "Question 2(a)(ii)",
        "topic": "Dubois-Prade T-Norm Multi-Criteria Decisions",
        "marks": "5",
        "question": """Ali is looking for a smartphone with "cheap and very powerful" characteristics. Using the Dubois-Prade class $t_{DPC}(a,b) = \\frac{ab}{\\max(a,b,0.6)}$ for the fuzzy intersection, determine which smartphone Ali should purchase.""",
        "answer": """**ANSWER SCHEME:**
Evaluating $t_{DPC}(\\mu_{\\text{cheap}}, \\mu_{\\text{very powerful}})$ entry-wise:
* $x_1: \\frac{0.35 \\times 0.81}{\\max(0.35, 0.81, 0.6)} = \\frac{0.2835}{0.81} = 0.35$
* $x_2: \\frac{1.0 \\times 0.04}{\\max(1.0, 0.04, 0.6)} = \\frac{0.04}{1.0} = 0.04$
* $x_3: \\frac{0.5 \\times 0.49}{\\max(0.5, 0.49, 0.6)} = \\frac{0.245}{0.6} = 0.4083$
* $x_4: \\frac{0.7 \\times 0.25}{\\max(0.7, 0.25, 0.6)} = \\frac{0.175}{0.7} = 0.25$
* $x_5: \\frac{0.6 \\times 0.36}{\\max(0.6, 0.36, 0.6)} = \\frac{0.216}{0.6} = 0.36$ `[M2, A1]`

$$\\text{Intersection Set} = \\frac{0.35}{x_1} + \\frac{0.04}{x_2} + \\frac{0.4083}{x_3} + \\frac{0.25}{x_4} + \\frac{0.36}{x_5}$$
**Decision:** Ali should select smartphone $x_3$ as it yields the maximum membership grade value ($0.4083$). `[A1]`"""
    }
]