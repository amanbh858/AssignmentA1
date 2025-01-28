Summary:
Feature Impact on Predictions:
From the models, I observed that features like 'brand', 'fuel', and 'owner' have a significant impact on car prices. For example, different car brands have different price ranges, so the model learns that brand plays an essential role in pricing. Similarly, fuel types can affect car pricing, as certain fuel types are more expensive or fuel-efficient than others. On the other hand, features like 'year' or 'mileage' seem to be less influential than expected, possibly due to how the data is distributed or the nature of the model.

Model Performance:
Among the models tested,By the data I think Linear Regression performed the best in terms of R² score, indicating that the model was able to explain a significant amount of the variance in the car price. The Support Vector Machine (SVM) showed decent performance but didn't outperform Linear Regression, likely due to the feature scaling affecting its performance with certain features. The Decision Tree algorithm, while interpretable, exhibited some overfitting and had lower predictive accuracy on the test data.
So when I deployed my model using flask framework I used the Linear Regression Model because I think it performed the best out of the other 3 models.
