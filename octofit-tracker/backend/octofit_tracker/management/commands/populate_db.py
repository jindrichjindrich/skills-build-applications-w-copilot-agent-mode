from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete all data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='pass')
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='pass')
        wonderwoman = User.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com', password='pass')
        spiderman = User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='pass')

        # Create activities
        Activity.objects.create(name='Run', user='ironman', team='Marvel')
        Activity.objects.create(name='Swim', user='batman', team='DC')
        Activity.objects.create(name='Bike', user='wonderwoman', team='DC')
        Activity.objects.create(name='Yoga', user='spiderman', team='Marvel')

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=100)
        Leaderboard.objects.create(team='DC', points=90)

        # Create workouts
        Workout.objects.create(name='Cardio Blast', description='High intensity cardio workout')
        Workout.objects.create(name='Strength Builder', description='Weight training for strength')

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
