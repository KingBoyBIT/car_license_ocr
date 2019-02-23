# Read me

- `train-license-digits.py` 训练和预测 0-9 A-Z

- `train-license-letters.py` 训练和预测 A-Z

- `train-license-province.py` 训练和预测省份汉字 "京", "闽", "粤", "苏", "沪", "浙"


运行脚本的时候，参数为train时为训练，predict时为测试，例：
```python
C:\Anaconda3\envs\tensorflow\python.exe D:/Codes/githubcodes/car_license_ocr/train-license-digits.py predict
2019-02-23 23:16:55.736432: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2
2019-02-23 23:16:55.993746: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1432] Found device 0 with properties: 
name: GeForce GTX 1070 major: 6 minor: 1 memoryClockRate(GHz): 1.683
pciBusID: 0000:01:00.0
totalMemory: 8.00GiB freeMemory: 6.63GiB
2019-02-23 23:16:55.994123: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1511] Adding visible gpu devices: 0
2019-02-23 23:16:56.819371: I tensorflow/core/common_runtime/gpu/gpu_device.cc:982] Device interconnect StreamExecutor with strength 1 edge matrix:
2019-02-23 23:16:56.819580: I tensorflow/core/common_runtime/gpu/gpu_device.cc:988]      0 
2019-02-23 23:16:56.819746: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1001] 0:   N 
2019-02-23 23:16:56.820028: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1115] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 6384 MB memory) -> physical GPU (device: 0, name: GeForce GTX 1070, pci bus id: 0000:01:00.0, compute capability: 6.1)
概率：  [1 100.00%]    [T 0.00%]    [Y 0.00%]
概率：  [6 100.00%]    [8 0.00%]    [H 0.00%]
概率：  [7 100.00%]    [Z 0.00%]    [R 0.00%]
概率：  [2 100.00%]    [R 0.00%]    [V 0.00%]
概率：  [Q 100.00%]    [U 0.00%]    [J 0.00%]
车牌编号是: 【1672Q】
```

# 其他注意事项

- 数据集为：`car_license_ocr.7z` ，训练和预测需解压缩
- `license_split.py`对测试图像进行了车牌定位检测，在HSV空间下用膨胀和腐蚀确定车牌坐标，实际环境下有待提高