import sys

nard_maf_file = "hg19_NARD+1KGP3.txt"

pos_count_map = {}
with open(nard_maf_file) as nmf:
	next(nmf)
	for line in nmf:
		line = line.strip()
		parts = line.split('\t')
		pos = parts[0] + ":" + parts[1] + ":" + parts[2]
		if pos not in pos_count_map:
			pos_count_map[pos] = 0
		pos_count_map[pos] = pos_count_map[pos] + 1

print "id chr position a0 a1 TYPE EAS ALL"
with open(nard_maf_file) as nmf:
	next(nmf)
	for line in nmf:
		line = line.strip()
		parts = line.split('\t')
		if (parts[3] == "-"):
			parts[3] = "."
		if (parts[4] == "-"):
			parts[4] = "."

		type = "Biallelic_VAR"
		if pos_count_map[parts[0] + ":" + parts[1] + ":" + parts[2]] > 1:
			type = "Multiallelic_VAR"
		print parts[0] + ":" + parts[1] + ":" + parts[3] + ":" + parts[4] + " " + parts[0] + " " + parts[1] + " " + parts[3] + " " + parts[4] + " " + type + " " + parts[5] + " " + parts[5]
