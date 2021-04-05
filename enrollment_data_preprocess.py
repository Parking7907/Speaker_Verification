#real time process for demo
import glob
import os
import librosa
import numpy as np
from hparam import hparam as hp

audio_path = glob.glob(os.path.dirname(hp.enrollment_data))                                        

def save_spectrogram_tisv():
    print("start text independent utterance feature extraction")
    os.makedirs(hp.data.train_path, exist_ok=True)   # make folder to save train file
    os.makedirs(hp.data.test_path, exist_ok=True)    # make folder to save test file

    utter_min_len = (hp.data.tisv_frame * hp.data.hop + hp.data.window) * hp.data.sr    # lower bound of utterance length
    total_speaker_num = len(audio_path)
    #train_speaker_num= (total_speaker_num//10)*9            # split total data 90% train and 10% test
    print("Enrollment starts..\n")
    print("Comparison....")
    utterances_spec = []
    folder = str(audio_path[0])
    print(folder)
    os_list = os.listdir(folder)
    os_list.sort()
    for utter_name in os_list:
        if utter_name[-4:] == '.wav':
            utter_path = os.path.join(folder, utter_name)         # path of each utterance
            utter, sr = librosa.core.load(utter_path, hp.data.sr)        # load utterance audio
            intervals = librosa.effects.split(utter, top_db=30)         # voice activity detection 
                # this works fine for timit but if you get array of shape 0 for any other audio change value of top_db
                # for vctk dataset use top_db=100
            for interval in intervals:
                if (interval[1]-interval[0]) > utter_min_len: 
                    #pdb.set_trace()          # If partial utterance is sufficient long,
                    utter_part = utter[interval[0]:interval[1]]         # save first and last 180 frames of spectrogram.
                else:
                    #pdb.set_trace()
                    pad = np.zeros(int(utter_min_len)-(interval[1]-interval[0]))
                    utter_tmp = utter[interval[0]:interval[1]]      
                    utter_part = np.concatenate((utter_tmp,pad),axis=0)

                S = librosa.core.stft(y=utter_part, n_fft=hp.data.nfft,
                                          win_length=int(hp.data.window * sr), hop_length=int(hp.data.hop * sr))
                S = np.abs(S) ** 2
                mel_basis = librosa.filters.mel(sr=hp.data.sr, n_fft=hp.data.nfft, n_mels=hp.data.nmels)
                S = np.log10(np.dot(mel_basis, S) + 1e-6)           # log mel spectrogram of utterances
                utterances_spec.append(S[:, :hp.data.tisv_frame])    # first 180 frames of partial utterance
                utterances_spec.append(S[:, -hp.data.tisv_frame:])   # last 180 frames of partial utterance
           
    utterances_spec = np.array(utterances_spec)
    print(utterances_spec.shape)
        
    np.save(os.path.join(hp.data.train_path, "speaker_enrollment.npy"), utterances_spec)
        

if __name__ == "__main__":
    save_spectrogram_tisv()