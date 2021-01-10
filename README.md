# INF221 Term Paper Team 45

Term paper on benchmarking sorting algorithm, This article is part of INF221 course at NMBU. The objective of this paper is to show the results of performing benchmark experiments on sorting algorithms. We implemented several sorting algorithms and compared them in terms of their run-time. The algorithms were investigated into four categories: quadratic (Insertion-Sort and Bubble-Sort), sub-quadratic (Merge-Sort and Quick-Sort), combined Merge-Insertion-Sort and built-in (Python-Sort and Numpy-Sort) algorithms. The input data were lists of float values with sizes from $2^{4}$ to $2^{14}$ in the form of $3$ different ordering permutations: sorted, reversed and random ordering. The study was conducted using Python programming language and several libraries like Numpy, Scipy, Pandas and Matplotlib. Quick-Sort showed very similar run-time in sorting reversed and sorted data. Merge-Sort also showed the same observation. For finding an explanation for these behaviours, we investigated these observations further by measuring the number of comparisons that Merge-Sort and Quick-Sort executed in sorting the data. The study also shows that Numpy-Sort and Python-Sort are faster than all other implemented algorithms. Bubble-Sort is the slowest sorting algorithm among all these algorithms. Additionally, we implemented a combined Merge-Insertion-Sort which performed slightly faster than Merge-Sort. A challenging question is left open that is why Python-Sort is $10$ times faster than our implementation of Merge-Insertion-Sort. 

Final report: https://github.com/mhmdrdwn/sort-algorithms/blob/main/report/term_paper.pdf

Implementations of different algorithms: https://github.com/mhmdrdwn/sort-algorithms/blob/main/code/algorithms.py

Benchmark setup: https://github.com/mhmdrdwn/sort-algorithms/blob/main/code/run_benchmarks.py

Visualization of results: https://github.com/mhmdrdwn/sort-algorithms/blob/main/analysis/visualize.ipynb

Analytical interpretation: https://github.com/mhmdrdwn/sort-algorithms/blob/main/analysis/nr_comparisons.ipynb
