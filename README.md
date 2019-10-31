find data/ -type f | xargs -n1 -I{} echo 'cat {} | python parse.py' | bash | sort > top-catrgories.csv
