# Diabetic Retinopathy Webapp
An AI powered website to check whether the person is suffering from diabetic retinopathy or not.

#### Tech Stack: Deep Learning, Django, Python, Basic Frontend technologies (HTML5, CSS)

### Understanding
Diabetic retinopathy is the leading cause of blindness in the working-age population of the developed world. It is estimated to affect over 93 million people.The US Center for Disease Control and Prevention estimates that 29.1 million people in the US have diabetes and the World Health Organization estimates that 347 million people have the disease worldwide. Diabetic Retinopathy (DR) is an eye disease associated with long-standing diabetes. Around 40% to 45% of Americans with diabetes have some stage of the disease. Progression to vision impairment can be slowed or averted if DR is detected in time, however this can be difficult as the disease often shows few symptoms until it is too late to provide effective treatment.

Currently, detecting DR is a time-consuming and manual process that requires a trained clinician to examine and evaluate digital color fundus photographs of the retina. By the time human readers submit their reviews, often a day or two later, the delayed results lead to lost follow up, miscommunication, and delayed treatment.

Clinicians can identify DR by the presence of lesions associated with the vascular abnormalities caused by the disease. While this approach is effective, its resource demands are high. The expertise and equipment required are often lacking in areas where the rate of diabetes in local populations is high and DR detection is most needed. As the number of individuals with diabetes continues to grow, the infrastructure needed to prevent blindness due to DR will become even more insufficient.

The need for a comprehensive and automated method of DR screening has long been recognized, and previous efforts have made good progress using image classification, pattern recognition, and machine learning. With color fundus photography as input, the goal of this competition is to push an automated detection system to the limit of what is possible – ideally resulting in models with realistic clinical potential. The winning models will be open sourced to maximize the impact such a model can have on improving DR detection. 
This my attempt to accomplish the task.

 Website <img src="Output/p1.png" >  For Normal Eye <img src="Output/p2.png"> For Infected Eye <img src="Output/p3.png"> 

### Requirements
For installing requirements: pip install requirements.txt.

For model file(.hdf5 or .h5) please visit the [kaggle competition](https://www.kaggle.com/c/diabetic-retinopathy-detection) page and copy the model file in models directory in the disease classification app to follow as per the code.

### Future Works
Even though the model might classify well and give good results there are a lot of chances to improve.

