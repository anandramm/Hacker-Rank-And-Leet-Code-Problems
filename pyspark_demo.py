#!/usr/bin/env python
# coding: utf-8

# In[21]:


from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[6]") \
                    .appName('Trial') \
                    .getOrCreate()


# In[22]:


import time 
t1=time.perf_counter()
#Create a dictionary of states and their codes
states = {"NY":"New York", "CA":"California", "FL":"Florida"}

#Broadcast the dictionary to all nodes
broadcastStates = spark.sparkContext.broadcast(states)

#Create an RDD of data with state codes
data = [("James","Smith","USA","CA"), ("Michael","Rose","USA","NY"), ("Robert","Williams","USA","CA"), ("Maria","Jones","USA","FL")]

rdd = spark.sparkContext.parallelize(data)

#Define a function that converts state codes to state names using the broadcast variable
def state_convert(code): return broadcastStates.value[code]

#Apply the function to the RDD using map transformation
result = rdd.map(lambda x: (x[0], x1, x2, state_convert(x3)))
#result = result.collect()
#Print the result


t2=time.perf_counter()

print("Time taken is ",t2-t1)


# In[23]:


import time 
t1=time.perf_counter()
#Create a dictionary of states and their codes
states_new = {"NY":"New York", "CA":"California", "FL":"Florida"}


#Create an RDD of data with state codes
data_new = [("James","Smith","USA","CA"), ("Michael","Rose","USA","NY"), ("Robert","Williams","USA","CA"), ("Maria","Jones","USA","FL")]

rdd_new = spark.sparkContext.parallelize(data_new)

#Define a function that converts state codes to state names using the broadcast variable
def state_convert(code): return rdd_new.collect()

#Apply the function to the RDD using map transformation
result_new = rdd.map(lambda x: (x[0], x1, x2, state_convert(x3)))
#result = result.collect()
#Print the result


t2=time.perf_counter()

print("Time taken is ",t2-t1)


# In[ ]:




