questions = [
    {
        "question_no": "Question 1(a)",
        "topic": "Linguistic Foundations Assessment",
        "marks": "4",
        "question": """Determine whether each of the following statements is TRUE or FALSE.

i) Linguistic variables can have values that are expressed as words from natural languages.
ii) A compound fuzzy proposition is a statement which can be described as “x is A”.
iii) The atomic fuzzy proposition must be considered as a fuzzy relation.
iv) Fuzzy logic provides a foundation for approximate reasoning with imprecise propositions using fuzzy set theory as the principal tool.""",
        "answer": """**ANSWER SCHEME:**
i) **TRUE** `[B1]`
ii) **FALSE** `[B1]`
iii) **FALSE** `[B1]`
iv) **TRUE** `[B1]`"""
    },
    {
        "question_no": "Question 1(b)",
        "topic": "General Hypothetical Syllogism Architectures",
        "marks": "4",
        "question": """Briefly explain the General Hypothetical Syllogism in fuzzy logic. Then give ONE (1) example of the proposition in fuzzy logic.""",
        "answer": """**ANSWER SCHEME:**
* **Explanation:** Given fuzzy relation $A \\rightarrow B$ in $U \\times V$ (which represents the premise IF x is A THEN y is B) and fuzzy relation $B' \\rightarrow C$ in $V \\times W$ (which represents the premise IF y is B' THEN z is C), a fuzzy relation $A \\rightarrow C'$ in $U \\times W$ (which represents the conclusion IF x is A THEN z is C') is derived through composition mappings. `[B2]`
* **Example:**
  * Premise 1: IF the speed is high, THEN the risk of accident is high.
  * Premise 2: IF the risk of accident is high, THEN the insurance premium is costly.
  * Conclusion: IF the speed is high, THEN the insurance premium is costly. `[M2]`
*(Accept any logically coherent chaining setup)*"""
    },
    {
        "question_no": "Question 2(a)",
        "topic": "Complex Logical Proposition Mappings",
        "marks": "4",
        "question": """Let A, B and C be fuzzy sets. Determine the membership function for the following fuzzy proposition where “and”, “or” and “not” are defined by the basic fuzzy operations:
$$\\text{"Not (a is A or b is B) and (a is not A or c is C)"}$$""",
        "answer": """**ANSWER SCHEME:**
Transforming logical strings into operational base structures:
$= \\mu_{\\overline{A \\vee B} \\wedge (\\overline{A} \\vee C)}(a, b, c)$
$= \\min\\left[ \\mu_{\\overline{A \\vee B}}(a,b), \\mu_{\\overline{A} \\vee C}(a,c) \\right]$ `[M2]`
$= \\min\\left[ \\left(1 - \\max(\\mu_A(a), \\mu_B(b))\\right), \\max\\left(1 - \\mu_A(a), \\mu_C(c)\\right) \\right]$ `[A2]`"""
    },
    {
        "question_no": "Question 2(b)",
        "topic": "Hedge Filtering via T-Norm Product Mix",
        "marks": "8",
        "question": """Let A and B be discrete fuzzy sets defined on $X = \\{x_1, x_2, x_3, x_4\\}$, where:
$$A = \\frac{0.4}{x_1} + \\frac{0.7}{x_2} + \\frac{0.3}{x_3} + \\frac{0.8}{x_4}$$
$$B = \\frac{0.4}{x_1} + \\frac{0.7}{x_2} + \\frac{0.3}{x_3} + \\frac{0.5}{x_4}$$

Suppose the linguistic hedges “very”, “somewhat” and “not” are represented by $\\mu_{very}(x) = \\mu(x)^2$, $\\mu_{somewhat}(x) = \\sqrt{\\mu(x)}$, and $\\mu_{not}(x) = 1 - \\mu(x)$. Using a combination of the Algebraic Product $t_{ap}(a,b) = ab$ for the t-norm, basic fuzzy union, and basic fuzzy complement, determine the fuzzy set for:
i) Very A and somewhat B.
ii) Somewhat not A or not somewhat B.""",
        "answer": """**ANSWER SCHEME:**
* **i) Very A and somewhat B:**
  $\\mu_{\\text{very } A} = \\frac{0.16}{x_1} + \\frac{0.49}{x_2} + \\frac{0.09}{x_3} + \\frac{0.64}{x_4}$ `[M1]`
  $\\mu_{\\text{somewhat } B} = \\frac{\\sqrt{0.4}}{x_1} + \\frac{\\sqrt{0.7}}{x_2} + \\frac{\\sqrt{0.3}}{x_3} + \\frac{\\sqrt{0.5}}{x_4} = \\frac{0.6325}{x_1} + \\frac{0.8367}{x_2} + \\frac{0.5477}{x_3} + \\frac{0.7071}{x_4}$ `[M1]`
  Apply Algebraic Product $a \\cdot b$:
  $= \\frac{0.16 \\times 0.6325}{x_1} + \\frac{0.49 \\times 0.8367}{x_2} + \\frac{0.09 \\times 0.5477}{x_3} + \\frac{0.64 \\times 0.7071}{x_4} = \\frac{0.1012}{x_1} + \\frac{0.4100}{x_2} + \\frac{0.0493}{x_3} + \\frac{0.4525}{x_4}$ `[M1, A1]`

* **ii) Somewhat not A or not somewhat B:**
  $\\mu_{\\text{somewhat not } A} = \\frac{\\sqrt{1-0.4}}{x_1} + \\frac{\\sqrt{1-0.7}}{x_2} + \\frac{\\sqrt{1-0.3}}{x_3} + \\frac{\\sqrt{1-0.8}}{x_4} = \\frac{0.7746}{x_1} + \\frac{0.5477}{x_2} + \\frac{0.8367}{x_3} + \\frac{0.4472}{x_4}$ `[M1]`
  $\\mu_{\\text{not somewhat } B} = \\frac{1-0.6325}{x_1} + \\frac{1-0.8367}{x_2} + \\frac{1-0.5477}{x_3} + \\frac{1-0.7071}{x_4} = \\frac{0.3675}{x_1} + \\frac{0.1633}{x_2} + \\frac{0.4523}{x_3} + \\frac{0.2929}{x_4}$ `[M1]`
  Apply basic union $\\max(a, b)$:
  $= \\frac{\\max(0.7746, 0.3675)}{x_1} + \\frac{\\max(0.5477, 0.1633)}{x_2} + \\frac{\\max(0.8367, 0.4523)}{x_3} + \\frac{\\max(0.4472, 0.2929)}{x_4}$
  $= \\frac{0.7746}{x_1} + \\frac{0.5477}{x_2} + \\frac{0.8367}{x_3} + \\frac{0.4472}{x_4}$ `[M1, A1]`"""
    }
]