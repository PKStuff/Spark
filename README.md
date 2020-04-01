# How to Run

## Clone the repo 
  git clone https://github.com/PKStuff/Spark.git

## Create virtual environment
   * python3 -m venv env_name
   * source env_name/bin/activate

## Installation
  * Installation of Java.
    *  Download Java .tgz file and extract in some folder like /usr/jdk
    *  Add JAVA_HOME and PATH in .profile
        e.g. 
        - export JAVA_HOME=/usr/jdk/jdk1.8.0_241/jre
        - export PATH=$PATH:/usr/jdk/jdk1.8.0_241/jre/bin
  * Install PySpark using Terminal
    
    - pip install pyspark


## Go to src and run
  * spark-submit trendingLang.py
