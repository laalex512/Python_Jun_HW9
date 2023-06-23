import quadratic_equation as qe

if __name__ == '__main__':
    filename = 'numbers'
    qe.csv_gen(filename, (5, 10))
    qe.passing_arguments(filename)
