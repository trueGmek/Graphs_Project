# NOTES

In this file there will be notes from the slides for the project, the porpoise of this is to keep the knowledge in one place.



## 1. COLOR REFINEMENT



## 

###### How do we define a partition:

​	With a k-colouring **α** of G, we associate the following *partition of nodes into colour classes: **πα= {αc ||αc|≥ 1}***. 

###### Partition Refinements:

For two partitions **π** and **ρ** of V, we say that **ρ** reﬁnes **π** if for all *u,v ∈ V: u ≡ _ρ v =⇒ u ≡ _π v.*

If in addition **π** is not equal to **ρ**, then **ρ** strictly reﬁnes **π**.

![image-20200310175133816](C:\Users\Piotrek\AppData\Roaming\Typora\typora-user-images\image-20200310175133816.png)

Partition **π** of V(G) is stable if colouring of the cells is a stable colouring



A stable partition π of V(G) is a coarsest stable partition if there is no stable partition ρ of V(G) such that π strictly reﬁnes ρ.

Analogously, for a given start partition π0, we deﬁne the coarsest stable partition that reﬁnes π0.



For every partition π0 of V(G), there is a unique coarsest stable partition of V(G) that reﬁnes π0, which is exactly the partition given by colour reﬁnement, when starting with π0.

## 2. BRANCHING

- There is a graph, which is a union of two graphs G and H, with stable colouring **α** and it does not define a **bijection**.

- There exists colour class **C** with k vertices of G and k vertices of $ 2 \leq k $. 

  Denote $C_g = C \cap V(G)$ and $C_h = C \cap V(H)$ .

- Choose $x \in C_g$. Every colour preserving isomorphism $f$ has $f(x) = y  $ for some $y \in C_h$
- Try out all possibilities for $f(x)$ (gives k branches of a recursive algorithm) : There exists a colour preserving isomorphism if and only if a colour preserving isomorphism will be found in at leas one branch
- In each branch, the choice $f(x) = y $ is encoded by giving both vertices a new, unique colour.
- Given the start colouring, we can apply colouring refinement  again, and continue recursively until either an isomorphism is found, or it is a concluded that no isomorphism with $f(x) = y$ exists.

![image-20200310192333109](C:\Users\Piotrek\AppData\Roaming\Typora\typora-user-images\image-20200310192333109.png)

PSEUDO CODE:

Subroutine$CountIsomorphism(D,I)$:

Input: **D** and **I** are equal length sequences of vertices of **G** and **H** respectively.

Output: The number of isomorphisms form **G** to **H** that follow **D**,**I**.



Compute the coarsest stable colouring **β** that reﬁnes $α(D,I)$;
if **β** is balanced:
	return 0
if **β** defines a bijection:
	return 1
Choose a colour class C with $|C| \geq $ 4.
Choose $x \in C \cap V(G)$

$num = 0$

for all $y \in C \cap V(H):$

​	$num := num + CountIsomorphism(D+x,I+y)$

return num



###### What does it mean that  **α** is balanced

A k-colouring **α** of $G\cup H$ is **balanced** if for every colour $c \in \{ 1,...,k \}$, it holds that $|\alpha^c \cap V(G)| = |\alpha^c \cap V(H)|$ 

###### When does **α** define a bijection

A k-colouring **α** of $G \cup H$ deﬁnes a bijection $f$ if for every colour $c \in \{ 1, ..., k\}$, it holds that $|\alpha^c \cap V(G)| = |\alpha^c \cap V(H)| = 1$ 

In this case, the bijection $f : V(G) → V(H)$ is chosen such that for all $v ∈ V(G), α(v) = α(f (v))$.





