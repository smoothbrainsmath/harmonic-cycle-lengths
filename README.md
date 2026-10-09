# Sharp Harmonic Cycle-Length Inequalities for Complete Multipartite Graphs

**Research preprint · October 2026 · Extremal graph theory**

[**Read the paper (PDF)**](harmonic_cycle_multipartite.pdf) · [LaTeX source](harmonic_cycle_multipartite.tex)

This repository contains a research note on the Erdős–Hajnal harmonic cycle-length conjecture. It establishes a sharp inequality for **all complete multipartite graphs**, together with two additional results for restricted classes of general graphs. The unrestricted conjecture is **not** claimed to be solved.

## The problem

For a finite simple graph \(G\), let \(\mathcal C(G)\) be the set of its **distinct** cycle lengths, and define

$$
s(G)=\sum_{\ell\in\mathcal C(G)}\frac1\ell,
\qquad
B_d=\sum_{j=2}^{d}\frac1{2j}=\frac{H_d-1}{2}.
$$

A sharp form of Erdős's conjecture asks whether every \(n\)-vertex graph satisfying \(n\ge 2d\) and \(e(G)\ge d(n-d)\) obeys \(s(G)\ge B_d\), with equality only for \(K_{d,n-d}\).

## Main theorem

If \(d\ge 2\), \(n\ge 2d\), and \(G\) is a **complete multipartite graph** on \(n\) vertices, then

$$
\boxed{e(G)>(d-1)(n-d+1)\quad\Longrightarrow\quad s(G)\ge B_d.}
$$

Equality holds **if and only if** \(G\cong K_{d,n-d}\). The strict edge threshold is sharp within this graph family: \(K_{d-1,n-d+1}\) meets the threshold with equality but has a smaller harmonic cycle-length sum.

The proof includes an exact description of the cycle-length spectrum of complete multipartite graphs. The manuscript also establishes:

- A bounded-vertex-cover case under the hypotheses \(\tau(G)\le d\), \(n\ge 2d+\binom d2\), and \(e(G)\ge d(n-d)\).
- A near-balanced case for **arbitrary graphs** when \(d\ge4\), \(2d\le n\le 2d+4\), and \(e(G)\ge d(n-d)\).

Both supporting theorems give the same lower bound and equality characterization.

## Files

| File | Contents |
| --- | --- |
| [`harmonic_cycle_multipartite.pdf`](harmonic_cycle_multipartite.pdf) | Typeset paper and proofs |
| [`harmonic_cycle_multipartite.tex`](harmonic_cycle_multipartite.tex) | Editable LaTeX source |
| [`verify_multipartite.py`](verify_multipartite.py) | Exact-arithmetic checks of the multipartite theorem |
| [`verify_graph_atlas.py`](verify_graph_atlas.py) | Graph Atlas checks of the original conjectured inequality for graphs of order at most seven |

## Reproduce

Compile the paper with a LaTeX installation supporting `pdflatex`:

```bash
pdflatex -interaction=nonstopmode -halt-on-error harmonic_cycle_multipartite.tex
pdflatex -interaction=nonstopmode -halt-on-error harmonic_cycle_multipartite.tex
```

Run the finite checks with Python 3:

```bash
python verify_multipartite.py
python -m pip install networkx numpy
python verify_graph_atlas.py
```

At the time of this README, the scripts report **26,018 qualifying multipartite parameter tests** (up to 21 vertices) and **1,194 qualifying Graph Atlas tests** (up to 7 vertices), with no violations. These checks are **finite sanity tests, not substitutes for proof**.

## Context and status

Montgomery, Milojević, Pokrovskiy, and Sudakov (2026) proved the corresponding stronger threshold for **general graphs when \(d\) is sufficiently large**. The main result here treats **all \(d\ge2\)**, but only for complete multipartite graphs. It does not settle the outstanding general cases.

**Status:** Working preprint. The proofs and code are available for scrutiny, but independent specialist review and a comprehensive novelty check are still needed. In particular, no priority claim is made that these restricted-family statements were previously unknown. Corrections and references to prior work are welcome through GitHub issues.

## References

- R. Montgomery, A. Milojević, A. Pokrovskiy, and B. Sudakov, *Minimising the harmonic sum of cycle lengths* (2026), [arXiv:2609.26401](https://arxiv.org/abs/2609.26401).
- [Erdős Problems — Problem #65](https://www.erdosproblems.com/65).
- Additional graph-theoretic references are listed in the paper.

> **Before academic submission:** Replace the author/affiliation placeholder in the LaTeX source with accurate details and seek an independent proof and originality review.
