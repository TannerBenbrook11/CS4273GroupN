# Ticket S1: Research Machine Learning Models

Author: Ameer Ghazal

## Model Goals

- Predict future power consumption given the time and date for future node placement.
- Highlight the tradeoff between computation expenses and training error.
- Report testing and training errors of the final model, along with enchanced or comparable accuracy of different models.
- Hypertune the model for enchanced accuracy (feature engineering, normalization, etc.)

## Types of Models

There are multiple machine learning models that are worth testing. Specifically deep neural networks or other regression models. DNN are typically used for large, complex, nonlinear data. Regression models are simpler all around (including interpretability - should not be an issue, assuming the technicality of our client).

Baseline: Early listed Regression (Linear, DTs)
Intermedidate: RFs, Gradient Boosting
Advanced: LSTM or GRU, latter DNNs

### Deep Neural Networks

- Complex, large, nonlinear data.
- Higher computational costs, but better for non-linearities and temporal dependency capturing (worth mentioning since there is always a budget).
- Future Idea: could be used for power spike specific cases, but this could make our work confusing.
- Require more resouces, more data, and may take longer to train on.
- Hidden layers, number of neurons, arbitrary learning rate (different hyperparameters).
- Complexitiy in understanding.

#### Feedforward (Basic) Neural Network (FNN)

- Simplest form DNN, where data flows in one direction (input -> hidden layers -> output).
- Works when time-depedency is not critical (seemingly may be critical for ours, not 100%).
- Simple implemention, less computationally expensive than other DNN's.

#### Recurrent Neural Network (RNN)

- Maintain hidden states to remember past inputs (may be god for time-series, power consumption-like data).
- Models temporal dependencies.
- Slower training, vanishing gradients (not sure what this entails).

#### Long Short-Term Networks (LSTM)

- Advanced RNN that solves vanishing gradient problem, of which are effective for time-series data with long-term dependencies.
- Captures both short and long term temporal dependies.
- Expensive compared to the simpler models.
- Objectively may be one of the better DNN's to test with, though the expense may deter us away.

#### Gated Recurrent Units (GRU)

- Can use GRU (Gated Recurrent Units) as an alternative to LSTMs, as they have less params, are faster to train, and perform similary.
- Help when resoucres may be limited.
- Could be a viable option.

There are many other DNNs out there to use, such as CNN (due to the time), transformer models, and more, but for now these are a good starting point in terms of notes.

### Regression Models

#### Linear Regression

- Linear relationship between the features and the target (power consumption).
- Relationship is roughly linear, which is a large limitation.
- Very simple, interpretable, fast to time.

#### Polynomial Regression

- Polynomial terms to linear regression (model non-linear terms).
- Overfitting is prominent if the degree is too high.

#### Decision Tree

- Nonlinear model that splits data into regions based off feature values.
- Good for complex power-consumption data with non-linear relationships.
- Prone to overfitting without regularization.

#### Random Forest Regression

- RF Regression is composed of many decision trees in order to reduce overfitting by averaging predictions.
- Supposedly handles noise and outliers well, but is computatioanlly expensive due to the arbitrary number of DTs.

#### Gradient Boosting Regression

- Advanced ensemble to build trees to minimize errors in predictions.
- High accuracy, handing missing values.
- Can be even slower than Random Forest Regression.
- XGBoost, LightGBM, etc.

Similar to DNNs, there are many more regression models, which we could experiment with, but if I put them all here, it would be too long.

## Metrics

- Accuracy (predicted vs. actual).
- Mean Absolute Error (MAE), MSE, Root MSE, Mean Absolute Percentage Error (MAPE).
- More, need to look into to such.

## Libraries

- Tensorflow, Keras, Pytorch for DNN.
- Scikitlearn, XGBoost, LightGBM.
- Pandas,

## Potential Avenues

Once the data is collected, cleaning, and prepared, we could:

1. Start with simple regression models for testing (potentially ones mentioned above).
2. Experiement with DNN's if resources are in place, along with the need for performance gains.
3. Test on the models respectively, comparing the actual vs. predicted power consumption. Compare which is better in the long term, accounting for all the dependencies and scenarios (cost, time, amount of data, etc.).
4. Report training and testing errors (account for underfitting, overfitting, etc.).
