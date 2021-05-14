# ait_nlu

## Introduction

The project basically deals with building a corpus of the words and sentences said by children who are aged between 3 to 4 years old. 
The first step was to collect the words said by the children by either visiting schools and study the behavior of the children. Due the current situation, i.e. pandemic, we were not able to. 

So, we decided to look for story books that were intented for the children aged 3 to 4 years. The books available online for children ranged from 2 to 5 years old. Filtering the books, we got around 10+ books to create the corpus and the Dependency Parse Tree(DPT).

The DPT is then used to identify the common words said by the children. 

Follow the below given steps to run the application on your machine.

## To convert PDT to text
Please do follow this. However, please take a note that this method doesn't work with every file.

### run this container
```bash
docker-compose up --build -d
```
### COPY PDF
copy PDF files to /dataset

### compute the DPT
```bash
docker-compose exec app python ./main.py
```

### Output
see output files at /output

## To compute the DPT

### run this app
```bash
docker-compose up --build -d
```

### COPY txt file
copy txt files to /data_for_dpt

### compute the DPT
```bash
docker-compose exec app python ./dpt/s0_find_dpt.py
```

### Output
see output files at /output_dpt

## To read all result

### run this app
```bash
docker-compose up --build -d
```

### reading
for All DPT
```bash
docker-compose exec app python ./dpt/s1_read_all_dpt_file.py
```

for distinct DPT
```bash
docker-compose exec app python ./dpt/s1_read_dpt_file.py
```



## End Note:
The books obtained online were limited. To improve the results, visiting pre-schools  and studying the behavior of children aged 3 - 4 years old to obtain the sentences will improve the corpus and the DPT.  