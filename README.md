
# Speaker_Verification
Design Project On Speaker Verification
 
Model Training Based on github of HarryVolek : https://github.com/HarryVolek/PyTorch_Speaker_Verification

Base Line Code Training on : TIMIT

I adjusted network for purpose (Sliding windows, Filter, learning rates...) and retrained to another datasets (Training / Test 8 : 2)

<1> (English) TIMIT : 0.0398

<2> (English) VoxCeleb : EER = 0.0426
=> Youtube crawled, speech dataset of celebrities

<3> (Korean) AI HUB Dataset(ETRI) : EER = 0.5 (not trained)
=> Basically because of dataset is dialogue between two person (not one)

<4> (Korean) 서울말뭉치 Dataset : EER = 0.094
=> Training data with "reading script" of fairy tales, fictions, and essays

<5> (Korean) Customized "HI, IIPHIS" Dataset : EER = 0.717 
=> Training dataset of short 'Hi IIPHIS' Voice of over 50 people for A.I Speaker Task & Speaker Verification Tasks (built by IIP Lab(http://iip.sogang.ac.kr))


Target object on Visualized Demo & Implementation on GUI Environment

Focus on Speaker Verification for security issues, such as biometric recognition system on "Voice"

# Demo

[![Demo](http://img.youtube.com/vi/eQJUCRxU7wE/0.jpg)](https://youtu.be/eQJUCRxU7wE) 

1. User Registration(사용자 등록) 버튼 클릭
2. ‘Record’ 버튼을 눌러 10초 간 ‘Hi IIPHIS’를 5번 발화하여 화자 등록, 잘 녹음되었는지 ‘Listen again’ 버튼을 눌러서 확인 가능, ‘Next’ 버튼으로 다음 화면 전환
3. ‘Record’ 버튼을 누르고 ‘Hi IIPHIS’를 2초 동안 한 번 발화하여 화자 검증, 잘 녹음되었는지 ‘Listen again’ 버튼을 눌러서 확인 가능
4. ‘Next’ 버튼으로 화자인증 성공 시 “보안 모듈 해제에 성공하였습니다. 무엇을 도와드릴까요?” / 실패 시 “보안 모듈 해제에 실패하였습니다. 다시 시도해 주세요.” 다음 화면전환
5. Revalidation 버튼을 누르면 다시 검증 부분으로 이동(이전 화면으로)



KIOSK Implementation would be final object 

: audio command working for authroized personnels, not working for unauthorized.




# Dependencies
(Training)

PyTorch 0.4.1

python 3.5+

numpy 1.15.4

librosa 0.6.1

(Demo)

