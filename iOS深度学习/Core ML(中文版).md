框架
#机器学习的核心
Integrate machine learning models into your app.
如何在你的APP里面集成机器学习的模型

--

#概述
With Core ML, you can integrate trained machine learning models into your app.
你可以在你的APP里面集成并且训练机器学习的模型,然后使用它.

![Core ML](images/c35ebf2d-ee94-4448-8fae-16420e7cc4ed.png)

A trained model is the result of applying a machine learning algorithm to a set of training data. The model makes predictions based on new input data. For example, a model that's been trained on a region's historical house prices may be able to predict a house's price when given the number of bedrooms and bathrooms.


Core ML is the foundation for domain-specific frameworks and functionality. Core ML supports Vision for image analysis, Foundation for natural language processing (for example, the 
NSLinguisticTagger
 class), and GameplayKit for evaluating learned decision trees. Core ML itself builds on top of low-level primitives like Accelerate and BNNS, as well as Metal Performance Shaders.
 
 ![Core ML](images/db81e861-1e06-4d14-8915-90707d9b114c.png)
 
Core ML is optimized for on-device performance, which minimizes memory footprint and power consumption. Running strictly on the device ensures the privacy of user data and guarantees that your app remains functional and responsive when a network connection is unavailable.