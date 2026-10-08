from sys import argv


def parse_genotype_counts(vcf_path, target_chrom="2", target_pos="136608646"):
    wt = 0
    het = 0
    hom = 0

    with open(vcf_path, "r", encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("#"):
                continue

            cols = line.strip().split("\t")
            chrom = cols[0]
            pos = cols[1]

            if chrom == target_chrom and pos == target_pos:
                for geno in cols[9:]:
                    alleles = geno[0:3]
                    if alleles == "0/0":
                        wt += 1
                    elif alleles == "0/1":
                        het += 1
                    elif alleles == "1/1":
                        hom += 1

    return wt, het, hom


def calculate_frequency(wt, het, hom):
    freq = None
    total_alleles = (wt + het + hom) * 2
    if total_alleles != 0:
        freq = (2 * hom + het) / total_alleles
    return freq


def format_frequency_message(freq):
    message = None
    if freq is not None:
        message = f"The frequency of the rs4988235 SNP is: {round(freq, 3)}"
    return message


def main():
    if len(argv) < 2:
        raise SystemExit("Usage: python exercises/day3/vcf_snooper.py INPUT.vcf")

    wt, het, hom = parse_genotype_counts(argv[1])
    freq = calculate_frequency(wt, het, hom)
    message = format_frequency_message(freq)

    if message is None:
        print("The target locus was not found in the file.")
    else:
        print(message)


if __name__ == "__main__":
    main()

