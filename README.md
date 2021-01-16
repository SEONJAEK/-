# Sewer-Crack-Detection
:Deep Learning based Sewer Defect Automatic Recognition System 

<p align="center">
  <img src="your_relative_path_here" width="350" title="논문">
  <img src="your_relative_path_here_number_2_large_name" width="350" alt="accessibility text">
</p>


## 1. '하수관로 결함 자동 인식 시스템' 개요
<pre><b>-주제: </b>: 딥러닝(Deep Learning) 기반 하수관로 결함 자동 인식 시스템<br>
<b>-연구 의도 </b>: 이전 하수관 관리를 위해 사용하던 방식은 검사관이 하수관 CCTV를 수동으로 관찰하여 <br>
하수관의 결함을 관측하고 심각성을 파악하였다. 이러한 수동 관측 방식은 많은 인적 자원과 시간을 소모한다.<br>
이런 문제를 해결하고자 딥러닝(Deep Learning) 기반 하수관로 결함 자동 인식 시스템을 제안한다.<br>
<b>-연구 내용 요약 </b>: 하수관로 CCTV 영상을 서울디지털재단으로부터 제공받았고 이를 활용해 <br>
딥러닝 모델인 VGG-19 모델을 적용하여 하수관로 자동 인식 시스템을 개발 연구를 진행하였다.<br></pre>
<br>
<br>

## 2. 연구 내용

<h3>1) 데이터 셋</h3>
총 데이터 개수: 4634개(Training Data + Testing Data)<br>
-Training Data: 4234개<br>
-Testing Data: 400개 (클래스 별 각 50개)

![class2](https://user-images.githubusercontent.com/69441007/104813677-13ee2680-584e-11eb-8ab1-7088d6ef6d61.gif)
![class1](https://user-images.githubusercontent.com/69441007/104813768-89f28d80-584e-11eb-866e-0c5943cc72e9.PNG)

<br>
<br>
<h3>2)하수관로 자동 인식 시스템 구조</h3>

![model](https://user-images.githubusercontent.com/69441007/104813811-dccc4500-584e-11eb-8f33-0e3215b80318.PNG)

<h3>3)실험 결과</h3><br>
<h3><1.Training Accuracy><br></h3>
  
![trainAccuracy](https://user-images.githubusercontent.com/69441007/104813835-05543f00-584f-11eb-82b5-83442aabda79.PNG)

-Epoch: 50<br>
-Batch size: 64<br>
-Training Accuracy: 97.6%<br>
-Training Data Set : 총 4234 장 (train: validation = 8: 2)<br>
<h4><ul>Training Data Set을 8:2 비율로 나누어 train data 와 validation data로 나누었고, Training Data의 평균 인식률은 97.6%의 정확도를 보였다.</ul><br></h4>

<h3><2.Testing Accuracy><br></h3>
  
![TestAccuracy](https://user-images.githubusercontent.com/69441007/104813781-a1317b00-584e-11eb-9ab6-0d55c33dab99.png)

-Testing Accuracy = 95.2%<br>
<h4><ul>Testing Data Set 이미지 400장(클래스 별 50장)을 사용하여 하수관 결함 자동 시스템 인식률을 측정하였고, Testing Data의 평균 인식률은 95.2%의 정확도를 보였다. </ul><br></h4>


