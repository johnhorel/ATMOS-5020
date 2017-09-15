'''Fibonacci Sequence using Lists'''
fib_sequence = []
for i in xrange(10):
    if i < 2:
        fib_sequence.append(i)
        continue

    fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])

# Print the results
print 'The Fibonacci Sequence is:\n%s ...' % ','.join(map(str, fib_sequence))
