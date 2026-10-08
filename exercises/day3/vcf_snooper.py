from sys import argv
with open(argv[1], 'r') as fh:  # Open the file given as the first argument in the command line

    wt  = 0      # Remember to initialize the counting outside the loop, otherwise it will reset for every iteration
    het = 0
    hom = 0

    for line in fh:
        if not line.startswith('#'):
            cols  = line.strip().split('\t')
            chrom = cols[0]                          # This is the chromosome
            pos   = cols[1]                          # This is the position of the SNP on the chromsome
            if chrom == '2' and pos == '136608646':  # Check if chrom and pos match. Notice the type! python reads all as strings!
                for geno in cols[9:]:                # Loop over the items in cols, starting from index 9
                    alleles = geno[0:3]              # Here we take the first 3 characters in the string geno
                    if alleles == '0/0':             # Conditional to test whether alleles matches '0/0'
                        wt += 1                      # If match, wt is increased by 1
                    elif alleles == '0/1':
                        het += 1
                    elif alleles == '1/1':        
                        hom += 1
                        
    freq = (2*hom + het)/((wt+hom+het)*2)                       # Calculate the alllele frequency
    print('The frequency of the rs4988235 SNP is: '+str(round(freq,3)))  # Print a nice message and format freq to a string before printing

