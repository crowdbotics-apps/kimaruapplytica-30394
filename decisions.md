# Decisions and Compromises
1. Using Viewsets- Easy to implement without much code. Best practice for maintaining a clean codebase and not reinventing the wheel. The functionalities were mostly CRUD and this comes out of the bod with  `ModelViewSets`. 
This also aided in the URL routing too. Very minimal code implemented to generate all relevant routes
2. Using a `base_model` Model- I noticed that there were  fields that were common in all models and thus, in line wth best principles of DRY(Do not Repeat Yourself), I chose to develop a base model with the common fields where all other models would inherit from.
3. Using `IntegerField()`- In the api docs description, the fields that would seem to be foreign keys are designated as Integers. Also, the relationship between the `subscription` field in `App` model and the `app` field in `Subscription` model is cyclic. With this situation, I chose to represent the fields as Integers on the assumption that the API consumer(Front end) would be the entity to ensure the numbers entered are valid foreign keys. 

The alternative would be to use Foreign keys, follow conventions and drop the subscription field in the App model to avoid the cyclic referencing, and use something like a `to_representation()` function in the model serializers to customize the output of the serializer and cater to the Foreign key relation.

