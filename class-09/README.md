# Django Custom User

The official Django documentation highly recommends using a custom User model for new projects. Why? Because it's a major pain if you need to add user features down the road.

Some kinds of projects may have authentication requirements for which Django’s built-in User model is not always appropriate. For instance, on some sites it makes more sense to use an email address as your identification token instead of a username.

This class is the end of "vanilla" Django. We'll be moving on to API development next. With that in mind let's take a look a great starter kit for a professional grade Django project `DjangoX`

## Learning Objectives

### Students will be able to

#### Describe and Define

- Django's Auth User model
- AbstractUser class
- Drawbacks of switching to custom User model later in project.

#### Execute

- Subclass AbstractUser
- Customize User fields
- Ensure Django Admin panel functionality is maintained

