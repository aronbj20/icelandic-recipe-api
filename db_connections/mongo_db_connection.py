import pymongo
from typing import List
from models.recipe_model import RecipeModel
from bson.objectid import ObjectId
from models.user_model import UserDbModel

class MongoDbConnection:
    def __init__(self, uri: str, db: str):
        self.client = self.__initialize(uri, db)

    def __initialize(self, uri, db) -> pymongo.MongoClient:
        client = pymongo.MongoClient(uri)
        return client[db]

    def insert_many_recipes(self, recipes: List[RecipeModel]) -> None:
        self.client["recipes"].insert_many(recipes)
    
    def insert_recipe(self, recipe: RecipeModel) -> None:
        """
            Inserts recipe if it does not exist. 
        """
        recipe = recipe.dict()
        recipe.pop('id', None)

        self.client["recipes"].update_one({'url': recipe["url"]},{'$set': recipe}, upsert=True)
    
    def safe_insert_recipe(self, recipe: RecipeModel) -> None:
        """
            Adds new recipe if it does not exist. Also add the groups to the recipe.
        """
        recipe = recipe.dict()
        groups = self.client['groups'].find({"tags": {"$in": recipe["tags"]}})
        g = set()
        for group in groups:
            g.add(group["group"])
        recipe["groups"] = list(g)
        self.insert_recipe(recipe=RecipeModel(**recipe))

    def get_all_tags(self) -> List[str]:
        res = self.client['recipes'].distinct("tags")
        return res

    def get_all_groups(self) -> List[str]:
        groups = self.client['groups'].find()
        return [group["group"] for group in groups]

    def set_groups(self):
        recipes = self.client['recipes'].find({"groups": { "$exists":True, "$eq":[]}})
        for recipe in recipes:
            groups = self.client['groups'].find({"tags": {"$in": recipe["tags"]}})
            g = set()
            for group in groups:
                g.add(group["group"])
            recipe["groups"] = list(g)
            self.insert_recipe(recipe=RecipeModel(**recipe))
        
    def get_recipes(self, page_size:int, page: int, query: dict = {}) -> List[RecipeModel]:
        results = self.client['recipes'].find(query).skip((page - 1) * page_size).limit(page_size)

        return [RecipeModel(**res) for res in results]
    
    def get_random_recipes(self, page_size, query) -> List[RecipeModel]:
        results = self.client["recipes"].aggregate([
            {"$match": query},
            {"$sample": {"size": page_size}}
        ])
        results = [RecipeModel(**res) for res in results]
        return results

    def get_recipe(self, id:str) -> RecipeModel:
        res = self.client['recipes'].find_one({"_id": ObjectId(id)})
        if not res: return None
        return RecipeModel(**res)
    
    def add_user(self, user: UserDbModel) -> None:
        userExists = self.client['users'].find_one({"username": user.username})
        print(userExists)
        if userExists: return -1

        self.client['users'].insert_one(user.dict())
    
    def get_user(self, username: str) -> UserDbModel:
        return UserDbModel(**self.client['users'].find_one({"username": username}))
