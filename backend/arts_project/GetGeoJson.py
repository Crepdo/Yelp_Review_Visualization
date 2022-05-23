import pandas as pd

def get_geojson():
    data = pd.read_csv('resources/new_orlean_restaurant_business.csv')
    result = {}
    result['type'] = 'FeatureCollection'
    crs = {
            'type': 'name',
            'properties': {
                'name': 'EPSG:3857'
                }
            }
    result['crs'] = crs
    features = []
    for _, row in data.iterrows():
        feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [row['longitude'], row['latitude']]
                },
            'properties': {
                'name': row['name'],
                'business_id': row['business_id'],
                }
            }
        features.append(feature)
    result['features'] = features
    return result

if __name__ == '__main__':
    get_geojson()
