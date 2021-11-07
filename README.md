# FacemaskDetection
마스크 착용 인식 시스템(2020.08.02 - 2020.08.22)
[관련링크](https://ghchoi0427.tistory.com/44)
---
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FdKmGR5%2FbtqJWSkmnbv%2FgVEyekKYADwxvHvxkhk460%2Fimg.png" height="250px" >

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcKq5hF%2FbtqJ1MDsM9T%2FrkjfafyK8AkKzd5iXDXdFK%2Fimg.png" height="250px" >

## Architecture
- ESP32와 PC는 서버와 클라이언트의 관계로 연결된다.
- ESP32 카메라 웹서버 예제를 베이스로 만들었다.
- 서버를 열고 PC에서 http 리퀘스트를 보내어 조작하도록 한다.
- ESP32와 아두이노는 Pin출력으로 소통한다.
- ESP32 자체의 핀 만으로 알람 시스템을 구현하기에는 부족해서 아두이노  나노를 추가했다.

## File description

- camServer_MaskDetection0819_light
  + `app_httpd.cpp` : esp32 서버 UI
  + `camServer_MaskDetection0819_light.ino` : 와이파이 연결 설정
  + `camera_index.h`
  + `camera_pins.h`
- mask_Detection_alarm
  + `mask_Detection_alarm.ino` : 인식 결과에 따른 알람 구현
- `createModel.py` : 학습 데이터를 바탕으로 모델을 생성
- `detect0811.py` : 마스크 착용인식
- `saved_model.h5` : 생성된 학습모델

##  Tech stack
`tensorflow`, `arduino`
