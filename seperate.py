import soundfile as sf
import numpy as np
import subprocess

### 分开通道部分

# 读取双通道WAV文件
data, sample_rate = sf.read('E:\\Works\\PycharmProjects\\DPCRN_DNS3\\dataset\\real_signal\\1.wav')

# 提取一个通道（例如左通道）
mono_data_0 = data[:, 0]  # 提取左通道，将索引改为0
mono_data_1 = data[:, 1]  # 提取右通道，将索引改为1

# 将数据写入单通道WAV文件
sf.write('E:\\Works\\PycharmProjects\\DPCRN_DNS3\\the_dir_of_source\\output_0.wav', mono_data_0, sample_rate)
sf.write('E:\\Works\\PycharmProjects\\DPCRN_DNS3\\the_dir_of_source\\output_1.wav', mono_data_1, sample_rate)
