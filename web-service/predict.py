import pickle
from flask import Flask, request, jsonify

with open("models/lin_reg.bin", "rb") as fp:
    (dv, model) = pickle.load(fp)


def prepare_features(ride:dict):
    features_dict = {}
    features_dict['PU_DO'] = f"{ride.get('PULocationID', '')}_{ride.get('DOLocationID', '')}"
    features_dict['trip_distance'] = ride['trip_distance']
    return features_dict
        
def predict(features: dict):
    sparse_ride = dv.transform(features)
    duration = model.predict(sparse_ride)
    return duration

app = Flask("ride-duration-prediction-service")

@app.route("/predict", methods=['POST'])
def predict_endpoint():
    ride = request.get_json()
    features = prepare_features(ride)
    duration = predict(features)
    response = {
        'duration': duration[0]
    }
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
    