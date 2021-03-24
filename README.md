# Detecting Pulsar Sightings with Machine Learning

## Motivation
A binary classification algorithm trained on statistical data garnered from the PulsarFeatureLab tool used to predict pulsar sightings. 

The data set shared here contains 16,259 spurious examples caused by radio frequency interference/noise, and 1,639 real pulsar examples. These examples have all been checked by human annotators.[1][2]

## Neural Network Topology and Results Summary
The binary-crossentropy loss function was leveraged along with the Adam optimizer for this classification problem.

![model](https://user-images.githubusercontent.com/48378196/96961401-4be81500-1550-11eb-9cd2-4e0f682c3b56.png)

By just the 2nd epoch, binary accuracy shoots up to >90%. After 30 epochs, both binary and validation accuracy are >99%. 

![pulsar_sighting_metricspng](https://user-images.githubusercontent.com/48378196/97005319-00525d00-158a-11eb-9a73-8f4f689dc1fe.png)

## License
[MIT](https://choosealicense.com/licenses/mit/) 

## References
[1] R. J. Lyon, B. W. Stappers, S. Cooper, J. M. Brooke, J. D. Knowles, Fifty Years of Pulsar Candidate Selection: From simple filters to a new principled real-time classification approach, Monthly Notices of the Royal Astronomical Society 459 (1), 1104-1123, DOI: 10.1093/mnras/stw656 [2] R. J. Lyon, HTRU2, DOI: 10.6084/m9.figshare.3080389.v1.
