import falcon
import json


class ObjRequestClass:
    def on_get(self, req, resp):
        content = {
            'success': 'My first falcon app',
            'firstParameter': 'Something First',
            'secondParameter': 'Something Second'
        }

        resp.status = falcon.HTTP_200
        resp.body = json.dumps(content)

api = falcon.API()
api.add_route('/myget', ObjRequestClass())