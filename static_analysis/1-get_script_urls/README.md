# WIP: Extract script URLs from dataset
_Note, this section uses pySpark_

## 1) Setup Spark:

1) You must have Open JDK 8. Install via `$ sudo apt-get install openjdk-8-jdk` if you don't have this installed (check if `/usr/lib/jvm/java-8-openjdk-amd64/` exists).

2) Download the latest version of [Spark](https://spark.apache.org/downloads.html) (prebuilt for Apache Hadoop 2.7 and later), and unpack the tar to a directory of your choosing.

3) Set some environment variables:
```
$ export PYSPARK_PYTHON=python3
$ export PATH=${PATH}:/path/to/spark-<version>-bin-hadoop2.7/bin
$ export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/ 
```

To run any of the pyspark scripts on their own, you can run
```
$ spark-submit sparkscript.py
```
