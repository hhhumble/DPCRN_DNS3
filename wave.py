import soundfile as sf

def get_wav_channels(file_path):
    try:
        audio_info = sf.info(file_path)
        data, samplerate = sf.read(file_path);
        print(audio_info)
        channels = audio_info.channels
        return channels, data, samplerate
    except Exception as e:
        print(f"Error occurred while getting channels: {e}")
        return None

# 示例用法
wav_file = "E:\\Works\\PycharmProjects\\DPCRN_DNS3\\dataset\\pre_noisy_signal\\1.wav"  # 替换为你的.wav音频文件路径
channels, data, samplerate = get_wav_channels(wav_file)
if channels is not None:
    print(f"WAV file has {channels} channels.")
    print(f"WAV file has {len(data)} length.")
