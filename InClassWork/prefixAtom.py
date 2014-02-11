def is_prefix_atom(List,A):
	return not[B for B in List if A.startwith(B) and A !=B]

def prefix_atom(List):
	return [A for A in List if is_prefix_atom(List, A)]

def prefix_dictionary(Dictionary):
	for A in K:
		Dictionary[A] = [B for B in L if B.startwith(A)]