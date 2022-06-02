import http
import os

import flask
import arts_project.sample_data

import arts_project.GetGeoJson
import arts_project.GetStarPerMonth
import arts_project.GetWordStreamJson

PORT = os.environ.get("PORT", 3001)
ENDPOINT_GRID = "/api/grid"
ENDPOINT_GEO = "/api/geo"
ENDPOINT_STAR = "/api/star"
ENDPOINT_WORDS = "/api/words"


app = flask.Flask(__name__, static_folder="../build")

# Grid Page Endpoint
@app.route(ENDPOINT_GRID)
def get_grid():
    return flask.jsonify(arts_project.sample_data.sample_orders)

@app.route(ENDPOINT_GEO)
def get_geo():
    geo_json = arts_project.GetGeoJson.get_geojson()
    return flask.jsonify(geo_json)

@app.route(ENDPOINT_STAR + '/<path:business_id>')
def get_star(business_id):
    j = arts_project.GetStarPerMonth.get_star_per_month_json(business_id)
    print(j)
    response = flask.jsonify(j)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route(ENDPOINT_WORDS + '/<path:business_id>')
def get_words(business_id):
    result = arts_project.GetWordStreamJson.get_words_stream_data(business_id)
    return flask.jsonify(result)


# Catching all routes
# This route is used to serve all the routes in the frontend application after deployment.
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    print("\n???\n")
    file_to_serve = "index.html"
    if path and os.path.exists(os.path.join(app.static_folder, path)):
        file_to_serve = path
    return flask.send_from_directory(app.static_folder, file_to_serve)


# Error Handler
@app.errorhandler(http.HTTPStatus.NOT_FOUND.value)
def page_not_found():
    json_response = flask.jsonify({"error": "Page not found"})
    return flask.make_response(json_response, http.HTTPStatus.NOT_FOUND)


if __name__ == "__main__":
    app.run(port=PORT)
