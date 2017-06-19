# Get task number from command line
import sys

task_number = int(sys.argv[1])

import tensorflow as tf

cluster = tf.train.ClusterSpec({"my_job": ["localhost:2222", "localhost:2223"]})
server = tf.train.Server(cluster, job_name="my_job", task_index=task_number)

print("Starting server #{}".format(task_number))

server.start()
server.join()
