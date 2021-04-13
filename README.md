
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

KIOSK Implementation is the final object 

: audio command working for authroized personnels, not working for unauthorized.




# Dependencies
(Training)

PyTorch 0.4.1

python 3.5+

numpy 1.15.4

librosa 0.6.1

(Demo)

