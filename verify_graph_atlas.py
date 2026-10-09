"""Exact finite checks for the Erdős–Hajnal harmonic cycle-length inequality.
Uses NetworkX's graph atlas, which contains every graph on <=7 vertices
up to isomorphism. Verification is finite evidence only, not a proof for all n.
"""
import networkx as nx
from fractions import Fraction
from collections import Counter

def cycle_lengths(G):
    # DFS, every closed simple walk visits a unique set; length only matters.
    N=G.number_of_nodes()
    a=nx.to_numpy_array(G,dtype=int)
    lengths=set()
    for start in range(N):
        stack=[(start, 1<<start, (start,))]
        while stack:
            x, visited, path=stack.pop()
            if len(path)>=3 and a[x,start]:
                lengths.add(len(path))
            for y in range(start+1,N):
                if y not in path and a[x,y]:
                    stack.append((y,visited|(1<<y),path+(y,)))
    return lengths

def s_value(G):
    return sum((Fraction(1,L) for L in cycle_lengths(G)),Fraction(0,1))

def target(d):
    return sum((Fraction(1,2*j) for j in range(2,d+1)),Fraction(0,1))

def verify_atlas():
    checked=Counter()
    equality=Counter()
    bad=[]
    for G in nx.graph_atlas_g():
        n=G.number_of_nodes()
        if n<4: continue
        m=G.number_of_edges()
        for d in range(2,n//2+1):
            if m<d*(n-d):continue
            checked[(n,d)]+=1
            v=s_value(G)
            if v<target(d):bad.append((n,d,m,v,'inequality'))
            if v==target(d):
                equality[(n,d)]+=1
                if not nx.is_isomorphic(G,nx.complete_bipartite_graph(d,n-d)):
                    bad.append((n,d,m,v,'nonunique'))
    print('Atlas tests:',sum(checked.values()),'graphs meeting threshold')
    print('Parameter cells:',len(checked),'Counterexamples:',len(bad))
    print('Equality examples:',sum(equality.values()),'equalities per cell:',dict(sorted(equality.items())))
    print('BAD EXAMPLES:',bad[:10])

if __name__=='__main__':
    verify_atlas()
