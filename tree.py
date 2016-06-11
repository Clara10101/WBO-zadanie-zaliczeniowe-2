from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
from Bio import AlignIO
from Bio.Phylo.Consensus import *
from Bio import Phylo

#drzewa konsensusowe dla wszystkich klastrow
#uliniowienia wielosekwencyjne do rekonstrukcji drzewa

def tree(from_cluster,to_cluster, grupa):

    consensus_trees = []

    for i in [x for x in range(from_cluster,to_cluster)]:

        msa = AlignIO.read('msa\msa_rodzina_' + str(i)+ '_s.fasta', 'fasta')
        print i
        calculator = DistanceCalculator('identity')

        try:
            dm = calculator.get_distance(msa)
            constructor = DistanceTreeConstructor(calculator, 'nj')
            trees = bootstrap_trees(msa, 50, constructor)

            trees_list = list(trees)
            not_included = set([])

            for j in range(len(trees_list)):
                target_tree = trees_list[j]
                support_tree = get_support(target_tree, trees_list)

            for node in support_tree.get_nonterminals():
                if node.confidence < 50:
                    not_included.add(j)

            trees = [trees_list[k] for k in range(len(trees_list)) if k not in not_included]

            if len(trees) > 0:
                consensus_trees.append(majority_consensus(trees))

        except:
            ValueError

    Phylo.write(consensus_trees,"drzewa_wynikowe_" + str(grupa),"newick")


