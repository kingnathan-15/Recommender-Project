from flask_cors import CORS
import joblib
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/api/predict_kmeans_clustering', methods=['POST'])
def cluster_identification():
    # data = request.get_json()
    # new_data = pd.DataFrame([{
    #     'Age': data.get('Age'),
    #     'Annual Income (k$)': data.get('Annual Income (k$)'),
    #     'Spending Score (1-100)': data.get('Spending Score (1-100)')
    # }])

    # expected_features = [
    #     'Age',
    #     'Annual Income (k$)',
    #     'Spending Score (1-100)'
    # ]

    # new_data = new_data[expected_features]

    # new_data_scaled = kmeans_scaler.transform(new_data)
    # prediction = kmeans_clustering_model.predict(new_data_scaled)

    # match int(prediction):
    #     case 0:
    #         prediction_text = "Targeted Premium"
    #     case 1:
    #         prediction_text = "Average Spenders"
    #     case 2:
    #         prediction_text = "Low Spenders"
    #     case 3:
    #         prediction_text = "Frugal Customers"
    #     case 4:
    #         prediction_text = "Luxury Shoppers"
    
    # # Returns the result as a JSON response:
    return jsonify({'Predicted Cluster = ': (prediction_text)})


if __name__ == '__main__':
    app.run(debug=True)