import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = './archive/student_performance.csv'
data = pd.read_csv(file_path)

# 1. Получите и визуализируйте (графически) статистику по датасету
# (включая количество, среднее значение, стандартное отклонение, минимум,
# максимум и различные квантили).

# Set display option to show all columns without truncation
pd.set_option('display.max_columns', None)

statistics = data.describe()
print(statistics)

# Visualize statistics
plt.figure(figsize=(10, 6))
sns.boxplot(data=data)
plt.title("Statistical Distribution of Features")
plt.xticks(rotation=45)
plt.show()

# 2. Проведите предварительную обработку данных, включая обработку отсутствующих
# значений, кодирование категориальных признаков и нормировка.

# Check for missing values
missing_values = data.isnull().sum()
print("Missing values per column:")
print(missing_values)

# Handle missing values by removing rows with any missing value
data = data.dropna()

# Encode categorical variables (Extracurricular Activities: Yes -> 1, No -> 0)
data['Extracurricular Activities'] = data['Extracurricular Activities'].map({'Yes': 1, 'No': 0})

print(data.head())

# 3. Разделите данные на обучающий и тестовый наборы данных.

# Split data into features (X) and target (y)
X = data[['Hours Studied', 'Previous Scores', 'Extracurricular Activities', 'Sleep Hours',
          'Sample Question Papers Practiced']].values
y = data['Performance Index'].values

# Add a column of ones to X for the intercept term (bias)
X = np.concatenate([np.ones((X.shape[0], 1)), X], axis=1)

# Split into train (80%) and test (20%) sets
train_size = int(0.8 * X.shape[0])
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]


# 4. Реализуйте линейную регрессию с использованием метода наименьших квадратов
# без использования сторонних библиотек, кроме NumPy и Pandas (для использования
# коэффициентов использовать библиотеки тоже нельзя). Использовать минимизацию
# суммы квадратов разностей между фактическими и предсказанными значениями для
# нахождения оптимальных коэффициентов.

# Function to compute the coefficients using the normal equation
def linear_regression(X, y):
    # Normal equation: theta = (X^T X)^-1 X^T y
    X_transpose = X.T
    theta = np.linalg.inv(X_transpose.dot(X)).dot(X_transpose).dot(y)
    return theta


# Train the model and get the coefficients
theta = linear_regression(X_train, y_train)

print("Coefficients (including intercept):", theta)

# Predictions for the test set
y_pred = X_test.dot(theta)

# Show some sample predictions
print("Actual values (test set):", y_test[:5])
print("Predicted values:", y_pred[:5])


# 5. Для каждой модели проведите оценку производительности, используя метрику
# коэффициент детерминации, чтобы измерить, насколько хорошо модель соответствует данным.

# Function to calculate R-squared (coefficient of determination)
def r_squared(y_true, y_pred):
    ss_res = np.sum((y_true - y_pred) ** 2)  # Residual sum of squares
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)  # Total sum of squares
    r2 = 1 - (ss_res / ss_tot)
    return r2


# Model 1: All features
X_train_model1 = X_train
X_test_model1 = X_test
theta_model1 = linear_regression(X_train_model1, y_train)
y_pred_model1 = X_test_model1.dot(theta_model1)
r2_model1 = r_squared(y_test, y_pred_model1)

# Model 2: Only "Hours Studied" and "Previous Scores"
X_train_model2 = X_train[:, [0, 1, 2]]  # Intercept + "Hours Studied" + "Previous Scores"
X_test_model2 = X_test[:, [0, 1, 2]]
theta_model2 = linear_regression(X_train_model2, y_train)
y_pred_model2 = X_test_model2.dot(theta_model2)
r2_model2 = r_squared(y_test, y_pred_model2)

# Model 3: "Hours Studied", "Sleep Hours", and "Extracurricular Activities"
X_train_model3 = X_train[:, [0, 1, 4, 3]]  # Intercept + "Hours Studied" + "Extracurricular Activities" + "Sleep Hours"
X_test_model3 = X_test[:, [0, 1, 4, 3]]
theta_model3 = linear_regression(X_train_model3, y_train)
y_pred_model3 = X_test_model3.dot(theta_model3)
r2_model3 = r_squared(y_test, y_pred_model3)

# Print R-squared for each model
print(f"R-squared for Model 1 (All features): {r2_model1}")
print(f"R-squared for Model 2 (Hours Studied, Previous Scores): {r2_model2}")
print(f"R-squared for Model 3 (Hours Studied, Sleep Hours, Extracurricular Activities): {r2_model3}")


# Бонусное задание: Ввести синтетический признак при построении модели

# 1. Create the synthetic feature: "Efficiency" = Sample Question Papers Practiced / Hours Studied
data['Efficiency'] = data['Sample Question Papers Practiced'] / data['Hours Studied']

# Replace any infinite or NaN values that might occur due to division by zero safely
data['Efficiency'] = data['Efficiency'].replace([np.inf, -np.inf], 0)
data['Efficiency'] = data['Efficiency'].fillna(0)

# Update X (features) to include the new synthetic feature
X_synthetic = data[['Hours Studied', 'Previous Scores', 'Extracurricular Activities', 'Sleep Hours', 'Sample Question Papers Practiced', 'Efficiency']].values

# Add a column of ones for the intercept term
X_synthetic = np.concatenate([np.ones((X_synthetic.shape[0], 1)), X_synthetic], axis=1)

# Split into training and test sets (80/20)
X_train_synthetic = X_synthetic[:train_size]
X_test_synthetic = X_synthetic[train_size:]
y_train_synthetic = y[:train_size]
y_test_synthetic = y[train_size:]

# Train the model using the synthetic feature
theta_synthetic = linear_regression(X_train_synthetic, y_train_synthetic)

# Predict on the test set
y_pred_synthetic = X_test_synthetic.dot(theta_synthetic)

# Calculate R-squared for the model with the synthetic feature
r2_synthetic = r_squared(y_test_synthetic, y_pred_synthetic)

# Print the result
print(f"R-squared for Model with Synthetic Feature (Efficiency): {r2_synthetic}")

