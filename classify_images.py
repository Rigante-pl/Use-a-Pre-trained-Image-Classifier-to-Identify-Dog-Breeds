#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: Michał Kucharczyk
# DATE CREATED: 31.03.2020                                 
# REVISED DATE: 
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the functin call within main.
#            -The CNN model architecture as model wihtin classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison 
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
# Imports classifier function for using CNN to classify images 
from classifier import classifier

def classify_images(images_dir, results_dic, model):

    for key in results_dic:

        
        model_label = classifier((images_dir + key), model)

        # Processes the results so they can be compared with pet image labels
        # set labels to lowercase (lower) and stripping off whitespace(strip)
        model_label = (model_label.lower()).strip()

        # defines truth as pet image label
        truth = results_dic[key][0]

        # If the pet image label is found within the classifier label list of terms
        # as an exact match to on of the terms in the list - then they are added to
        # results_dic as an exact match(1) using extend list function
        if truth in model_label:
            results_dic[key].extend([model_label, 1])


        # if not found then added to results dictionary as NOT a match(0) using
        # the extend function
        else:
            results_dic[key].extend([model_label, 0])