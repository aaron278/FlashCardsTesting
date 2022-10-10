from flask import Flask
import sys
sys.path.append('backend/src')
import unittest
from __init__ import firebase
from auth.routes import auth_bp
from deck.routes import deck_bp
from cards.routes import card_bp

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app=Flask(__name__, instance_relative_config=False)
        self.app.register_blueprint(deck_bp)
        self.app=self.app.test_client()
        self.app.post('/login',json=dict(email='aaronadb@gmail.com',password='flashcards123'),follow_redirects=True)

    def test_deck_id_route_get_valid_id(self):
        '''Test the deck/id route of our app with a valid deck id'''
        id='-NDxoI5diQd242trg5-S'
        response=self.app.get('deck/'+id);
        assert response.status_code==200
        
       
    def test_deck_id_route_post(self):
        '''Test the deck/id route of our app with the post method'''
        id='-NDxoI5diQd242trg5-S'
        response=self.app.post('deck/'+id)
        assert response.status_code==405
    
    def test_deck_all_route(self):
        '''Test the deck/all route of our app'''
        response=self.app.get('/deck/all',query_string=dict(localId='Test'))
        assert response.status_code==200

    def test_deck_all_route_post(self):
        '''Test that the post request to the '/deck/all' route is not allowed'''
        response=self.app.post('/deck/all')
        assert response.status_code==405

    def test_create_deck_route(self):
        '''Test the create deck route of our app'''
        response=self.app.post('/deck/create',json=dict(localId='Test',title='TestDeck',description='This is a test deck',visibility='public'))
        assert response.status_code==201
        
    def test_update_deck_route_post(self):
        '''Test the deck/update route of our app with'''
        id='-NDxoI5diQd242trg5-S'
        response=self.app.patch('deck/update'+id,json=dict(localId='Test',title='TestDeck',description='This is a test deck',visibility='public'))
        print(response.status_code)
        assert response.status_code==201

if __name__=="__main__":
    unittest.main()
