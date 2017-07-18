import pandas as pd
import numpy as np
import tensorflow as tf



#定义常量
rnn_unit=10       #hidden layer units
input_size=7
output_size=1
lr=0.0006         #学习率

f=open('ball.csv')
df=pd.read_csv(f)     #读入股票数据
data=df.iloc[:,2:9].values
data=data[::-1]
print('data',data)


#输入层、输出层权重、偏置

weights={'in':tf.Variable(tf.random_normal([input_size,rnn_unit])), 'out':tf.Variable(tf.random_normal([rnn_unit,1]))}

biases={'in':tf.Variable(tf.constant(0.1,shape=[rnn_unit,])), 'out':tf.Variable(tf.constant(0.1,shape=[1,]))}




#——————————————————获取训练集——————————————————


#——————————————————获取测试集——————————————————


#——————————————————定义神经网络变量——————————————————


#——————————————————训练模型——————————————————


#——————————————————预测模型————————————————————





#保存


# ## Save to file
# # remember to define the same dtype and shape when restore
# W = tf.Variable([[1,2,3],[3,4,5]], dtype=tf.float32, name='weights')
# b = tf.Variable([[1,2,3]], dtype=tf.float32, name='biases')
#
# # init= tf.initialize_all_variables() # tf 马上就要废弃这种写法
# # 替换成下面的写法:
# init = tf.global_variables_initializer()
#
# saver = tf.train.Saver()
#
# with tf.Session() as sess:
#     sess.run(init)
#     save_path = saver.save(sess, "my_net/save_net.ckpt")
#     print("Save to path: ", save_path)





#提取
# 先建立 W, b 的容器
# W = tf.Variable(np.arange(6).reshape((2, 3)), dtype=tf.float32, name="weights")
# b = tf.Variable(np.arange(3).reshape((1, 3)), dtype=tf.float32, name="biases")
#
# saver = tf.train.Saver()
# with tf.Session() as sess:
#     # 提取变量
#     saver.restore(sess, "my_net/save_net.ckpt")
#     print("weights:", sess.run(W))
#     print("biases:", sess.run(b))