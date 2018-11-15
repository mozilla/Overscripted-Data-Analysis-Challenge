import sys
from slugify import slugify
from pyspark.sql import SparkSession, functions, types

################################################################################
# Safety for spark stuff
spark = SparkSession.builder.appName('URL extractor').getOrCreate()
assert sys.version_info >= (3, 4) # make sure we have Python 3.4+
assert spark.version >= '2.1' # make sure we have Spark 2.1+


################################################################################
# Function to generate a text file from the script URL
def shorten_name(url_name):
    # Strip out 'http', 'https' and '/'
    shortened_url = url_name.replace('https://', '').replace('http://', '').replace('/', '_')

    # Shorten url to 250 characters (max file system can support)
    shortened_url = slugify(shortened_url)[:250]

    # Specify the suffix for each downloaded file
    suffix = '.txt'

    # Final output
    file_name = shortened_url + suffix
    return file_name


################################################################################
def main():

    # Specify target directory
    #   TODO: this should be controlled via the config.ini file
    MAIN_DIR        = '/mnt/Data/UCOSP_DATA/'
    PARQUET_FILES   = MAIN_DIR + 'sample_full_data/*'
    #PARQUET_FILES   = MAIN_DIR + 'full_data/*'
    OUTPUT          = MAIN_DIR + 'resources/sample_full_url_list'

    # Read in dataset, selecting the 'script_url' column and filtering duplicates
    data = spark.read.parquet(PARQUET_FILES).select('script_url').distinct()

    # User Defined Function to convert script URL to a filename usable by ext4
    shorten_udf = functions.udf(shorten_name, returnType=types.StringType())

    # Apply the UDF over the whole list to generate a new column 'filename'
    # Sort by 'filename' as this will be used to check for existing files
    data = data.withColumn('filename', shorten_udf(data.script_url)).sort('filename')

    # Sanity check
#    data.show()
#    data.printSchema()

    # Save the data to parquet files
    data.write.parquet(OUTPUT)


################################################################################
if __name__ == '__main__':
    main();
