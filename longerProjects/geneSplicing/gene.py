def setup(A, B, C, T):
    # Create all the necessary variables
    a_solution = [float(A), 0]    
    b_solution = [0, float(B)]
    c = float(C)
    t = float(T)
    iteration = 0
    target_ratio = float(A) / float(B)

    while True:

        # Total of solution A
        a_total = a_solution[0] + a_solution[1]

        # Puts c mL from solution A to B
        b_solution = [b_solution[0] + c * (a_solution[0] / a_total), b_solution[1] + c * (a_solution [1] / a_total)]
        a_solution = [a_solution[0] - c * (a_solution[0] / a_total), a_solution[1] - c * (a_solution[1] / a_total)] 
        
        #Total of solution B
        b_total = b_solution[0] + b_solution[1]

        # Puts c mL from solution B to A
        a_solution = [a_solution[0] + c * (b_solution[0] / b_total), a_solution[1] + c * (b_solution [1] / b_total)]
        b_solution = [b_solution[0] - c * (b_solution[0] / b_total), b_solution[1] - c * (b_solution[1] / b_total)]

        iteration += 1

        a_mix = a_solution[0] / a_solution[1]
        b_mix = b_solution[0] / b_solution[1]

        # Tolerance and showing iterations
        if abs(a_mix - target_ratio) < t and abs(b_mix - target_ratio) < t:
            print(iteration)
            break

with open("gene_splicing_test.dat") as fhand:
    flist = [line.split() for line in fhand]
    for i in flist:
        if len(i) != 4:
            continue
        else:
            A, B, C, T = i
            setup(A, B, C, T)


