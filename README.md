# Apriori-Algorithm
Apriori.py is a Python file which implements Apriori Algorithm for Frequent item set mining.

Methods details are following:
- `getSubSet(S)`: return the list of subsets of S, and the number of elements in each subset is `len(S) - 1` 
- `isSubSetExist(tar, L)`: calculate if each value in L is in tar,1 exist,0 the opposite, the purpose of the method is to get value to prune.
- `Apriori(tar, thr, le)`: the main method of this file, the type of tar is a dictionary, whose key is each transation's index and value is transation detail, `thr` express support threshold, `le` express the items' number of each set
