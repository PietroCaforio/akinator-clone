.PHONY: data deps

data:
	@echo "Downloading data"
	mkdir -p data
	cd data && \
	wget https://storage.googleapis.com/pantheon-public-data/person_2025_update.csv.bz2 && \
	bzip2 -d person_2025_update.csv.bz2

deps:
	@echo "creating environment"
	conda env create -f environment.yml && \
	conda activate akinator-clone