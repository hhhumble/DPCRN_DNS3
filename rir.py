# import soundfile as sf
# import numpy as np
# import subprocess
#
# ### 分开通道部分
#
# # 读取双通道WAV文件
# data, sample_rate = sf.read('E:\\Works\\PycharmProjects\\DPCRN_DNS3\\the_dir_of_source\\1.wav')
#
# # 提取一个通道（例如左通道）
# mono_data_0 = data[:, 0]  # 提取左通道，将索引改为0
# mono_data_1 = data[:, 1]  # 提取右通道，将索引改为1
# emerge_data = (mono_data_0 + mono_data_1) / 2;
#
#
# # 将数据写入单通道WAV文件
# sf.write('E:\\Works\\PycharmProjects\\DPCRN_DNS3\\the_dir_of_source\\emerge.wav', emerge_data, sample_rate)

import os
import glob
import soundfile as sf

# 音频文件夹路径
folder_path = 'E:\\Works\\PycharmProjects\\DPCRN_DNS3\\dataset\\real_signal'

# 获取文件夹中所有 WAV 音频文件的路径
audio_files = glob.glob(os.path.join(folder_path, '*.wav'))

# 遍历每个音频文件
for audio_file in audio_files:
    # 读取音频文件
    data, sample_rate = sf.read(audio_file)

    # 在这里可以对音频数据进行处理或执行其他操作
    # 例如，可以对音频进行特征提取、转换、处理等

    # 输出文件名
    file_name = os.path.basename(audio_file)
    print("当前处理的文件名:", file_name)

    # 输出音频数据的样本率
    print("音频数据的样本率:", sample_rate)

    # 输出音频数据的形状
    print("音频数据的形状:", data.shape)

    # 输出音频数据的前几个样本
    print("音频数据的前几个样本:", data[:5])

    # 在这里可以根据需求进行其他处理或操作
    # ...

    # 提取通道（左通道 右通道）
    channel_0 = data[:, 0]  # 提取左通道
    channel_1 = data[:, 1]  # 提取右通道
    emerge_channel = (channel_0 + channel_1) / 2;

    # 将数据写入单通道WAV文件
    sf.write('E:\\Works\\PycharmProjects\\DPCRN_DNS3\\dataset\\pre_real_signal\\' + file_name, emerge_channel, sample_rate)

    # 进行下一个音频文件的处理
    print("-------------------")