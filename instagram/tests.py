from django.test import TestCase
from .models import Profile,Post,Following

# Create your tests here.
class ProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.ian= Profile(user_name = 'ian', bio ='swimmer', email ='adika19ian@gmail.com')
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.ian,Profile))
        
        # Testing Save Method
    def test_save_method(self):
        self.ian.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)
        


class PostTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.ian= Profile(user_name = 'ian', bio ='swimmer', email ='adika19ian@gmail.com')
        self.ian.save_profile()

        # Creating a new tag and saving it
        self.new_following = following(name = 'testing')
        self.new_following.save()

        self.new_post= Post(title = 'Test Post',post = 'This is a random test Post',profile = self.ian)
        self.new_post.save()

        self.new_post.following.add(self.new_following)

    def tearDown(self):
        Profile.objects.all().delete()
        following.objects.all().delete()
        Post.objects.all().delete()   