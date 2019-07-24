# Face Recognition and Video Filter Application
##### Computational Photography | Portland State University | Spring 2018
***
Final project for computational photography course taken at Portland State University. This algorithm uses haar features to detect landmarks of the face, including eyes, nose, and mouth. This implementation works on human figures as well as cartoons; similarly to the original Instagram stories and Snapchat facial recognition algorithms.
***
#### Motivation
Facial recognition and video filter application has risen to a top priority for many big tech companies in the past decade. Current applications for facial recognition include-but are not limited to-secure access to buildings, computer systems, ATMs, in use for identifying persons for law enforcement, and more recently, for marketing purposes [1]. 

Since OpenCV now has facial recognition libraries available for developers worldwide, we see many successful products that find faces; a stark comparison to technologies available previous to Viola-Jones object detection framework in 2001 [3] which now serves as the building blocks for OpenCV Cascade Classifier library. 

We implement facial recognition and Gaussian Blurring to simulate shallow depth of field. We see a similar application in the built-in features in Google’s Pixel 2 and Apple’s IPhone portrait modes. We will see results from our method that detect what some would classify as false-positive face detection results. Because of this reason, it is apparent that further work must be done via a simple neural network. Furthermore, through these results, we conclude research must continue in computer vision and computational photography to continue advancement in facial recognition algorithms to ensure actual faces are detected for cases aforementioned above.
***

#### Method
The algorithm can be split into three major steps. Firstly, we build the infrastructure to detect a face and major facial regions in the video frame. Secondly, detection of facial landmarks which is crucial for filter application. Thirdly, apply filter or sprite onto facial landmarks. In the final implementation presented in this paper, we apply a filter to the background, instead of the face; this leaves the face untouched by the filter, simulating a naive approach to simulating a shallow depth of field.
***
#### Results

Results presented are at three points; they accurately depict the translation from idea, to implementation of concepts, then full application of facial recognition and filter application. Although results present as somewhat acceptable face detection, Figure I and II are chosen to prove fallacy in implementation. In particular, faces that are not human are detected. This could be a desired result for a funny sprite application onto a non-human face, however, in the case of security verification, this result is unacceptable.

Figure I shows Part I implementation of Haar feature detection. With this application, we see accurate results for face, eyes, mouth, but no detection of nose. We think this is because the model has lip jewelry which may obstruct the detection of the Haar feature corresponding to the nose region.

Implementation of Part II without Part I integration is depicted in Figure II. We see accurate readings for regions and landmarks such as eyebrows, nose, convex hull, mouth and eyes on the human model. However, the tattoo face detection is not accurately detecting the convex hull, mouth, or nose of the tattoo face.

After integrating Haar detection and facial landmarks together (algorithm Part I and II), we see resilience in slight obstructions (Figure IV) but when more than half the face is obstructed, the algorithm no longer detects the face (Figure III). 
***
#### Future Work
The current approach has good results but also gives false-positives. In some cases, the false-positive results may be desirable, but in the event that is not desirable, we plan to implement a simple neural network to determine human face from static faces such as in Figure I and II. Furthermore, the current approach to overlaying the Gaussian blur is naive and not believable, we plan to configure the filter to blur everything outside of the convex hull, instead of everything outside of the facial region.
***

![alt text](https://github.com/aleenawatson/facial_recognition/blob/master/figures/figure1.png "Figure 1")

#### References
A. K. Jain, A. Ross and S. Prabhakar, "An introduction to biometric recognition," in IEEE Transactions on Circuits and Systems for Video Technology, vol. 14, no. 1, pp. 4-20, Jan. 2004. doi:10.1109/TCSVT.2003.818349, URL:http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=1262027&isnumber=28212
 “Fourier analysis.” Wikipedia, Wikimedia Foundation, 1 Apr. 2018, en.wikipedia.org/wiki/Fourier_analysis
“Haar-like Feature.” Wikipedia, Wikimedia Foundation, 1 Apr. 2018, en.wikipedia.org/wiki/Haar-like_feature.
Holczer, Balazs. “Computer Vision - Integral Images.” YouTube, YouTube, 25 Feb. 2018, www.youtube.com/watch?v=x41KFOFGnUE.
Ramesh, Varun. “Haar Feature Detection for Face Tracking.” YouTube, YouTube, 3 Apr. 2011, www.youtube.com/watch?v=0WBUlRADBd0.