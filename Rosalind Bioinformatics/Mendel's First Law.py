# Sample Dataset: 2 2 2
# Sample Output: 0.78333

homo_dominant = int(input('int 1: '))
hetero_dominant = int(input('int 2: '))
homo_recessive = int(input('int 3: '))

# determine probability of selecting any of the 3 gene types
total = homo_dominant + hetero_dominant + homo_recessive

# P(dom) = P(total) - !P(dom), therefore P(recessive) = !P(dom)
# 3 types of parental combinations result in child having recessive trait.
P_2homo = (homo_recessive/total)*((homo_recessive - 1) / (total-1))
P_homo_hetero = (hetero_dominant/total)*(homo_recessive / (total - 1))
P_hetero_hetero = (hetero_dominant/total)*((hetero_dominant - 1)/(total - 1) * 0.25)

# total probability of recessive gene
P_recessive = P_2homo + P_homo_hetero + P_hetero_hetero

# reminder: P(A) = 1 - !P(A)
P_dom = 1 - P_recessive
print(P_dom)
