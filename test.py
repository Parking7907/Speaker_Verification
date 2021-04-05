#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 21:49:16 2018

@author: harry
"""

import os
import random
import time
import torch
import pdb
from torch.utils.data import DataLoader

from hparam import hparam as hp
from data_load import SpeakerDatasetTIMIT, SpeakerDatasetTIMITPreprocessed
from speech_embedder_net import SpeechEmbedder, GE2ELoss, get_centroids, get_cossim


def test(model_path):
    
    if hp.data.data_preprocessed:
        test_dataset = SpeakerDatasetTIMITPreprocessed()
    else:
        test_dataset = SpeakerDatasetTIMIT()
    test_loader = DataLoader(test_dataset, batch_size=hp.test.N, shuffle=False, num_workers=hp.test.num_workers, drop_last=True)
    
    embedder_net = SpeechEmbedder()
    embedder_net.load_state_dict(torch.load(model_path))
    embedder_net.eval()
    #pdb.set_trace()
    avg_EER = 0
    thres = 0.60
    for e in range(hp.test.epochs):
        batch_avg_EER = 0
        for batch_id, mel_db_batch in enumerate(test_loader):
            #pdb.set_trace()
            assert hp.test.M % 2 == 0
            enrollment_batch, verification_batch = torch.split(mel_db_batch, int(mel_db_batch.size(1)/2), dim=1)
            
            enrollment_batch = torch.reshape(enrollment_batch, (hp.test.N*hp.test.M//2, enrollment_batch.size(2), enrollment_batch.size(3)))
            #print(enrollment_batch.size(2))
            verification_batch = torch.reshape(verification_batch, (hp.test.N*hp.test.M//2, verification_batch.size(2), verification_batch.size(3)))
            
            perm = []
            for i in range(verification_batch.size(0)):
                perm.append(i)
            unperm = perm
            #perm = random.sample(range(0,verification_batch.size(0)), verification_batch.size(0))
            #unperm = list(perm)
            #for i,j in enumerate(perm):
            #    unperm[j] = i
                
            #verification_batch = verification_batch[perm]
            enrollment_embeddings = embedder_net(enrollment_batch)
            verification_embeddings = embedder_net(verification_batch)
            #verification_embeddings = verification_embeddings[unperm]
            
            enrollment_embeddings = torch.reshape(enrollment_embeddings, (hp.test.N, hp.test.M//2, enrollment_embeddings.size(1)))
            verification_embeddings = torch.reshape(verification_embeddings, (hp.test.N, hp.test.M//2, verification_embeddings.size(1)))
            enrollment_centroids = get_centroids(enrollment_embeddings)
            
            sim_matrix = get_cossim(verification_embeddings, enrollment_centroids)
            #pdb.set_trace()
            
            sim_matrix_thresh = sim_matrix>thres
            k=0
            print(sim_matrix)
            for i in range(2):
                for j in range(2):
                    sim_matrix_data = sim_matrix_thresh[i,:,j]
                    print(sim_matrix_data)
                    if (i+j)%2 == 1:
                        for m in sim_matrix_data:
                            if m:
                                k=k+1
                                print(k)
                    #else:
                    #    for n in sim_matrix_data:
                    #        if n==0:
                    #            k=k+1
                    #            print(k)
            


            if k>5:
                print("Same Person!")
            else:
                print("Different Person!")

    return k
if __name__=="__main__":
        test(hp.model.model_path)
