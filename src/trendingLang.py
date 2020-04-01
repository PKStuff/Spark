from pyspark import SparkContext, SparkConf
import sys
sys.path.insert(0, '.')
from commons.Utils import Utils
from datetime import datetime


def get_data(line: str):
    return "{}".format(Utils.COMMA_DELIMITER.split(line)[6])

if __name__ == '__main__':
    conf = SparkConf().setAppName("StackOverflow").setMaster("local[5]")
    sc = SparkContext(conf = conf)

    line_data = sc.textFile("in/survey_results_public.csv")


    prof_coders = line_data.filter(lambda line: line.split(',')[1] == "I am a developer by profession")

    data = prof_coders.map(get_data)

    wordCounts = data.countByValue()

    folder_name = str(datetime.today())

    data.saveAsTextFile("out/" + folder_name + "/professional.text")

    for word, count in sorted(wordCounts.items(), key=lambda kv:(kv[1], kv[0]), reverse=True):
        print("{} : {}".format(word, count))


